from enum import Enum


# data = (0x1C, 0xE3, 0xFC, 0x03)
# l = 0
# for i in range(0, 4):
#     for j in range(0, 4):
#         for k in range(0, 4):
#             for m in range(0,4):
#                 print("{} {} {} {}   {} 第{}次".format(hex(data[i]), hex(data[j]), hex(data[k]),hex(data[m]), hex(data[i] ^ data[j] ^ data[k]^data[m]), l))
#                 l += 1

def main():
    data = (0x01, 0xfe, 0x18, 0x17, 0xe7, 0x01)  # a1 + a66 全排列


def getOp():
    op = ("+", "/", "^")
    return


if __name__ == '__main__':
    res = 0x01
    data = (0x00, 0x19, 0xe6, 0xff, 0x02,0x00)

    print("##########if==ff 减1 #################")
# FE + 1 = 00
#
s =  [[x, y, z] for x in [1, 2, 3] for y in ['a', 'b', 'c'] for z in ['0', 'r', 'z']]

a =[]
for x in[1,2,3]:
    for y in ['a', 'b', 'c']:
        for z in ['0', 'r', 'z']:
            a.append([x,y,z])
print(s)

print(a)