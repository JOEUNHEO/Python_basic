#-*- coding:utf-8 -*-

result = raw_input("입력:")

print "type:", type(result)
print "result:", result

# str type 을 unicode 로 바꾸기
result2 = result.decode("utf-8")

print "type:", type(result2)
print "result2:", result2

print "Step09_Rawinput.py 가 종료 됩니다."
