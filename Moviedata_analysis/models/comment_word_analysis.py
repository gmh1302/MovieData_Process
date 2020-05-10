import pymysql
from konlpy.tag import Okt

def getConnection():
    # 연결시에 바로 호스트와 포트 유저 정보, 데이터베이스와 인코딩정보를 설정할 수 있다. 또한 자동으로 commit()을 해줄수도 있으며, 넘겨줄 데이터를 자동으로 dict 형태로 넘겨줄 수도 있다.
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='1234', db='moviedata', charset='utf8')
    return conn

def create_word_cloud():
    rank_word = "최고 냄새 재밌게 몰입 소름 가난 별로 명작 긴장감 불편한 스릴러 비극 풍자 감탄 디테일 찝찝한"
    wordcloud = WordCloud(font_path='font/NanumGothic.ttf', background_color='white').generate(rank_word)

    plt.figure(figsize=(22,22)) # 이미지 사이즈 지정
    plt.imshow(wordcloud, interpolation='lanczos') # 이미지의 부드럽기 정도
    plt.axis('off') # x y축 숫자 제거
    plt.show()
    plt.savefig()

# def comment_all_num(): # 댓글의 총 갯수를 구하는 함수
#     try:
#         conn = getConnection()
#         cursor = conn.cursor()
#         sql = "select count(*) from movie_score"
#         result = cursor.execute(sql)
#         cursor.close()
#         all_num = cursor.fetchall()[0][0]
#         print("Success")

#     except Exception as e :
#         print("Error ====", e)
#     finally :
#         conn.close()

#     return all_num


# def comment_tp_insert(tp): # 빈출 단어 데이터를 DB에 삽입하기 위한 함수
#     print(tp)
#     try :
#         conn = getConnection()
#         cursor = conn.cursor()
#         for i in range(0,len(tp)):
#             sql = "insert into comment_word_rank(idx, word, word_num) values (%s,%s,%s)"
#             cursor.execute(sql,(i,tp[i][0],tp[i][1]))
#         conn.commit()
#     except Exception as e :
#         print("Error ====", e)
#     finally :
#         conn.close()
#     return 'completed'


# def comment_word_select(all_num): # 오스카 수상일 이전/이후의 댓글 단어를 도출하는 함수
#     dict = {}
#     okt = Okt()

#     conn = getConnection()
#     cursor= conn.cursor()
#     sql = "select comm from movie_score"

#     result = cursor.execute(sql)

#     cursor.close()
#     tup = cursor.fetchall()

#     for i in range(0, all_num):
#         lst = []
#         cmt = tup[i][0]
#         for val in okt.pos(cmt):
#             if val[1] == 'Noun' or val[1] == 'Adjective': lst.append(val[0])
#         for val in lst:
#             if val not in dict: dict[val] = 1 # 만약 딕셔너리에 없으면 단어 추가 후 1을 대입
#             else: dict[val]+=1 # 딕셔너리에 있을 경우 1을 증가시킴.
#         print('i = ', i)

#     tp = sorted(dict.items(), key=lambda x:x[1], reverse=True) # 단어 빈출이 높은 순으로 나열
#     return tpz