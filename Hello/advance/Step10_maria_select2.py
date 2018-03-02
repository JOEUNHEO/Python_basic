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
    
    try:
        # select 인자 입력 받기
        inputNum=input("회원번호:")
        
        #Maria DB 연결 객체
        conn=mysql.connector.connect(**config) #dict type 을 풀어서전달
        # query 문을 수행해줄 객체
        cursor=conn.cursor()
        # 실행할 query 문 
        sql='''
            SELECT num,name,addr 
            FROM member 
            WHERE num=%s
            ORDER BY num DESC
        '''
        # query 문 수행
        # select 인자를 tuple 로 전달한다.
        cursor.execute(sql, (inputNum,))
        '''
            cursor.fetchone() 하면 tuple 이 리턴된다.
            tuple 에는 select 된 row 의 정보가 들어 있다. 
            select 된 결과가 없을때는 None 이 리턴된다.
        '''
        result=cursor.fetchone()
        print result
        
        if result:
            num=result[0]
            name=result[1]
            addr=result[2]
            print u'번호: {}, 이름:{}, 주소:{}'\
                .format(num, name, addr)
        else:
            print '{} 번 회원은 존재하지 않습니다.'.format(inputNum)
            
    except Exception, e:
        print e
    finally:
        try:
            conn.close()
        except NameError:
            pass
    
    print "메인 메소드가 종료 됩니다."
    
    
    
    
    
    
    
    
    
    