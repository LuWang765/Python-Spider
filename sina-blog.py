import urllib.request
import urllib.error
from html.parser import HTMLParser
import os
import time
import re

#在这个爬虫中，主要用的正则表达式获取博客内容；有一个为解决问题是HTMLParser中data只能输出被<br />切割的第一部分（已经编出输出data的class）。


class sina_spider():

    #def __init__(self,url):

        #self.url=url


    def get_html(self,url):

        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        req=urllib.request.Request(url=url,headers=header)

        try:
            response=urllib.request.urlopen(req)
            html=response.read().decode('utf-8')
            return html
        except urllib.error.HTTPError as e:
            if hasattr(e,'reason'):
                print('The http reason is: ',e.reason)
        except urllib.error.URLError as e:
            if hasattr(e,'reason'):
                print('The url reason is: ',e.reason)

    def get_title(self,url):

        html=self.get_html(url)
        entire_title=re.search(r'<title>(.*?)</title>',html,re.S).group(1)
        title=re.sub('_韩寒_新浪博客','',entire_title)
        print (title)

    def get_content(self,url):
        html=self.get_html(url)
        content_url=re.search(r'content="format=html5; url=(.*?)">',html).group(1)
        print(content_url)
        content_html=self.get_html(content_url)
        content=re.search(r'<div class="content b-txt1">(.*?)<!-- 广告 -->',content_html,re.S).group(1)
        content=re.sub(r'<br />','',content)
        print(content.strip())
        #hp=htmlpaser()
        #hp.feed(content_html)
        #hp.close()

def get_blog(url):
    url_circulation='http://blog.sina.com.cn/s/blog_4701280b0102ek51.html'
    while url_circulation:
        sina_spider().get_title(url_circulation)
        sina_spider().get_content(url_circulation)

        html=sina_spider().get_html(url_circulation)
        url_circulation=re.search(r'后一篇：</span><a href="(.*?)">',html,re.S).group(1)
        print(url_circulation)




class htmlpaser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.select=False

    def handle_starttag(self, tag, attrs):
        if tag=='div':
            if ('class','content b-txt1') in attrs:
                self.select=True

    def handle_endtag(self, tag):
        if tag!='/div':
            self.select=False

    def handle_data(self, data):
        if self.select:
            print(data.strip())



if __name__=='__main__':
    url='http://blog.sina.com.cn/s/blog_4701280b0102ek51.html'
    #ss=sina_spider()
    #ss.get_title(url)
    #ss.get_content(url)
    get_blog(url)




