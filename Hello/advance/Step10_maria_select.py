#-*- coding:utf-8 -*-

import mysql.connector

# DB 접속 정보를 dict type 으로 준비한다.
config={
        'user':'root',
        'password':'maria',
        'host':'127.0.0.1',
        'database':'mingu',
        'port':3306
    }

if __name__ == '__main__':
    
    try:
        #maria DB 연결 객체
        conn = mysql.connector.connect(**config) #dict type인 config 를 풀어서 전달
        # query 문을 수행해줄 객체
        cursor=conn.cursor() # Java 에서는 PreparedStatement 객체
        # 실행할 query 문
        sql="""
                SELECT num, name, addr
                FROM member
                ORDER BY num DESC
            """
        # query 문 수행
        cursor.execute(sql)
        # result 는 tuple 이 순서대로 들어 있는 list 이다.
        result = cursor.fetchall() # Java 에서는 ResultSet 객체
        
        for tmp in result:
            # tmp 는 select 된 row 정보가 들어 있는 tuple 이다.
            num = tmp[0]
            name = tmp[1]
            addr = tmp[2]
            print u"번호:{}, 이름:{}, 주소:{}".format(num, name, addr)
        
    except Exception, e:
        print e
    finally:
        conn.close()
        
    print "메인 메소드가 종료 됩니다."