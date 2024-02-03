#crawling
import requests
from bs4 import BeautifulSoup

url = 'https://www.musinsa.com/ranking/best?new_product_yn=Y'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'html.parser')
clothesList = soup.find(id='goodsRankList').find_all('li')

companyList = []
rank = 1
for index,item in enumerate(clothesList):
    company = item.select('.item_title > a')
    if company:
        companyList.append({'rank':rank, 'company':company[0].text})
        rank += 1
print(companyList)

