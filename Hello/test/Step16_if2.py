#-*- coding:utf-8 -*-

# 양자 택일의 if 문 블럭구성

inputNum=input("양의 정수 입력:")

if inputNum%2 == 1:
    print u'{} 는 홀수 입니다.'.format(inputNum)
else:
    print u'{} 는 짝수 입니다.'.format(inputNum)

# 다중 if문 구성

jumsu = input("정수 입력(0~100):")

if jumsu>=90:
    print '성적은 A 입니다.'
elif jumsu>=80:
    print '성적은 B 입니다.'
elif jumsu>=70:
    print '성적은 C 입니다.'
elif jumsu>=60:
    print '성적은 D 입니다.'
else:
    print '성적은 F 입니다.'

