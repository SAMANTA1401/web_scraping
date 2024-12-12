import requests

url = 'https://timesofindia.indiatimes.com/technology/tech-news/us-may-ban-follow-indias-ban-on-another-chinese-technology-giant/articleshow/116223973.cms'
r = requests.get(url)

import requests
def fetchandsave(url,path):
    r = requests.get(url)
    with open(path, 'w') as f:
        f.write(r.text)

fetchandsave(url, 'data/article.html')

#zenrows proxy

proxy = "http://5990352685421c3bc23ace4cb8d626594e4f826e:@api.zenrows.com:8001"
proxies = {"http": proxy, "https": proxy}

response = requests.get(url, proxies=proxies, verify=False)
print(response.text)