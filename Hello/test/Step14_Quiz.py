#-*- coding:utf-8 -*-
'''
    로또번호 추출하는 예제
'''
import random

nums=set()
'''
while True:
    # 1~45 사이의 랜덤한 점수 얻어내기
    ranNum = int(random.random()*45)+1
    nums.add(ranNum)
    if(len(nums)==6): # 6개 모두 추출 되었으면
        break # 반복문 탈출
'''    

while len(nums)<6:
    # 1~45 사이의 랜덤한 점수얻어내기
    ranNum = int(random.random()*45)+1
    nums.add(ranNum)

# set 에 들어 있는 데이터를 list 에 넣기

lottoNums = list(nums) # list 객체 생성하면서 인자로 set 전달

#정렬
lottoNums.sort()

for tmp in lottoNums:
    print tmp
