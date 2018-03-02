#-*- coding:utf-8 -*-
'''
    - function type
    
    1. 특정 시점에 일괄 실행할 명령문을 모아 놓을 수 있다.
    2. function 도 참조값으로 관리된다.
    3. 변수에 할당 가능
    4. 함수의 인자로 전달 가능
'''

# test1 이라는 이름의 빈 함수 만들기 (세미콜론과 들여쓰기로 범위 설정)
def test1():
    pass

test1() # test1 함수 호출하기

# "hello" 를 출력하는 test2 라는 이름의 함수 만들기
def test2():
    print "hello"
    
test2() # test2 함수 호출하기

# test2 함수를 참조해서 변수에 대입하기
a=test2

print "Step06_function.py 가 종료 됩니다."
