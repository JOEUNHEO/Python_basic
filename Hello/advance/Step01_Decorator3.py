#-*- coding:utf-8 -*-

def myDeco(func):
    def wrapper(arg):
        if arg=='김구라':
            arg='개구라'
        func(arg)
        
    return wrapper

@myDeco
def test1(name):
    print "name:", name
    print "test1() 수행됨"

test1('김구라')
print "------"
test1('해골')
print "------"
test1('원숭이')