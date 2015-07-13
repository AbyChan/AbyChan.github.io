title: postgresql 端口不对外开放问题
date: 2015-03-30 12:02:33
tags:
- postgresql
- port
---
突然遇到了一个问题， 服务器的postgresql连接不上了，用nmap扫了以下5432端口没有打开

但是在服务器上netstats ps -e|grep 5432 nmap iptables 等等的命令都显示open

就是在外面扫不到

google了下，解决方法如下

vim /etc/postgresql/(版本号)/main/postgresql.conf

修改listen_addresses为对外的interface的ip地址

重启pgsql，ok

