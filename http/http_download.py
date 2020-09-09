from bs4 import BeautifulSoup
import re
import urllib.request
from urllib.request import urlopen
import os

# 매개변수 다운로드
image_type = "Project"
movie = "Avatar"
url = "https://www.google.com/search?q="+movie+"&source=lnms&tbm=isch"

# URL 매개변수와 적절한 헤더로 Beatiful Soup 객체를 생성한다.
# requests 모듈은 HTTP 호출을 생성하는 동안 자신의 User-Agent를 사용한다.
# 요청 환경 설정 후 요청하기
header = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(
    urlopen(urllib.request.Request(url, headers=header)), 'lxml')

# 이미지 소스의 url을 얻는 방법
images = [a['src'] for a in soup.find_all(
    "img", {"src": re.compile("gstatic.com")})][:5]
for img in images:
    print("Image Source:", img)

# read(): 원시 형식의 이미지를 이진 데이터로 반환해서, 로커 파일 시스템의 파일에 기록
for img in images:
    raw_img = urlopen(img).read()
    cntr = len([i for i in os.listdir(".") if image_type in i]) + 1
    f = open(image_type + "_" + str(cntr)+".jpg", 'wb')
    f.write(raw_img)
    f.close()
