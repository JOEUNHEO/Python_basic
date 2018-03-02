#-*- coding:utf-8 -*-

def ourDeco(func):
    def wrapper(*args, **kwargs):
        print args, kwargs
        func(*args, **kwargs)
        
    return wrapper

@ourDeco
def test1():
    print "test1()"

@ourDeco
def test2(num):
    print "test2()"

@ourDeco
def test3(num, name):
    print "test3()"

test1()
test2(1)
test3(2, "haegol")
test3(num=3, name="monkey")
