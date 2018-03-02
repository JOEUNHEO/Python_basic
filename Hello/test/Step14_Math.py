#-*- coding:utf-8 -*-
'''
    math 모듈 import 해서 사용하기
'''
import math
import random

num=123.45678

result1=math.floor(num) # 내림 연산
result2=math.ceil(num) # 올림 연산

print result1, result2

# 0 이상 1 미만의 무작위 실수 얻어내기
ranNum = random.random()
print ranNum

# 0 이상 10 미만의 실수
ranNum2 = random.random()*10

# 0 이상 10 미만의 정수
ranNum3 = int(random.random()*10)

# 10 이상 20 미만의 정수
ranNum4 = int(random.random()*10)+10

# 75 이상 100 미만의 정수
ranNum5 = int(random.random()*25)+75

count=0

while True:
    count=count+1
    if count==5:
        break
    print count
    
# 로또번호 6 개를 무작위로 얻어내서 출력해 보세요.

a = set()

while True:
    if(len(a)==6):
        print a
        break
    lotto = int(random.random()*45)+1
    a.add(lotto)
