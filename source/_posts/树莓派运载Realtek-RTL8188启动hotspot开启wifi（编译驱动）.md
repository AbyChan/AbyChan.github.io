title: 树莓派运载Realtek RTL8188启动hotspot开启wifi（编译驱动）
date: 2014-12-17 19:40:07
tags:
- linux
- 树莓派
---
最近想搞点玩意，需要在户外开热点，树莓派是个不错的选择
驱动方面不太熟悉，参考了网上几篇文章，但是总是卡在最后一步，失败！
无奈，只能去官网的社区寻求帮助，终于解决了，用的是桥bridge-utils分配ip，用dhcp可以参考其他文章，都一样的原理
由于树莓派的特殊性，本配置教程会配置成开机自启动.

####下载驱动：
```bash
wget http://andypi.co.uk/downloads/v1.1.tar.gz
```

####cd进去编译：
```bash
sudo make
sudo make install
```

####默认配置文件（这一步还是蛮关键的）
```bash
sudo vim /etc/default/hostapd
```
把这句搞上去DAEMON_CONF=”/etc/hostapd/hostapd.conf”

####配置wifi信息：
```bash
sudo nano /etc/hostapd/hostapd.conf
```

####刚才编译的时候会重写这个文件，ssid和密码一定要改，不然无法启动
修改interfaces信息：sudo nano /etc/network/interfaces
加上下面的（貌似只加前两句就行）
```bash
auto br0
iface lo inet loopback
iface br0 inet dhcp
bridge_fd 1
bridge_hello 3
bridge_maxage 10
bridge_stp off
bridge_ports eth0 wlan0
```

####设置开机自启动：
```bash
sudo update-rc.d hostapd defaults
```

然后重启，如果没有错误的话应该可以搜索到自己配置的wifi了
最后一步有些前辈不重启用了这样的语句
```bash
sudo hostapd -B /etc/hostapd/hostapd.conf
```
这样的话总是失败
我用了这样的方法
```bash
sudo ifup wlan0
sudo ifdown wlan0(这两条命令可以反了，我也忘了...)
sudo service hostapd restart
```
大家可以试试
