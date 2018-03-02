#-*- coding:utf-8 -*-

class Phone(object):
    def call(self):
        print "전화를 걸어요"

class HandPone(Phone):
    def mobileCall(self):
        print "이동중에 전화를 걸어요"
    def takePicture(self):
        print "100만 화소의 사진을 찍어요"

class SmartPhone(HandPone):
    def doInternet(self):
        print "인터넷을 해요"
    #사진 찍는 메소드 재정의
    def takePicture(self):
        #부모의 메소드 호출 여부(생략 가능)
        #HandPone.takePicture(self)
        print "1000만 화소의 사진을 찍어요"

if __name__ == '__main__':
    p1=Phone()
    p2=HandPone()
    p3=SmartPhone()
    
    print "Phone type"
    p1.call()
    
    print "HandPhone type"
    p2.call()
    p2.mobileCall()
    
    print "SmartPhone type"
    p3.call()
    p3.mobileCall()
    p3.doInternet()