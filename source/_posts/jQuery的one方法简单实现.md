title: jQuery的one方法简单实现
date: 2015-06-10 19:18:18
tags:
- jquery
- one
- javascript
- 前端
---

##jQuery One
jquery的one方法：
```javascript
$("p").one("click",function(){
  $(this).animate({fontSize:"+=6px"});
});
```

这个方法很好用，经常用在动画过渡完成的事件绑定上，
最近在开发一些简单的手机端网页，考虑到不是很复杂加
上网络效率，连zepto都不想用，不过one方法实在使得很
顺手，so？只能简单实现一下one方法了

##自删除处理器
```
document.getElementById("myelement").addEventListener("click", handler);

// handler function
function handler(e) {
    // remove this handler
    e.target.removeEventListener(e.type, handler);

    alert("You'll only see this once!");
}
```

*需要注意的是，有些朋友喜欢用callee，例如这样：*
```javascript
document.getElementById("myelement").addEventListener("click", handler);
 
// handler function
function handler(e) {
    // remove this handler
    e.target.removeEventListener(e.type, arguments.callee);
 
    alert("You'll only see this once!");
}
```
*方便是方便，但是callee已经在ES5严格模式中禁用了，
不推荐使用，详细请看这里
[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions_and_function_scope/arguments/callee](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions_and_function_scope/arguments/callee)*

##one函数工厂
```javascript
// create a one-time event
function onetime(node, type, callback) {
    var handler = function() {
      // remove event
      e.target.removeEventListener(e.type, handler);
      // call handler
      return callback(e);
    }

    // create event
    node.addEventListener(type, handler);
}
```

然后就能直接用了

```javascript
 // one-time event
 onetime(document.getElementById("myelement"), "click", handler);
 
 // handler function
 function handler(e) {
   alert("You'll only see this once!");
 }
```



