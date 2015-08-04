title: Javascrtipt之tap事件封装
date: 2015-08-04 17:26:54
tags:
- javascript
- web mobile
- tap
- 300 delay
- 事件封装
---

虽然说移动web的300延迟已经是一个说烂的话题,也有很多解决方案,fasttap和fastclick也很好,但是为了学习一下javascript的事件封装,我还是简单地把tap事件封装了一下.

fasttap和fastclick的思路是大同小异,我的是思路是借鉴fasttap的.

###fastclick
封装了一个fastclick类,全局绑定了document,检测浏览器是否需要fastclick,如果不需要就不处理,如果需要就绑定touch系列事件和mouse系列事件,检测一系列场景,preventDefault之后再发送一个新的click事件.

###fasttap
跟fastclick差不多的,但是自定义了一个tap事件,preventDefault之后发送一个click事件

###我的实现
我跟fasttap有一点不同,我是preventDefault之后发送自定义的tap事件
[github repo](https://github.com/AbyChan/Tap.js)

##原理
###300秒延迟的原因
说到移动开发，不得不说一下这个click事件，在手机上被叫的最多的就是点击的反应慢，就是click惹出来的事情。情况是在这样，在手机早期，浏览器有系统级的放大和缩小的功能，用户在屏幕上点击两次之后，系统会触发站点的放大/缩小功能。不过由于系统需要判断用户在点击之后，有没有接下来的第二次点击，因此在用户点击第一次的时候，会强制等待300ms，等待用户在这个时间内，是否有用户第二次的提交，如果没有的话，就会click的事件，否则就会触发放大/缩小的效果。

这个设计本来没有问题，但是在绝大多数的手机操作中，用户的单击事件的概率大大大于双击的，因此所有用户的点击都必须要等300ms，才能触发click事件，造成给用户给反应迟钝的反应，这个难以解决。业界普遍解决的方案是自己通过touch的事件完成tap，替代click。不过tap事件来实际的应用中存在下面所说的问题。

不过有个好消息，就是手机版chrome21.0之后，对于viewport width=device-width，并且禁止缩放的设置，click点击将取消300ms的强制等待时间，这个会是web的响应时间大大提升。ios至今还没有此类消息。不过这个还需要有一段时间。

当然,并不是所有的都支持user-scalable=0

而微软的有另一种实现的方法:
```
if (layer.style.touchAction === 'none' || layer.style.touchAction === 'manipulation') {
return true;

}
```
或者直接css
```css
a, button {
  -ms-touch-action: none;
        touch-action: none;

}
```
####移动事件顺序

-   touchstart
-   touchmove
-   touchend
-   mouseover
-   mousemove
-   mousedown
-   mouseup
-   click

而延迟是在mouseup和click之间,想要强制取消延迟,可以在mouseup之前事件中preventDefault就可以了,之后的事件都会被阻止掉,再发送一个假的事件就ok了


##自定义事件
```javascript
utils.createEvent = function(name) {
    if (document.createEvent) {
          var event = window.document.createEvent('HTMLEvents');

      event.initEvent(name, true, true);

      return event;

    }
};
```

###发送事件
```javascript
  utils.emitEvent = function(e, eventName) {
      if (document.createEvent) {
            return e.target.dispatchEvent(utils.createEvent(eventName));

  }
};
```

###处理touch
```javascript
 var handler = {

    start: function(e){
          e = utils.getOriginEvent(e);

      coord.start = [e.pageX, e.pageY];
            coord.offset = [0, 0];

},

    move: function(e){
          if ( !coord.start  ) {
                  return false;

}
      e = utils.getOriginEvent(e);
            coord.move = [e.pageX, e.pageY];

      coord.offset = [
              Math.abs(coord.start[0] - coord.move[0]),
                      Math.abs(coord.start[1] - coord.move[1])

];

},

    end: function(e){

      e = utils.getOriginEvent(e);
            if ( coord.offset[0] <  Tap.options.fingerMaxOffset && coord.offset[1] < Tap.options.fingerMaxOffset) {

        utils.emitEvent(e, Tap.options.eventName);


}

      coord = {};


},

    //fire tap event and prevent click event(init fn will fake click event to this)
        tap: function(e) {
              utils.emitEvent(e, Tap.options.eventName);
                    return e.preventDefault();

},

    click: function(e) {
          //for unsuportted tap env
                if(!utils.emitEvent(e, Tap.options.eventName)) {
                        return e.preventDefault();

}


}


};
```

###检测touch设备
由于有ie这个另类,检测要用两种方法
####现代浏览器
```javascript
if ('ontouchstart' in window) {
  /* browser with Touch Events
       running on touch-capable device */

}
```
####ie
```javascript
if (navigator.msMaxTouchPoints > 0) {
  /* IE with pointer events running
       on touch-capable device */

}
```


