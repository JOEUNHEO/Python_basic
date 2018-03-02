#-*- coding:utf-8 -*-
'''
    문자열 format
'''

result1=u'내이름은 {} 입니다.'.format(u'김구라')

print result1

result2=u"cat:{0}, dog:{1}".format(u'고양이', u'개')

print result2

#{}안에 index를 명시하지 않아도 순서대로 적용.
result3=u'cat:{}, dog:{}'.format(u'고양이', u'개')

print result3

result4=u'cat:{1}, dog:{0}'.format(u'개', u'고양이')

print result4