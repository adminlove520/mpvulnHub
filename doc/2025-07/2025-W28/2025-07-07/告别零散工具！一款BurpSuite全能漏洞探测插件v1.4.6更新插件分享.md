> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247493216&idx=1&sn=cf4bb7dfb28d39e2e378a50a5bc917ed

#  告别零散工具！一款BurpSuite全能漏洞探测插件v1.4.6更新|插件分享  
TheCryingGame  渗透安全HackTwo   2025-07-07 16:00  
  
0x01 工具介绍  
  
  
**在漏洞探测中疲于切换工具？TsojanScan作为BurpSuite全能插件，集Fastjson、SpringBoot、SQL注入等30+漏洞检测于一体，以最少请求实现精准打击！支持2025新版BurpSuite，新增Nacos/XyzDnsLog等模块，优化逻辑提升稳定性。无论你是渗透新手还是老手，这款开源神器将彻底改变你的工作流。文末附实战技巧和项目地址，点击关注获取进阶指南！**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOE1vTofY5Yib7uB6RtqITs96vNqhDpbq0z5zgdxz5yyBZwBwZ6Te8W3Wg/640?wx_fmt=png&from=appmsg "")  
  
  
**注意：**  
现在只对常读和星标的公众号才展示大图推送，建议大家把  
**渗透安全HackTwo**  
"**设为****星标⭐️**  
"  
**否****则可能就看不到了啦！**  
  
**下载地址在末尾#渗透安全HackTwo**  
  
0x02   
功能简介  
  
  
功能特性  
#### 面板  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEadicHudPPRUUCicSxTmpjiawhNrYsOj65Ls9LsJmqJf2shg6eD71PrAow/640?wx_fmt=png&from=appmsg "")  
### 自定义黑名单，插件不扫描黑名单的url列表，进行Reg匹配优先级第一  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEZjkrm1d48KMxMfiaY2V9EClKPJicUh9fC7EmZcSffaMyOUN3xbH35GcA/640?wx_fmt=png&from=appmsg "")  
#### 主动探测  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOErYcTpxZEr9W6mEAo4gHj17gF8BhNItnJBD9nyHxnBvjdHn3n0j69vQ/640?wx_fmt=png&from=appmsg "")  
#### fastjson >=1.2.80探测  
#### 本地环境  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEWwZgmNjRmvREgUkESmZaK345AiaIn16BeLQoeOHUYkTn9pnhCGkvuTg/640?wx_fmt=png&from=appmsg "")  
#### 预查询DNSlog接口  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEBalhMbgejb7UmD4UNCygFtT4IoM5Tag13A9knJxMuKRINRiaH2sJPUg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEgnAjgMTGibungHGn8UqHuKHbe45EhwBUVyU5PMuYicGx8lRFL1FWUictw/640?wx_fmt=png&from=appmsg "")  
#### 扫描  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEkGagqhAJYRiaBvOEp8ONicGVSozVF0UicmzglW6OqR1oyoVyAWQ93QNgA/640?wx_fmt=png&from=appmsg "")  
#### 判断准确版本  
#### 1.2.80版本探测如果收到了两个dns请求，则证明使用了1.2.83版本，如果收到了一个 dns 请求，则证明使用了1.2.80版本。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOErAbEMDLy28h6jS5jfFvicWxfWz8Zx9p9LLZCsCtMj0MSG3umL6juGNA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOE9DNQk13sKmicvBLmnbym881H2AXJX4wEu16m0ibaLBBMiaEFiarLicX7Uug/640?wx_fmt=png&from=appmsg "")  
  
DNSLog查询漏报  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEPwfPjpaM8ZYowRQpsHXrHkJTyY7Ddl1sU5ou8ibEyZ7vewPiaC5Kde2w/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOE0gnK6EE0IjFJAID4icia2Y50IJBvSIKJqib36zpocZh6RXo0jQUiaLghdQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEUBnVRgic88N8gvyEbfKlaa3Ub9F1anPG0k7F4YgHcbic5JxL0pbNbPibQ/640?wx_fmt=png&from=appmsg "")  
  
