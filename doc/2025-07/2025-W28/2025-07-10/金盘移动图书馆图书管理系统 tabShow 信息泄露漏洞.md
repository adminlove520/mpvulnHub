> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkzMTcwMTg1Mg==&mid=2247492090&idx=1&sn=d3730d112f227a6e2220302b76ba7ea4

#  金盘移动图书馆图书管理系统 tabShow 信息泄露漏洞  
Superhero  Nday Poc   2025-07-10 01:57  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Melo944GVOJECe5vg2C5YWgpyo1D5bCkYN4sZibCVo6EFo0N9b7Kib4I4N6j6Y10tynLOdgov9ibUmaNwW5yeoCbQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Melo944GVOJECe5vg2C5YWgpyo1D5bCkhic5lbbPcpxTLtLccZ04WhwDotW7g2b3zBgZeS5uvFH4dxf0tj0Rutw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Melo944GVOJECe5vg2C5YWgpyo1D5bCk524CiapZejYicic1Hf8LPt8qR893A3IP38J3NMmskDZjyqNkShewpibEfA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
内容仅用于学习交流自查使用，由于传播、利用本公众号所提供的  
POC  
信息及  
POC对应脚本  
而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号Nday Poc及作者不为此承担任何责任，一旦造成后果请自行承担！  
  
  
**01**  
  
**漏洞概述**  
  
  
金盘移动图书馆图书管理系统 tabShow 存在信息泄露漏洞，未经身份验证的远程攻击者可利用此漏洞获取后台账号密码等敏感信息，从而登录后台，使系统处于极不安全的状态。  
  
**02******  
  
**搜索引擎**  
  
  
FOFA:  

```
icon_hash=&#34;89337953&#34;
```

  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwJ4PqvQpOAibes7tibfU2Fle9bbHfBQSCCYJQ3bL4QpXu9MkgvmbGseqXT79fRiaQItz0a9Ge0I1nm6g/640?wx_fmt=png&from=appmsg "")  
  
  
**03******  
  
**漏洞复现**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwJ4PqvQpOAibes7tibfU2Fle9boYWTyy79Rgaicw5GPffaoQG7BqyUibIibS8JoUcluvwOKUb5MgzeTTWQ/640?wx_fmt=png&from=appmsg "")  
  
  
**04**  
  
**自查工具**  
  
  
nuclei  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwJ4PqvQpOAibes7tibfU2Fle9PI59CY2lnkkibKawiaquxbLrCrLwG3TYy6jS0J7RJhDEZTB187hoFzEg/640?wx_fmt=png&from=appmsg "")  
  
afrog  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwJ4PqvQpOAibes7tibfU2Fle9yp0GbhDrJutM87KIbRYniaX6duMZjPkbSN2W6n928o2MHlBzfntrsbA/640?wx_fmt=png&from=appmsg "")  
  
xray  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwJ4PqvQpOAibes7tibfU2Fle9tbsUAJ8uc4LOiaPnVMX12fs9dddIKJp1ZVbNd3icDQQFdxfr1iaQnLqvA/640?wx_fmt=png&from=appmsg "")  
  
  
**05******  
  
**修复建议**  
  
  
1、关闭互联网暴露面或接口设置访问权限  
  
2、升级至安全版本  
  
  
**06******  
  
**内部圈子介绍**  
  
  
【Nday漏洞实战圈】🛠️   
  
专注公开1day/Nday漏洞复现  
 · 工具链适配支持  
  
 ✧━━━━━━━━━━━━━━━━✧   
  
🔍 资源内容  
  
 ▫️ 整合全网公开  
1day/Nday  
漏洞POC详情  
  
 ▫️ 适配Xray/Afrog/Nuclei检测脚本  
  
 ▫️ 支持内置与自定义POC目录混合扫描   
  
🔄 更新计划   
  
▫️ 每周新增7-10个实用POC（来源公开平台）   
  
▫️ 所有脚本经过基础测试，降低调试成本   
  
🎯 适用场景   
  
▫️ 企业漏洞自查 ▫️ 渗透测试 ▫️ 红蓝对抗   
▫️ 安全运维  
  
✧━━━━━━━━━━━━━━━━✧   
  
⚠️ 声明：仅限合法授权测试，严禁违规使用！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/wnJTy44dqwLJNGic1zib33kic8nRYia3Uuvv5BJyvALx1xxibmDMhbJNRbnXRrHpVoFzXq49CVOJmEkfEKf3fjDEXgQ/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
