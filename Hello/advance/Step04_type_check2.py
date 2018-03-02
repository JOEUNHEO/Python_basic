#-*- coding:utf-8 -*-
import types

class Flower:
    pass

class Rose:
    pass

class Tulip:
    pass

# 함수
def myFunction():
    pass


if __name__ == '__main__':
    f1=Flower()
    f2=Rose()
    f3=Tulip()
    if isinstance(f1, Flower):
        print "f1 은 Flower type 입니다."
    if isinstance(f2, Flower):
        print "f2 는 Flower type 입니다."
    if isinstance(f2, Rose):
        print "f2 는 Rose type 입니다."
    if isinstance(f3, Flower):
        print "f3 는 Flower type 입니다."
    if isinstance(f3, Tulip):
        print "f3 는 Tulip type 입니다."
        
    # 함수의 type 체크 : types 를 import 해서 체크한다.
    if isinstance(myFunction, types.FunctionType):
        print "myFunction 은 function type 입니다."
    
    # 클래스의 참조값을 변수에 담기
    gura = Flower
        
    # 클래스의 type 체크
    if isinstance(gura, types.ClassType):
        print "gura 는 class type 입니다."
        
    