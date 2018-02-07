
import threading
def main():
    thread1=threading.Thread(target=f1)
    thread1.start()
    thread2=threading.Thread(target=f2)
    thread2.start()
def f1():
    print '2\n'
def f2():
    print 3
if __name__==("__main__"):
    main()
