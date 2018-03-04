# -*- coding:utf-8 -*-
import os

url = 'http://www.jianshu.com/p/c712b9c2700c?open_source=weibo_search'
os.system(
    '/Users/yhs/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs snapshot.js {} test.png'.format(url))
