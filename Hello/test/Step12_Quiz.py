#-*- coding:utf-8 -*-
'''
    input() 함수를 이용해서 숫자를 입력 받아서
    
    2 를 입력하면 구구단 2단 출력
    3 을 입력하면 구구단 3단 출력
    .
    .
    
      하는 코드를 작성해 보세요.
      
      출력 형식
    
    - 구구단 2 단 -
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
'''

result = input("입력:")

result2=u" - 구구단 {} 단 - ".format(result)

print result2

for i in range(1, 10, 1):
    # i를 1~9 까지 변하게 하고 결과값을 계산한다.
    result3="{} x {} = {}".format(result, i, result*i)
    # 결과값을 형식에 맞게 출력하기
    print result3