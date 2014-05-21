#coding:utf-8

import sys
import urllib2
import re

try:
    from bs4 import BeautifulSoup
except ImportError:
    print "Sorry we need BeautifulSoup4 !!"
    print "please install it!('sudo pip install BeautifulSoup4')"
    sys.exit()


def max_page():

    one_page = 35

    url = 'http://www.22mm.cc/mm/top/rec.html'

    try:
        html = urllib2.urlopen(url)
    except:
        return
    soup = BeautifulSoup(html)
    showpage = soup.find_all('div',{'class':'ShowPage'})
    for s in showpage:
        if s.find('span'):
            span = s.find('span')
            break
    group = []
    for i in span.text:
        group.append(i)
    group = int(''.join(group[1:5]))
    max_page = group/one_page+1

    return max_page

class Mm(object):
    """
        Initialize the entire site, get all kinds of ways to solve the problem web crawling
    """
    def __init__(self,page=97):
        self.page = page

    def begin_url(self):

        """
            Been designated to crawl the page url, returns a list
        """
        base_url = 'http://www.22mm.cc/mm/top/rec_'
        postfix_url = '.html'
        first_url = 'http://www.22mm.cc/mm/top/rec.html'
        list_url = [first_url]




        for i in range(2,self.page+1):
            list_url.append(base_url+str(i)+postfix_url)
        print list_url
        # import pdb;pdb.set_trace()
        return list_url

    def detail_url(self):
        """
            from begin_url
        """
        detail_page = []
        domain_url = 'http://www.22mm.cc'
        for url in self.begin_url():
            try:
                html = urllib2.urlopen(url,timeout=5)
            except IOError:
                continue
            soup = BeautifulSoup(html)

            for ul in soup.find_all('ul',{'class':'pic'}):
                for a in ul.find_all('a',href=True):
                    detail_page.append(domain_url+a['href'])
        print detail_page

        return detail_page





    def img_url(self,url):
            try:
                html = urllib2.urlopen(url,timeout=5)
            except IOError:
                return
            list_url = url.split('/')
            list_url.pop()
            soup = BeautifulSoup(html)
            all_url = []

            if soup.find_all('div',{'class':'lipagenum'}):
                lipagenum = soup.find_all('div',{'class':'lipagenum'})
                for atag in lipagenum:
                    for a in atag.find_all('a'):
                        all_url.append(a['href'])

                last_url = all_url[-1]
            else:
                pagelist = soup.find_all('div',{'class':'pagelist'})
                for atag in pagelist:
                    for a in atag.find_all('a'):
                        all_url.append(a['href'])

                last_url = all_url[-2]

            list_url.append(last_url)
            new_url = '/'.join(list_url)
            # http://www.22mm.cc/mm/bagua/gehdhdcl_lekid-5.html
            # 得到最后当前组的最后一页的详细页面地址。
            try:
                html = urllib2.urlopen(new_url,timeout=5)
            except IOError:
                return
            soup = BeautifulSoup(html)
            script = str(soup.find_all('script'))

            rec = re.compile('(http://[^; ,\'"<>|\[\]]+\.(jpg|png|gif))')
            re_url = rec.findall(script)
            list_url = [ s[0].replace('big', 'pic') for s in re_url ]
            print '正在解析一组图片的url:'+ str(list_url)
            return list_url










