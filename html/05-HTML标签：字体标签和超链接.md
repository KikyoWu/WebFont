- [05-HTML标签：字体标签和超链接.md](#05-html标签字体标签和超链接md)
  - [本文主要内容](#本文主要内容)
  - [文本格式化标签](#文本格式化标签)
  - [字体标签](#字体标签)
    - [特殊字符（转义字符）](#特殊字符转义字符)
    - [下划线`u`、中划线`s`、斜体`i`](#下划线u中划线s斜体i)
    - [粗体标签`<b>`或`<strong>`（已废弃）](#粗体标签b或strong已废弃)
    - [字体标签`<font>`（已废弃）](#字体标签font已废弃)
    - [上标`<sup>` 下标`<sub>`](#上标sup-下标sub)
  - [三、超链接](#三超链接)
    - [1、外部链接：链接到外部文件](#1外部链接链接到外部文件)
    - [2、锚链接](#2锚链接)
    - [3、邮件链接](#3邮件链接)
    - [超链接的属性](#超链接的属性)

# 05-HTML标签：字体标签和超链接.md

## 本文主要内容

&emsp;&emsp;字体标签： `<font>`、 `<b>`、 `<u>` 、`<sup>` 、`<sub>`

&emsp;&emsp;超链接 `<a>`

## 文本格式化标签

| 标签     | 描述                                  |
| :------- | :------------------------------------ |
| `<b>`      | 定义粗体文本。 还可使用`style="font-weight: bold;"` 代替                       |
| `<big>`    | 定义大号字。                          |
| `<em>`     | 定义着重文字。                        |
| `<i>`      | 定义斜体字。还可使用`style="font-style: italic;"` 代替                        |
| `<small>`  | 定义小号字。                          |
| `<strong>` | 定义加重语气。                        |
| `<sub>`    | 定义下标字。                          |
| `<sup>`    | 定义上标字。                          |
| `<ins>`    | 定义插入字。                          |
| `<del>`    | 定义删除字。                          |
| `<s>`      | *不赞成使用。*使用 `<del>`<br />（文档中已被删除的文本） 代替。       |
| `<strike>` | *不赞成使用。*使用 `<del>` 代替。       |
| `<u>`      | *不赞成使用。*使用样式（style="text-decoration-line:underline"）代替。 |

| 值           | 描述                                                         |
| :----------- | :----------------------------------------------------------- |
| none         | 默认值。规定 text-decoration 没有线条。                      |
| underline    | 规定在文本下方显示线条。                                     |
| overline     | 规定在文本上方显示线条。                                     |
| line-through | 规定显示横穿文本的线条。                                     |
| initial      | 将此属性设置为其默认值。参阅 [initial](https://www.w3school.com.cn/cssref/css_initial.asp)。 |
| inherit      | 从其父元素继承此属性。参阅 [inherit](https://www.w3school.com.cn/cssref/css_inherit.asp)。 |

## 字体标签

### 特殊字符（转义字符）

- ` `：空格 （non-breaking spacing，不断打空格）
- `<`：小于号（less than）
- `>`：大于号（greater than）
- `&`：符号`&`
- `"`：双引号
- `'`：单引号
- `©`：版权`©`
- `™`：商标`™`
- `绐`：文字`绐`。其实，`#32464`是汉字`绐`的unicode编码。

&emsp;&emsp;比如说，你想把`<p>`作为一个文本在页面上显示，直接写`<p>`是肯定不行的，因为这代表的是一个段落标签，所以这里需要用到**转义字符**。应该这么写：

```html
这是一个HTML语言的&lt;p&gt;标签
```

&emsp;&emsp;正确的效果如下：

[![Paste_Image.png](https://camo.githubusercontent.com/31534f7eae6da40da1c307f58a252497639e3362769d4836d18716fe04e2d7d9/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31312e706e67)](https://camo.githubusercontent.com/31534f7eae6da40da1c307f58a252497639e3362769d4836d18716fe04e2d7d9/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31312e706e67)

&emsp;&emsp;错误的效果如下：

[![Paste_Image.png](https://camo.githubusercontent.com/6cc4e1a4033152934b66d9072143df2c1524f3f8ee4c6ba10d5bc30b7400112b/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31322e706e67)](https://camo.githubusercontent.com/6cc4e1a4033152934b66d9072143df2c1524f3f8ee4c6ba10d5bc30b7400112b/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31322e706e67)

&emsp;&emsp;其实我们只要记住前三个符号就行了，其他的在需要的时候查一下就行了。而且，EditPlus软件中是可以直接点击这些符号进行选择的：

[![Paste_Image.png](https://camo.githubusercontent.com/aac05907123cc8aa9c4adcdced0124522b1aa31a27d0b24e8510f70f2f9ba525/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31332e706e67)](https://camo.githubusercontent.com/aac05907123cc8aa9c4adcdced0124522b1aa31a27d0b24e8510f70f2f9ba525/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31332e706e67)

&emsp;&emsp;来一张表格，方便需要的时候查询：

| 特殊字符 | 描述           | 字符的代码 |
| -------- | -------------- | ---------- |
|          | 空格符         | `&nbsp;`      |
| <        | 小于号         | `&lt;`        |
| >        | 大于号         | `&gt;`        |
| &        | 和号           | `&amp;`       |
| ￥       | 人民币         | `&yen;`       |
| ©        | 版权           | `&copy;`      |
| ®        | 注册商标       | `&reg;`       |
| °        | 摄氏度         | `&deg;`       |
| ±        | 正负号         | `&plusmn;`    |
| ×        | 乘号           | `&times;`     |
| ÷        | 除号           | `&divide;`    |
| ²        | 平方2（上标2） | `&sup2;`      |
| ³        | 立方3（上标3） | `&sup3;`      |

### 下划线`u`、中划线`s`、斜体`i`

- `<u>`：下划线标记
- `<s>`或`<del>`：中划线标记（删除线）
- `<i>`或`<em>`：斜体标记

**注释：请尽量避免为文本加下划线 - 用户会把它混淆为一个超链接**

&emsp;&emsp;效果：

[![Paste_Image.png](https://camo.githubusercontent.com/690be1ff4d6ecdf192debc210310084ea26368f1d257b421b6d843d1a43b2496/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31352e706e67)](https://camo.githubusercontent.com/690be1ff4d6ecdf192debc210310084ea26368f1d257b421b6d843d1a43b2496/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31352e706e67)

&emsp;&emsp;上面的这几个标签，常用于做一些小装饰、小图标。比如：

[![img](https://camo.githubusercontent.com/fafe449d5aceb35f32faaeba9ca299250bcab8658e4b7ac3ed8c4b3b6b232d3e/687474703a2f2f696d672e736d79687661652e636f6d2f32303138303131385f323334302e706e67)](https://camo.githubusercontent.com/fafe449d5aceb35f32faaeba9ca299250bcab8658e4b7ac3ed8c4b3b6b232d3e/687474703a2f2f696d672e736d79687661652e636f6d2f32303138303131385f323334302e706e67)

&emsp;&emsp;这张图中，我们通过查看京东网站的代码发现，箭头处的小图标都是用的标签`<i>`。

### 粗体标签`<b>`或`<strong>`（已废弃）

效果：

[![Paste_Image.png](https://camo.githubusercontent.com/7d5da30708e1d9134a84f6f34c8a46b17d0ff88372a352958b65d83cc59d45d8/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31342e706e67)](https://camo.githubusercontent.com/7d5da30708e1d9134a84f6f34c8a46b17d0ff88372a352958b65d83cc59d45d8/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31342e706e67)

### 字体标签`<font>`（已废弃）

使用css代替 `style="font-weight: bold;"`

属性：

- `color="红色"`或`color="#ff00cc"`或`color="new rgb(0,0,255)"`：设置字体颜色。 设置方式：单词 \ #ff00cc \ rgb(0,0,255)。
  - 修改为css格式`style="color:red;"`。
- `size`：设置字体大小。 取值范围只能是：1至7。取值时，如果取值大于7那就按照7来算，如果取值小于1那就按照1来算。如果想要更大的字体，那就只能通过css样式来解决。
  - 修改为css格式`style="font-size:20px;"`。
- `face="微软雅黑"`：设置字体类型。
  - 修改为css格式`style="font-family:arial;"`。

举例：

```
<font face="微软雅黑" color="#FF0000" size="10">vae</font>
```

效果：

[![Paste_Image.png](https://camo.githubusercontent.com/b2da600e9518ece24e0163f0b3f4311fc0514c19c9bc2bdb2f1834f033061f65/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31302e706e67)](https://camo.githubusercontent.com/b2da600e9518ece24e0163f0b3f4311fc0514c19c9bc2bdb2f1834f033061f65/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31302e706e67)

### 上标`<sup>` 下标`<sub>`

上小标这两个标签容易混淆，怎么记呢？这样记：`b`的意思是`bottom：底部` 举例：

```
O<sup>2</sup>    5<sub>3</sub>
```

效果：

[![Paste_Image.png](https://camo.githubusercontent.com/70bb169f7d2bb320305043905ef148e338bbd3175e0534c79a99f2b0fe458bb1/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31362e706e67)](https://camo.githubusercontent.com/70bb169f7d2bb320305043905ef148e338bbd3175e0534c79a99f2b0fe458bb1/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31362e706e67)

## 三、超链接

超链接有三种形式，下面分别讲讲。

### 1、外部链接：链接到外部文件

举例：

```
<a href="02页面.html">点击进入另外一个文件</a>
```

a是英语`anchor`“锚”的意思，就好像这个页面往另一个页面扔出了一个锚。是一个文本级的标签。

href（hypertext reference）：超文本地址。读作“喝瑞夫”，不要读作“喝夫”。

效果：

[![Paste_Image.png](https://camo.githubusercontent.com/922c3e96574e85913c942a448d09b75c704039c425a959c0ec6e7d4138b33fbb/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31372e706e67)](https://camo.githubusercontent.com/922c3e96574e85913c942a448d09b75c704039c425a959c0ec6e7d4138b33fbb/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31372e706e67)

当然，我们也可以直接点进链接，访问一个网址。代码举例如下：

```
<a href="http://www.baidu.com" target="_blank">点我点我</a>
```

### 2、锚链接

**锚链接**：给超链接起一个名字，作用是**在本页面或者其他页面的的不同位置进行跳转**。比如说，在网页底部有一个向上箭头，点击箭头后回到顶部，这个就可以利用锚链接。

首先我们要创建一个**锚点**，也就是说，使用`name`属性或者`id`属性给那个特定的位置起个名字。效果如下：

[![Paste_Image.png](https://camo.githubusercontent.com/65afff723be193570b70d5a03624cbfcbe8bf2fa9f7c8571c5fc1c0e6f73b861/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31382e706e67)](https://camo.githubusercontent.com/65afff723be193570b70d5a03624cbfcbe8bf2fa9f7c8571c5fc1c0e6f73b861/687474703a2f2f696d672e736d79687661652e636f6d2f323031352d31302d30312d636e626c6f67735f68746d6c5f31382e706e67)

上图中解释：

第11行代码表示，顶部这个锚的名字叫做name1。 然后在底部设置超链接，点击时将回到顶部（此时，网页中的url的末尾也出现了`#name1`）。注意**上图中红框部分的`#`号不要忘记了**，表示跳到名为name1的特定位置，这是规定。如果少了`#`号，点击之后，就会跳到name1这个文件或者name1这个文件夹中去。

如果我们将上图中的第28行代码写成：

```
<a href="a.html#name1">回到顶部</a>
```

那就表示，点击之后，跳转到`a.html`页面的`name1锚点`中去。

说明：name属性是HTML4.0以前使用的，id属性是HTML4.0后才开始使用。为了向前兼容，因此，name和id这两个属性都要写上，并且值是一样的。

### 3、邮件链接

代码举例：

```
<a href="mailto:xxx@163.com">点击进入我的邮箱</a>
```

效果：点击之后，会弹出outlook，作用不大。

### 超链接的属性

- `href`：目标URL

- `title`：悬停文本。

- `name`：主要用于设置一个锚点的名称。

- ```
  target
  ```

  ：告诉浏览器用什么方式来打开目标页面。

  ```
  target
  ```

  属性有以下几个值：

  - `_self`：在同一个网页中显示（默认值）
  - `_blank`：**在新的窗口中打开**。
  - `_parent`：在父窗口中显示
  - `_top`：在顶级窗口中显示

`title`属性举例：

```
<a href="09_img.html" title="很好看哦">结婚照</a>
```

效果如下：

[![img](https://camo.githubusercontent.com/edbb8ddeea5ab296be5ff154a1248ebe8b8231e348bd5e0701d4278fd8ff475b/687474703a2f2f696d672e736d79687661652e636f6d2f32303137303633305f313431352e706e67)](https://camo.githubusercontent.com/edbb8ddeea5ab296be5ff154a1248ebe8b8231e348bd5e0701d4278fd8ff475b/687474703a2f2f696d672e736d79687661652e636f6d2f32303137303633305f313431352e706e67)

`target`属性举例：

```
<a href="1.html" title="悬停文本" target="_blank">链接的内容</a>
```

blank就是“空白”的意思，就表示新建一个空白窗口。为啥有一个_ ，就是规定，无需解释。 也就是说，如果不写`target=”_blank”`那么就是在相同的标签页打开，如果写了`target=”_blank”`，就是在新的空白标签页中打开。

#### 备注1：分清楚img和a标签的各自的属性

区别如下：

```
<img src="1.jpg" />
<a href="1.html"></a>
```

#### 备注2：a是一个文本级的标签

比如一个段落中的所有文字都能够被点击，那么应该是p包裹a：

```
<p>
	<a href="">段落段落段落段落段落段落</a>
</p>
```

而不是a包裹p：

```
<a href="">
	<p>
		段落段落段落段落段落段落
	</p>
</a>
```

a的语义要小于p，a就是可以当做文本来处理，所以p里面相当于放的就是纯文字。