- [04-HTML标签：排版标签.md](#04-html标签排版标签md)
  - [排版标签](#排版标签)
  - [标题标签](#标题标签)
  - [HTML 注释](#html-注释)
  - [段落标签`<p>`](#段落标签p)
  - [水平线标签`<hr />`](#水平线标签hr-)
  - [换行标签`<br />`](#换行标签br-)
  - [`<div>`和`<span>`标签](#div和span标签)
    - [div和span的介绍](#div和span的介绍)
    - [div和span的区别](#div和span的区别)
  - [内容居中标签 `<center>`](#内容居中标签-center)
  - [预定义（预格式化）标签`<pre>`](#预定义预格式化标签pre)

# 04-HTML标签：排版标签.md

## 排版标签

```html
- `<h1>`
- <p>
- `<hr />`
- `<br />`
- <div>
- `<span>`
- `<center>`
- <pre>
```

下面来详细介绍一下排版标签。

## 标题标签

标题使用`<h1>`至`<h6>`标签进行定义。`<h1>`定义最大的标题，`<h6>`定义最小的标题。具有align属性，属性值可以是：left、center、right。

代码举例：

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<h1>H1：千古壹号，永不止步</h1>
	<h2>H3：千古壹号，永不止步</h2>
	<h3>H3：千古壹号，永不止步</h3>
	<h4>H4：千古壹号，永不止步</h4>
	<h5>H5：千古壹号，永不止步</h5>
	<h6>H6：千古壹号，永不止步</h6>
</body>
</html>
```

效果演示：

[![img](https://camo.githubusercontent.com/bdd0708f91b5d2a54104a4c8160a2ad65b200e90a7b940f785efd5bfe5fe0aa1/687474703a2f2f696d672e736d79687661652e636f6d2f32303230303430325f313035302e706e67)](https://camo.githubusercontent.com/bdd0708f91b5d2a54104a4c8160a2ad65b200e90a7b940f785efd5bfe5fe0aa1/687474703a2f2f696d672e736d79687661652e636f6d2f32303230303430325f313035302e706e67)

## HTML 注释

HTML 注释的格式如下：

```
<!-- 我是 html 注释  -->
```

## 段落标签`<p>`

段落，是英语“paragraph“缩写。

**作用**：可以把 HTML 文档分割为若干段落。在网页中如果要把文字有条理地显示出来，离不开段落标签。就如同我们平常写文章一样，整个网页也可以分为若干个段落。

代码举例：

```
<p>This is a paragraph</p>
<p>This is another paragraph</p>
```

属性：

- `align="属性值"`：对齐方式。属性值包括left center right。

属性举例：

[![Paste_Image.png](https://camo.githubusercontent.com/0fe1aa35a18eb457a74f82da5fb151010e6f8e34b4a327a3e061d98e99c9206a/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c3136363434302d316463643261643665363335333535392e706e67)](https://camo.githubusercontent.com/0fe1aa35a18eb457a74f82da5fb151010e6f8e34b4a327a3e061d98e99c9206a/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c3136363434302d316463643261643665363335333535392e706e67)

HTML标签是分等级的，HTML将所有的标签分为两种：

- **文本级标签**：p、span、a、b、i、u、em。文本级标签里只能放**文字、图片、表单元素**。（a标签里不能放a和input）
- **容器级标签**：div、h系列、li、dt、dd。容器级标签里可以放置任何东西。

从学习p的第一天开始，就要牢牢记住：**p标签是一个文本级标签，p里面只能放文字、图片、表单元素**。其他的一律不能放。

错误写法：（尝试把 h 放到 p 里）

```
	<p>
		我是一个小段落
		<h1>我是一级标题</h1>
	</p>
```

网页效果如下：

[![img](https://camo.githubusercontent.com/ad1f36a2e5b13ee56a4e600c8ceba29783766f9ecf3ddeffe6c659c4888ccc32/687474703a2f2f696d672e736d79687661652e636f6d2f32303137303633305f313130322e706e67)](https://camo.githubusercontent.com/ad1f36a2e5b13ee56a4e600c8ceba29783766f9ecf3ddeffe6c659c4888ccc32/687474703a2f2f696d672e736d79687661652e636f6d2f32303137303633305f313130322e706e67)

上图显示，浏览器不允许你这么做，我们使用Chrome的F12审查元素发现，浏览器自己把p封闭掉了，不让你去包裹h1。

PS：Chrome浏览器是HTML5支持度最好的浏览器。提供了非常好的开发工具，非常适合我们开发人员使用。审查元素功能的快捷键是F12。

## 水平线标签`<hr />`

> horizontal 单词的发音：[ˌhɒrɪˈzɒntl]。

水平分隔线（horizontal rule）可以在视觉上将文档分隔成各个部分。在网页中常常看到一些水平线将段落与段落之间隔开，使得文档结构清晰，层次分明。

代码举例：

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<p>自古情深留不住</p>
	<hr />
	<p>总是套路得人心</p>
</body>
</html>
```

运行效果：

[![img](https://camo.githubusercontent.com/853152fd67775fd766abdcc40bbcdd2b58187b03580b3a6bdbed6f9403d11d95/687474703a2f2f696d672e736d79687661652e636f6d2f32303230303430315f313933302e706e67)](https://camo.githubusercontent.com/853152fd67775fd766abdcc40bbcdd2b58187b03580b3a6bdbed6f9403d11d95/687474703a2f2f696d672e736d79687661652e636f6d2f32303230303430315f313933302e706e67)

属性介绍：

- `align="属性值"`：设定线条置放位置。属性值可选择：left right center。
- `size="2" `：设定线条粗细。以像素为单位，内定为2。
- `width="500"`或`width="70%"`：设定线条长度。可以是绝对值（单位是像素）或相对值。如果设置为相对值的话，内定为100%。
- `color="#0000FF"`：设置线条颜色。
- `noshade`：不要阴影，即设定线条为平面显示。若没有这个属性则表明线条具阴影或立体。

属性效果演示：

[![Paste_Image.png](https://camo.githubusercontent.com/81fca3453dada3c3a2360b62fc9599a490b67c85ffc6e2bff5d6d9c3fb0c1fef/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f30352e706e67)](https://camo.githubusercontent.com/81fca3453dada3c3a2360b62fc9599a490b67c85ffc6e2bff5d6d9c3fb0c1fef/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f30352e706e67)

## 换行标签`<br />`

如果希望某段文本强制换行显示，就需要使用换行标签。

```
This <br/> is a para<br/>graph with line breaks
```

效果如下：

[![img](https://camo.githubusercontent.com/a6a91d81ec0d69885715db82225ce135ebacaf195596bfd2f39c6a04f0241ddd/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c30332e706e67)](https://camo.githubusercontent.com/a6a91d81ec0d69885715db82225ce135ebacaf195596bfd2f39c6a04f0241ddd/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c30332e706e67)

## `<div>`和`<span>`标签

div和span是非常重要的标签，div的语义是division“分割”； span的语义就是span“范围、跨度”。想必你应该听说过“div + css”布局。

### div和span的介绍

- **div标签**：可以把标签中的内容分割为独立的区块。必须单独占据一行。
- **span标签**：和div的作用一致，但不换行。

代码举例：

[![Paste_Image.png](https://camo.githubusercontent.com/ba96b32b9f2a0d0a8e15c0dc7e2aec49f93ad5a29fea02e7a93084d7e638b75a/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f30382e706e67)](https://camo.githubusercontent.com/ba96b32b9f2a0d0a8e15c0dc7e2aec49f93ad5a29fea02e7a93084d7e638b75a/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f30382e706e67)

div标签的属性：

- `align="属性值"`：设置块儿的位置。属性值可选择：left、right、 center。

### div和span的区别

`<span>`和`<div>`唯一的区别在于：`<span>`是不换行的，而`<div>`是换行的。

如果单独在网页中插入这两个元素，不会对页面产生任何的影响。这两个元素是专门为定义CSS样式而生的。或者说，DIV+CSS来实现各种样式。

div在浏览器中，默认是不会增加任何的效果的，但是语义变了，div中的所有元素是一个小区域。 div标签是一个**容器级**标签，里面什么都能放，甚至可以放div自己。

span也是表达“小区域、小跨度”的标签，但只是一个**文本级**的标签。 就是说，span里面只能放置文字、图片、表单元素。 span里面不能放p、h、ul、dl、ol、div。

span举例：

```
<p>
	简介简介简介简介简介简介简介简介
	<span>
		<a href="">详细信息</a>
		<a href="">购买</a>
	</span>
</p>
```

div举例：

```html
<div class="header">
	<div class="logo"></div>
	<div class="nav"></div>
</div>
<div class="content">
	<div class="guanggao"></div>
	<div class="dongxi"></div>
</div>
<div class="footer"></div>
```

我们亲切地称这种模式叫做“**div+css**”：**div标签负责布局、结构、分块，css负责样式**。

## 内容居中标签 `<center>`

此时center代表是一个标签，而不是一个属性值了。只要是在这个标签里面的内容，都会居于浏览器的中间。 效果演示：

[![Paste_Image.png](https://camo.githubusercontent.com/b587eaccffd648adda2256be74df14053cb402ecaab0c34fd0aaf4e2619fbf04/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f30362e706e67)](https://camo.githubusercontent.com/b587eaccffd648adda2256be74df14053cb402ecaab0c34fd0aaf4e2619fbf04/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f30362e706e67)

到了HTML5里面，center标签不建议使用，建议使用css布局来实现。

```html
<p style="text-align:center">永不止步</p>
```

或者:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    p.center {text-align: center;}
  </style>
</head>
<body>
  <figure>
    <p class="center">永不止步</p>
</body>
</html>
```

## 预定义（预格式化）标签`<pre>`

含义：将保留标签内部所有的空白字符(空格、换行符)，原封不动地输出结果（告诉浏览器不要忽略空格和空行）。

说明：真正排网页过程中，`<pre>`标签几乎用不着。 效果演示：