title: '把你的用户关进监牢里面:) 控制ssh登陆自动chroot'
date: 2015-05-31 15:51:24
tags:
- chroot jail
- chroot
- gentoo
- linux
- shh
---

上一篇[博客](<%- relative_url(',', 'CubieBoard4用Chroot监狱安装Gentoo子系统' -%>) %>)我介绍如何chroot安装gentoo系统，接下来，我为大家介绍如何让用户ssh登陆后自动我chroot进制定的目录

假设/mnt/gentoo是一个可以chroot的目录

新建一个chrootjail用户组（各发行版可能不太一样）
```bash
sudo groupadd chrootjail
sudo adduser tester chrootjail（把tester加入chrootjail）
```

然后在/etc/ssh/sshd_config中加入以下代码
```bash
Match group chrootjail
            ChrootDirectory /mnt/gentoo
```

重启ssh服务即可
```bash
sudo service ssh restart
```

注意，ssh用户默认使用自己的uid登陆chroot系统
