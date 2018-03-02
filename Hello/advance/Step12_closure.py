#-*- coding:utf-8 -*-

# Step12_closure.py 모듈 안에서의 전역 변수 
myName='김구라'

def test1():
    # 함수 외부에 정의된 myName 참조가능
    print myName

def test2():
    myName='원숭이'
    # 함수 안에 정의된 myName 을 참조한다. 
    print myName

def test3():
    # 함수 안에서 전역변수 만들기
    global yourName
    yourName='Acorn'
 

if __name__ == '__main__':
    test1()
    test2()
    test3()
    
    print yourName
    
    
    
    
    
    
    
    
    
    