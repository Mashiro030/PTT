import requests
from bs4 import BeautifulSoup

url="https://www.ptt.cc/bbs/PC_Shopping/index.html"
domain='https://www.ptt.cc'
def get_all_href(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    results = soup.select("div.title")#抓標題，用css選取

    for item in results:#抓取頁面每一篇文章的連結
        there_is_a_item = item.select_one("a")
        title = item.text
        if there_is_a_item:#確認文章有沒有被刪除
            article_url=there_is_a_item.get('href')
            print(title, domain + article_url)
        
for page in range(1,4):#抓取前3頁的路徑 例如:https://www.ptt.cc/bbs/PC_Shopping/index4402.html....
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    btn = soup.select('div.btn-group.btn-group-paging > a')#上一頁按鈕，選取div且class=btn-group.btn-group-paging 子節點為a 
    up_page_href = btn[1]['href']
    next_page_url = domain + up_page_href
    url = next_page_url
    get_all_href(url = url)#呼叫函式

def get_article_info(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, "lxml")
    results = soup.select('span.article-meta-value')
    if results:
        print('作者:', results[0].text)
        print('看板:', results[1].text)
        print('標題:', results[2].text)
        print('時間:', results[3].text)
        
for page in range(1,4):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    results = soup.select('div.title')
    for item in results:#抓取頁面每一篇文章的連結
        there_is_a_item = item.select_one("a")
        title = item.text
        if there_is_a_item:#確認文章有沒有被刪除
            article_url=there_is_a_item.get('href')
            get_article_info(article_url=domain+there_is_a_item.get('href'))






