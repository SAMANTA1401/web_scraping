import requests
from bs4 import BeautifulSoup

with open("sample.html") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title.string, type(soup.title.string))
# print(soup.div)
# print(soup.find_all('div')[0]) # returns a list  class_='article_content'
# print(type(soup.find_all('div')[0]))

