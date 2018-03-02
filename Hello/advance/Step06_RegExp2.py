#-*- coding:utf-8 -*-
import re


# 검증할 문자열
msg='javascript python java c++'

if __name__ == '__main__':
    
    # 정규 표현식
    pattern='python'
    # Match 객체를 얻어낸다
    m=re.search(pattern, msg)
    
    if m: # 만일 Match 객체가 존재하면
        print "m.group() :", m.group() # 찾은 문자열
        print "m.start() :", m.start() # 찾은 문자열의 시작 인덱스
        print "m.end() :", m.end() # 찾은 문자열의 끝 인덱스
        print "m.span() :", m.span() # (시작, 끝) tuple