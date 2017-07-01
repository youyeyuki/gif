#encoding: utf-8
import socket
from hashlib import sha1
from random import randint
from struct import unpack, pack
from socket import inet_aton, inet_ntoa
from bisect import bisect_left
from threading import Timer
from time import sleep
import os
from datetime import *
import time

from bencode import bencode, bdecode

BOOTSTRAP_NODES = [
  ("router.bittorrent.com", 6881),
  ("dht.transmissionbt.com", 6881),
  ("router.utorrent.com", 6881)
] 
TID_LENGTH = 4
KRPC_TIMEOUT = 10
REBORN_TIME = 5 * 60
K = 8

def entropy(bytes):
  s = ""
  for i in range(bytes):
    s += chr(randint(0, 255))
  return s

def random_id():
  hash = sha1()
  hash.update( entropy(20) )
  return hash.digest()

def decode_nodes(nodes):
  n = []
  length = len(nodes)
  if (length % 26) != 0: 
    return n
  for i in range(0, length, 26):
    nid = nodes[i:i+20]
    ip = inet_ntoa(nodes[i+20:i+24])
    port = unpack("!H", nodes[i+24:i+26])[0]
    n.append( (nid, ip, port) )
  return n

def encode_nodes(nodes):
  strings = []
  for node in nodes:
    s = "%s%s%s" % (node.nid, inet_aton(node.ip), pack("!H", node.port))
    strings.append(s)

  return "".join(strings)

def intify(hstr):
  return long(hstr.encode('hex'), 16)	

def timer(t, f):
  Timer(t, f).start()


class BucketFull(Exception):
  pass


class KRPC(object):
  def __init__(self):
    self.types = {
      "r": self.response_received,
      "q": self.query_received
    }
    self.actions = {
      "ping": self.ping_received,
      "find_node": self.find_node_received,
      "get_peers": self.get_peers_received,
      "announce_peer": self.announce_peer_received,
    }

    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.socket.bind(("0.0.0.0", self.port))

  def response_received(self, msg, address):
    self.find_node_handler(msg)

  def query_received(self, msg, address):
    try:
      self.actions[msg["q"]](msg, address)
    except KeyError:
      pass

  def send_krpc(self, msg, address):
    try:
      self.socket.sendto(bencode(msg), address)
    except:
      pass


class Client(KRPC):
  def __init__(self, table):
    self.table = table

    timer(KRPC_TIMEOUT, self.timeout)
    timer(REBORN_TIME, self.reborn)
    KRPC.__init__(self)

  def find_node(self, address, nid=None):
    nid = self.get_neighbor(nid) if nid else self.table.nid
    tid = entropy(TID_LENGTH)
    
    msg = {
      "t": tid,
      "y": "q",
      "q": "find_node",
      "a": {"id": nid, "target": random_id()}
    }
    self.send_krpc(msg, address)

  def find_node_handler(self, msg):
    try:
      nodes = decode_nodes(msg["r"]["nodes"])
      for node in nodes:
        (nid, ip, port) = node
        if len(nid) != 20: continue
        if nid == self.table.nid: continue
        self.find_node( (ip, port), nid )
    except KeyError:
      pass

  def joinDHT(self):
    for address in BOOTSTRAP_NODES: 
      self.find_node(address)

  def timeout(self):
    if len( self.table.buckets ) < 2:
      self.joinDHT()
    timer(KRPC_TIMEOUT, self.timeout)

  def reborn(self):
    self.table.nid = random_id()
    self.table.buckets = [ KBucket(0, 2**160) ]
    timer(REBORN_TIME, self.reborn)

  def start(self):
    self.joinDHT()

    while True:
      try:
        (data, address) = self.socket.recvfrom(65536)
        msg = bdecode(data)
        self.types[msg["y"]](msg, address)
      except Exception:
        pass

  def get_neighbor(self, target):
    return target[:10]+random_id()[10:]


