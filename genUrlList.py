#coding=utf-8
#!/usr/bin/python

from lxml import etree
tree = etree.parse("public/sitemap.xml")
root = tree.getroot()

rstFile = open('public/sitelist.txt', 'w+')
urls = []
for url in root:
    for child in url:
        if child.tag == '{http://www.sitemaps.org/schemas/sitemap/0.9}loc':
            urls.append(child.text + '\n')
            rstFile.write(child.text + '\n')
rstFile.close()

body = ''.join(urls)
print body

import httplib, urllib
headers = {"Content-type": "text/plain",  "Accept": "text/plain", 'User-Agent': 'curl/7.12.1' }
conn = httplib.HTTPConnection("data.zz.baidu.com")
conn.request("POST", "/urls?site=tyan.io&token=2Po8M2T4ijaQqxed", body)
response = conn.getresponse()
print response.status, response.reason + '\n', response.read()
