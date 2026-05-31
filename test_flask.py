from flask import Flask, render_template, request #기능 : flask 웹서버 앱 생성, render_ index.html 불러옴, request 웹에 보낸 값 받음
import requests #웹사이트 html 가져오기
from bs4 import BeautifulSoup #가져온 html에서 태그 찾기 도구

app = Flask(__name__)   #flask 웹앱 생성

@app.route("/", methods=["GET", "POST"]) #주소로 접속했을 때 home() 실행
def home():
    url_list = [] #크롤링한 링크 담는 상자

    if request.method == "POST": # *처음 접속시에는 request.method의 값은 GET이라서 if request.method =="POST"가 false이다. scan 버튼 누르면 POST 요청을 Flask 서버로 보냄 -> TRUE 돼서 아래로 진입
        url = request.form.get("url")  # HTML input에서 가져온 값이 url 변수에 들어감

        try:
            response = requests.get(url)
            if response.status_code == 200: #접속 성공시
                soup = BeautifulSoup(response.content, 'html.parser')
                links = soup.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href and not href.startswith(('#', 'javascript')): #href가 존재하고, #으로 시작하지 않는 것 출력
                        url_list.append(href)
            else:
                url_list.append(f"Error: 상태 코드 {response.status_code}") #내 잘못 아닌듯
        except Exception as e:
            url_list.append(f"헐에러남???: {e}")

    return render_template("index.html", links=url_list) #templates의 index.html에 url_list를 links라는 이름으로 전달
    
if __name__ == "__main__": #이 파일을 직접 실행했을 때만 app.run~ 실행
    app.run(debug=True) #flask 서버 실행. 주소 : http://127.0.0.1:5000