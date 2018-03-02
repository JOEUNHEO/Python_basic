#-*- coding:utf-8 -*-
'''
    변수에 들어있는 데이터의 type 체크
    
    isinstance( 값, type )
    
    메소드는 bool type 을 리턴 합니다.
'''

if __name__ == '__main__':
    
    inputData=input("입력:")
    
    if isinstance(inputData, int):
        print "int type 입니다."
    elif isinstance(inputData, float):
        print "float type 입니다."
    elif isinstance(inputData, str):
        print "str type 입니다."
    elif isinstance(inputData, dict):
        print "dict type 입니다."
    elif isinstance(inputData, list):
        print "list type 입니다."
    else:
        print "기타 등등 type 입니다."