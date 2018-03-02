#-*- coding:utf-8 -*-

# test.GuraUtil 모듈로 부터 SayHello, SayBye 메소드 import 하기
from test.GuraUtil import SayHello, SayBye
from test import AcornUtil

# import 된 메소드 사용하기
SayHello()
SayBye()

# import 된 AcornUtil 의 변수 차조
print AcornUtil.name
# import 된 AcornUtil 의 메소드 사용
AcornUtil.study()

print "Step13_import.py 에 들어온 실행순서가 종료 됩니다."