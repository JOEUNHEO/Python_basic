#-*- coding:utf-8 -*-

#가상의 공격 유닛을 생성할 클래스
class AttackUnit:
    #모든 객체가 공유할 클래스 변수 만들고 초기값 부여
    attackPower=10
    #공격하는 인스턴스(객체) 메소드
    def attack(self):
        print "{}의 파워로 공격합니다.".format(AttackUnit.attackPower)
        
    #클래스명으로 접군하는 클래스 메소드 만들기
    @classmethod
    def setPower(cls, power): #cls:클래스의 참조값(python에서는 class도 객체로 간주) /
        #첫번째 인자로 클래스의 참조값이 들어온다.
        cls.attackPower=power
        #AttackUnit.AttackPower=power 과 동일 / 상속 관계로 얽혀 있으면 서로 다른 동작일 수 있음
    
    @classmethod
    def showPower(cls):
        print "현재의 공격력: {}".format(cls.attackPower)
    
if __name__ == '__main__':
    #AttackUnit.attack() 해당과 같이 호출 불가
    unit1=AttackUnit()
    unit2=AttackUnit()
    unit3=AttackUnit()
    
    #클래스 메소드를 클래스명으로 사용해보기
    print "AttackUnit.showPower()"
    AttackUnit.showPower()
    
    AttackUnit.setPower(20)
    AttackUnit.showPower()
    
    print "---클래스 메소드를 이용해서 클래스 변수 수정 후 --"
    print "unit1.attack()"
    unit1.attack()
    print "unit2.attack()"
    unit2.attack()
    print "unit3.attack()"
    unit3.attack()