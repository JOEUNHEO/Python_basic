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
        삭제할 회원의 번호를 입력 받아서 삭제하는 예제
    '''
    try:
        # 삭제할 회원 번호를 입력 받는다.
        inputNum=input("삭제할 회원번호:")
        #Maria DB 연결 객체
        conn=mysql.connector.connect(**config) #dict type 을 풀어서전달
        # query 문을 수행해줄 객체
        cursor=conn.cursor()
        # 실행할 sql 문 
        sql='''
           DELETE FROM member
           WHERE num=%s
        '''
        cursor.execute(sql, (inputNum,))
        
        # sql 문의 영향을 받은 row 의 갯수 얻어내기
        print cursor.rowcount
        
        if cursor.rowcount > 0:
            conn.commit()
            print '{} 번 회원의 정보를 삭제 했습니다.'.format(inputNum)
        else:
            print '{} 번 회원은 존재하지 않습니다.'.format(inputNum)
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
    
    
    
    
    
    
    
    
    
    