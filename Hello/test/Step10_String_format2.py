#-*- coding:utf-8 -*-
'''
    문자열 format
'''

result1=u"내 이름은 {name} 이고 주소는 {addr} 입니다.".format(name=u'김구라', addr=u'노량진')

print result1

#tuple type
mem1=(1, u'김구라', u'노량진')
result2=u'번호:{}, 이름:{}, 주소:{}'.format(mem1[0], mem1[1], mem1[2])

print result2

result3=u'번호:{}, 이름:{}, 주소:{}'\
        .format(*mem1) #mem1에 있는 데이터를 순서대로 인자로 전달

print result3

# dict type
mem2={'num':2, 'name':u"해골", 'addr':u"행신동"}

result4=u'번호:{num}, 이름:{name}, 주소:{addr}'\
        .format(num=mem2['num'], name=mem2['name'], addr=mem2['addr'])
        
print result4

result5=u'번호:{num}, 이름:{name}, 주소:{addr}'\
        .format(**mem2)
        
print result5