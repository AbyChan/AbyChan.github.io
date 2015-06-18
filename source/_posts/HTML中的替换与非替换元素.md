title: HTML中的替换与非替换元素
date: 2015-06-16 02:15:48
tags:
- 前端
- css
- html
- 替换元素
---

很多朋友在学习BFC IFC或者阅读W3C文档的时候都会看到替换元素(Replaced element)，不少人会说W3C没有提供详细说明，也不知道替换元素与非替换元素是什么，其实W3C在CSS2定义章节的时候已经说明了
[CSS2文档](www.w3.org/TR/2008/REC-CSS2-20080411/conform.html#replaced-element)
>  **Replaced element** An element for which the CSS formatter knows only the intrinsic dimensions. In HTML, IMG, INPUT, TEXTAREA, SELECT, and OBJECT elements can be examples of replaced elements. For example, the content of the IMG element is often replaced by the image that the "src" attribute designates. CSS does not define how the intrinsic dimensions are found.

还有更详细的
> **Replaced element** An element whose content is outside the scope of the CSS formatting model, such as an image, embedded document, or applet. For example, the content of the HTML IMG element is often replaced by the image that its “src” attribute designates. Replaced elements often have intrinsic : an intrinsic width, an intrinsic height, and an intrinsic ratio. For example, a bitmap image has an intrinsic width and an intrinsic height specified in absolute units (from which the intrinsic ratio can obviously be determined). On the other hand, other documents may not have any intrinsic dimensions (for example, a blank HTML document). User agents may consider a replaced element to not have any intrinsic dimensions if it is believed that those dimensions could leak sensitive information to a third party. For example, if an HTML document changed intrinsic size depending on the user’s bank balance, then the UA might want to act as if that resource had no intrinsic dimensions. The content of replaced elements is not considered in the CSS rendering model.

其实这个置换元素本身确实没有什么定义，这要从html和css分家那时候说起，那时候的是替换元素没有具体的名单，只是一种笼统的说法。而后来到html4后期，开始出现了一些名单，明确规定了可替换元素，就是HTML, IMG, INPUT, TEXTAREA, SELECT,和OBJECT等等标签。可以理解为内容是从外部获取的元素，有些也是没有固定尺寸的，比如一个html文档。

当然，这个替换元素本身没有什么意义，但是在放在行内级盒里面有衍生出两个重要的概念，行内可替换元素与行内非替换元素。

####行内可替换元素
行内替换元素的框属性（边距，填充和边框属性），在行内盒中像块级元素一样处理，内容的高度和宽度是由height和width定义，为空则auto。padding，margin也能自定义，在元素外渲染，例如img标签，它是行内元素，但是也是替换元素，所以可以定义高度宽度，行内可替换元素与行级盒唯一有关的就是margin。

####行内非替换元素
非替换元素的元素就是非替换元素了（废话：)），行内非替换元素与行内替换元素有很大的不同，内联非替换元素的宽度是由它的内容（这是受字体属性并且还字间距，字母间距，水平对齐影响）所决定的，无法定义width和height，或者说，定义了也不渲染。水平的margin，padding可以定义，但是忽略断行的渲染。

行内替换元素的高度更为复杂。首先，margin无法定义，高度height也无法定义，唯一可以控制高度的是行高line-height，但是行高对布局没有影响。具体的行高模型如下

{% asset_img inlinebox.png %}

这个模型有五条线，分别是：逻辑顶部，字体顶部，基线，字体底部，和逻辑底部。从字体顶部到字体底部（即，字体边缘之间）的距离被称为字体高度，从逻辑顶部到逻辑底部（即，逻辑边缘之间）的距离被称为逻辑高度。 （逻辑高度由line-height属性给出）
