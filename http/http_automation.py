from bs4 import BeautifulSoup
from threading import Thread
from urllib.request import urlopen
# 식당 위치
home_url = "https://www.yelp.com"
find_what = "Restaurants"
location = "London"

# 검색 기준과 일치하는 모든 식당을 가져온다.
search_url = "https://www.yelp.com/search?find_disc="+find_what+"&find_loc="+location
s_html = urlopen(search_url).read()
soup_s = BeautifulSoup(s_html, 'lxml')

# 런던의 상위 10개 식당의 URL을 가져온다.
s_urls = soup_s.select('a.lemon--a__09f24__IEZFH')[:10]
print(s_urls)
url = []
for u in range(len(s_urls)):
  url.append(home_url+s_urls[u]['href'])
print(url)

# 실제 스크래핑 작업을 수행하는 함수
def scrape(ur):
  html = urlopen(ur).read()
  soup = BeautifulSoup(html, "lxml")

  title = soup.select('.biz-page-title')
  saddress = soup.select('.street-address')
  phone = soup.select('.biz-phone')

  if title:
    print("Title:", title[0].getText().strip())
    print("--------")
  
threadlist = []
i = 0

# 스크래핑을 수행할 스레드 생성
while i<len(url):
  t = Thread(target = scrape, arges=(url[i],))
  t.start()
  threadlist.append(t)
  i = i+1

for t in threadlist:
  t.join()