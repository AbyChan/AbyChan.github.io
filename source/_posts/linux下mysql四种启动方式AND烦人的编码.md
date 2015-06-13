title: linux下mysql四种启动方式AND烦人的编码
date: 2014-12-01 09:04:30
tags:
- linux
- database
- 编码
- 数据库
- 乱码
---

#1.mysqld
```bash
bin/mysqld
#or
bin/mysqld --defaults-file=../my.cnf
```
如果是标准化安装的话./bin/mysqld --defaults-file=../my.cnf --user=mysql
client登陆也可以 --defaults=../my.cnf
关闭的话 bin/mysqladmin shutdown 不过如果用户不是root的话还登陆不了，-h root@localhost -p

#2.mysqld_safe

跟上面一样，启动这个模式会把my.cof中的[mysqld_safe]的读取了

#3.mysql.server
```bash
support-files/mysql.server start
#关闭
support-files/mysql.server stop
```
设置开机启动cp ./mysql.server /etc/rc.d/init.d/mysql

#4.mysqld_multi

-_-这个我没有研究过，是分布式的吧。。。。

最头疼的问题来了，utf编码！
乱码先检查连接参数?useUnicode=true&amp;characterEncoding=UTF-8
再检查表编码，数据库编码
当然，很有可能都不行，在sql中输入下面的语句
```bash
show variables like 'character%';
show variables like 'collation_%';
```

可以看到
```bash
+————————–+—————————-+
| Variable_name | Value |
+————————–+—————————-+
| character_set_client | latin1 |
| character_set_connection | latin1 |
| character_set_database | latin1 |
| character_set_filesystem | binary |
| character_set_results | latin1 |
| character_set_server | latin1 |
| character_set_system | utf8 |
| character_sets_dir | /usr/share/mysql/charsets/ |
+————————–+—————————-+


mysql> show variables like 'collation_%';
+----------------------+-----------------+
| Variable_name        | Value           |
+----------------------+-----------------+
| collation_connection | utf8_general_ci |
| collation_database   | utf8_general_ci |
| collation_server     | utf8_general_ci |
+----------------------+-----------------+
```
可能会有很多地方不是utf8，可以用下面的命令一个个改
```bash
set @@collation_server = utf8_general_ci;
```

也可以在my.cnf中改
```bash
[mysqld]
character-set-server = utf8
init_connect=’SET NAMES utf8′
[client]
default-character-set=utf8

[mysql]
default-character-set=utf8
```
改完重启
如果还不行（我就试过，搞了老半天），可以把数据库重建，记得在建的时候设置默认编码utf8
