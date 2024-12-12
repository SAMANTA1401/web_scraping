import requests
from bs4 import BeautifulSoup
import pandas as pd


#zenrows proxy
proxy = "http://5990352685421c3bc23ace4cb8d626594e4f826e:@api.zenrows.com:8001"
proxies = {"http": proxy, "https": proxy}


data = {'title': [], 'price': []}


url = "https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
r = requests.get(url,proxies=proxies,verify=False)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

# spans = soup.find_all(class_="KzDlHZ")
# for span in spans:
#     print(span.text)


spans = soup.select("div.KzDlHZ")
for span in spans:
    # print(span.string)
    data['title'].append(span.string)


prices = soup.select("div._4b5DiR")
for price in prices:
#     print(price.children[0].get_text())
    # print(price.find("span").get_text())
    data['price'].append(price.text)
    if len(data['price']) == len(data['title']):
        break



# for span,price in zip(spans,prices):
#     print(span.text,',',price.text) #,type(span.text))spans:


# for price in prices:
#     if("classname" in price.get("class")):
#         print(price.find("span").get_text())

print(len(data['title']), len(data['price']))

df = pd.DataFrame.from_dict(data)
df.to_csv('data/flipkart_mobile.csv', index=False)
df.to_excel('data/flipkart_mobile.xlsx', index=False)