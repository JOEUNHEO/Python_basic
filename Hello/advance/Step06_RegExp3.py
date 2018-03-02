#-*- coding:utf-8 -*-
'''
    정규 표현식으로 매칭되는 모든 문자열 찾기
'''
import re

msg='monday tuesday wednesday thursday friday saturday sunday'

if __name__ == '__main__':
    
    pattern = '[a-z]*day'
    
    # pattern 에 매칭되는 모든 문자를 찾아서 list 로 리턴해준다.
    result=re.findall(pattern, msg)
    
    print result
    
    print "pattern 에 매칭되는 문자열 갯수:", len(result)
    print "- 매칭되는 문자열 목록 -"
    for tmp in result:
        print tmp