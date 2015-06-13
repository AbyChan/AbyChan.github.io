title: CubieBoard4用Chroot监狱安装Gentoo子系统
date: 2015-05-31 00:47:03
tags:
- cubieboard
- chroot
- gentoo
- 树莓派
- raspberry
---

##Why？
闲得蛋疼，手上有一些arm设备，突然想在cubieboard4上装个gentoo，cubieboard的编译速度还是可以，我曾经试过在上面编译[phantomjs](http://phantomjs.org/)（加上webkit的），用了一个小时二十分钟，速度虽然不快，但是勉勉强强跑个gentoo应该没问题。
但是问题来了，cubieboard4还没有出gentoo啊，本来想自己编译一下组装上去的，但是想了想还是太麻烦，而且手上没有机子装的是UBUNTU12.04，加上官网上发布的系统都有些问题，要是自己编译肯定也会有不少问题。
so？还是算了，chroot上安装一个吧，不安装xorg当个服务器玩玩呗，而且没事还能在其他arm上面跑跑，告诉别人树莓派上面跑了个gentoo逼格还是蛮高的。

##Prepare
-   armv7[hf]设备一台，当然，你也可以在amd64或者其他机器上跑，都是一样的。不过我觉得那样还不如自己装个gentoo呢：）
-   8G-32G U盘一枚，我推荐16G，8G太小32G用不了。当然，你也可以自己建个ISO固定文件什么的（我不会的：）
-   联网：）

##Install some package
```bash
sudo apt-get install dchroot debootstrap
```
其他系统请自行google

##Partition & Format
对U盘分区，这里推荐Gparted吧，还是图形界面好用吧，随便你怎么分，不过我随便玩玩的心态就只分了一个区，推荐ext3或者ext4


##Mount
挂载分区，随便怎么挂，Chroot不用root权限的。不过我建议还是/mnt/gentoo
```bash
sudo mount /dev/sda1 /mnt/gentoo
```

##Download stage & portage
到[Gentoo镜像](https://www.gentoo.org/downloads/mirrors/)中找你喜欢的镜像，选择自己的cpu架构，版本，把stageX.bz2*这个压缩包下回来。
然后到snapshots这个目录，把最新的portage下载回来（不分架构）

##Extract the tarball
解压
```bash
sudo mv stage3*.bz2* portage.bz2* /mnt/gentoo
sudo tar xvjpf stage3*.bz2
sudo rm stage3*.bz2* /mnt/gentoo
tar xvjf /mnt/gentoo/portage-<date>.tar.bz2 -C /mnt/gentoo/usr
```
(别直接复制哥，自己稍微改一下，我相信会用gentoo的哥们都是木有问题的）

##Mount dev & proc
把设备和进程都挂载进去，因为这不是虚拟化，随便和DNS解析都复制进去，有必要的话把locale也复制进去吧，locale好像在/usr/lib/locale
```bash
sudo cp -L /etc/resolv.conf /mnt/gentoo/etc/resolv.conf
sudo mount -t proc none /mnt/gentoo/proc
sudo mount -o bind /dev /mnt/gentoo/dev
```

##chroot
恭喜，如果没有什么问题的话，已经可以chroot进去gentoo系统了，没错，就是这么简单
注意一点，chroot进去是默认用自己uid和变量，也就是root chroot进去用的是uid=0，所以刚进去什么也没有配置的话建议还是su进root里面在chroot
```bash
sudo chroot /mnt/gentoo /bin/bash
```

##configure
```bash
/usr/sbin/env-update
source /etc/profile
emerge --sync
```
##Finally
该干嘛干嘛：）
Tip：如果想在其他arm设备上chroot，只需要把u盘插上去，重复上面的配置工作即可（不用重新分区解压等等）建议自己写个shell脚本自动化配置

##Next？
下一篇文章我给大家介绍一下如果使用ssh登陆时自动chroot