class Server(Client):
  def __init__(self, master, table, port):
    self.table = table
    self.master = master
    self.port = port
    Client.__init__(self, table)

  def ping_received(self, msg, address):
    try:
      nid = msg["a"]["id"]
      msg = {
        "t": msg["t"],
        "y": "r",
        "r": {"id": self.get_neighbor(nid)}
      }
      self.send_krpc(msg, address)
      self.find_node(address, nid)
    except KeyError:
      pass

  def find_node_received(self, msg, address):
    try:
      target = msg["a"]["target"]
      neighbors = self.table.get_neighbors(target)
      
      nid = msg["a"]["id"]
      msg = {
        "t": msg["t"],
        "y": "r",
        "r": {
          "id": self.get_neighbor(target), 
          "nodes": encode_nodes(neighbors)
        }
      }
      self.table.append(KNode(nid, *address))
      self.send_krpc(msg, address)
      self.find_node(address, nid)
    except KeyError:
      pass

  def get_peers_received(self, msg, address):
    try:
      infohash = msg["a"]["info_hash"]

      neighbors = self.table.get_neighbors(infohash)

      nid = msg["a"]["id"]
      msg = {
        "t": msg["t"],
        "y": "r",
        "r": {
          "id": self.get_neighbor(infohash), 
          "nodes": encode_nodes(neighbors)
        }
      }
      self.table.append(KNode(nid, *address))
      self.send_krpc(msg, address)
      self.master.log(infohash)
      self.find_node(address, nid)
    except KeyError:
      pass

  def announce_peer_received(self, msg, address):
    try:
      infohash = msg["a"]["info_hash"]
      nid = msg["a"]["id"]

      msg = { 
        "t": msg["t"],
        "y": "r",
        "r": {"id": self.get_neighbor(infohash)}
      }

      self.table.append(KNode(nid, *address))
      self.send_krpc(msg, address)
      self.master.log(infohash)
      self.find_node(address, nid)
    except KeyError:
      pass

class KTable(object):
  def __init__(self, nid):
    self.nid = nid
    self.buckets = [ KBucket(0, 2**160) ]

  def append(self, node):
    index = self.bucket_index(node.nid)
    try:
      bucket = self.buckets[index]
      bucket.append(node)
    except IndexError:
      return
    except BucketFull:
      if not bucket.in_range(self.nid): return

      self.split_bucket(index)
      self.append(node)

  def get_neighbors(self, target):
    nodes = []
    if len(self.buckets) == 0: return nodes
    if len(target) != 20 : return nodes

    index = self.bucket_index(target)
    try:
      nodes = self.buckets[index].nodes
      min = index - 1
      max = index + 1

      while len(nodes) < K and ((min >= 0) or (max < len(self.buckets))):
        if min >= 0:
          nodes.extend(self.buckets[min].nodes)

        if max < len(self.buckets):
          nodes.extend(self.buckets[max].nodes)

        min -= 1
        max += 1

      num = intify(target)
      nodes.sort(lambda a, b, num=num: cmp(num^intify(a.nid), num^intify(b.nid)))
      return nodes[:K]
    except IndexError:
      return nodes

  def bucket_index(self, target):
    return bisect_left(self.buckets, intify(target))

  def split_bucket(self, index):
    old = self.buckets[index]
    point = old.max - (old.max - old.min)/2
    new = KBucket(point, old.max)
    old.max = point
    self.buckets.insert(index + 1, new)
    for node in old.nodes[:]:
      if new.in_range(node.nid):
        new.append(node)
        old.remove(node)

  def __iter__(self):
    for bucket in self.buckets:
      yield bucket


class KBucket(object):
  __slots__ = ("min", "max", "nodes")

  def __init__(self, min, max):
    self.min = min
    self.max = max
    self.nodes = []

  def append(self, node):
    if node in self:
      self.remove(node)
      self.nodes.append(node)
    else:
      if len(self) < K:
        self.nodes.append(node)
      else:
        raise BucketFull

  def remove(self, node):
    self.nodes.remove(node)

  def in_range(self, target):
    return self.min <= intify(target) < self.max

  def __len__(self):
    return len(self.nodes)

  def __contains__(self, node):
    return node in self.nodes

  def __iter__(self):
    for node in self.nodes:
      yield node

  def __lt__(self, target):
    return self.max <= target


class KNode(object):
  __slots__ = ("nid", "ip", "port")
  
  def __init__(self, nid, ip, port):
    self.nid = nid
    self.ip = ip
    self.port = port

  def __eq__(self, other):
    return self.nid == other.nid



#using example
class Master(object):
  def __init__(self, f):
    self.f = f
    

  def log(self, infohash):
    
    self.f.write(infohash.encode("hex")+"\n")
    os.system("echo magnet:?xt=urn:btih:"+infohash.encode("hex")+">>1.txt")
    self.f.flush()
try:
  d = date.today()
  f = open("%s.log" % d, "a")
  m = Master(f)
  s = Server(Master(f), KTable(random_id()), 8006)
  s.start()	 
except KeyboardInterrupt:
  s.socket.close()
  f.close()
