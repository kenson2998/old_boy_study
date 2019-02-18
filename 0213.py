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
first_html = "https://search.bilibili.com/all?keyword=老男孩Python3.5自动化开发运维S14"
first_html2 = first_html + "&page=2"
first_req = request_fun(first_html)
first_req2 = request_fun(first_html2)
for i in first_req.find_all("a", {'class': 'title'}):
    second_html = 'https://' + i['href'][2:i['href'].find('?')]
    second_req = request_fun(second_html)
    start1 = second_req.title.string.find(u'共')
    start2 = second_req.title.string.find(u'章')
    chapters = (second_req.title.string[start1 + 1:start2])
    for ii in range(1, int(chapters) + 1):
        htmls.append(i['href'][2:i['href'].find('?')] + '?p=' + str(ii))
for i in first_req2.find_all("a", {'class': 'title'}):
    second_html = 'https://' + i['href'][2:i['href'].find('?')]
    second_req = request_fun(second_html)
    start1 = second_req.title.string.find(u'共')
    start2 = second_req.title.string.find(u'章')
    chapters = (second_req.title.string[start1 + 1:start2])
    for ii in range(1, int(chapters) + 1):
        htmls.append(i['href'][2:i['href'].find('?')] + '?p=' + str(ii))

print(2)
# print(sorted(htmls.items(),key=lambda d: int(d[1]['章節'])))
def StartSh(htmls):

    os.system("{0} {1}".format('you-get',htmls))
    print(2)

#
if __name__ == "__main__":
    p = Pool(50)
    print(1)
    p.map(StartSh,htmls)
