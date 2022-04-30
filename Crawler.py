#抓取原始碼 (HTML)
import urllib.request as Req
url = "https://www.ptt.cc/bbs/movie/index.html"
#建立一個 Request 物件, 附加 Header 的資訊--->由瀏覽器內找尋, 用哪個瀏覽器,哪種系統...等等資訊
request = Req.Request(url, headers ={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"})

#with Req.urlopen(url) as Resp:
with Req.urlopen(request) as Resp:

    data = Resp.read().decode("utf-8")
#print(data)    

#解析原始碼 (HTML)
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
print(root.title) 
print(root.title.string) 
#
titles = root.find("div", class_="title") #找  div 標籤, 篩選條件 class = title
print(titles)  
print(titles.a.string)  
print("========================================")  
#
titles = root.find_all("div", class_="title") #找  div 標籤, 篩選條件 class = title
#print(titles)  
for title in titles:
    if title.a != None: #沒有被刪除
        print(title.a.string)  
