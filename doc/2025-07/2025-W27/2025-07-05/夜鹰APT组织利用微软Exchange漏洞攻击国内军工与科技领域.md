> **原文链接**: https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651324483&idx=1&sn=a5a6d0f5b93f52732649237949b05bd9

#  夜鹰APT组织利用微软Exchange漏洞攻击国内军工与科技领域  
 FreeBuf   2025-07-05 11:01  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibAnU4vEr36WbU2bsWK319vloQ6I9pmVhooC97RsiaQtcHEN9DWkvWWdBOPOucSJ3QDtlQNDQ8U2Hw/640?wx_fmt=png&from=appmsg "")  
  
  
网络安全研究人员近日披露了一个名为夜鹰（NightEagle，又称APT-Q-95）的未记录威胁组织，该组织利用微软Exchange服务器漏洞实施攻击，其攻击链包含零日漏洞利用，主要针对我国国内的政府、国防和科技部门。  
  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibAnU4vEr36WbU2bsWK319v1Y0JM0gjq7tocz5gwjtNVTiab9EzMgXyWgnMK9mZTibBgrKUxQj2hkuw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**Part01**  
## 攻击特征与基础设施  
##   
  
据奇安信红雨滴团队报告，该威胁组织自2023年开始活跃，其网络基础设施更换速度极快。相关发现已在2025年7月1日至3日举办的第三届马来西亚国家网络防御与安全展览会（CYDES 2025）上公布。  
  
  
安全厂商在解释"夜鹰"命名缘由时表示：  
"该组织行动速度如鹰，且主要在中国夜间时段活动"。奇安信补充称，该组织主要针对高科技、芯片半导体、量子技术、人工智能和军事领域的实体机构，核心目的是窃取情报。  
  
  
**Part02**  
### 定制化攻击工具分析  
  
  
奇安信表示，调查始于在某客户终端发现定制版的Go语言工具Chisel。该工具被配置为计划任务，每四小时自动启动一次。  
  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibAnU4vEr36WbU2bsWK319vOHnd4jzht8fsjg4WuHjWkj2N5g4eyHmiatF8euHhzM1ia7QWtU8MrI8Q/640?wx_fmt=jpeg&from=appmsg "")  
  
  
报告指出：攻击者修改了开源内网穿透工具Chisel的源代码，硬编码执行参数，使用指定用户名密码，与指定C&C地址的443端口建立socks连接，并映射到C&C主机的指定端口实现内网穿透功能。  
  
  
**Part03**  
### 零日漏洞利用细节  
  
  
分析发现，木马程序通过.NET加载器投递，该加载器被植入微软Exchange服务器的IIS服务中。进一步分析确认攻击者利用零日漏洞获取machineKey，从而未经授权访问Exchange服务器。  
  
  
报告称：攻击者利用该密钥对Exchange服务器进行反序列化操作，从而在任何符合版本的服务器上植入木马，远程读取任意人员的邮箱数据。  
  
  
奇安信认为，根据攻击活动集中在北京时间晚9点至次日凌晨6点的特征，该威胁组织很可能来自北美地区。微软尚未对  
Exchange服务器漏洞问题发表回复。  
  
  
**参考来源：**  
  
NightEagle APT Exploits Microsoft Exchange Flaw to Target China's Military and Tech Sectors  
  
https://thehackernews.com/2025/07/nighteagle-apt-exploits-microsoft.html  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651324107&idx=1&sn=f89429997e0347cfe1580cc8ca6e858b&scene=21#wechat_redirect)  
  
### 电台讨论  
  
****  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
   
  
