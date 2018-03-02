#-*- coding:utf-8 -*-

'''
    - 여러가지 연산자 알아보기
    
    1. 논리 연산자
    2. 대입 연산자
    3. 비교 연산자
    4. 산술 연산자
'''

# 1. 논리 연산자 : bool type 데이터를 연산 ( and, or, not)

print "-- or 연산 --"
print "False or False :", False or False 
print "False or True :", False or True 
print "True or False :", True or False 
print "True or True :", True or True

print "-- and 연산 --"
print "False and False :", False and False 
print "False and True :", False and True 
print "True and False :", True and False 
print "True and True :", True and True

print"-- not 연산 --"
print "not True :", not True
print "not False :", not False

# 2. 대입연산자 : =, +=, -=, *=, /=, %=

name = "kimgura"
num = 10

# num = num + 1
num += 1 # 위의 표현식을 줄이면 아래와 같다 
# num = num+5
num += 5
# num = num-1
num -= 1
# num = num-3
num -= 3
# num = num*2
num *= 2
# num = num/3
num /= 3
# num = num%3
num %= 3

# 3. 비교 연산자 : == , != , >, >= , <, <=
# 비교 연산의 결과는 bool type 으로 나타난다.

print "10 == 10 : ", 10 == 10
print "10 != 10 : ", 10 != 10
print "10 > 20 : ", 10 > 20
print "10 >= 20 :", 10 >= 20
result = 10 < 20
print "result : ", result

isEqual = "abcd" == "abcd"
isDifferent = "1234" != "1234"
print "isEqual : ", isEqual
print "isDifferent : ", isDifferent

# 4. 산술 연산자
# +, -, *, /, %

result1 = 10 + 1
result2 = 10 - 10
result3 = 10 * 10
result4 = 3 / 2.0 # 결과를 실수 값으로 얻어내고 싶으면 최소 하나는 실수여야한다.
result5 = 3 / 2 # 3을 2로 나눈 몫이 얻어내진다.
result6 = 3 % 2 # 3을 2로 나눈 나머지가 얻어내진다.

# 증감 연산자는 존재 하지 않는다.

myNum = 0

# 증감연산 없음
#myNum++
#myNum--

# 증감 연산 대신 대입 연산자를 이용해야 한다
myNum += 1 # 1증가
myNum -= 1 # 1감소

'''
    - javascript 3 항 연산
    
    var isRun=true;
    
    var result = isRun ? '달려요' : '정지!';
    
    - Java 3 항 연산
    
    boolean isRun=true;
    
    String result = isRun ? "달려요" : "정지!";
'''

# 3 항연산

isRun=True

result=u'달려요' if isRun else u'정지!'

print 'result:', result

# 비교연산 응용

inputNum = input("숫자입력:")

result2 = 0 <= inputNum <= 10

print "입력한 숫자가 0 이상 10 이하 인지 여부: ", result2
