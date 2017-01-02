import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import os
import time

#在这个爬虫程序中，使用BeautifulSoup不能获得完整的html文本，待解决！

class sina_blog():

    def __init__(self):
        pass
    # obtain html text by parsing given url
    def get_html(self,url):
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        req=urllib.request.Request(url=url,headers=header)

        try:
            response=urllib.request.urlopen(req)
            html=response.read().decode('utf-8')
            return html
        except urllib.error.HTTPError as e:
            if hasattr(e,'reason'):
                print('The HTTPError reason is: ',e.reason)
        except urllib.error.URLError as e:
            if hasattr(e,'reason'):
                print('The URLError reason is: ',e.reason)

    # obtain blog title by using BeautifulSoup
    def get_title(self,url):
        html=self.get_html(url)
        time.sleep(1)
        soup=BeautifulSoup(html,"html.parser")
        print('#####',soup,'luwang')
        tag=soup.title
        return tag.string

        #if tag['class']=='blog_title':
           #return tag.string

    # obtain blog content by using BeautifulSoup
    def get_content(self,url):
        html=self.get_html(url)
        soup=BeautifulSoup(html,"html.parser")
        print(soup.prettify())
        tag=soup.find('div',class_="articalContent   ")
        return tag#.string


    def save_article(self,url):
        folder='blog_article2'
        os.mkdir(folder)
        os.chdir(folder)

        title=self.get_title(url)
        content=self.get_content(url)
        name=title+'.txt'
        with open(name,'wb') as f:
            title= str(title).encode('utf-8')
            f.write(title)
            f.write(content)


if __name__=='__main__':
    url='http://blog.sina.com.cn/s/blog_4701280b0102eo83.html'
    blog=sina_blog()
    blog.save_article(url)


