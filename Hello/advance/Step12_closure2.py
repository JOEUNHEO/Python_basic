#-*- coding:utf-8 -*-

def test1():
    myName='김구라'
    
    # 함수는 만들어 질때 외부 환경을 캪쳐해서 저장한다.
    def inner():
        print 'inner() :', myName
    
    # inner 함수의 참조값 리턴 
    return inner

if __name__ == '__main__':
    # 리턴 되는 값을 a 에 저장
    a=test1()
    a()