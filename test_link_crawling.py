import requests
from bs4 import BeautifulSoup

print("목표 : 입력된 URL 내 모든 링크 추출")
print('------------------------------------------------------------------')


url_list = []

url = input("URL을 입력 : ")
response = requests.get(url) #GET 메소드를 사용하여 url에 HTTP Requests 전송->웹페이지 다운로드

if response.status_code == 200: #정상 응답 반환 시 아래 코드블록 실행
    soup = BeautifulSoup(response.content, 'html.parser') #응답 받은 HTML 파싱(목록을 트리구조로 분석함)
    links = soup.find_all('a') #a href를 전부 찾는 것이므로 selec말고 find_all 사용

    print('******1. 웹사이트 정보******')
    print(f"접속 URL : {url}")
    print(f"상태 코드 : {response.status_code}") #response에서 상태코드 가져옴
    print(f"서버 정보 : {response.headers.get('Server', 'None')}") #response의 header 내용 중 Server만 가져오고 없으면 None올 표시
    
    print('******2. 링크 크롤링(5개)******')
    for link in links:
        href = link.get('href') #나중에 또 쓰기위해 가져온 href를 href에 담음
        
        if href and href != '#': # 빈값 제거를 위해 if문 사용, #나오길래 # 제거함
            url_list.append(href)
    for url in url_list:
        print(url)
    print('------------------------------')
    
else:
    print('error') #오류 시 메시지 출력
    