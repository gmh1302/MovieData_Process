import requests
import bs4
import pandas as pd

cnt = 0
score_result = dict()

for page in range(1,10):
    url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=161967&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="+str(page)

    res = requests.get(url, format(1))
    obj = bs4.BeautifulSoup(res.text, 'xml')
    movie_data_list = obj.find_all('div', {'class':'score_result'})[0].find_all('li')

    for li in movie_data_list:
        score_result[cnt] = {'score': int(li.em.text),
                             'reple': li.p.text.strip()
                             'pf_reple' : }
        if score_result[cnt]['reple'][0:3] == '관람객':
            score_result[cnt]['reple'] = score_result[cnt]['reple'][3:]
            score_result[cnt]['reple'] = score_result[cnt]['reple'].lstrip()
        cnt+=1

##################### 데이터를 csv로 저장 #################

df = pd.DataFrame(score_result).T
print(df)
df.to_csv('score_result.csv', encoding='utf-8-sig')

########################################################

