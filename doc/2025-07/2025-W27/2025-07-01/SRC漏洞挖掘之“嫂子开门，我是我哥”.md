> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkyNzM2MjM0OQ==&mid=2247497798&idx=1&sn=2c78f0ec8d3d1f242ce515062c3695df

#  SRC漏洞挖掘之“嫂子开门，我是我哥”  
原创 小恰  隐雾安全   2025-07-01 01:00  
  
**No.0**  
  
**前言**  
  
  
在一次日常的漏洞挖掘过程中，在一个微信小程序中本来毫无头绪的时候，在巧合之下点开了另外一个小程序，结果两个小程序竟存在联系，经过不断测试，挖出水平越权漏洞。  
  
成功达成成就“嫂子开门，我是我哥”  
  
**No.1**  
  
**正文**  
  
  
开局就是这样一个小程序（我们称之为小程序A）  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLnal0BJB5cZpOwgTVs5rygHISAt0yicu0FDibicr7icuibX19Lz5SDyfhfbdw/640?wx_fmt=png&from=appmsg "")  
  
  
随便输入一个手机号13111111111之后，会显示如下  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLnu3VxjTBt2VOeF8abyZLcJicYQWv3VxgLAZU5VK3v3QZxtPqpFlrcPQg/640?wx_fmt=png&from=appmsg "")  
  
  
可以知道13111111111这个手机号绑定的用户名、学号以及学校，但是用户名被打码了，抓返回包也是打码数据，这也构不成敏感信息泄露，只能先放在一边。  
  
  
然后我又点开了另一个小程序（小程序B），在小程序B的个人中心处有一个添加学员的功能点  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLnsz4ictudAHFpNYszph8OFNrx42czOOd2yqsomERpgOOzU9X8AOm4wqg/640?wx_fmt=png&from=appmsg "")  
  
  
有两个方式添加：手机号绑定和学员号绑定  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLns1Xb46oTrHETdbdwWV0qn4rlQkecTInxjLcDZ5m71ddkkkCEcWzt8Q/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLn5fYHkfsW2owr4rn8dw0wecKxXibbzjh8DxlTetQ242o4pdQzz2vEakQ/640?wx_fmt=png&from=appmsg "")  
  
  
等一下，这个学员号看起来好眼熟啊，会不会是小程序A中的学号呢？试试呗，反正又不会怎么样  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLns2ibjAOvic2JJUg1cgCiaoXVUhUCGvx215UBO7PUTsWv8StSB3qECboXw/640?wx_fmt=png&from=appmsg "")  
  
  
好家伙，这明文信息就这么轻松得到了，事情变得有趣起来了呢。当时我看到了信息名片下面有一个获取验证码，想着会不会有验证码回显导致的任意用户绑定，于是bp抓到如下数据包  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLnhuZWTQbhXPyNqgAbJQtFgQ3HoMLaEh6IsKPCxYq2vK9FwROWAYSiaTg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLn8c1aelYHGgxX0OPGZmeRQTV8XjBKiae0CHxUGh0qb9rdia6diaBKbXdhQ/640?wx_fmt=png&from=appmsg "")  
  
  
遗憾的是，该发送短信的接口不存在验证码回显，但数据包携带的数据引起了我的注意。“userId”经测试是自己账号的身份id，而“studentId”就是用户名为“家长”的账号的身份id。这样一来我首先想要去测试的就是水平越权漏洞。  
  
  
仍旧在当前小程序的个人中心，来到个人信息修改处  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLnb0YpyC0Ay6O4mTVBZTYcAOAFYA8aMmytGicZ9dsaibCvxCgiaYJRbibQrQ/640?wx_fmt=png&from=appmsg "")  
  
  
点击“修改”时bp抓包  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLnTPX6CIwCIuTA3YKLkC3ErMTZjZNXAr5pEtZfTpKdDKujfJ0iaq6aBtQ/640?wx_fmt=png&from=appmsg "")  
  
  
数据包如下  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLnNEEXWZDgWcM7XbvyqicY9ojegqWRkBAAXZicgCS4dZVc8ibBadFMYpicrA/640?wx_fmt=png&from=appmsg "")  
  
  
哟？！，改成我们之前说到的id试试  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLnEiaBVekCBfJTv1W8Wl5wzLLEu0fckfkspD7Dy9chFsuaCNDjVM0Nl2w/640?wx_fmt=png&from=appmsg "")  
  
  
再次去查那个账号时，发现已经被越权修改了  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLnbCUyNzkicgYIHvYAMe9LxRIAsuGq3qRmOIdpmLLAELstu3JjyAMjXzA/640?wx_fmt=png&from=appmsg "")  
  
  
好的，得吃！直接写报告提交。  
  
  
**No.3**  
  
**网安沟通交流群**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ELQKhUzr34z27aOjKIs2R1F4Vva1bgLnnhKNA0RYdlHUuUdbvDTibtib8jf2mGB5pbLOicuoNd3lxnDPwICjjeQnQ/640?wx_fmt=jpeg&from=appmsg "")  
  
**扫码加客服小姐姐拉群**  
  
  
  
