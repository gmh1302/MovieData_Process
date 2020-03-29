import requests
import bs4
import pandas as pd

cnt = 0
score_result = dict()

for page in range(1,10):
    url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=161967&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="+str(page)
    # for문을 이용하여 url 마지막 page 부분에 숫자를 증가시켜 모든 페이지 데이터를 긁어올 수 있도록 하였다.
    res = requests.get(url, format(1))
    obj = bs4.BeautifulSoup(res.text, 'xml')
    movie_data = obj.find_all('div', {'class':'score_result'})[0].find_all('li') # 네티즌의 평점과 댓글 등이 담겨있는 부분을 딕셔너리로 담았다.

    for li in movie_data:
        score_result[cnt] = {'score': int(li.em.text),
                             'reple': li.p.text.strip() #댓글의 앞뒤 공백을 strip()함수를 통해 제거하였다.
                            } # score_result 딕셔너리에 네티즌의 '평점'과 '리뷰'를 담았다.
        
        if score_result[cnt]['reple'][0:3] == '관람객': # 등급이 '관람객'인 경우 댓글 앞에 표기가 되어 있어서 순수히 댓글만을 출력하기 위해 '관람객' 문자열을 제거
            score_result[cnt]['reple'] = score_result[cnt]['reple'][3:] # 관람객 문자열 이후의 댓글을 변수에 설정.
            score_result[cnt]['reple'] = score_result[cnt]['reple'].lstrip() #'관람객'글자를 제거한 후 공백이 포함되어 있는 댓글의 공백처리를 하였다.
        cnt+=1

##################### 데이터를 csv로 저장 #################

df = pd.DataFrame(score_result).T
print(df)
df.to_csv('score_result.csv', encoding='utf-8-sig')

########################################################

