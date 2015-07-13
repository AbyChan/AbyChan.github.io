title: Linux下自签发ssl证书
date: 2015-06-30 13:05:19
tags:
- linux
- ssl
---

 每一次访问12306买票的时候总是要弹出吓人的非安全链接，这12306也够傲的，花点前买个证书就了事了，非要要人安装根证书。

当然，总是有人瞎猜可能是美帝的东西，不安全，容易泄露国家机密，不过，支付页面就是花钱买的证书https://epay.12306.cn/

算了，在国家机构混，最可能就是管理层的原因呗，猜也没用。

言归正传：ssl的安全性

http的安全性怎么样我就不多说了，可以自行google

只要是走http协议，总有办法黑你。

有人说：可以md5加密hash一下啊

非也，md5可以加密登陆，但是注册就加密不了，hash之后根本无法还原，而且在web领域，key是公开了，根本加密不了

我也看到有些腾讯邮箱的外部登陆是用rsa加密的

但是照样可以伪造爆破，中间人可以发起重放攻击，中间人照样可以获取你的cookies，也许腾讯是将安全行压在了http-only这个浏览器特性上了，但是依我一己之见，凡是在客户端的数据都是不安全的，有些人把火狐hack一下照样可以伪造cookies

所以啊

####ssl是十分有必要的

当然，ssl一般是要钱，不过在开发过程中，我们可以自己签发一个ssl证书


###1-生成私钥



```bash
openssl genrsa -des3 -out server.key 1024
```

会提示输入密码，这个PEM密码怎么说，一般人在选择去除，请看第三步

####2-生成证书签名请求（CSR）
这个生成的请求其实是买ssl证书的步骤，是发到证书机构的，不过这个不说了，我们现在是自签发
```bash
openssl req -new -key server.key -out server.csr
```
会提示输入很多信息，一般是一路回车

####3-去除私钥密码

去除之前的PEM密码是十分有必要的。

因为如果不去除，nginx 和 apache在开启的时候会问你PEM密码，就是你第一步输入那个，这样的话非常不方便，而且谁也不能保证服务不会宕机和重启，一旦重启和宕机就麻烦了。

```bash
cp server.key server.key.org
openssl rsa -in server.key.org -out server.key
```

这样就能去除了

####4-自签发证书

生成一个一年的证书
```bash
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

####ok
这样就成功了，server.key 和server.crt就是我们需要的东西。至于安装，每一个http服务器和容器都不相同，大家可以自行google

