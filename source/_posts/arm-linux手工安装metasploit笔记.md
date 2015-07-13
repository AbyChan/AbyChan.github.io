title: linux手工安装metasploit笔记
date: 2015-04-30 11:58:58
tags:
- linux
- cb4
- metasploit
- arm
---

（linux全适用）
买了一块cubieboard4
性能挺好，想在上面安装metasploit，不过源上面没有，决定手工安装

metasploit是用ruby写的（慢是有原因的，不过话说回来，即使是慢，也是大名鼎鼎的，hack界也没有听说过什么有名气的静态语言项目，所以说，不管效率如何，开发出来了就是牛B）

安装依赖，这里以debian为例


```bash
sudo apt-get install build-essential libreadline-dev libssl-dev libpq5 libpq-dev libreadline5 libsqlite3-dev libpcap-dev openjdk-7-jre git-core autoconf postgresql pgadmin3 curl zlib1g-dev libxml2-dev libxslt1-dev vncviewer libyaml-dev curl zlib1g-dev
```

安装ruby，2.1.5以上，源上面没有，可以考虑用rvm，或者rbenv，这里不多做介绍

```bash
sudo gem install bundler
```

然后再安装一个nmap，源或编译

配置数据库，创建角色一定要输入密码

```bash
sudo -s
su postgres

createuser msf -P -S -R -D
createdb -O msf msf

exit
exit
```
下载metasploit源码

```bash
git clone https://github.com/rapid7/metasploit-framework.git
cd metasploit-framework
```


不是编译，一般不会有什么错误，安装完成之后将bin文件放进路径（非必须）
```bash
cd metasploit-framework
sudo bash -c 'for MSF in $(ls msf*); do ln -s /opt/metasploit-framework/$MSF /usr/local/bin/$MSF;done'
```
配置数据库
```bash
/opt/metasploit-framework/config/database.yml
```

```yml
shell
production:
adapter: postgresql
database: msf
username: msf
password: （刚才的密码）
host: 127.0.0.1
port: 5432
pool: 75
timeout: 5
```

Ok了

msfconsole试试吧
