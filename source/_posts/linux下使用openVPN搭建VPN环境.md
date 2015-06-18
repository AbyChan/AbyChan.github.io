title: linux下使用openVPN搭建VPN环境
date: 2015-06-18 16:09:45
tags:
- vpn
- openvpn
- linux
---

vpn能用来干嘛我就不多说了，我之前一直在用shadowsocks，现在想在digitalocean上给自己搭建一个vpn环境。

###vpn协议
####PPTP – 老协议，非常不安全，但是配置和使用比较简单，不推荐使用
####L2TP/IPsec – 安全，但是用的人比较少。
####OpenVPN – 最流行的协议，安全快速。

这里，我们用openvpn来搭建vpn网络。

##服务器端
###1 安装openvpn
以ubuntu为例
```bash
sudo apt-get install openvpn
```

###2 配置rsa密码
我们用easy-rsa来生成密码
先把系统的easy-rsa生成密码脚本复制过来
```bash
find /usr -name easy-rsa
```
定位目录位置
然后复制过来，例如我的就在/usr/share下面
复制到当前目录，home目录
```bash
cp -r /usr/share/ easy-rsa/.
```
然后用你打开里面的vars文件
修改KEY_CN这个参数为server
其他的最好也修改以下，国家省份等等

###3 生成证书和钥匙
在easy-rsa目录下：
```
source ./vars
./build-ca
./build-key-server server
./build-dh
```
中间碰见交互输入一律回车，朋友yes or no一律yes
然后修改执行权限我
```bash
sudo chmod 400 server.key server.crt ca.crt ta.key
```

###4 生成客户端钥匙（key）
继续在easy-rsa目录下：
```bash
./build-key client1
```
建议多生成几把

###5 openvpn配置
```bash
find /usr -name server.conf*
```
用上面的命令定位示例配置文件
如果是压缩文件就解压缩，然后复制到你指定的地方
然后打开它进行配置
将里面的钥匙文件改成刚才easy-rsa文件夹里面keys的文件，一一对应，把前面的路径加上去就好了。

###6 启动openvpn
```bash
sudo openvpn server.conf
```
应该就能启动成功了，如果提示找不到钥匙文件，再改改就好了

###7 配置iptable和dns
现在openvpn启动好了，不过先别急，现在就算连上去也访问不了外网的
```bash
sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"
```
如果永久写入的话，在 /etc/sysctl.conf中加入下面一行
```bash
net.ipv4.ip_forward=1
```
配置NAT到内核：
```bash
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
```
想要永久写入的话：
```bash
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
```
然后在 /etc/network/interfaces中写入：
```bash
up iptables-restore < /etc/iptables.ipv4.nat
```

dns：
在刚才的server.conf中写入
```bash
dhcp-option DNS 10.8.0.1
```

##客户端（linux）

###1 安装openvpn
不再累述

###2 配置文件
```bash
find /usr -name client.conf
```
定位示例文件，然后复制复制下来
编辑：
修改下面两行
```bash
remote server1 1194
;remote server1 1194
```
server1改成服务器的ip


然后在服务器中把三个文件复制过来，分别是
client1.key, ca.crt and client1.crt
在client.confi中修改对应的配置

在最后面加上
```bash
dhcp-option DNS 10.8.0.1
```

###3 配置dns
在/etc/resolvconf/ resolv.conf.d/head中加上下面一句：
```bash
nameserver 10.8.0.1
```

然后
```bash
sudo resolvconf -u
```

###4 连接
```bash
sudo openvpn client.conf
```

###OK!

