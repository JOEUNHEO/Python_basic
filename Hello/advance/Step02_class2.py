#-*- coding:utf-8 -*-

class Car:
    # 생성자
    def __init__(self, name):
        # 객체를 생성할 때 생성자에 전달되는 인자를 필드에 저장
        self.name=name # 필드를 동적으로 추가
        
    # 메소드
    def showInfo(self):
        info="이차의 제조사는 {} 입니다.".format(self.name)
        print info
    
c1=Car('Hyundai')
c2=Car('Kia')

print 'c1.name :', c1.name
print 'c2.name :', c2.name

c1.showInfo()
c2.showInfo()