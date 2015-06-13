title: linux二进制安装mysql5.6
date: 2014-11-23 11:34:07
tags:
- linux
- mysql5.6
- binary
---

到oracle官网上下载二进制压缩文件
解压出来想放哪就放哪，有些人喜欢放在根，有些人喜欢放在主目录
安装：
```bash
shell> sudo groupadd mysql
shell> sudo useradd -r -g mysql mysql
shell> cd /usr/local
shell> sudo ln -s full-path-to-mysql-VERSION-OS mysql (当然你放在这里就不用了，改名即可)
shell> cd mysql
shell> chown -R mysql .
shell> chgrp -R mysql .
shell> scripts/mysql_install_db --user=mysql
shell> chown -R root .
shell> chown -R mysql data
shell> bin/mysqld_safe --user=mysql &（opensuse的话root限制了很多函数，先把chown换回来，执行了这条再执行上两条）
下一条命令可选
shell> cp support-files/mysql.server /etc/init.d/mysql.server
```

添加到PATH:
```bash
sudo vim /etc/profile
#添加：
mysql config
export PATH=/usr/local/mysql/bin:$PATH
source /etc/profile
```


这样就可以在命令行启动mysql了，不过还没有设置用户名密码：
```bash
 mysql -u root
SELECT User, Host, Password FROM mysql.user;
+------+--------------------+----------+
| User | Host               | Password |
+------+--------------------+----------+
| root | localhost          |          |
| root | myhost.example.com |          |
| root | 127.0.0.1          |          |
|      | localhost          |          |
|      | myhost.example.com |          |
+------+--------------------+----------+
```

可见密码为空
```bash
mysql -u root
mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpwd');
mysql> SET PASSWORD FOR 'root'@'127.0.0.1' = PASSWORD('newpwd');
mysql> SET PASSWORD FOR 'root'@'%' = PASSWORD('newpwd');
```
