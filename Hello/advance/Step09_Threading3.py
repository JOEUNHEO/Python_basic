#-*- coding:utf-8 -*-
from pip._vendor import requests
import threading


def getHtml(url):
    #get 방식 요청해서 응답 객체를 리턴 받는다.
    responseObj = requests.get(url)
    # 응답 문자열 출력
    print responseObj.text

# Thread 클래스를 상속 받아서 클래스 정의하기
class myThread(threading.Thread):
    # 생성자
    def __init__(self):                    
        # 부모 생성자에 필요한 값 전달하기
        threading.Thread.__init__(self)
        #인자로 전달된 url 을 필드에 저장
        self.url = url
        
    # 스레드의 본체가 되는 run() 메소드 재정의하기
    def run(self):
        responseObj= requests.get(self.url)
        print responseObj.text
    
if __name__ == '__main__':
    print "메인 스레드가 시작됨"
    
    # 요청 url
    url="http://daum.net"
    
    t1 = threading.Thread(target=getHtml, args=(url,))
    # 데몬 쓰레드는 메인 쓰레드가 종료되면 같이 종료된다.
    # t1.daemon=True
    t1.start()
    
    #responseObj=requests.get("http://daum.net")
        
    # 응답 문자열 출력하기
    #print responseObj.text
    
    print "메인 스레드가 종료됨"