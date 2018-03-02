#-*- coding:utf-8 -*-

from pip._vendor import requests
import threading

#Thread 클래스를 상속 받아서 클래스 정의
class MyThread(threading.Thread):
    def __init__(self, url):
        #부모 생성자에 필요한 값 전달
        threading.Thread.__init__(self)
        #인자로 전달된 url을 필드에 저장
        self.url=url
    
    #스레드의 본체가 되는 run()메소드 재정의
    def run(self):
        responseObj=requests.get(self.url)
        print responseObj.text
    

if __name__ == '__main__':
    print "메인 스레드 시작"
    
    # 요청 url
    url="http://daum.net"
    t1=MyThread(url)
    #데몬 스레드는 메인 스레가 종료되면 같이 종료된다.
    #t1.daemon=True
    t1.start()
    
    t1.join()
    
    print "메인 스레드 종료"