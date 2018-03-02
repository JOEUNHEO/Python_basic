#-*- coding:utf-8 -*-

'''
Created on 2018. 2. 22.

@author: acorn
'''

class Coffee:
    def drink(self):
        print "커피를 마셔요"

class StarBucks:
    #생성자의 인자로 전달되는 지점명을 branch라는 필드에 저장
    def __init__(self, branch):
        self.branch=branch
    
    #Coffee 객체를 생성해서 리턴
    def getCoffee(self):
        return Coffee()
    
    #count가 정수일 때 해당 숫자만큼 Coffee객체를 생성해서 참조값을 list type에 담아 list 리턴
    def getCoffees(self, count):
        list1=[]
        for i in range(count):                
            list1.append(Coffee())
            
        return list1
    
    #지점명을 콘솔창에 출력
    def showInfo(self):
        print "지점명:{}".format(self.branch)

if __name__ == '__main__':
    #1. StarBucks 객체를 생성해서 참조값을 변수에 담기(지점:종각)
    starBranch=StarBucks("종각")
    #2. getCoffee() 메소드를 호출해서 리턴되는 Coffee 객체의 .drink()메소드를 호출해 보세요.
    starBranch.getCoffee().drink()
    print "-------------" 
    #3. getCooffees() 메소드를 호출하면서 5를 전달하고 리턴되는 list객체에 있는 Coffee객체의 .drink()메소드를 모두 호출
    coffeeList=starBranch.getCoffees(5)
    for tmp in coffeeList:
        tmp.drink()
    print "-------------" 
    #4. showInfo() 메소드 호출
    starBranch.showInfo()