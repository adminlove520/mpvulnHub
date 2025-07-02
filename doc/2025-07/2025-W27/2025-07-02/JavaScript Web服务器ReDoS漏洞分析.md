> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247497768&idx=1&sn=e6f334fb01b193eb918f67dc041f8393

#  JavaScript Web服务器ReDoS漏洞分析  
angel010  七芒星实验室   2025-07-01 23:05  
  
**免责声明：**  
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
  
文章作者：先知社区(  
angel010  
)  
  
文章来源：https://xz.aliyun.com/news/2403  
  
  
本文摘自论文《Freezing the Web: A Study of ReDoS Vulnerabilities in JavaScript-based Web Servers》，发表于27届USENIX Security Symposium（2018）。  
  
正则表达式(regular expression)就是用一个“字符串”来描述一个特征,然后去验证另一个“字符串”是否符合这个特征，是各类软件中广泛应用。但正则表达式有一缺点，就是很容易出错，而这可以帮助攻击者绕过检查，开发者却更相信正则表达式的正确性。  
  
正则表达式的一个安全方面的考虑却常常被忽略——
```
性能
```

  
，即字符串匹配正则表达式的时间。一般来说，匹配正则表达式可能需要几分钟到几个小时。比如，30个
```
a
```

  
匹配正则表达式
```
/(a+)+b/
```

  
在Node.js JavaScript平台上需要15秒钟时间，而匹配35个a需要8分钟时间。如果服务器应用时存在性能问题，那么攻击者就可以利用该漏洞构造一起很难匹配的输入，发起ReDoS（regular expression denial of service）攻击。  
# ReDoS攻击  
  
ReDoS攻击是一种算法复杂性攻击，利用了字符串匹配正则表达式的最坏情况。  
  
回溯算法并不是正则匹配中用的最多的，但因其容易实现是使用最广泛的一种匹配算法。下面是一些正则表达式和输入，算法需要进行多次回溯操作。  
## 回溯算法匹配  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUiclVuO8A0yVBEa8PxLaj7Om8gaPuIwabDvMptOp9Rdw9bDMtqeIqyFxFPYpV27NkliafXEmfTMWPoDw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUiclVuO8A0yVBEa8PxLaj7Om84nGrlTTl9IDm72JGCwLoeHe2b7qWpcnIoI3bWHgMteBqmGem3VfQHg/640?wx_fmt=png&from=appmsg "")  
## ReDoS攻击  
  
ReDOS攻击就利用了这些
```
pathological cases
```

  
。以正则表达式
```
/ˆa*a*b$/
```

  
为例，如图2所示，输入字符串为
```
aaa
```

  
。每个字符
```
a
```

  
都可以用两次传递来匹配，
```
4 ! 5 and 8 ! 9
```

  
。在每一步，算法需要决定采取了哪些过渡。最后，因为输入字符串中没有字母b，所以算法在状态11会失败。但在做出输入与模式不匹配的结论前，算法会尝试所有可能的方式来匹配字符a，比如回溯3次。研究人员发现这些类型都存在ReDoS漏洞，以此说明服务端JavaScript的重要性。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUiclVuO8A0yVBEa8PxLaj7Om8enUXMv4aLRLnHov7msoqvgcXaFVYmib5Izwvj3HO41Jy6nzibVS4PA3g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUiclVuO8A0yVBEa8PxLaj7Om8nL0IZWgFfvTnurF7BSNH4XmwK7uGq5qdVktQWqqiaorSl02Vu4AG04g/640?wx_fmt=png&from=appmsg "")  
# Server-side JavaScript  
  
JavaScript是最流行的编程语言之一，但主要用于客户端任务。而Node.js的广泛应用使JavaScript开始应用到服务端。但一个主循环的计算请求会减慢所有的入请求，比如匹配指数级复杂度的正则表达式的字符串匹配会减慢所有的请求处理。因为在基于JavaScript的服务器中，正则表达式是在主循环中匹配的，所以针对基于JavaScript的服务器的ReDoS攻击造成的危害要比对多线程的web服务器造成的危害大很多。  
# 使用的方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUiclVuO8A0yVBEa8PxLaj7Om8rzNOuticiadfsyRBbibH5djYsP4cia6DxwybzPgvLVHlRE1ibuibWxDNWsSA/640?wx_fmt=png&from=appmsg "")  
## npm分析  
  
研究人员认为如果正则表达式的输入线性增长，匹配时间超线性增长，那么这个正则表达式就是有漏洞的。研究人员发现主流的npm模块中存在ReDoS漏洞。  
- 首先，下载主流的模块并用JS代码的AST来提取正则表达式；  
  
- 然后，通过查询数据库来找出有漏洞的特定模式；  
  
## 创建漏洞利用  
  
