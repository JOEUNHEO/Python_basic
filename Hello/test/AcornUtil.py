#-*- coding:utf-8 -*-
'''
    test/AcornUtil.py
'''


name='Acorn Academy'

def study():
    print u'프로그래밍 공부를 해요'
    
def test2(num=0, name=u"아무게", isMan=True, addr=u"어디게"):
    print "num",num
    print "name",name
    print "isMan",isMan
    print "addr",addr
    
test2(num=99, name=u"김구라")
a={10,20,30,40,50}
print a

numbers2=[1,2,3,4,5,6,7,8,9,10]
print 'numbers2:',numbers2[-3:-1]

a={10,20,30}
b={20,30,40}

result=a.union(b)
print 'result:',result