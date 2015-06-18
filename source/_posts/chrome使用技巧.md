title: chrome使用技巧
date: 2015-06-16 18:54:02
tags:
- chrome
---

chrome占内存是众所周知的了，相比之下firefox开好几十个标签内存也没有什么变化。当然，火狐的速度没有chrome快，但是chrome的快是建立在烧cpu的基础上的，chrome一打开，会调整cpu的频率还是什么的，我也不是很懂，好像是把cpu的睡眠时间缩短了还是什么的，所以笔记本特别耗电。而且chrome的prefetch机制相当猛，打开了一个页面它就会根据预设的权重来预加载一些url，所以chrome的快不是渲染引擎的快，渲染引擎还是火狐的Gecko的跑第一，当然chrome的v8比火狐的蜘蛛猴spidermonkey快也是公认的，不然node也不会选择v8。

废话了那多，其实我还是想主要介绍一些chrome的参数设置。当然，我有个朋友他喜欢用台式机，16g的内存加上强大的cpu，他说chrome占不占资源无所谓，当然不是所有人都方便使用台式机的，这里我介绍chrome的几个参数来节省一下内存。

在linux下为例，在命令行中输入：
```bash
google-chrome --process-per-site
```

因为chrome和firefox的内存机制不一样，其实我也不是很懂它们具体的实现，大概就是firefox每个标签都会公用javascript的内存还有渲染内存，而chhrome默认是每一个标签都新实例化内存空间什么的，完全独立，也就是--process-per-tab这个参数是默认，当然，chrome有chrome的想法，它认为firefox那样共用进程，当一个标签错误，会导致整个浏览器崩溃，而自己chrome即使一个标签崩溃了，也可以shift+esc调出任务窗口来把标签kill掉而保证浏览器的正常。
呵呵，当然，我觉得chrome这个机制就是个傻逼机制，先不论是否每个用户都懂得shift+esc来管理标签进程，浏览器又不是服务器，崩溃就崩溃呗，有什么大不了，很多人都会设置打开浏览器就恢复之前的窗口，崩溃就当是释放一下系统资源好了，有必要每个标签开一个空间吗？

好吧，我们继续
当然，我们还是可以设置的

```bash
google-chrome --process-per-site
```
这个命令会设置每个网站共用一个进程

先前还可以设置整个浏览器共用一个进程
```bash
--single-process
```
然而，这个参数被废弃掉了，呵呵。

好吧，我们介绍一下其他有用的参数
-   --disable-3d-apis  关掉3d效果
-   --disable-accelerated-video 关掉gpu加速视屏
-   --disable-gpu 关掉gpu的使用
-   --disable-translate 关掉翻译功能
-   --dns-prefetch-disable 关掉dns预抓取
-   --no-experiments 关掉实验功能
-   --purge-memory-button 在任务管理器中可以清除内存
-   --restore-last-session 恢复上次的session


更全的[api](http://peter.sh/experiments/chromium-command-line-switches/#load-extension)

当然，选好了参数之后也不用每次都输入，在图标文件中修改就可以了，以linux用户为例
修改/usr/share/applications/中的google-chrome.desktop文件
中间有一句Exec=/usr/bin/google-chrome-stable
在后面加就可以了

