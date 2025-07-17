> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzg5NDg4MzYzNQ==&mid=2247486560&idx=1&sn=947416fb8d17302f5b18efcaf4cbe2fa

#  代码审计-Java项目-SSTI模板注入  
原创 xiaoheizi  小黑子安全   2025-07-17 06:21  
  
代码审计必备知识点：  
  
1  
、  
代码审计开始前准备：  
  
环境搭建使用，工具插件安装使用，掌握各种漏洞原理及利用  
,  
代码开发类知识点。  
  
2、代码审计前信息收集：  
  
审计目标的程序名，版本，当前环境(系统,中间件,脚本语言等信息),各种插件等。  
  
3、代码审计挖掘漏洞根本：  
  
可控变量及特定函数，不存在过滤或过滤不严谨可以绕过导致的安全漏洞。  
  
4、代码审计展开计划：  
  
审计项目漏洞原理->审计思路->完整源码->应用框架->验证并利用漏洞。  
  
代码审计两种方法  
：  
  
功能点或关键字分析可能存在  
的  
漏洞  
  
-  
抓包或搜索关键字找到代码出处及对应文件  
。  
  
-  
追踪过滤或接收的数据函数，寻找触发此函数或代码的地方进行触发测试。  
  
  
-常规或部分M  
VC  
模型源码可以采用关键字的搜索挖掘思路。  
  
  
-框架  
  
MV  
C   
墨香源码一般会采用功能点分析抓包追踪挖掘思路。  
  
1.  
搜索关键字找敏感函数  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCIlnNxeT7FCVA8Hp7B3HBpCCYEwz6P0TOt7ep6Ys8tgPr8cLJ3Udc4mHiclRROb5ricE1YiaFRS2cIicYQ/640?wx_fmt=png&from=appmsg "")  
  
2.  
根据目标功能点判断可能存在的漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCIlnNxeT7FCVA8Hp7B3HBpCCrruViafRH38poSzo4pDY9lfe5Dp516ok91AvRDd7LBB88sN3C8ws0gA/640?wx_fmt=png&from=appmsg "")  
  
JAVA  
项目——  
RCE  
漏洞产生层面  
  
1  
、服务端直接存在可执行函数（  
exec  
()  
等），且对传入的参数过滤不严格导致RCE漏洞  
  
2  
、服务端不直接存在可执行函数（  
exec  
()  
等），且对传入的参数过滤不严格导致RCE漏洞  
  
3  
、由表达式注入导致的RCE漏洞，如：OGNL、  
SpEL  
、MVEL、EL、  
Fel  
、JST  
+  
EL等  
  
4  
、由java后端模板引擎注入导致的RCE漏洞，如：  
Freemarker  
、  
Velocity  
、  
Thymeleaf  
等  
  
5  
、由java一些脚本语言引起的RCE漏洞，如：  
Groovy  
、  
JavascriptEngine  
等  
  
6  
、由第三方开源组件引起的RCE漏洞，如：  
Fastjson  
、  
Shiro  
、  
Xstream  
、  
Struts2  
等  
  
案例：代码审计  
-  
SSTI-OFCMS-  
模板  
  
Freemarker  
  
1.  
在  
CNVD  
获取到  
OFCMS  
  
v1.1.3  
版本后台模板定制处存在命令执行漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCIlnNxeT7FCVA8Hp7B3HBpCCs9jeT7OsweekLSG55TuMBuWUciaH5TQibmlGmqkSGrOnDtoWWSGjL4Tg/640?wx_fmt=png&from=appmsg "")  
  
2.  
使用  
idea  
打开源码，部署好环境并且启动  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCIlnNxeT7FCVA8Hp7B3HBpCCA4SCh2jFb43H1nTXSG9qaSib9cJ3MqJeicecicTVtWVnaI91vKHygRWfw/640?wx_fmt=png&from=appmsg "")  
  
3.  
根据  
cnvd  
给出的信息知道漏洞产生在模板处，所以第一步打开  
pom.xml  
查看项目引用的模板引擎。  
  
发现使用了  
freemarker  
模板引擎，将鼠标移动到上面时还提示此版本存在模板注入漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCIlnNxeT7FCVA8Hp7B3HBpCCFics9CO9FdR3xCzic5URdtzZzXGVcpGvxoBNicUQqxiaNhtO7TIwvicrOrg/640?wx_fmt=png&from=appmsg "")  
  
