- [06-HTML标签：图片标签.md](#06-html标签图片标签md)
  - [img标签介绍](#img标签介绍)
    - [介绍](#介绍)
    - [能插入的图片类型](#能插入的图片类型)
  - [img标签的`src`属性](#img标签的src属性)
    - [写法一：图片的相对路径](#写法一图片的相对路径)
    - [写法二：图片的绝对路径](#写法二图片的绝对路径)
    - [相对路径和绝对路径的总结](#相对路径和绝对路径的总结)
  - [img标签的其他属性](#img标签的其他属性)
    - [width、height 属性](#widthheight-属性)
    - [Alt 属性](#alt-属性)
    - [title 属性](#title-属性)
    - [align 属性](#align-属性)
    - [其他已废弃的属性](#其他已废弃的属性)

# 06-HTML标签：图片标签.md

## img标签介绍

### 介绍

img: 英文全称 image（图像），代表的是一张图片。

如果要想在网页中显示图像，就可以使用img 标签，它是一个单标签。语法如下：

```
<img src="图片的URL" />
```

### 能插入的图片类型

- 能够插入的图片类型是：jpg(jpeg)、gif、png、bmp等。
- 不能往网页中插入的图片格式是：psd、ai等。

HTML页面不是直接插入图片，而是插入图片的引用地址，所以要先把图片上传到服务器上。

## img标签的`src`属性

这里涉及到图片的一个属性：

- `src`属性：指图片的路径。英文名称 source。

在写**图片的路径**时，有两种写法：相对路径、绝对路径

### 写法一：图片的相对路径

相对当前页面所在的路径。两个标记 `.` 和 `..` 分表代表当前目录和上一层目录。

举例1：

```
<!-- 当前目录中的图片 -->
<img src="2.jpg">
<img src=".\2.jpg">

<!-- 上一级目录中的图片 -->
<img src="..\2.jpg">
```

相对路径不会出现这种情况：

```
aaa/../bbb/1.jpg
```

`../`要么不写，要么就写在开头。

举例2：

```
<img src="images/1.jpg">
```

上方代码的意思是说，当前html页面有一个并列的文件夹`images`，在文件夹`images`中存放了一张图片`1.jpg` 效果：

[![Paste_Image.png](https://camo.githubusercontent.com/f9d61d122399ff10f9f71845cfa19061498b9368f2b100a0839ec4e17b82feed/687474703a2f2f696d672e736d79687661652e636f6d2f32303135313030315f31392e6a7067)](https://camo.githubusercontent.com/f9d61d122399ff10f9f71845cfa19061498b9368f2b100a0839ec4e17b82feed/687474703a2f2f696d672e736d79687661652e636f6d2f32303135313030315f31392e6a7067)

相对路径的面试题。现有如下文件层级图：

[![img](https://camo.githubusercontent.com/8300b52bf8c01aeb05457192ac027f775ad1faa3929c755342a906196027e6eb/687474703a2f2f696d672e736d79687661652e636f6d2f32303137303633305f313133332e706e67)](https://camo.githubusercontent.com/8300b52bf8c01aeb05457192ac027f775ad1faa3929c755342a906196027e6eb/687474703a2f2f696d672e736d79687661652e636f6d2f32303137303633305f313133332e706e67)

问题：如果想在index.html中插入1.png，那么对应的img语句是？

分析：

现在document是最大的文件夹，里面有两个文件夹work和photo。work中又有一个文件夹叫做myweb。myweb文件夹里面有index.html。 所以index.html在myweb文件夹里面，上一级就是work文件夹，上两级就是document文件夹。通过document文件夹当做一个中转站，进入photo文件夹，看到了1.png。

答案：

```
<img src="../../photo/1.png" />
```

### 写法二：图片的绝对路径

绝对路径包括以下两种：

（1）以盘符开始的绝对路径。举例：

```
<img src="C:\Users\qianguyihao\Desktop\html\images\1.jpg">
```

（2）网络路径。举例：

```
<img src="http://img.smyhvae.com/20200122_200901.png">
```

大家打开上面的img中的链接，可能有惊喜哦。

### 相对路径和绝对路径的总结

相对路径的好处：站点不管拷贝到哪里，文件和图片的相对路径关系都是不变的。相对路径使用有一个前提，就是网页文件和你的图片，必须在一个服务器上。

问题：我的网页在C盘，图片却在D盘，能不能插入呢？

答案： 用相对路径不能，用绝对路径也不能。

注意：可以使用file://来插入，但是这种方法，没有任何意义！因为服务器上没有所谓c盘、d盘。

下面的方法是行的，但是没有任何工程上的意义，这是因为服务器没有盘符，linux系统没有盘符：

```
<img src="file://C:\Users\qianguyihao\Pictures\明星\1.jpg" alt="" />
```

**总结一下**：

无论是在 a 标签还是 img 标签上，如果要用路径。只有两种路径能用，就是相对路径和绝对路径：

- 相对路径从自己出发，找到别人。
- 绝对路径，就是`http://`或者`https://`开头的路径。
- 绝对不允许使用`file://`开头的文件，这个是完全错误的！

## img标签的其他属性

### width、height 属性

- `width`：图像的宽度。
- `height`：图像的高度。

width和height，在 HTML5 中的单位是 CSS 像素，在 HTML 4 中既可以是像素，也可以是百分比。可以只指定 width 和 height 中的一个值，浏览器会根据原始图像进行缩放。

**重要提示**：如果要想保证图片等比例缩放，请只设置width和height中其中一个。

### Alt 属性

- `alt`：当图片不可用（无法显示）的时候，代替图片显示的内容。alt是英语 alternate “替代”的意思，代表替换资源。

`Alt`属性效果演示：

[![Paste_Image.png](https://camo.githubusercontent.com/db38cc9e1dbf141ea5590262207847feaff5255b77895a9ede2aec930712d2db/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f32312e706e67)](https://camo.githubusercontent.com/db38cc9e1dbf141ea5590262207847feaff5255b77895a9ede2aec930712d2db/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f32312e706e67)

如上图所示：当图片 src 不可用的时候，显示文字。这样做，至少能让用户知道，这个图片大概是什么内容。

### title 属性

- `title`：**提示性文本**。鼠标悬停时出现的文本。

title 属性不该被用作一幅图片在 alt 之外的补充说明信息。如果一幅图片需要小标题，使用 figure 或 figcaption 元素。

title 元素的值一般作为提示条(tooltip)呈现给用户，在光标于图片上停下后显示出来。尽管这确实能给用户提供更多的信息，您不该假定用户真的能看到：用户可能只有键盘或触摸屏。如果要把特别重要的信息提供给用户，可以选择上面提供的一种方法将其内联显示，而不是使用 title。

举例：

```
<img src="images/1.jpg" width="300" height="`188" title="这是美女">
```

效果：

[![Paste_Image.png](https://camo.githubusercontent.com/a6e5d1ce97c5722e870a1136ea2c1fe009f7e95821f7d8672bc18728e6cdb7ad/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f32302e706e67)](https://camo.githubusercontent.com/a6e5d1ce97c5722e870a1136ea2c1fe009f7e95821f7d8672bc18728e6cdb7ad/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f32302e706e67)

### align 属性

- 图片的`align`属性：**图片和周围文字的相对位置**。属性取值可以是：bottom（默认）、center、top、left、right。

如果想实现图文混排的效果，请使用align属性，取值为left或right。

我们来分别看一下这`align`属性的这几个属性值的区别。

1、`align=""`，图片和文字低端对齐。即默认情况下的显示效果：

[![img](https://camo.githubusercontent.com/3153f125392954ae71a5fa66621c654df46a69f45e255fd705eef6b15c29e8a7/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30322d636e626c6f67735f68746d6c5f31392e706e67)](https://camo.githubusercontent.com/3153f125392954ae71a5fa66621c654df46a69f45e255fd705eef6b15c29e8a7/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30322d636e626c6f67735f68746d6c5f31392e706e67)

2、`align="center"`：图片和文字水平方向上居中对齐。显示效果：

[![img](https://camo.githubusercontent.com/9246d8bff771dc67b1ba1771f03e5f26c19d37bdd2493fdeb83f2af807ae140a/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30322d636e626c6f67735f68746d6c5f32312e706e67)](https://camo.githubusercontent.com/9246d8bff771dc67b1ba1771f03e5f26c19d37bdd2493fdeb83f2af807ae140a/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30322d636e626c6f67735f68746d6c5f32312e706e67)

3、`align="top"`：图片与文字顶端对齐。显示效果：

[![img](https://camo.githubusercontent.com/1515e8a96354ca0e9551ab8fde5b49a80d03033362aefcecf608fb72a5b482c4/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30322d636e626c6f67735f68746d6c5f32322e706e67)](https://camo.githubusercontent.com/1515e8a96354ca0e9551ab8fde5b49a80d03033362aefcecf608fb72a5b482c4/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30322d636e626c6f67735f68746d6c5f32322e706e67)

4、`align="left"`：图片在文字的左边。显示效果：

[![img](https://camo.githubusercontent.com/f6a41cbcef896e2b1310d6e441b82a47dc7af1ae35b190e2853e965b78b247be/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30322d636e626c6f67735f68746d6c5f32332e706e67)](https://camo.githubusercontent.com/f6a41cbcef896e2b1310d6e441b82a47dc7af1ae35b190e2853e965b78b247be/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30322d636e626c6f67735f68746d6c5f32332e706e67)

5、`align="right"`：图片在文字的右边。显示效果：

[![img](https://camo.githubusercontent.com/adfe4397e165adc9a540cbf67a43fa84f4e7cb01315c2fbdd858d6f65909ec35/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30322d636e626c6f67735f68746d6c5f32342e706e67)](https://camo.githubusercontent.com/adfe4397e165adc9a540cbf67a43fa84f4e7cb01315c2fbdd858d6f65909ec35/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30322d636e626c6f67735f68746d6c5f32342e706e67)

### 其他已废弃的属性

- `Align`（已废弃）：指图片的水平对齐方式，属性值可以是：top、middle、bottom、left、center、right。
  - 该属性已废弃，替换为 `vertical-align`这个CSS属性。
- 图片底下带有标题，对齐方式用 `<figcaption style="text-align: center;">贪吃蛇</figcaption>` 或者 `<figure style="text-align: center;">贪吃蛇</figure>`
- `<center>`已经废弃，所以图片对齐方式
  - 可选择`<div>` 标签可以把文档分割为独立的、不同的部分来将图片单独分成一部分，再在`<div>` 标签中定义css 格式`<div style="text-align: center">`。或者在头标签 `<head>` 里使用`class`选择器，选择css格式：
  ```html
  <style>
    div.center {text-align: center;}
  </style>
  ```
  
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <!-- <style>
    div.center {text-align: center;}
  </style> -->
</head>
<body>
  <figure>
    <div style="text-align: center">
    <!-- <div class="center" -->
    哈哈<img src="html/test/image/11.1.png" style="vertical-align: middle;"/>哈哈
  
    </div>
    <figcaption style="text-align: center;">贪吃蛇</figcaption>
  
  </figure>
</body>
</html>
```

- `border`（已废弃）：给图片加边框，单位是像素，边框的颜色默认黑色。该属性已废弃，替换为 `border`这个CSS属性。
  - 替换为 `style="border-style:值;"`
    - `border-style` 属性指定要显示的边框类型。
      - 允许以下值：
        - dotted - 定义点线边框
        - dashed - 定义虚线边框
        - solid - 定义实线边框
        - double - 定义双边框
        - groove - 定义 3D 坡口边框。效果取决于 border-color 值
        - ridge - 定义 3D 脊线边框。效果取决于 border-color 值
        - inset - 定义 3D inset 边框。效果取决于 border-color 值
        - outset - 定义 3D outset 边框。效果取决于 border-color 值
        - none - 定义无边框
        - hidden - 定义隐藏边框
        - border-style 属性可以设置一到四个值（用于上边框、右边框、下边框和左边框）。
    - `border-width` 属性指定四个边框的宽度。
      - 可以将宽度设置为特定大小（以 px、pt、cm、em 计），也可以使用以下三个预定义值之一：thin、medium 或 thick：
      - border-width 属性可以设置一到四个值（用于上边框、右边框、下边框和左边框
    - `border-color` 属性用于设置四个边框的颜色。
      - 可以通过以下方式设置颜色：
        - name - 指定颜色名，比如 "red"
        - HEX - 指定十六进制值，比如 "#ff0000"
        - RGB - 指定 RGB 值，比如 "rgb(255,0,0)"
        - HSL - 指定 HSL 值，比如 "hsl(0, 100%, 50%)"
        - transparent
        - 注释：如果未设置 border-color，则它将继承元素的颜色。
      - border-color 属性可以设置一到四个值（用于上边框、右边框、下边框和左边框）。
- `Hspace`（已废弃）：指图片左右的边距。
- `Vspace`（已废弃）：指图片上下的边距。
  - 边距用css的`style="margin-top:100px"`代替。
    - CSS 拥有用于为元素的每一侧指定外边距的属性：
      - margin-top
      - margin-right
      - margin-bottom
      - margin-left
    - 所有外边距属性都可以设置以下值：
      - auto - 浏览器来计算外边距
      - length - 以 px、pt、cm 等单位指定外边距
      - % - 指定以包含元素宽度的百分比计的外边距
      - inherit - 指定应从父元素继承外边距
    - 提示：允许负值。