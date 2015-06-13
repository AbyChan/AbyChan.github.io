title: OpenSuSE13 fcitx无法调用输入法问题
date: 2014-11-09 20:08:15
tags:
- opensuse
- fcitx
- 输入法
---

fcitx无法调用输入法，只能干输入英文


解决如下：

修改 /etc/sysconfig/language

```bash
INPUT_METHOD = fcitx

LC_CTYPE=zh_CN.UTF-8

```


修改 ～/.bashrc(也可以修改其他配置文件)

```bash
export XDG_CONFIG_HOME=/home/tyan/.config/fcitx(根据实际目录而定)
export XMODIFIERS=@im=fcitx
export XIM="fcitx"
export XIM_PROGRAM="fcitx"
```


如果在firefox或其他应用上无法调出，也可以添加下面两项

```bash
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
```
