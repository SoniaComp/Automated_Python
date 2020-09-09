# Automated_Python

## 파이썬은 가상환경 설치
$ virtualenv env

$ source evn/bin/activate

### pip install 설치한 모듈
* PyPDF2

## 이메일
MIME(Multipurpose internet Mail Extensions): 서식 있는 텍스트 및 첨부파일

FTP(File Transfer Protocol): 컴퓨터 간의 메시지 전송

SMTP(Simple Mail Transfer Protocol): 이메일 작업에서 가장 널리 사용되는 프로토콜

## SMS
평문 및 CSV(comma-separated value) 파일을 사용한 작업을 살펴본 다음 범위를 확장해 엑셀 워크 시트, 워드문서 및 PDF 파일 작업에 대해 살펴봄
```
$ pip install falsk
$ pip install Twilio
```

$ ngrok 소프트웨어

로컬 머신을 인터넷으로 터널링하는 것을 도와준다. 이는 NAT 혹은 방화벽 뒤에 있는 로컬 서버를 인터넷에 노출할 수 있음을 의미한다.
정말로 강력한 유틸리티다! 

## 음성 메시지
VoIP: Voice over Internet Protocol의 약어

인터넷 자체와 같은 인터넷 프로토콜 네트워크를 통해 음성 및 멀티미디어를 전송하는데 사용되는 기술

## HTTP
HTTP 요청으로 데이터를 검색하거나 페이지와 이미지를 다운로드 할 수 있을 뿐만 아니라 정보 수집을 위한 페이지 콘텐츠를 파싱하고 파이썬으로 의미있는 통찰력을 생성하고자 분석할 수 있다.

파이썬 모듈: requests, urlib2, lxml, BeautifulSoup4, selenium

#### HTTP
WWW의 데이터 통신을 위한 비상태 애플리케이션 프로토콜. 적형적인 HTTP 세션은 연속적인 요청 혹은 응답 트랜잭션을 포함한다.

클라이언트는 특정 IP 및 포트의 서버에게 TCP 연결을 시작한다.

HTTP는 주어진 웹 URL에서 수행될 액션을 나타내는 요청 메소드를 정의한다.


#### 웹 스크래핑
컴퓨터 프로그램을 이용해 정해진 형식의 필요한 정보를 추출하려는 의도로 웹 사이트 페이지를 분리하는 방법

cf. 웹 크롤링: 엡 인덱싱을 목적으로 웹을 체계적으로 탐색하고 사용자가 웹을 좀 더 효과적으로 검색할 수 있도록 웹 페이지 색인을 위한 검색엔진에서 사용되는 봇이 웹을 탐색하는 것

적법성
* https://www.quora.com/What-is-the-legality-of-web-scraping
* https://en.wikipedia.org/wiki/Web_scraping#Legal_issues

```
$ pip install lxml, requests
```

#### 웹 컨텐츠 파싱 및 추출
웹 스크래핑은 추출을 포함하기 때문에, 흥미로운 데이터를 얻기 위해 웹 페이지의 HTML 콘텐츠를 파싱하기 전까지는 웹 스크래핑은 발생할 수 없다.
```
$ pip install beautifulsoup4
```

#### 웹 컨텐츠 다운로드
표준 라이브러리인 urllib를 사용해보자

#### 써드파티 REST API 작업
깃허브 기스트: 작업을 공유하는 가장 좋은 방법
개념을 이해할 수 있는 여러 파일로 동료 혹은 작은 앱에 도움을 주는 작은코드
깃헙은 기스트의 생성, 목록조회, 삭제, 수정을 허용하며, 
기스트를 생성, 수정, 목록조회, 삭제해본다.

#### 비동기 HTTP
동기식 방식으로 웹 어플리케이션을 개발하면 클라이언트가 요청할 때마다 서버는 데이터 베이스 혹은 네트워크를 통해 I/O 호출을 생성해 정보를 검색한 다음 다시 클라이언트에게 제공한다. 이러한 I/O 호출을 생성해 정볼르 검색한 다음 다시 클라이언트에게 제공한다. 웹 서버는 클라이언트의 여러 요청을 처리하는 스레드 풀을 유지한다. 서버가 요청을 처리할 수 있을 만큼 오래 대기하면 스레드 풀이 곧 소진되어 서버는 중단될 수 있다.

토네이도: 논블로킹 네트워크 I/O를 사용하고 수만개의 실시간 연결로 확장 문제를 해결한다.

토네이도는 싱글스레드 이벤트 루프의 방식으로 작동한다. 이 이벤트 루프는 계속 이벤트 폴링하여 해당 이벤트 핸들러로 전달한다.

ioloop로 실행하는 request와는 달리, 일반적인 동기 웹 서버는 이 I/O 호출의 응답을 기다리고 요청 스레드를 블록한다. 비동기 프레임워크인 토네이도는 작업을 트리거하고, 큐에 추가하고, I/O 호출을 생성하고, 실행 스레드를 이벤트 루프로 반환한다.

이벤트 루프는 계속해서 작업 큐를 모니터링 하고 I/O 호출의 응답을 폴링한다.
이벤트가 사용가능한 경우에는 이벤트핸들러인 async_callback()을 실행해 콘텐츠와 응답을 출력한 다음 이벤트 루프를 중지한다.

토네이도 같은 이벤트 기반 웹 서버는 커널 수준 라이브러리를 사용해 이벤트를 모니터링한다. kqueue, epoll

* kqueue:https://linux.die.net/man/4/epoll
* freebsd:https://www.freebsd.org/cgi/man.cgi?kqueue

#### 셀레늄을 이용한 웹 자동화
엡에 로그인이 필요한 경우. 브라우저 자체를 제어하는 것은 어떤가

셀레늄: 브라우저를 펼치게 해주어 사람이 그것을 수행하는 것처럼 작업하도록 돕는다. 셀레늄은 파이어 폭스, 크롬, 사파리, 인터넷 익스플로러처럼 가장 널리 사용되는 브라우저를 지원한다.

