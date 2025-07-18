> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzU2MjY1ODEwMA==&mid=2247492530&idx=1&sn=e5ff5d50784c8302e7aaec9ad7384bc9

#  SRC另类思路分享：不受限制的资源调用  
行行行之  知微守望   2025-07-18 05:27  
  
### 0x00前言  
  
对于SRC的挖掘思路，很多师傅已经给出了挖掘实用技巧。今天带来一篇本人的思路分享：不受限制的资源调用。  
#### 0x01.进入正题  
  
相信在各位的学习、生活中都遇到过这样的页面![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVyKtqbrojPN6Dh6R5LNeu3o8aGPRLpJu0Hj66CHRG0iaSJlawWr7PHLOI8GvwjWPm13OFhx45EicCvA/640?wx_fmt=png&from=appmsg "")  
  
  
此处我以某厂商的云服务购买为例，由图可知，需要我们输入姓名、身份证、联系电话等。如果按照我们普通的挖掘思路，此处可能存在的漏洞是不是有SQL、XSS、越权查看他人提交信息、CSRF等等，其实此处可以利用一种新的思路，我称之为不受限制的资源调用。  
#### 0x02.漏洞测试  
  
此处我们先输入自己的真实姓名+身份证号，然后把身份证号的最后一位7，改成5，进行提交，此时可以发现，提示我们需要输入正确的身份证号码，同时Burp没有任何数据包请求，判断此处是前端做了校验，校验用户输入的身份证号是否能够与规则匹配。同时可在JS文件中找到相应规则，此处校验不通过会返回false阻止我们进行提交。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVyKtqbrojPN6Dh6R5LNeu3o50SQge8rtmry78kCFYbalazs0LWH2iaialVhKE3FY2Gg1J6cAkICK25Q/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVyKtqbrojPN6Dh6R5LNeu3oJm84ggibyeFphyiaE933WIUTB9bn7JGlCBHicHg0qPa0usxfV3juyrd5w/640?wx_fmt=png&from=appmsg "")  
##### console有如下结果：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVyKtqbrojPN6Dh6R5LNeu3oNUcV1W0Ju0aQaQs2NRxCiaNRHIyJ2sZUbpqyqdwweu62ibjlFMNRDLvw/640?wx_fmt=png&from=appmsg "")  
  
所以此时，我们需要把身份证号改成一个正确的身份证号，把姓名也改成正确的姓名，同时进行提交，此时可见，在我们的Burp中出现了我们想要的数据包，包含了我们的姓名、身份证号、联系电话等等。此时我们再将数据包中的6改成5，也就是把真实身份证号又改回去一个不存在的身份证号，然后抓取返回包，可见，此时后端又做了一个验证，告知我们：身份证验证错误。![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVyKtqbrojPN6Dh6R5LNeu3oDkkMxVDJbvV4UEiciaqwmh0IX9uiacCjftGa3ETIluuBZU7GBrfF89jibg/640?wx_fmt=png&from=appmsg "")  
  
  
错误图：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVyKtqbrojPN6Dh6R5LNeu3otcKqFxAl2bqFno4nsibdhFmjMfniclq11ESgiajJEdlHOIw5bGdaBSwGA/640?wx_fmt=png&from=appmsg "")  
  
#### 0x03.原理剖析  
  
此时先不着急往下进行测试，我们先来了解一下身份证验证的原理：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVyKtqbrojPN6Dh6R5LNeu3ovUQliboX62roFSiamTBscLyJTxLLahPicX0DuUmhuZzaCxVAmxPzvUrRA/640?wx_fmt=png&from=appmsg "")  
  
  
这里我做了一张流程图，假如我此时是一名开发者，我需要给我的APP加上实名验证功能，那么我可以直接去向最上层的那个机构申请接口吗？不能，因为我不是企业，而且我也不是属于它直系应用的开发者。我只能向他的下级，也就是腾讯、阿里、百度这样的企业去申请API接口，同时这些公司会把我们提交的数据，提交给最上层的那个机构，并且根据返回的数据，给我们返回的数据。也就是身份证号验证成功，或者二要素验证不一致。  
  
我们再来说一下直系应用与企业的区别，直系应用去申请二要素验证，一般是不用花钱的。而我们作为个人开发者，或者企业，去调用那个接口，其实是要钱的。我们在网上随便找一些关键字，可以看到，价格其实还是蛮高的。![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVyKtqbrojPN6Dh6R5LNeu3o1cIrdJQgysVdIuRZHJqgDzibvjwPPicLbOaewZMGbzbcNvgTssGCYZGg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVyKtqbrojPN6Dh6R5LNeu3oN3icrsEPMzkIVfhiaxicwoTH0UUiaFMGC36Wfmx1Ziaia7t44mZsTBkzJsFw/640?wx_fmt=png&from=appmsg "")  
#### 0x04.深入理解  
  
那么此时是不是可以利用楼上所示的接口？去做一些事情呢，我这里假设要对别人进行社工，那么他的姓名是XXX，身份证号的后四位或者后六位我不知道，就可以对他进行一个爆破。此时我们勾选上最后四位，然后把数值调整到0000-9999之间，此时根据返回包的长度大小、可判断身份证号码是否正确。![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVyKtqbrojPN6Dh6R5LNeu3oe2iaOE2OQ5qOxNweoibv8lmWBkic4pHLF0l7deicJUjER07UwATeibjDSKA/640?wx_fmt=png&from=appmsg "")  
  
  
此处可见，我们利用某平台开放的实名认证接口，可以完成我们自己想做的身份证二要素验证，同时由于厂商没有做限制，便可以无限消耗此厂商的资源，从而达到我们的目的。像本文中的二要素验证，以及短信验证，还有活人检测，其实都是基于Money的，在我们的SRC挖掘过程中，也可以去尝试一下这些点。  
  
0x05 参考链接  

```
https://xz.aliyun.com/news/10139
```

  
真心感觉自己要学习的知识好多，也有好多大神卧虎藏龙、开源分享。作为初学者，我们可能有差距，不论你之前是什么方向，是什么工作，是什么学历，是大学大专中专，亦或是高中初中，只要你喜欢安全，喜欢渗透，就朝着这个目标去努力吧！有差距不可怕，我们需要的是去缩小差距，去战斗，况且这个学习的历程真的很美，安全真的有意思。但切勿去做坏事，我们需要的是白帽子，是维护我们的网络，安全路上共勉。  
  
  
**本文版权归作者和微信公众号平台共有，重在学习交流，不以任何盈利为目的，欢迎转载。**  
  
****  
**由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。公众号内容中部分攻防技巧等只允许在目标授权的情况下进行使用，大部分文章来自各大安全社区，个人博客，如有侵权请立即联系公众号进行删除。若不同意以上警告信息请立即退出浏览！！！**  
  
****  
**敲敲小黑板：《刑法》第二百八十五条　【非法侵入计算机信息系统罪；非法获取计算机信息系统数据、非法控制计算机信息系统罪】违反国家规定，侵入国家事务、国防建设、尖端科学技术领域的计算机信息系统的，处三年以下有期徒刑或者拘役。违反国家规定，侵入前款规定以外的计算机信息系统或者采用其他技术手段，获取该计算机信息系统中存储、处理或者传输的数据，或者对该计算机信息系统实施非法控制，情节严重的，处三年以下有期徒刑或者拘役，并处或者单处罚金；情节特别严重的，处三年以上七年以下有期徒刑，并处罚金。**  
  
