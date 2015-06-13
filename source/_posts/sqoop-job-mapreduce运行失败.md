title: sqoop job mapreduce运行失败
date: 2014-11-17 21:45:07
tags:
- linux
- hadoop
- mapreduce
---

无缘无故失败，查不出原因

原因：文件过大，hadoop maprduce设置的jvm内存不够
```bash
cd ……/hadoop/conf
vim mapred-site.xml
```

添加节点
```xml
<property>
   <name>mapred.child.java.opts</name>
   <value>-Xmx600m</value>
</property>
```
