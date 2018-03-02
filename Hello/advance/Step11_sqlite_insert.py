#-*- coding:utf-8 -*-

'''
    python 은 sqlite3 database 를 내장하고 있다.
'''
import sqlite3


if __name__=='__main__':
    
    print(sqlite3.sqlite_version)
    try:
        conn=sqlite3.connect('test.db')
        # cursor 객체의 참조값을 얻어와서 
        cursor=conn.cursor()
        # table 이 존재하지 않으면 table 만들기
        cursor.execute('''
            CREATE TABLE  
            IF NOT EXISTS member
            (num INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, addr TEXT)
        ''')
        
        # sqlite 를 사용할때 바인딩 인자 표시는 ? 로 표기 
        sql=u'''
            INSERT INTO member
            (name, addr) 
            VALUES(?, ?)
        '''
        
        #이름과 주소를 입력 받아서 
        inputName=raw_input("이름:").decode('utf-8')
        inputAddr=raw_input('주소:').decode('utf-8')
        # sqlite DB 에 저장하기 
        cursor.execute(sql, (inputName, inputAddr))
        
        conn.commit()
        print "회원정보를 저장했습니다."
        
    except Exception, e:
        print e
    finally:
        try:conn.close()
        except NameError: pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    