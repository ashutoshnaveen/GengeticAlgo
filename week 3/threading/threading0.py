import threading
def do_this():
    global x
    while (x<300):
        x+=1
        pass
    print x
def do_after():
    global x
    while (x<600):
        x+=1
        pass
    print x
def main():
    global x
    x=0
    new_thread=threading.Thread(target=do_this)
    new_thread.start()
    new_thread.join()
    print new_thread.ident
    new_next_thread=threading.Thread(target=do_after)
    new_next_thread.start()
    print new_next_thread.ident
    print new_thread.ident
    print new_next_thread.ident
if (__name__=="__main__"):
    main()