基于npm模块的ReDoS 漏洞，研究人员创建了利用这些模块的攻击web服务器的漏洞利用。主要思想是假设服务端web应用可能使用该模块。最后，建立一个快速安装并实现使用该模块的web应用例子。然后，创建用户控制数据可以到达有漏洞的正则表达式的HTTP请求，构造可以触发长匹配时间的输入值。  
  
**有漏洞的正则表达式：**  
例1: content  

```
/^([^\/]+\/[^\ s ;]+) (?:(?:\ s *;\s* boundary =(?: &#34; ([^&#34;
]+)&#34; |([^; &#34;]+) )) |(?:\ s*;\ s *[^=]+=(?:(?: &#34; (?:[^ &#34;
]+)&#34;) |(?:[^; &#34;]+) )))*$/i
```

  
例2: ua-parser-js  

```
/ip[ honead ]+(.* os\s([\w]+) *\ slike \ smac |;\ sopera )/
```

  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUiclVuO8A0yVBEa8PxLaj7Om8xBpFEPxHsCDB9fru2Ml7d9r267mS2e7JfJyiafSs3ribe9Guia6lUCvXw/640?wx_fmt=png&from=appmsg "")  
### HTTP级的Payload创建  
  
对每个payload，创建应用场景：  

```
var MobileDetect = require (&#34;mobile - detect &#34;);
var headers = req . headers [&#34;user - agent &#34;];
var md = new MobileDetect ( headers );
md. phone ();
```

## 分析网站ReDoS漏洞影响  
  
研究人员发现通过模块接口，有漏洞的正则表达式可以利用这些模块发现ReDoS攻击。每个漏洞都至少出现在一个包中，而不同包的依赖和下载数是不同的。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUiclVuO8A0yVBEa8PxLaj7Om898JlwlrNZvKjqWwbtJGyD48zBL8LdJLricRqBGoCSFfeMSISS3egq9A/640?wx_fmt=png&from=appmsg "")  
  
针对不同的漏洞模块和header的使用场景，研究人员给出了漏洞利用。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUiclVuO8A0yVBEa8PxLaj7Om8UFmPmMmmAtWTM8Ist8k2gdKYpLWTEJO3ibyibJhx413mUdzTcGIPSfcQ/640?wx_fmt=png&from=appmsg "")  
# 预防措施  
  
首先，为了限制通过HTTP header传播的payload的效果，header的大小应该做出限制。这种方法可以缓解一些潜在攻击的效果，但对于与HTTP header相关的漏洞的效果是有限的。因为从网络接收的输入也可以被利用来进行攻击。  
  
第二种预防机制是使用更复杂的正则表达式引擎，这些引擎应该确保线性匹配的时间。问题是这些引擎并不支持高级正则表达式特征，比如先行断言(lookahead)和后行断言(lookbehind)。Davis等人提出一种只调用回溯引擎的混合解决方案，Rust等语言也已经采用了这种方案。但这并不能完全解决该问题，因为一些含有高级特征的正则表达式仍可能含有ReDoS漏洞。研究人员建议Node.js给正则表达式API加一个timeout参数，如果某个匹配花费时间太长，那么Node.js就停止匹配。这也是一种易于实现和应用的方法。  
# 结论  
  
本文分析了基于JavaScript的web服务器的ReDoS漏洞，并说明该漏洞是影响主流网站的重要问题。研究人员在实验中共发现8个漏洞，影响超过339个主流网站。攻击者可以阻塞有漏洞的网站几秒钟甚至更长的时间。  
  
论文下载地址：https://www.usenix.org/system/files/conference/usenixsecurity18/sec18-staicu.pdf  
研究PPT下载地址：https://www.usenix.org/conference/usenixsecurity18/presentation/staicu  
  
**推 荐 阅 读**  
  
      
  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247491634&idx=1&sn=a1873ac267a553dbe39d9b8eae72c5d1&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247493905&idx=2&sn=32dabb1937bb95a440a7e79d05519a44&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247492829&idx=2&sn=8b06dc14b5843d622465cb26c6ddbbe5&scene=21#wechat_redirect)  
  
[](http://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247491787&idx=2&sn=509e2b46d9144323fc9d13a1567296c3&chksm=cf611bc3f81692d5579b8a9128ff711eea3f7660b1ccd884e0be264e895fbfcb4c995c609be8&scene=21#wechat_redirect)  
  
[](http://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247491804&idx=2&sn=eb334c8bb0be9ea0a3baf21db6e8fd07&chksm=cf611bd4f81692c2e80f7855552fdb63b52b89c8b4fbfd50fabbf7cf478aff60c23ff0c22d8c&scene=21#wechat_redirect)  
  
  
横向移动之RDP&Desktop Session Hija  
  
  
