title: 'OpenSuSE13.2 安装 oracle 12c '
date: 2014-11-19 22:27:06
tags:
- opensuse
- oracle
- linux
- database
---

虽然说oracle 12c对opensuse的支持还不是很好，但是要求不是很高的花，还是可以在o妹上跑一跑的。
下载就不用说了，官网上找，下回来两个zip压缩包。

##安装：
如果不标准话安装的话，会出现很多问题，so，还是老老实实建用户和dba组吧
```bash
groupadd dba
groupadd oinstall
useradd -g oinstall -G dba oracle
```
##创建目录和设置权限：
```bash
 mkdir -p ~/app/oracle
chown -R oracle:oinstall ~/app/oracle
chmod -R 775 ~/app/oracle
```
##安装依赖包：
```bash
binutils-2.21.1-0.7.25
gcc-4.3-62.198
gcc-c++-4.3-62.198
glibc-2.11.3-17.31.1
glibc-devel-2.11.3-17.31.1
ksh-93u-0.6.1
libaio-0.3.109-0.1.46
libaio-devel-0.3.109-0.1.46
libcap1-1.10-6.10
libstdc++33-3.3.3-11.9
libstdc++33-32bit-3.3.3-11.9
libstdc++43-devel-4.3.4_20091019-0.22.17
libstdc++46-4.6.1_20110701-0.13.9
libgcc46-4.6.1_20110701-0.13.9
make-3.81
sysstat-8.1.5-7.32.1
xorg-x11-libs-32bit-7.4
xorg-x11-libs-7.4
xorg-x11-libX11-32bit-7.4
xorg-x11-libX11-7.4
xorg-x11-libXau-32bit-7.4
xorg-x11-libXau-7.4
xorg-x11-libxcb-32bit-7.4
xorg-x11-libxcb-7.4
xorg-x11-libXext-32bit-7.4
xorg-x11-libXext-7.4
```
##配置
至于SELinux，opensuse本身就不用，我也没配
内核也一样，在pc上运行配不配也无所谓，我配了一下，还登陆不了kde，索性也没配，后面一样能装
su - oracle
登陆到oinstall用户
/etc/security/limits.conf中添加如下配置:
```bash
oracle soft nproc 2047
oracle hard nproc 16384
oracle soft nofile 1024
oracle hard nofile 65536
oracle soft stack 10240
oracle hard stack 10240
```
 /etc/pam.d/login中添加如下配置：
```bash
session required /lib/security/pam_limits.so
session required pam_limits.so
```
/etc/profile中添加如下配置：
```bash
if [ $USER = "oracle" ]; then
ulimit -u 16384
ulimit -n 65536
fi
```
修改.bash_profile 添加下面的配置：
```bash
TMP=/tmp; export TMP
TMPDIR=$TMP; export TMPDIR
ORACLE_BASE=<span style="font-family:Arial;">~</span>/app/oracle; export ORACLE_BASE
ORACLE_HOME=$ORACLE_BASE/product/12.1.0/db_1; export ORACLE_HOME
ORACLE_SID=epps; export ORACLE_SID
ORACLE_TERM=xterm; export ORACLE_TERM
PATH=/usr/sbin:$PATH; export PATH
PATH=$ORACLE_HOME/bin:$PATH; export PATH
LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib; export LD_LIBRARY_PATH
CLASSPATH=$ORACLE_HOME/JRE:$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib; export CLASSPATH
if [ $USER = "oracle" ]; then
if [ $SHELL = "/bin/ksh" ]; then
ulimit -p 16384
ulimit -n 65536
else
ulimit -u 16384 -n 65536
fi
fi
```
使之生效：
```bash
source .bash_profile
```
##开始安装
点击.sh安装文件，稍等片刻弹出图形界面，貌似不支持中文环境
根据自己的情况next，next……
其中有一步会提示权限不够
在这一步时，无法继续，因为oracle账户无法创建oraInventory目录，所以必须先创建该用户并授权
```bash
mkdir -p ~/app/oraInventory
chown -R oracle:oinstall ~/app/oraInventory
chmod -R 775 ~/app/oraInventory
```

后面弹出要执行两个.sh文件，root后执行第一个ok，执行第二个出现suse专有的错误，root下系统函数无法调用，我是直接定位到那一行注释掉整个if-else语句
后面就没有什么
！！注意 上面的~/目录随大家情况而定

启动oracle：
在oracle用户下：
```bash
lsnrctl start
启动监听
lsnrctl stop 关闭监听
```

##refence
oracle官方文档：[https://docs.oracle.com/database/121/nav/portal_11.htm](https://docs.oracle.com/database/121/nav/portal_11.htm)

参考文章：[http://www.cnblogs.com/kerrycode/archive/2013/09/13/3319958.html](http://www.cnblogs.com/kerrycode/archive/2013/09/13/3319958.html)
