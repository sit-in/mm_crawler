#coding:utf-8

import Queue
import threading
import string
import urllib
import os

from mm.mm import Mm

mm = Mm()

img_urls = []

class ThreadUrl(threading.Thread):
    """ docstring for ThreadUrl:

            ThreadUrl Inherited thread,to run multi-threaded
            list_url : this is a list.
    """
    def __init__(self, queue,site):
        self.queue = queue
        self.site = site
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                url = self.queue.get()
                list_url = self.site.img_url(url)
                img_urls.extend(list_url)
            except:
                pass
            self.queue.task_done()

def mainprocess(website=mm,num=10,limit=None,newdir='pics'):
    """
        docstring for mainprocess:
            1.Used Queue,running multi-threaded crawl,
                the default number of threads is 10.
            2.website is from all kinds of customize website,default MM.

    """
    queue = Queue.Queue()

    for i in range(num):
        t = ThreadUrl(queue,website)
        t.setDaemon(True)
        t.start()

    for url in website.detail_url():
        queue.put(url)
        queue.join()

    if not os.path.exists(newdir):
        os.makedirs(newdir)

    os.chdir(newdir)
    i = 1

    for img_url in img_urls:
        filename = string.zfill(000000+i,6)+'.'+ img_url.split('.')[-1]
        print "开始下载： %s" % img_url
        try:
            urllib.urlretrieve(img_url,filename)
            i = i + 1
        except IOError:
            continue
        print "已经保存在：%s目录文件名 %s" % (newdir,filename)
        if limit and i == limit+1:
            break

if __name__ == "__main__":
    mainprocess(mm)
