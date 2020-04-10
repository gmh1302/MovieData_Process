from bs4 import BeautifulSoup as bs
from konlpy.tag import Okt
import requests


url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=161967&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=newest"
html = bs(requests.get(url).content, "html.parser", from_encoding="utf-8")
cnt = html.select("body > div > div > div.score_total > strong > em")[0].contents[0].replace(',','')

lst = []; dict = {}
okt = Okt()

for x in range(244,int(cnt)//10+2): # 244페이지부터 수상일 이전의 댓글이 존재합니다. 1부터 돌리기에는 시간이 너무 오래걸려서 융통성있게 244부터 시작했습니다.
    html  = bs(requests.get(url + "&page=" + str(x)).content, "html.parser", from_encoding="utf-8")
    size = len(html.select("body > div > div > div.score_result > ul > li > div.score_reple > p")) # 페이지당 댓글의 수만큼 for문을 돌리도록 설정(마지막 페이지에 댓글이 10개가 아닐 수도 있기 때문)

    for i in range(1,size+1):

        #유저의 리뷰를 단 날짜 크롤링 코드
        date    = html.select("body > div > div > div.score_result > ul > li:nth-of-type("+str(i)+") > div.score_reple > dl > dt > em:nth-of-type(2)")[0].contents[0]
        date2   = int(date[0:10].replace(".", ""))

        # 네이버 영화 댓글 크롤링 코드
        comment_line = html.select("body > div > div > div.score_result > ul > li:nth-of-type("+str(i)+") > div.score_reple > p")[0]
        n = int(len(comment_line))
        comment = comment_line.contents[n - 2]
        if int(len(comment)) > 1:
            comment = comment.contents[1].contents[1].contents[0].strip()
        else:
            comment = comment.contents[0].strip()

        print(date2, '   ', comment)

        for val in okt.pos(comment): # konlpy 모듈을 사용했을 때, '명사' 혹은 '형용사'가 도출될 시, 리스트에 추가
            if val[1] == 'Noun' or val[1] == 'Adjective': lst.append(val[0])

for val in lst:
    if val not in dict: dict[val] = 1 # 만약 딕셔너리에 없으면 단어 추가 후 1을 대입
    else: dict[val]+=1 # 딕셔너리에 있을 경우 1을 증가시킴.
print(sorted(dict.items(), key=lambda x:x[1], reverse=True)) # 단어 빈출이 높은 순으로 나열
