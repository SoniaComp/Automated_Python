import bs4
myfile = open('html_python.html')
soup = bs4.BeautifulSoup(myfile, 'lxml')
# 항상 파서를 정의해야 한다.
# 파서는 질의 데이터가 쉽게 처리되기 위한 지정된 형식의 파일을 읽도록 도와준다.

print("\nBeautifulSoup Object:", type(soup))
print(soup.find_all('h3')[0].getText())