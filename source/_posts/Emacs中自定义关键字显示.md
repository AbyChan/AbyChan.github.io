title: Emacs中自定义关键字显示
date: 2015-06-14 16:42:29
tags:
- emacs
- pretty-mode
- 关键字
- emasc美化
---

先看一张截图，是jquery源码部分
{% asset_img show.png %}

这里面，我改动了三个关键字显示
function变成f（数学函数的那个符号）
var 改成了一个圆圈标志
return 改成了胖箭头

当然，有些人喜欢改得天花龙凤，但是我觉得改几个就够了

下面教大家怎么做
这个在以前需要安装差价pretty-mode或者pretty-symbol-mode，不过24已经继承了里面了，叫做prettify-symbols-mode

首先需要开启prettify，这里我开了全局，大家可以自己hook
```lisp
(global-prettify-symbols-mode 1)
```

然后定义symbol list
```lisp
(defun js-pretty-lambda ()
  "make some word or string show as pretty Unicode symbols"
  (setq prettify-symbols-alist
        '(
          ("function" . 10765) ; ⨍
          ("var" . 10050)    ;
          ("return" . 10145)    ; ➡
          )))
'))
```
其中10765这个代码是emacs的unicode代码，可以到[http://xahlee.info/comp/unicode_math_operators.html](http://xahlee.info/comp/unicode_math_operators.html)中查找

最后hook到js2-mode上
```lisp
(add-hook 'js2-mode-hook 'js-pretty-lambda)
```

大功告成了
