#coding=utf-8
#!/usr/bin/python

def getArchiveUrl(filepath):
    rst = []
    with open(filepath) as f:
        for line in f:
            rst.append(line)
    return rst


def readSiteMap(filepath):
       from lxml import etree
       tree = etree.parse(filepath)
       root = tree.getroot()

       rstFile = open('public/sitelist.txt', 'w+')
       urls = []
       for url in root:
           for child in url:
               if child.tag == '{http://www.sitemaps.org/schemas/sitemap/0.9}loc':
                   urls.append(child.text + '\n')
                   rstFile.write(child.text + '\n')
       rstFile.close()
       #return ''.join(urls)
       return urls

def getNewUrl(archiveUrl, urllib):
    rst = []
    for url in urllib:
        if url not in archiveUrl:
            rst.append(url)
    return rst

def push2Baidu(body):
    import httplib, urllib
    headers = {"Content-type": "text/plain",  "Accept": "text/plain", 'User-Agent': 'curl/7.12.1' }
    conn = httplib.HTTPConnection("data.zz.baidu.com")
    conn.request("POST", "/urls?site=tyan.io&token=2Po8M2T4ijaQqxed", body)
    response = conn.getresponse()
    print response.status, response.reason + '\n', response.read()

if __name__ == '__main__':
    archiveUrl = getArchiveUrl('urlarchive')
    urllist = readSiteMap('public/sitemap.xml')
    newUrl = getNewUrl(archiveUrl, urllist)



