title: Linux下uWSGI+NGINX部署Django+AngularJs
date: 2014-12-28 12:20:37
tags:
- linux
- uWSGI
- nginx
- django
- angular
---

最近尝尝鲜，试试单页面框架Augular，之前就有单页面前端开发经验，不过那是用jQuery的
最近jQuery缺点太明显了，太臃肿了，大的前端应用往往都是一个一个jq组建，插件堆积而出，加上对DOM操作的随意性，使得应用的可读性和可维护性非常差
Angular就不介绍了，最吸引人的无非是MVC
不过做到一半遇到了一个致命性问题
应用是前后端分离的，angular的$http貌似只能处理同域的请求
例如我要请求www.google.com/someapi
会自动在前面加斜杠请求
我加上http://还是没用
能用上的各种方法都用过了
$httpProvider.defaults.useXDomain = true;
delete $httpProvider.defaults.headers.common['X-Requested-With'];
设置跨域也没用（1.X已经默认设置夸域了）
全部请求错误，request已经发出去了，服务器也响应了，但是response就是为空
（如果哪位前辈知道麻烦告诉本菜-。-）

没办法，只能直接跟Django后端绑在一起了
nginx处理静态的angular，其他通过socket转到uWSGI处理
nginx：
```bash
#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    upstream django {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      8000;
    # the domain name it will serve for
    server_name localhost; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /home/tyan/。。。。。;  # your Django project's media files - amend as required
    }

    location /static {
        alias /home/tyan/python/stockPredict//dist/; # your Django project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /home/tyan/...../uwsgi_params; # the uwsgi_params file you installed
    }
}


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}
```

uwigs_params

```bash
uwsgi_param  QUERY_STRING       $query_string;
uwsgi_param  REQUEST_METHOD     $request_method;
uwsgi_param  CONTENT_TYPE       $content_type;
uwsgi_param  CONTENT_LENGTH     $content_length;

uwsgi_param  REQUEST_URI        $request_uri;
uwsgi_param  PATH_INFO          $document_uri;
uwsgi_param  DOCUMENT_ROOT      $document_root;
uwsgi_param  SERVER_PROTOCOL    $server_protocol;
uwsgi_param  HTTPS              $https if_not_empty;

uwsgi_param  REMOTE_ADDR        $remote_addr;
uwsgi_param  REMOTE_PORT        $remote_port;
uwsgi_param  SERVER_PORT        $server_port;
uwsgi_param  SERVER_NAME        $server_name;
```

uwsgi.ini(随便什么名字，放在manage.py旁边)


```bash
# mysite_uwsgi.ini file
[uwsgi]

# Django-related settings
# the base directory (full path)
chdir           = /home/tyan/python/（项目目录,manage.py旁边)
# Django's wsgi file
module          = (项目名字).wsgi
# the virtualenv (full path)
home            = /home/tyan/env(虚拟环境，没用虚拟环境不填)

# process-related settings
# master
master          = true
# maximum number of worker processes
processes       = 10
# the socket (use the full path to be safe
socket          = 127.0.0.1:8001
# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum          = true
```

配置好了，进入项目目录运行uwsgi --ini uwsgi.ini
打开8000就能看到项目了，进入/static/就能看到angular，/static配置在nginx 那里，可以改，当然你的angular也能放在那里
注意uWSGI现在打开的socket，http打开是打不开的，必须通过nginx
如果单独打开uWSGI用http的话，可以在后面加参数uwsgi --ini uwsgi.ini --protocol=http
罗嗦一下，django的静态和meta目录一定要配好
以static为例url和root一样要配

```bash
STATIC_URL = '/static/'



TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../' 'front/template/'),
)

STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../', 'static/')
```
urls.py：

```python
from django.conf import settings
from django.conf.urls.static import stati
urlpatterns += [
   。。。。。
   namespace='rest_framework')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```
