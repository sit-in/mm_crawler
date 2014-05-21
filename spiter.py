#!/usr/bin/env python
# coding:utf-8

from optparse import OptionParser

from mm.mm import Mm,max_page
from mythread import mainprocess

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-n", "--number", dest="num",
                      help="Specify the number of concurrent threads", metavar="NUM")
    parser.add_option("-o", "--other dir", dest="otherdir",
                      help="Specify the picture is stored in the directory", metavar="other")
    parser.add_option("-l", "--limit", dest="limit",
                      help="limiting the number of pictures", metavar="LIMIT")

    (options, args) = parser.parse_args()
    num,limit,otherdir = options.num,options.limit,options.otherdir

    maxpage = max_page()

    if not num:
      num = 10
    else:
      num = int(num)
    if not limit:
      limit = ''
    else:
      limit = int(limit)
      page = (limit/400)+1  #计算每页图片在460左右，为保证解析的url大于用户指定的，取400
      if page > max_page:
        page = max_page

    if not otherdir:
      otherdir = 'pics'

    print "我们将解析：%d 页的图片URL链接。。。" % page
    mm = Mm(page)

    mainprocess(website=mm,num=num,limit=limit,newdir=otherdir)