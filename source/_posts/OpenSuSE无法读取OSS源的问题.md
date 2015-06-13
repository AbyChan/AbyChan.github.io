title: OpenSuSE无法读取OSS源的问题
date: 2015-05-31 14:46:11
tags:
- opensuse
- opensuse13.2
- oss
- opensuse依赖
---

最近又装上了OpenSuSE，我曾经的最爱！（现在确实发现了opensuse的一些不足，例如包管理器）

但是不知道这次又出现了什么问题，安装一些软件总是报错无法依赖，费了老大的劲才发现原来是OSS和NON-OSS里面的包无法读取
当时我就懵B了，明明源在里面的啊，中科大的源也一并加上了（其实是一样，OpenSuSE采用了MirrorBrain 技术， 中央服务器会按照 IP 地理位置中转下载请求到附近的镜像服务器，我在武汉ip会转到USTC）
又费了老大的劲，终于发现原因了
一下是OSS的目录
```bash
[   ] ARCHIVES.gz                      27-Oct-2014 20:27   50M   Details
[   ] ChangeLog                        27-Oct-2014 20:14   57M   Details
[DIR] EFI/                             27-Oct-2014 21:14    -
[TXT] GPLv2.txt                        25-Oct-2014 11:10   18K   Details
[TXT] GPLv3.txt                        25-Oct-2014 11:10   34K   Details
[   ] INDEX.gz                         27-Oct-2014 20:27  291K   Details
[   ] README                           25-Oct-2014 11:10  1.1K   Details
[IMG] SuSEgo.ico                       25-Oct-2014 11:10  2.2K   Details
[DIR] boot/                            27-Oct-2014 21:14    -
[   ] content                          27-Oct-2014 20:27   19K   Details
[   ] content.asc                      27-Oct-2014 21:00  481    Details
[   ] content.key                      27-Oct-2014 21:00  1.0K   Details
[TXT] control.xml                      25-Sep-2014 14:02   47K   Details
[   ] directory.yast                   27-Oct-2014 20:27  256    Details
[DIR] docu/                            27-Oct-2014 21:14    -
[   ] gpg-pubkey-3dbdc284-53674dd4.asc 25-Oct-2014 11:10  1.0K   Details
[   ] gpg-pubkey-307e3d54-4be01a65.asc 25-Oct-2014 11:10  673    Details
[   ] license.tar.gz                   25-Oct-2014 11:10   41K   Details
[   ] ls-lR.gz                         27-Oct-2014 20:27  536K   Details
[DIR] media.1/                         27-Oct-2014 21:14    -
[   ] openSUSE13_2_NET.exe             25-Sep-2014 11:07  554K   Details
[DIR] suse/                            27-Oct-2014 21:14    -
```

不知道什么时候开始目录变成这样了，正确的源在最后的目录suse里面
所以正确的源url是http://download.opensuse.org/distribution/13.2/repo/oss/suse/

non-oss同理

悲哉我大蜥蜴啊，想说爱你不容易啊
