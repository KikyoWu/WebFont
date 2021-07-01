- [01-认识Web和Web标准.md](#01-认识web和web标准md)
  - [Web、网页、浏览器](#web网页浏览器)
    - [Web](#web)
    - [网页](#网页)
    - [浏览器](#浏览器)
  - [Web标准](#web标准)
    - [W3C组织](#w3c组织)
    - [Web 标准](#web-标准)
  - [HTML、HTML5、CSS、XML/JSON、XHTML、JavaScript、AJAX的区别](#htmlhtml5cssxmljsonxhtmljavascriptajax的区别)
  - [什么是 HTML](#什么是-html)
    - [什么是HTML5](#什么是html5)
    - [CSS](#css)
    - [xml/json](#xmljson)
    - [XHTML](#xhtml)
    - [JavaScript](#javascript)
    - [AJAX  (Asynchronous Javascript And XML)](#ajax--asynchronous-javascript-and-xml)
    - [Web Server 和 Web Services](#web-server-和-web-services)

# 01-认识Web和Web标准.md

## Web、网页、浏览器

### Web

Web（World Wide Web）即全球广域网，也称为万维网。

我们常说的`Web端`就是网页端。

### 网页

**网页是构成网站的基本元素**。网页主要由文字、图像和超链接等元素构成。当然，除了这些元素，网页中还可以包含音频、视频以及Flash等。

我们在浏览器上输入网址后，打开的任何一个页面，都是属于网页。

### 浏览器

浏览器是网页运行的平台，常见的浏览器有谷歌（Chrome）、Safari、火狐（Firefox）、IE、Edge、Opera等。

关于浏览器的详细介绍，可以看下一篇文章：《[浏览器的介绍](https://github.com/qianguyihao/Web/blob/master/01-html/02-浏览器的介绍.md)》

## Web标准

### W3C组织

**W3C**：World Wide Web Consortium，万维网联盟组织，用来制定web标准的机构（组织）。

W3C 万维网联盟是国际最著名的标准化组织。1994年成立后，至今已发布近百项相关万维网的标准，对万维网发展做出了杰出的贡献。

W3C 组织就类似于现实世界中的联合国。

为什么要遵循WEB标准呢？因为很多浏览器的浏览器内核不同，导致页面解析出来的效果可能会有差异，给开发者增加无谓的工作量。因此需要指定统一的标准。

### Web 标准

**Web标准**：制作网页要遵循的规范。

Web标准不是某一个标准，而是由W3C组织和其他标准化组织制定的一系列标准的集合。

**1、Web标准包括三个方面**：

- 结构标准（HTML）：用于对网页元素进行整理和分类。
- 表现标准（CSS）：用于设置网页元素的版式、颜色、大小等外观样式。
- 行为标准（JS）：用于定义网页的交互和行为。

根据上面的Web标准，可以将 Web前端分为三层，如下。

**2、Web前端分三层**：

- HTML（HyperText Markup Language）：超文本标记语言。从**语义**的角度描述页面的**结构**。相当于人的身体组织结构。
- CSS（Cascading Style Sheets）：层叠样式表。从**审美**的角度美化页面的**样式**。相当于人的衣服和打扮。
- JS：JavaScript。从**交互**的角度描述页面的**行为**。相当于人的动作，让人有生命力。

**3、打个比方**：（拿黄渤举例）

HTML 相当于人的身体组织结构：

[![img](https://camo.githubusercontent.com/26ecb9ea6aadc420d34f4c032575e0107d3c1677d7a8dd1b3ec083c79d13efba/687474703a2f2f696d672e736d79687661652e636f6d2f32303230303332325f313235302e706e67)](https://camo.githubusercontent.com/26ecb9ea6aadc420d34f4c032575e0107d3c1677d7a8dd1b3ec083c79d13efba/687474703a2f2f696d672e736d79687661652e636f6d2f32303230303332325f313235302e706e67)

CSS 相当于人的衣服和打扮：

[![img](https://camo.githubusercontent.com/4aa339489b77df69590546d67c7c4727190718d5803ad51e4964ecf8de1c8dd4/687474703a2f2f696d672e736d79687661652e636f6d2f32303230303332325f313235312e706e67)](https://camo.githubusercontent.com/4aa339489b77df69590546d67c7c4727190718d5803ad51e4964ecf8de1c8dd4/687474703a2f2f696d672e736d79687661652e636f6d2f32303230303332325f313235312e706e67)

JS 相当于人的行为：

[![img](https://camo.githubusercontent.com/c8b748a3427a4ef6a1889b0df3187d25526b6dc0a5c767e7983fea1e67d5c37b/687474703a2f2f696d672e736d79687661652e636f6d2f32303230303332325f323232302e676966)](https://camo.githubusercontent.com/c8b748a3427a4ef6a1889b0df3187d25526b6dc0a5c767e7983fea1e67d5c37b/687474703a2f2f696d672e736d79687661652e636f6d2f32303230303332325f323232302e676966)

## HTML、HTML5、CSS、XML/JSON、XHTML、JavaScript、AJAX的区别

## 什么是 HTML

- HTML 不是一种编程语言，而是一种*标记语言*
- HTML 标签是由*尖括号*包围的关键词， 标签通常是*成对出现*，标签对中的第一个标签是开始标签，第二个标签是结束标签
- 浏览器不会显示 HTML 标签，而是使用标签来解释页面的内容

### 什么是HTML5

- HTML5 是最新的 HTML 标准。

  HTML5 是专门为承载丰富的 web 内容而设计的，并且无需额外插件。

  HTML5 拥有新的语义、图形以及多媒体元素。

  HTML5 提供的新元素和新的 API 简化了 web 应用程序的搭建。

  HTML5 是跨平台的，被设计为在不同类型的硬件（PC、平板、手机、电视机等等）之上运行。

### CSS

- 自定义样式，现行通用的规定样式的语言是CSS
- 用css写一些定义样式的代码，然后在 html 文件里用一个<link>标签把这些规定样式的 CSS 代码与表达内容语义的 HTML 代码关联起来
- CSS 代码的格式基本是属性:值

### xml/json

- xml是可扩展标记语言,通常用于传输和储存数据,相似的还有json.前端和服务器之间通常需要一种双方都认可的格式进行数据的传递和存储。 
- .xml/json或其他格式指定了数据内容的存储格式,使用该数据的双方只需按照规定的格式写入/读出内容即可完成数据的传输和存储.以json为例,其基本格式为：{标题：内容}，根据这个格式，后台从json文件中读出需要的内容，例如{我是标题：我是要被读出的内容}，并按照这种格式发送给前端，前端通过js等语言对这些内容进行解析即可。
- 前端的一些配置信息，如用户登录名称、性别、网页底色等信息都可以暂存在xml/json文件中,根据需要随时读取. 服务器后台也可将前端需要的数据内容，以xml/json的格式发送给前端，达到数据交互的目的。

### XHTML

- XHTML是 HTML 的近亲 XML 和 HTML 的杂交品种，对语法要求比较严格，并且为了兼容 XML，在语法上与 HTML 有一些不同

### JavaScript

-  Javascript（JS） 给页面添加一些动态的效果
-  写一些 JS 的代码，保存在 xxx.js 里，在 html 文件中用 <script> 关联进来

### AJAX  (Asynchronous Javascript And XML)  

- 异步JavaScript和XML这不是一个全新的技术,而是利用已有的js/css/xml等技术达到前端数据及时更新的效果.
- 对用户而言，前端页面的刷新就是点击页面刷新按钮 或者F5实现页面内容的刷新。页面刷新的目的是让页面从新从服务器获取数据，通常是在页面长时间未更新数据，至于多长时间算长，没有定论。例如，门户网站的新闻列表，可能1个小时之内，服务器后台已增加了很多条新的新闻，前端可以通过刷新，从新获取最新的新闻展示在页面上。
- AJAX就是实现了自动更新需要刷新的数据的效果。其基本思路是前端js与后台不断通讯,及时获取前端某部分数据的变化信息,及时进行自动数据获取更新,使用户无需刷新网页即可保持页面数据最新的状态。例如，球赛文字直播、股票实时信息等。

### Web Server 和 Web Services

- 浏览器给服务器发一个请求，服务器不是一看就知道怎么响应的，这些请求和响应要有一个通用的写法，也就是要有一个协议，常用的是 HTTP 协议。
  - Web Server服务器知道按协议要写什么东西进去，完成客户端与服务器的交互
  - 除了提供 Web Service， Web Server 还会兼顾很多功能，包括提供缓存，平衡负载
- 要让这些形形色色的机器能够通过网络进行交互，我们就需要指明一种协议（比如 HTTP/HTTPS）和一种数据封装格式（比如 HTML/XML），Web Server 提供的 Web Service，指的就是这种协议+格式的交流体系