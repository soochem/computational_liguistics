'''
twitter 크롤링
'''

import tweepy
import time

# 트위터 앱의 Keys and Access Tokens 탭 참조(자신의 설정 값을 넣어준다)
consumer_key = ""
consumer_secret = ""

# 1. 인증요청(1차) : 개인 앱 정보
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = ""
access_token_secret= ""

# 2. access 토큰 요청(2차) - 인증요청 참조변수 이용
auth.set_access_token(access_token, access_token_secret)

# 3. twitter API 생성
api = tweepy.API(auth)

keyword = "comfortable"     # 자신이 검색하고 싶은 키워드 입력
search = [] # 크롤링 결과 저장할 변수

cnt = 1
while(cnt <= 150):   # 10page 대상으로 크롤링
   tweets = api.search(keyword)
   for tweet in tweets:
       search.append(tweet)
   cnt += 1
   time.sleep(1.3)

print(len(search)) # 문서 길이
print(search[0]) # 첫번째 text 보기
'''
data = {}   # 전체 문서 추가
i = 0       # 문서 번호
for tweet in search:
    data['text'] = tweet.text   # text키에 text문서 저장
    print(i, " : ", data)   # 문서번호 : 문서내용
    i += 1
'''
# 전체 문서를 파일 저장

import os

wfile = open(os.getcwd()+"/twitter.txt", 'w',encoding='utf-8')   # 쓰기 모드
data = {}   # 전체 문서 추가
i = 0       # 문서 번호

for tweet in search:
    s = tweet.text.replace('\n',' ')
    data['text'] = s   # text키에 text문서 저장
    #s = str(data['text'].encode('ascii'))
    #s = str(data['text'].encode('UTF-8')\ + b"\n")
    #data['text']=data['text'].encode('UTF-8')+b"\n"
    wfile.write(data['text']+'\n')  # 파일 출력
    i += 1

wfile.close()


