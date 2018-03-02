#-*- coding:utf-8 -*-

'''
     - dict type
     
     1. key:value 형태로 데이터를 관리한다.
     2. 순서가 없다.
     3. key 값을 이용해서 저장된 데이터를 참조한다.
'''

dict1={"num":1, "name":"kimgura", "isMan":True}

# dict1["key"] 형태로 데이터를 참조한다.
a=dict1["num"]
b=dict1["name"]
c=dict1["isMan"]

print "a:", a
print "b:", b
print "c:", c

# dict 에 있는 데이터 수정
dict1["num"]=999 # 참조해서 대입 연산자를 이용해서 값을 대입하면 된다.

print "수정후 dict1[num] :", dict1["num"]

# 특정방 삭제
del dict1["isMan"] # del 이라는 예약어와 함께 방을 참조하면 된다.

print "Step03_Dict.py 가 종료 됩니다."
