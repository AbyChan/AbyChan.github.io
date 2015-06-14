title: 安卓数据线ssh连树莓派（超简单）
date: 2014-12-19 22:31:10
tags:
- 树莓派
---

无需联网，无需无限网卡
树莓派:
```bash
sudo vim /etc/network/interfaces
```
添加或修改这句iface usb0 inet dhcp
然后手机数据线插上树莓派，开启usb网络共享
用better terminal或者terminal ide输入下面的命令
```bash
netcfg
```bash
rndis0的ip就是树莓派的ip了
可以直接ssh上去
或者用其他方法查看树莓派的ip，方法有很多哈
