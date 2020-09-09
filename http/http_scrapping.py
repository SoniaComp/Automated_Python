from lxml import html
import requests

page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)
# fromstring(): 페이지의 컨텐츠를 html 형식으로 변환하여 트리를 가져옴
print("Page Obejct:", tree)
plans = tree.xpath('//h3[@class="h2-mktg text-bold mt-1"]/text()')
# Xpath로 선택한 후, text()로 텍스트 데이터를 반환했다.
pricing = tree.xpath('//span[@class="default-currency"]/text()')
print("Plans:", plans, "\nPricing:", pricing)
