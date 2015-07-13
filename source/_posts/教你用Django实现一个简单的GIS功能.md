title: 教你用Django实现一个简单的GIS功能
date: 2015-05-10 12:07:17
tags:
- django
- gis
- postgresql
- web gis
---

地理信息系统（Geographic Information System或 Geo－Information system，GIS）有时又称为“地学信息系统”。它是一种特定的十分重要的空间信息系统。它是在计算机硬、软件系统支持下，对整个或部分地球表层（包括大气层）空间中的有关地理分布数据进行采集、储存、管理、运算、分析、显示和描述的技术系统。

看上去挺简单，但是实现起来是挺复杂的，这里面涉及到专用的地理数据库，图层，空间查询等等。

这里，我使用的是Django GEO框架实现一个简单的通过GPS（WGS-84坐标系）坐标查询具体城市功能。

Django是一个python敏捷开发框架，十分方便，这里就不诸多介绍了，就算没有学过，上手也是非常简单的。

django-admin.py startproject gisApp
创建一个叫gisApp的应用

然后 python manage.py startapp ChinaCity

创建了一个叫ChinaCity的可插拔模块

在gisApp目录里面的settings.py中修改INSTALLED_APPS 元组，加入’gisApp’

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ChinaCity',

```


然后参考https://docs.djangoproject.com/en/1.7/ref/contrib/gis/这里把类库配置好，把数据库安装上，推荐用postgresql，因为postgresql支持的地理查询功能最强大。

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'ChinaCity',
```

我们打算通过使用API调用这个查询功能，用ReSTful风格，所以用到了Django restful framework，十分易用的restful框架


```bash
pip install djangorestframework
```

然后再加一个配置模块

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'ChinaCity',
```

到这里，环境已经配好了，可以开始写功能了

我们要用到中国的城市空间数据，在网上到处都是
下载了一份保存到ChinaCity/data/china/CHN_adm2.shp

使用django自动的扫描功能
```bash
python manage.py ogrinspect SMGIS/data/china/CHN_adm2.shp ChinaCity –mapping –multi
```
得到的数据如下

```python
class ChinaCity(models.Model):
    id_0 = models.IntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=75)
    id_2 = models.IntegerField()
    name_2 = models.CharField(max_length=75)
    nl_name_2 = models.CharField(max_length=75)
    varname_2 = models.CharField(max_length=150)
    type_2 = models.CharField(max_length=50)
    engtype_2 = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=-1)
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for ChinaCity model
chinacity_mapping = {
    'id_0' : 'ID_0',
    'iso' : 'ISO',
    'name_0' : 'NAME_0',
    'id_1' : 'ID_1',
    'name_1' : 'NAME_1',
    'id_2' : 'ID_2',
    'name_2' : 'NAME_2',
    'nl_name_2' : 'NL_NAME_2',
    'varname_2' : 'VARNAME_2',
    'type_2' : 'TYPE_2',
    'engtype_2' : 'ENGTYPE_2',
    'geom' : 'MULTIPOLYGON',
}
```

稍作修改，我们在ChinaCity.models新建一个类
```python
class ChinaCity(models.Model):
    id_0 = models.IntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=75)
    id_2 = models.IntegerField()
    name_2 = models.CharField(max_length=75)
    nl_name_2 = models.CharField(max_length=75)
    varname_2 = models.CharField(max_length=150)
    type_2 = models.CharField(max_length=50)
    engtype_2 = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
```

然后新建一个Load.py

```python
chinacity_mapping = {
    'id_0' : 'ID_0',
    'iso' : 'ISO',
    'name_0' : 'NAME_0',
    'id_1' : 'ID_1',
    'name_1' : 'NAME_1',
    'id_2' : 'ID_2',
    'name_2' : 'NAME_2',
    'nl_name_2' : 'NL_NAME_2',
    'varname_2' : 'VARNAME_2',
    'type_2' : 'TYPE_2',
    'engtype_2' : 'ENGTYPE_2',
    'geom' : 'MULTIPOLYGON',
}



world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/china/CHN_adm2.shp'))

def run(verbose=True):
    lm = LayerMapping(ChinaCity, world_shp, chinacity_mapping,
                      transform=False, encoding='UTF-8')

    lm.save(strict=False, verbose=verbose)
```
打开shell
```bash
python manage.py shell
```

```bash
from gisApp.ChinaCity import Load
load.run()
```

这样我们就已经导入数据到空间数据库了

接下来我们要写api了

新建一个serializers.py

```python
from rest_framework import serializers
from .models import ChinaCity

class ChinaCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChinaCity
        fields = ('name_2',)
```

这是一个序列化类

然后我们在views中

```python
from rest_framework.views import APIView
from .models import ChinaCity
from .serializers import ChinaCitySerializer
from rest_framework.response import Response
from rest_framework import permissions

class ChinaCityQuery(APIView):
    permission_classes = (permissions.AllowAny, )
    def getCityObj(self, position):
        print position
        #try:
        return ChinaCity.objects.filter(geom__contains=position)[0]
        #except:
            #raise Http404
    def get(self, request, position, format=None):
        position = 'POINT(' + position + ')'
        city = self.getCityObj(position)
        return Response( ChinaCitySerializer(city).data )

```

接下来在gisApp中的urls.py中

```python
from ChinaCity.views import *
#gis
urlpatterns += [
    url(r'^api/gis/city/(?P<position>[\d\s\.]+)$', ChinaCityQuery.as_view()),
]
```

已经写好了，打开django自带的服务器


```bash
python manage.py runserver
```

在浏览器中打开
http://localhost:8000/api/gis/city/116.395645%2039.929986
其中最后116.395645%2039.929986是坐标



{% asset_img 1.png %}

大功告成

