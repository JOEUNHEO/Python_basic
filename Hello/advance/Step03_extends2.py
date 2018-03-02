#-*- coding:utf-8 -*-

class Engine:
    # 생성자
    def __init__(self):
        # isStarted 라는 필드에 False 저장하기
        self.isStarted=False
    # 엔진을 시작 시키는 메소드   
    def start(self):
        print "시동을 걸어요"
        self.isStarted=True
        
class Car:
    def __init__(self, engine):
        self.engine=engine
        
    # 달리는 메소드
    def drive(self):
        if not self.engine.isStarted:
            print "시동을 먼저 걸어주세요."
            return
        print "신나게 달려요"
        
    # 시동을 거는 메소드
    def startEngine(self):
        self.engine.start()
        
# Car 클래스를 상속받는 SuperCar 클래스 정의
class SuperCar(Car):
    # 생성자
    def __init__(self, engine):
        # 부모 생성자에 필요한 값 전달
        Car.__init__(self, engine)
    # 빨리 달리는 기능
    def driveFast(self):
        if not self.engine.isStarted:
            print "시동을 먼저 걸어주세요"
            return
        print "엄청 빨리 달려요"
        

if __name__=='__main__':
    #car 객체를 생성해서 drive() 메소드를 호출해보세요.
    car1=Car(Engine())
    car1.startEngine()
    car1.drive()
    
    print "-----------"
    car2=SuperCar(Engine())
    car2.startEngine()
    car2.drive()
    car2.driveFast()