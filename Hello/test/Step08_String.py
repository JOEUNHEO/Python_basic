#-*- coding:utf-8 -*-
'''
    문자열 데이터 다우기
'''

# str type
str1 = 'abcd'

# unicode type (한글이 포함되어 있으면 unicode type 을 사용한다.)
str2 = u'abcd 김구라'

# 문자열의 내용 비교
name1='kim'
name2='kim'

result1 = name1==name2

myComment = 'abcdeeee'

print "id:", id(myComment)
print "길이:", len(myComment)
print "e 의 포함 횟수:", myComment.count('e')
print "e 로 시작하는지 여부:", myComment.startswith('e')

# 문자열의 내용이 같으면 id값(참조값)도 같다
name1 = u"김구라"
name2 = u"해골"
name3 = u"김구라"

print "name1 id:", id(name1)
print "name2 id:", id(name2)
print "name3 id:", id(name3)


print "result1:", result1
