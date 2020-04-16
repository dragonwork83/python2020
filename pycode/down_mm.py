'''
@Author: your name
@Date: 2020-04-12 13:37:59
@LastEditTime: 2020-04-12 13:38:52
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python2020/pycode/down_mm.py
'''

import requests
from bs4 import BeautifulSoup

#爬取网页的通用代码框架
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()    #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "状态异常"
def get_list(text):
    #print(text)
    connect = BeautifulSoup(html,"html.parser")
    print(connect.a)

if __name__ == "__main__":
    url = "https://smtmm.win"
    html_text = getHTMLText(url)
    get_list(html_text)