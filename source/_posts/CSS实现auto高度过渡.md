title: CSS实现auto高度过渡
date: 2015-06-17 02:26:57
tags:
- css3
- transition
- 高度过渡
- 过渡
- 前端
---
以前，在实现不定高度伸缩的时候，只能通过javascript来实现动画效果，不过现在css3横行，加上移动web开发的需求，很多动画都只使用了css3的过渡transition功能。
在高度过渡的时候，很多朋友都遇到过高度过渡效果不佳的情况，或者是不能自动控制高度，下面我来教大家使用max-height这个css属性来实现。
下面是一个例子，当鼠标hover上去灰色块的时候，就会自动来下一块。
{% raw %}
<style>
#outsidebox {
background-color: #ccc;
height: 150px;
width: 150px;
}
#inbox {
max-height: 0;
overflow: hidden;
-webkit-transition: max-height 0.3s;
-moz-transition: max-height 0.3s;
transition: max-height 0.3s;
background-color: gray;
}
#inbox p {
margin: 0;
color: white;
text-align: center;
}
#outsidebox:hover #inbox{
max-height:100px;
}
#help-text {
text-align: center;
color: red;
postition: relative;
top: 40%;
}
</style>
<div id="outsidebox">
  <div id="inbox">
    <p>
      你好，世界
    </p>
    <p>
      你好，世界
    </p>
    <p>
      你好，世界
    </p>
</div>
<p id="help-text">Hover me</p>
</div>
{% endraw %}

代码如下：
```html
<style>
#outsidebox {
background-color: #ccc;
height: 150px;
width: 150px;
}
#inbox {
max-height: 0;
overflow: hidden;
-webkit-transition: max-height 0.3s;
-moz-transition: max-height 0.3s;
transition: max-height 0.3s;
background-color: gray;
}
#inbox p {
margin: 0;
color: white;
text-align: center;
}
#outsidebox:hover #inbox{
max-height:100px;
}
#help-text {
text-align: center;
color: red;

}
</style>
<div id="outsidebox">
  <div id="inbox">
    <p>
      你好，世界
    </p>
    <p>
      你好，世界
    </p>
    <p>
      你好，世界
    </p>
</div>
<p id="help-text">Hover me</p>
</div>
```
需要注意的是，max-height设置为很大也没有所谓，只要不小与里面box的高度就可以。
