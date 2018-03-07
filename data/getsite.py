# !/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re

headers = {
    'Cookie': "PHPSESSID=u6u34bd05vrf2p6s3t2gg88d57; ZH=b003fb2243b1fcf733cc0376f0137a27"}
urls = [
    "http://www.zone-h.org/archive/special=1/page={}?zh=1".format(x) for x in range(1, 2)]
f = open('defaced_sites.txt', 'w')
for url in urls:
    res = requests.get(
        "http://www.zone-h.org/archive/special=1/page=1?zh=1", headers=headers)
    domain_list = re.findall(
        '<a[\s]*href="/mirror/id/(.*?)">', res.text)  # 保留小数点
    # domain_list = re.findall('border="0"></td>\s*<td>(.*?)\.*[\s]*</td>',res.text) #不保留小数点
    # domain_list = re.findall(
    #     'border="0"></td>\s*<td>(.*?)[\s]*</td>', res.text)  # 保留小数点
    print domain_list.__len__(), "results found:"
    for t in domain_list:
        print t
        rr = requests.get(
            "http://www.zone-h.org/mirror/id/{}".format(t),
            headers=headers
        )
        domain = re.findall(
            '<strong>Domain:</strong> (.*?)</li>',
            rr.text
        )
        f.write(domain[0] + "\n")
