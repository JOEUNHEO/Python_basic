#-*- coding:utf-8 -*-
import threading
import time


def printCount(num, name):
    #전달 받은 인자 출력해 보기
    for i in range(10):
        print "num:",num, " name:",name
        # time 페키지의 sleep() 메소드를 이용해서 스레드 1초 sleep
        time.sleep(1)
        print i
    
    print "end printCount()"
    

if __name__ == '__main__':
    
    print "메인 스레드가 시작 되었습니다."
    # printCount 함수를 다른 스레드에서 수행 시키기
    
    # 스레드 객체 생성해서  .Thread(target=함수) 
    t=threading.Thread(target=printCount, args=(1, u'김구라'))
    # 스레드 시작 시키기 
    t.start()
    
    # 스래드 객체 하나더 생성해서 
    t2=threading.Thread(target=printCount, kwargs={'num':2, 'name':u"해골"})
    # 스레드 시작 시키기 
    t2.start()
    
    print "메인 스레드가 종료 됩니다."
    