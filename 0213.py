import requests
from bs4 import BeautifulSoup
from multiprocessing import Process, Pool
import os


def request_fun(html):
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    req = requests.get(url=html, headers=header)
    req.encoding = 'utf-8'
    soups = BeautifulSoup(req.text, 'lxml')
    return soups


htmls, counts = [], 0
titles,hts = [], []
first_html = "https://search.bilibili.com/all?keyword=老男孩Python3.5自动化开发运维S14"
first_html2 = first_html + "&page=2"
first_req = request_fun(first_html)
first_req2 = request_fun(first_html2)
for i in first_req.find_all("a", {'class': 'title'}):
    second_html = 'https://' + i['href'][2:i['href'].find('?')]
    second_req = request_fun(second_html)
    start1 = second_req.title.string.find(u'共')
    start2 = second_req.title.string.find(u'章')
    start3 = second_req.title.string.find(u'第')
    start4 = second_req.title.string.find(u'周')
    chapters = (second_req.title.string[start1 + 1:start2])
    chapters2 = (second_req.title.string[start3 + 1:start4])
    titles.append(chapters2)
    for ii in range(1, int(chapters) + 1):
        htmls.append(i['href'][2:i['href'].find('?')] + '?p=' + str(ii))
    hts.append(i['href'][2:i['href'].find('?')])
for i in first_req2.find_all("a", {'class': 'title'}):
    second_html = 'https://' + i['href'][2:i['href'].find('?')]
    second_req = request_fun(second_html)
    start1 = second_req.title.string.find(u'共')
    start2 = second_req.title.string.find(u'章')
    chapters = (second_req.title.string[start1 + 1:start2])
    for ii in range(1, int(chapters) + 1):
        htmls.append(i['href'][2:i['href'].find('?')] + '?p=' + str(ii))

htmls2 = ['https://www.bilibili.com/video/av22425490/?p=3', 'https://www.bilibili.com/video/av22425490/?p=9', 'https://www.bilibili.com/video/av22474469/?p=8','https://www.bilibili.com/video/av22474469/?p=11','https://www.bilibili.com/video/av22474469/?p=14']
# print(sorted(htmls.items(),key=lambda d: int(d[1]['章節'])))
print(titles)
print(hts)
def StartSh(htmls):

    os.system("{0} {1}".format('you-get',htmls))

#
if __name__ == "__main__":
    p = Pool(50)
    # print(1)
    p.map(StartSh,htmls2)
