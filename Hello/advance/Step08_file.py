#-*- coding:utf-8 -*-
'''
Created on 2018. 2. 23.

@author: acorn
'''
import os
import codecs

if __name__ == '__main__':
    # 현재 작업 디렉토리 출력하기
    print "os.getcwd() :", os.getcwd()
    # os 의 파일 구분자 읽어오기
    print "os.sep :", os.sep
    # 읽어올 파일의 경로 구성하기
    filePath = os.getcwd()+os.sep+"myMemo.txt"
    print "filePath :", filePath
    
    # 파일 열기 .open(경로, 모드, 인코딩)
    f=codecs.open(filePath, "r", "utf-8") # "r" 은 읽기 모드
    
    # 텍스트 문서의 내용 읽어들이기
    result = f.read()
    print result
    # 파일 닫기
    f.close()
    # 파일을 만들어서 문자열 기록하기
    letterPath = os.getcwd()+os.sep+"myMemo2.txt"
    letter = codecs.open(letterPath, "w", "utf-8") # "w" 는 쓰기 모드
    letter.write(u"To my Friend ~\n")
    letter.close() #close() 하는 순간 파일이 만들어 진다.
    
    # 파일을 열어서 문자열 추가하기
    letter2 = codecs.open(letterPath, "a", "utf-8") # "a" 는 추가 모드
    for i in range(3):
        letter2.write(u"안녕하세요!\n")
    letter2.close()
    
    print u".readLine() 테스트"
    letter3 = codecs.open(letterPath, "r", "utf-8")
    # 한줄씩 읽어와서 출력하기
    print letter3.readline()
    print letter3.readline()
    letter3.close()
    
    print "--------------"
    letter4 = codecs.open(letterPath, "r", "utf-8")
    #모든 라인 다 읽어와서 출력하기
    while True:
        line = letter4.readline()
        if not line: # 더이상 읽을라인이 없으면
            break # 반복문 탈출
        print line
    letter4.close()
    
    print "--------------"
    letter5 = codecs.open(letterPath, "r", "utf-8")
    #한줄 씩 읽은 데이터를 list 에 담아서 리턴 받는다.
    lines = letter5.readlines()
    print lines
    # list 에 있는 문자열 모두 출력하기
    for tmp in lines:
        print tmp
    
    letter5.close()
        
    print "메인 스레드가 종료 됩니다."