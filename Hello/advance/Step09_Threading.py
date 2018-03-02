#-*- coding:utf-8 -*-
import threading

def printCount():
    
    for i in range(10000):
        print i
    
    print "end printCount()"

if __name__ == '__main__':
    
    print "메인 스레드가 시작 되었습니다"
    
    # printCount 함수를 다른 스레드에서 수행 시키기
    
    # 스레드 객체 생성해서 .Thread(target=함수)
    t=threading.Thread(target=printCount)
    # 스레드 시작 시키기
    t.start()
    print "메인 스레드가 종료 됩니다."