扫描  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEvDiauLkbLozF0dOOaN1N2w2nndSiaxDTEy25ooJq4c5YF72wlnQXg6mw/640?wx_fmt=png&from=appmsg "")  
#### 判断准确版本  
#### 1.2.80版本探测如果收到了两个dns请求，则证明使用了1.2.83版本，如果收到了一个 dns 请求，则证明使用了1.2.80版本。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEw7rDibormQO5iabdjV0OSAmU7KEHxlTLMhx5B2wciavv6CfQOuDQmdbsQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOETicxHJPOBM0OBsVCnoH1qiceiaMYUic7ojjeRO7zW0GYaOKDXHXG0WKOtQ/640?wx_fmt=png&from=appmsg "")  
#### DNSLog查询漏报  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEctHkxrNfbZrScu2uzMRboxNibFxPwQLHCpRgszNBa84DibNKfXJXoyRA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEsgxCNXVuA5K0xYNQibTp0lRjjflOUE900VaOvEprkCHjQqufubGicYjg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOE2TyBQeYDBrrBabwoDyKxSWcWwNtfW9mBcLNTZtH1XQCEzGfwaUwaDQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOE2TyBQeYDBrrBabwoDyKxSWcWwNtfW9mBcLNTZtH1XQCEzGfwaUwaDQ/640?wx_fmt=png&from=appmsg "")  
  
注意⚠️  
：扫描结束后才会在BurpSuite的Target、Dashboard模块显示高危漏洞，进程扫描中无法进行同步，但可以在插件中查看（涉及到DoPassive方法问题）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEicQxavyFwetZuV4dwvGpjxTicE2RW1wYtZy1x7wu6RIPyhv2eX9n3ttA/640?wx_fmt=png&from=appmsg "")  
  
  
0x03更新说明  

```
新增XyzDnsLog平台，删除不可用的DnsLog，由于国内政策问题，建议使用Ceye dnslog平台;
修复适配Burp Suite Pro 2024/2025年度版本报错问题;
增加sql语法错误的页面回显扫描模块，只显示sql错误显示（参数后面增加单引号、双引号、反斜线，去查看有没有SQL错误语句）
增加jpath主动模块化扫描，集合SpringBoot Env、Druid、Swagger 相关无害化POC;
更新dnslog平台，删除不可用的dnslog，默认设置Ceye dnslog平台;
修复新版本BurpSuite版本报错问题 #23 ;
修复删除测试垃圾代码，优化插件稳定性
```

  
0x04 使用介绍  
  
📦用法：  
加载插件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qLz32sSCvA7CAyIxwffOEO3Jn4w6E5XJ8r0jGVUpAd7yCwRxVkz8Pwowh0Yzl3joKRTGHBxurrw/640?wx_fmt=png&from=appmsg "")  
  
  
  
**0x05 内部VIP星球介绍-V1.4（福利）**  
  
        如果你想学习更多**渗透测试技术/应急溯源/免杀/挖洞赚取漏洞赏金/红队打点/HW漏洞库**  
欢迎加入我们**内部星球**  
可获得内部工具字典和享受内部资源和  
内部交流群，**每1-2天更新1day/0day漏洞刷分上分****(2025POC更新至4000+)**  
**，**  
包含网上一些**付费****工具及BurpSuite自动化漏****洞探测插件，AI代审工具等等**  
。shadon\Quake\  
Fofa高级会员，CTFShow等各种账号会员共享。详情直接点击下方链接进入了解，觉得价格高的师傅可后台回复"   
**星球**  
 "有优惠券名额有限先到先得！全网资源  
最新  
最丰富！**（🤙截止目前已有1900+多位师傅选择加入❗️早加入早享受）**  
  
****  
2025HW漏洞情报分享：https://t.zsxq.com/Faujy  
  
****  
  
**👉****点击了解加入-->>内部VIP知识星球福利介绍V1.4版本-1day/0day漏洞库及内部资源更新**  
  
****  
  
  
结尾  
  
# 免责声明  
  
  
# 获取方法  
  
  
**公众号回复20250708获取下载**  
  
# 最后必看-免责声明  
  
  
      
文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如  
用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。  
本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。  
如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！  
  
  
  
# 往期推荐  
  
  
**1.内部VIP知识星球福利介绍V1.4（AI自动化工具）**  
  
**2.CS4.8-CobaltStrike4.8汉化+插件版**  
  
**3.最新BurpSuite2025.2.1专业版（新增AI模块）**  
  
**4. 最新xray1.9.11高级版下载Windows/Linux**  
  
**5. 最新HCL AppScan Standard**  
  
  
渗透安全HackTwo  
  
微信号：关注公众号获取  
  
后台回复星球加入：  
知识星球  
  
扫码关注 了解更多  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qFFAxdkV2tgPPqL76yNTw38UJ9vr5QJQE48ff1I4Gichw7adAcHQx8ePBPmwvouAhs4ArJFVdKkw/640?wx_fmt=png "二维码")  
  
  
  
[全面资产收集流程及方法解析 万字长文窥探信息收集|挖洞技巧](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247491574&idx=1&sn=48d865c82a228bd135a035419c765e94&scene=21#wechat_redirect)  
  
  
