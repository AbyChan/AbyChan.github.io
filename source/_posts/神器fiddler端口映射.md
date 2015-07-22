title: 神器fiddler端口映射
date: 2015-07-22 19:57:09
tags:

- fiddler
- 端口映射
- port forwarding
- prot mapping
---

在公司是在虚拟机上装linux来用的，而且是vmware player，做端口映射十分麻烦（好吧，其实是我不会用windows），想在手机上测试，于是麻烦来了。

折腾了好久，最终用fiddler来解决的，记录一下，突然发现会用windows还是挺牛逼的，呵呵。

###1·配置fiddler默认端口8888

###2·tools -> Fiddler Options 确认钩中Allow remote clients to connect

###3·rule -> customize rules

###4·在OnBeforeRequest这个函数下面添加下面一句判断
if (oSession.host.toLowerCase() == "<你的ip地址>:8888") oSession.host = "<虚拟机ip地址>:80";


####注意一下，一开始我配置过127.0.0.1:8888 127.0.0.1:8989 0.0.0.0:8888等等，但是都不行，想要在手机上访问到，必须要填写自己的ip地址加8888，也就是说跟fiddler端口一样的

####然后重启fiddler就ok啦
