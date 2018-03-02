#-*- coding:utf-8 -*-

import mysql.connector

#DB 접속 정보를 dict type 으로 준비한다.
config={
        'user':'root',
        'password':'maria',
        'host':'127.0.0.1',
        'database':'mingu',
        'port':3306
    }

if __name__ == '__main__':
    '''
        회원의 이름과 주소를 입력 받아서 DB 에 저장하는 예제
    '''
    try:
        # 이름 입력 받기
        inputName=raw_input("이름:").decode('utf-8')
        # 주소 입력 받기
        inputAddr=raw_input("주소:").decode('utf-8')
        
        #Maria DB 연결 객체
        conn=mysql.connector.connect(**config) #dict type 을 풀어서전달
        # query 문을 수행해줄 객체
        cursor=conn.cursor()
        # 실행할 sql 문 
        sql='''
           INSERT INTO member
           (name, addr)
           VALUES(%s, %s)
        '''
        # sql 문 수행하기
        cursor.execute(sql, (inputName, inputAddr))
        
        # DB 에 실제 반영하기
        conn.commit()
        print "회원 정보를 저장 했습니다."
    except Exception, e:
        print e
        # 롤백이 필요 하다면 ...
        conn.rollback()
    finally:
        try:
            conn.close()
        except NameError:
            pass
    
    print "메인 메소드가 종료 됩니다."
    
    
    
    
    
    
    
    
    
    