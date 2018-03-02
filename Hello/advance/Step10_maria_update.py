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
        회원의 정보를 수정하는 예제
    '''
    try:
        # 수정할 회원의 번호
        num=1
        # 수정할 회원의 이름
        name=u'이정호'
        # 수정할 회원의 주소
        addr=u'아현동'
        
        #Maria DB 연결 객체
        conn=mysql.connector.connect(**config) #dict type 을 풀어서전달
        # query 문을 수행해줄 객체
        cursor=conn.cursor()
        # 실행할 sql 문 
        sql=u'''
          UPDATE member
          SET name=%s, addr=%s
          WHERE num=%s
        '''
        cursor.execute(sql, (name, addr, num))
        if cursor.rowcount > 0:
            print "회원정보를 수정했습니다."
            conn.commit()
        else:
            print "회원 정보 수정 실패"
       
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
    
    
    
    
    
    
    
    
    
    