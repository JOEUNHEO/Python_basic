#-*- coding:utf-8 -*-
import sqlite3

if __name__ == '__main__':
    try:
        # test.db database 파일을 open (없으면 생성)
        conn=sqlite3.connect("test.db")
        
        cursor=conn.cursor()
        
        sql='''
            SELECT num,name,addr
            FROM member
            ORDER BY num DESC
        '''
        result=cursor.execute(sql)
        
        for tmp in result:
            num=tmp[0]
            name=tmp[1]
            addr=tmp[2]
            print u"번호:{}, 이름:{}, 주소:{}"\
                .format(num, name, addr)
        
    except Exception, e:
        print e
    finally:
        try: conn.close()
        except NameError: pass
      
      
      
      
      
        
    