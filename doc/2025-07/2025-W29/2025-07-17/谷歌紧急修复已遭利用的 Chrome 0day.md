> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523583&idx=1&sn=f3695d751d9189ce3ff6b61f71cc9942

#  谷歌紧急修复已遭利用的 Chrome 0day  
Ddos  代码卫士   2025-07-16 10:07  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**谷歌发布 Chrome Desktop (138.0.7204.157/.158) 稳定版，修复了六个漏洞，其中一个已遭在野利用。目前，该安全更新已发布 Windows、Mac 和 Linux 版本，自动更新有望在几天或几周后发布。**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRRbmOnuRdJWeyWKga3vkZgq3e0ibI4Bq1nM4F2UmgbaibBfDs67uQDTWJYzz1LtaRc0EtKnfcvvYjA/640?wx_fmt=png&from=appmsg "")  
  
  
本次更新最紧急的漏洞是一个高危漏洞CVE-2025-6558，与对ANGLE和GPU组件中的不受信任输入的验证不正确有关。该漏洞由谷歌威胁团队 (TAG) 的研究员 Clément Lecigne 和 Vlad Stolyarov 发现，目前正被攻击者用于获得越权访问权限或者在目标机器上执行恶意代码。  
  
谷歌证实称，“谷歌已发现CVE-2025-6558的在野利用。”ANGLE 是将 WebGL 和其它图像调用翻译成主机系统原生API的重要图层。该图层中的漏洞可导致攻击者操纵渲染流程，运行恶意代码。  
  
除了CVE-2025-6558外，谷歌还修复了如下高危漏洞：  
  
- CVE-2025-7656：位于Chrome JavaScript 引擎V8中的整数溢出漏洞，由 Shaheen Fazim 报送并获得7000美元的赏金。该漏洞可导致内存损坏以及任意代码执行后果。  
  
- CVE-2025-7657：位于用于视频、声音和文件共享的实时通信协议 WebRTC 中的一个释放后使用漏洞，由 jakebiles 报送，可导致内存损坏、远程崩溃或攻陷后果。  
  
  
  
在任何平台 Windows、Mac 或 Linux 上使用 Chrome 的用户，应立即更新。Chrome 一般会在后台提供自动更新，但用户可导航至“设置＞关于Chrome＞更新”手动检查，重启浏览器以确保已应用补丁。  
  
  
开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[谷歌紧急修复已遭利用的 Chrome 0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523414&idx=1&sn=af483917f833027e64a5dc3b05e6f56a&scene=21#wechat_redirect)  
  
  
[谷歌悄悄紧急修复已遭利用的 Chrome 0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523177&idx=1&sn=6ead40fb0a70735a161f4ecd984a3f01&scene=21#wechat_redirect)  
  
  
[Chrome修复已遭活跃利用的0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523031&idx=1&sn=40bc8fad7dc229f984420d3f6109a0b9&scene=21#wechat_redirect)  
  
  
[Firefox 存在严重漏洞，类似于 Chrome 已遭利用0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522612&idx=2&sn=50c7ad88e87b485a09c7ae916f9d9677&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://securityonline.info/urgent-chrome-update-google-patches-critical-zero-day-cve-2025-6558-under-active-attack/  
  
  
题图：  
Pixabay Licen  
se  
  
****  
**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg "")  
  
**奇安信代码卫士 (codesafe)**  
  
国内首个专注于软件开发安全的产品线。  
  
   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif "")  
  
   
觉得不错，就点个 “  
在看  
” 或 "  
赞  
” 吧~  
  
