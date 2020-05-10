import pymysql

def getConnection():
    # 연결시에 바로 호스트와 포트 유저 정보, 데이터베이스와 인코딩정보를 설정할 수 있다. 또한 자동으로 commit()을 해줄수도 있으며, 넘겨줄 데이터를 자동으로 dict 형태로 넘겨줄 수도 있다.
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='1234', db='moviedata', charset='utf8')
    return conn

def select_after_data(): # 오스카 수상일 이후 평균 평점을 구하기 위한 함수
    try:
        conn = getConnection()
        cursor= conn.cursor()
        sql = "select avg(score2) from movie_score WHERE date_time>=20200210 AND num<=20200427"
        cursor.execute(sql)
        avg_after = round(cursor.fetchone()[0],2)
        cursor.close()
        print("Success")
    except Exception as e :
        print("Error ====", e)
    finally :
        conn.close()
    return avg_after*10


def select_before_data(): # 오스카 수상일 이후 평균 평점을 구하기 위한 함수
    try:
        conn = getConnection()
        cursor= conn.cursor()
        sql = "select avg(score2) from movie_score WHERE date_time>=20190530 AND num<=20200208"
        cursor.execute(sql)
        avg_before = round(cursor.fetchone()[0],2)
        cursor.close()
        print("Success")
    except Exception as e :
        print("Error ====", e)
    finally :
        conn.close()
    return avg_before*10
