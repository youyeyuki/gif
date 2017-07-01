import threading
def work(ha, ss):
    for i in range(0, 10):
        print(ha, ss)


def work2(ha, ss):
    for i in range(0, 10):
        print(ha, ss+"+++++")

t = threading.Thread(target=work,args=("work","work"))
t.start()
print("========")
t2 = threading.Thread(target=work2,args=("work","work"))
t2.start()