4.  
根据  
cnvd  
公开信息来到网站后台找到漏洞产生位置，发现有很多模板文件。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCIlnNxeT7FCVA8Hp7B3HBpCCyq3f1JSpEwLrMlPDf2v68xQRQ84g3WJg0iaYu5ib3MKjQNEicPk1Z6CbQ/640?wx_fmt=png&from=appmsg "")  
  
5.  
在任意模板文件中写入  
payload  
。  
  
payload  
：  
<#assign ex="freemarker.template.utility.Execute"?new()>${ ex("calc") }  
  
这里选择的模板文件是  
index.html :  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCIlnNxeT7FCVA8Hp7B3HBpCCWyGCC55V8dh3SltsObhZcdUib8lvXhbZRdxibIauRcrvDibiaGSy5oibmnw/640?wx_fmt=png&from=appmsg "")  
  
6.  
访问  
index.html  
模板文件，成功执行命令，弹出计算器  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCIlnNxeT7FCVA8Hp7B3HBpCCyibCVjpwo7rADm7B3aKJhWlL5BrC5D3ABia4AUc8p15QbqPKwwlbMfuA/640?wx_fmt=png&from=appmsg "")  
  
推荐一下作者最新研发的yakit被动漏洞检测插件，可挖掘企业src漏洞。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavtzDPaxIm6PXM8IuzuAB6ViceOVwpEMvHH403GNQp59nju2Q49TvqOpg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
以上漏洞都是不需要任何技巧的，作者只是开启插件在目标网站用鼠标“点点点点”就挖掘出这么多漏洞，完全  
  
“零基础”“  
  
零成本”挖洞  
  
目前一共开发了四个插件：  
  
被动  
sql  
注入检测  
  
被动  
xss  
扫描优化版  
  
被动目录扫描好人版  
  
被动  
ssrf  
及  
log4j  
检测  
  
插件使用效果：[记一次企业src漏洞挖掘连爆七个漏洞！](https://mp.weixin.qq.com/s?__biz=Mzg5NDg4MzYzNQ==&mid=2247486552&idx=1&sn=41c4e4a40fd104f53e22f5a7143c88ad&scene=21#wechat_redirect)  
  
  
插件使用教程：  
[新一代SQL注入检测技术，小白也能轻松挖到漏洞！](https://mp.weixin.qq.com/s?__biz=Mzg5NDg4MzYzNQ==&mid=2247486516&idx=1&sn=8ce41df1c1c32eddb5762dc6c362a85b&poc_token=HEcld2ij2mPrmNUdYokG5LVG3B9lMQFCmGocR1XA&scene=21#wechat_redirect)  
  
  
知识星球——小黑子安全圈  
[  
精华版  
]  
    
开业大吉！  
  
每一个插件都是非常实用的，有没有用作者也已经通过  
  
企业  
src   
漏洞的挖掘来证明了，并且只需要开启插件  
  
点击鼠标就可以全自动挖掘漏洞。  
  
需要获取插件的小伙伴可以扫描下方二维码加入我的知识星球，星球  
 99  
元  
/  
年  
  
，前  
50  
个加入的  
 77  
元  
/  
年。  
  
加入知识星球的同学会提供  
  
yakit  
  
安装  
  
和  
  
插件  
  
使用教程。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavyafDg4ZciajrrTwTH4VWgO5MnmzRk1FMbiaZT2mQxbjb1JJicMDQLXDlw/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp "")  
  
本星球只提供精华内容，没有烂大街的东西。会持续更新  
yakit  
插件和各种漏洞漏洞探针和利用工具，哪怕你是什么都不懂的小白用了插件点点鼠标就能挖到漏洞。  
  
注！！！红包返现！！！拉新活动！！！  
  
星球接受使用插件挖到漏洞的投稿，我审核通过会返  
30  
红包，直接微信转，文章我会发公众号  
(  
每人仅限一次  
)  
。  
  
拉新人加入星球待满三天也会返  
20  
红包  
(  
微信直接转  
)  
。插件会一直优化和上新，欢迎大家加入星球。  
  
