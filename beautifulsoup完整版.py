import requests
from bs4 import BeautifulSoup

url="https://www.ptt.cc/bbs/PC_Shopping/index.html"
domain='https://www.ptt.cc'
for page in range(1,4): #抓取前3頁的路徑 例如:https://www.ptt.cc/bbs/PC_Shopping/index4402.html....
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    btn = soup.select('div.btn-group.btn-group-paging > a')
    up_page_href = btn[1]['href']
    next_page_url = domain + up_page_href
    url = next_page_url
    # print(url)

url="https://www.ptt.cc/bbs/PC_Shopping/index.html"
def get_all_href(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    results = soup.select("div.title")#抓標題，用css選取

    for item in results:#抓取頁面每一篇文章的連結
        there_is_a_item = item.select_one("a")
        title = item.text
        if there_is_a_item:#確認文章有沒有被刪除
            print(title, domain + there_is_a_item.get('href'))
        
for page in range(1,4):#抓取前3頁的路徑 例如:https://www.ptt.cc/bbs/PC_Shopping/index4402.html....
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    btn = soup.select('div.btn-group.btn-group-paging > a')#上一頁按鈕，選取div且class=btn-group.btn-group-paging 子節點為a 
    up_page_href = btn[1]['href']
    next_page_url = domain + up_page_href
    url = next_page_url
    get_all_href(url = url)#呼叫函式



