#mmspiter
---
#所用的库
---
- `urllib`
- `urllib2`
- `BeautifulSoup`
- `Queue`
- `threading`

#抓取过程
---
    1. 首先找到能遍历完网站数据的链接：通过观察分析mm网站，找到 ‘推荐图片’ 页面在网站更新数据后都会在这个页面展现。
    2. 其次通过分析推荐图片的每一页，提取出每一页中对应的所有大图的详细展示页面，到达图片的详细页面。
    3. 进入到详细页面，分析发现大图url都在经过js处理，并且在script标签中，其中的url也不全正确。
    4. 分析源码的script标签与浏览器正确解析的imgurl对比，发现只需进行提取源码的script标签中的imgurl并将错误的big字段替换为pic就行。

    5. 继续分析script标签发现一组图片的url都在该组图片最后一张的源码script标签中，利用正则进行取出。

#执行过程
---
    1. 程序初始化对象mm，通过指定图片的数量（limit），默认不限制数量（整个网站图片），得到一个多于图片数量的page=(limit/400)+1页（经过计算大概每页460张图片左右），以减少对图片的详细展示页面url解析。
    2. 调用主函数mainprocess，传入对象，网站线程数（默认10），指定目录文件夹（默认pics），图片数量。
    3. 使用队列，运行多线程抓取数据，调用detail_url方法得到指定页返回的详细url并放入队列。
    4. 线程从每一个队列中取出单个url，调用img_url方法得到整组图片的真实url，将所有的imgurl合并到img_urls列表。
    5. 循环下载保存到文件夹中。
    

#用法
---
    ➜  mm_crawler git:(master) ✗ python spiter.py -h
    Usage: spiter.py [options]

    Options:
      -h, --help            show this help message and exit
      -n NUM, --number=NUM  Specify the number of concurrent threads
      -o other, --other dir=other
                            Specify the picture is stored in the directory
      -l LIMIT, --limit=LIMIT
                            limiting the number of pictures
#正在
---
1. 完善优化代码，进行单元测试。
2. 使用django框架做web app。

#后期
---
- 考虑扩展性准备用使用Selenium和PhantomJS解析带JS的网页。
 

