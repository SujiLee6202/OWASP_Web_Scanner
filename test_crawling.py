import requests
from bs4 import BeautifulSoup

print("<<owasp web scanner started>>")

print("목표 : 입력된 URL에 접속하고, 제목, 상태코드, 서버 정보 출력")
print('------------------------------------------------------------------')

url = 'https://news.naver.com/section/105'
response = requests.get(url) #GET 메소드를 사용하여 url에 HTTP Requests 전송->웹페이지 다운로드

if response.status_code == 200: #정상 응답 반환 시 아래 코드블록 실행
    soup = BeautifulSoup(response.content, 'html.parser') #응답 받은 HTML 파싱(목록을 트리구조로 분석함)
    titles = soup.select('div.sa_text') #파싱한 데이터 중 div clas = sa_text 인 데이터 저장/id : div#아이디명, class : div.클리스명

    print('******1. 웹사이트 정보******')
    print(f"접속 URL : {url}")
    print(f"상태 코드 : {response.status_code}") #response에서 상태코드 가져옴
    print(f"서버 정보 : {response.headers.get('Server', 'None')}") #response의 header 내용 중 Server만 가져오고 없으면 None올 표시
    
    print('******2. 기사 제목/요약 내용 크롤링(5개)******')
    for title in titles[:5]:
        print(f'기사 제목 : {title.select_one('strong.sa_text_strong').get_text()}') #.get_text() : 텍스트 데이터만 출력
        print(f'기사 내용 요약 : {title.select_one('div.sa_text_lede').get_text()}')
        print('------------------------------')
        
else:
    print('error') #오류 시 메시지 출력
    