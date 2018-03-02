#-*- coding:utf-8 -*-

'''
    class 정의하기
'''

# Car 클래스 정의하기
class Car:
    # 생성자
    def __init__(self):
        print "Car 클래스의 생성자 호출됨"
    # 메소드 정의하기
    def drive(self):
        print "달려요!"

# 클래스를 이용해서 객체를 생성해서 참조값을 c1 변수에 담기
c1=Car()
# c1 변수에 담겨 있는 참조값을 이용해서 객체의 메소드 호출
c1.drive()

print "id(c1) :", id(c1)

print "Step02_class.py 가 종료 됩니다."
