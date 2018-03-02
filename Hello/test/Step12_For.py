#-*- coding:utf-8 -*-

for i in range(5):
    print i
    
print "---------"

names=[u'김구라', u'해골', u'원숭이', u'주뎅이', u'덩어리']

for i in range(len(names)):
    print i, names[i]

print "--------"

# names 배열에 있는 문자열을 역순으로 출력해 보세요.

for i in range(len(names)-1, -1, -1):
    print i, names[i]
    
