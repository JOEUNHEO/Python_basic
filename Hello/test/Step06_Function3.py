#-*- coding:utf-8 -*-
'''
    함수에 여러개의 인자를 동적으로 전달하기
'''

def test1(*args):
    # args 는 tuple type 이다.
    print args
    
test1()
test1(10)
test1(10, 20)
test1(10, 20, 30)

print "Step06_Function3.py 가 종료 됩니다."

