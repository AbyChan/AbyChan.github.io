title: 教大家申请免费ssl证书
date: 2015-06-30 13:31:26
tags:
- ssl
- free ssl
- free
---

上一篇文章我为大家介绍了如何自签发证书，其实外国有几个网站是提供免费申请ssl证书服务的

我就为我的demo网站申请了一个[coffee club](http://lovecofe.club)

当然，免费的东西不能要求太多，只是最基本的证书，当然也不会弹出吓人的非安全链接页面

下面，我来教大家怎么做：

###需要的东西：
-   chrome或者firefox（如果你用ie，我就呵呵一笑了）
-   一个域名（好像没有域名也没必要申请。。。）


我向大家推荐这个免费申请的网站：[StartSSL.com](http://www.startssl.com/)

点进这个网站，在导航右边有个control panel，先注册，如果你想申请第二等级的证书，最好填写真实的信息

注册完了再点击control panel然后点击申请，chrome会问你信任它的证书，放心点击信任吧

填完申请表他会人工审核你的信息，我之前申请的时候地址没有写私人地址，他们马上就发邮件给我叫我改，过程很快的，一般都能申请成功。

申请成功之后就像之前一样填写发到你邮箱里面的验证码。

然后就可以开始生成证书了。

问你生成的私钥级别，选high。

下一步下一步，最后浏览器问你安装证书，点击信任。

接下来，他要验证你的域名
{% asset_img 1.png %}
我选择的是邮箱验证，应该是验证你买域名时候填的邮箱吧

验证过了之后我们选择web服务器的ssl/tls证书
{% asset_img 2.png %}

输入PEM密码，然后就生出私钥ssl.key了
{% asset_img 3.png %}

记得保存下来，中间不能有空格什么的

继续，然后选择你要认证的域
{% asset_img 4.png %}

也可以选择子域
{% asset_img 5.png %}

继续，就得到了ssl.crt证书了
{% asset_img 6.png %}

保存起来，点击finish

现在，我们已经得到了ssl.key , ssl.crt两个文件，现在已经可以安装到服务器了。

不过ssl.key是加密过的文件，放在nginx 和 apache中它会问你PEM密码，所以我们一般会把ssl.key解密

```bash
openssl rsa -in ssl.key -out private.key
```

大功告成了
