> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzI4MDQ5MjY1Mg==&mid=2247516905&idx=1&sn=900d3adbb01a34ee0615ded711105778

#  网站API挖掘提取与漏洞探测工具 -- Super-API-Finder(6月30日更新)  
hackerchuan1  Web安全工具库   2025-07-01 16:00  
  
资料合集  
  
链接：https://pan.quark.cn/s/770d9387db5f  
  
===================================  
  
**免责声明**  
  
请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，  
安全性自测  
，  
大家都要把工具当做病毒对待，在虚拟机运行。  
如有侵权请联系删除。个人微信：  
ivu123ivu  
  
  
**0x01 工具介绍**  
  
1.支持响应信息中的敏感信息、URL、URI，JS信息提取,比如前端泄露的aeskey，iv，AppSecret AppId，阿里云，腾讯云 Cloud Key，手机号，账号密码，JDBC等等 2.自动基于已知路径信息计算PATH对应的实际URL 3.自动访问 挖掘出来的URL信息 进行递归式的信息提取. 4.对webpack的js提取 5.常见漏洞探测，swagger-ui未授权，spring boot信息泄露,AppSecret AppId，阿里云，腾讯云 Cloud Key，信息泄露手机号账号密码，Druid未授权，普罗米修斯未授权访问，docker未授权访问，GraphQL api，JDBC泄露，elastic search未授权访问等。  
  
**0x02 安装与使用**  
  
![222222222片_20250630105617](https://mmbiz.qpic.cn/sz_mmbiz_png/8H1dCzib3UibsQTnqhnxI79t1aAr8MmCHA4Ag6hicG944dL4RnGbwHBayhMubbLYWUbR0e8wYQxnNSdrHSmdmaLsg/640?wx_fmt=png&from=appmsg "")  
  
   
![3333_20250630105654](https://mmbiz.qpic.cn/sz_mmbiz_png/8H1dCzib3UibsQTnqhnxI79t1aAr8MmCHAa0WYDhAibRoMby40R5ot1ZQHsBBEJ1bFelYpZicmvnLiaaEZEWDdHX3Rw/640?wx_fmt=png&from=appmsg "")  
  
   
![44444片_20250630105727](https://mmbiz.qpic.cn/sz_mmbiz_png/8H1dCzib3UibsQTnqhnxI79t1aAr8MmCHAhrdMFxJvhBzl1UFialL7C8xPEPo9lb9DTdicFGFSQo1wuh402QW3kp8w/640?wx_fmt=png&from=appmsg "")  
  
   
![1751252159243](https://mmbiz.qpic.cn/sz_mmbiz_png/8H1dCzib3UibsQTnqhnxI79t1aAr8MmCHA4Ag6hicG944dL4RnGbwHBayhMubbLYWUbR0e8wYQxnNSdrHSmdmaLsg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/8H1dCzib3Uibu7uX2oYjbbibndft14nzUMIoRia7UqCAgMXSZAu1iaBDWSWLLuFnyibwfOiaCLO7YXaC6qib8icgHXwoe3Q/640?wx_fmt=jpeg "")  
  
  
  
  
**·****今 日 推 荐**  
**·**  
  
> 《红队VS蓝队：网络攻防实战技术解析》分为红方攻击篇（第1~5章）和蓝方防守篇（第6~10章）两部分。红方攻击篇从实战演练的传统攻击思路出发，介绍了互联网信息收集、外网边界突破、内网渗透、权限提升与维持四大环节，覆盖了实战攻击的全流程。最后通过几个攻击方的经典案例，分享了不同场景下的攻击思路与技巧。蓝方防守篇从讲述完整的保障体系出发，介绍了常用的技术、保障时期防护体系的落地、常态化运营与重要时期保障之间的转换、特殊场景下的防护策略等，并在第10章通过4个案例分享了笔者团队实施的保障案例，希望读者能从中了解保障的真实过程及准备过程中的检查要点。  
  
  
  
  
