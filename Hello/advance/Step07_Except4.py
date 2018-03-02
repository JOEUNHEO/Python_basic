#-*- coding:utf-8 -*-
'''
    Custom 예외 발생 시키기
    
    - 프로그래머가 의도하는 시점에 직접 예외를 발생 시킬 수 있다.
    
    raise 예외객체
'''

# 예외 객체를 생성할 class 정의하기

class MyError(Exception):#Exception 클래스를 상속 받아서 만든다.
    # 생성자
    def __init__(self, msg):
        self.msg = msg
    
    # 예외 메세지 리턴
    def __str__(self):
        return self.msg
    
if __name__ == '__main__':
    print "메인 스레드가 시작 되었습니다."
    
    try:
        msg = input("숫자 입력:")
        
        if not isinstance(msg, int):
            # 프로그래머가 원하는 시점에 직접 예외 발생 시키기
            raise MyError('정수를 입력햐라니까 말을 안듣네~~') # java 에서는 throw new exception
        print "입력한 정수:", msg
    except MyError, me:
        print me
    
    print "메인 스레드가 종료 됩니다."