import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

#테이블 생성
cursor.execute("DROP TABLE IF EXISTS tblAddr")
cursor.execute("""CREATE TABLE tblAddr (name CHAR(16) PRIMARY KEY, phone CHAR(16), addr TEXT)""")

#테이블 요소 추가
cursor.execute("INSERT INTO tblAddr VALUES('김상향','123-123','인천')")

#테이블 요소 검색
cursor.execute("SELECT * FROM tblAddr")
table = cursor.fetchall()
for record in table:
    print("이름: %s, 번호:%s,주소:%s"%record)

re = cursor.fetchone()
print("이름: %s, 번호:%s,주소:%s"%re)

#테이블 요소 수정
cursor.execute("UPDATE tblAddr SET addr='제주도' WHERE name='김상형'")
#테이블 요소 삭제
cursor.execute("DELETE FROM tblAddr WHERE name='김상형'")
con.commit()
cursor.close()
con.close()