> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkwMTQ0NDA1NQ==&mid=2247493534&idx=3&sn=01f7df8ff1225368e326cb0fcc2ab29f

#  漏洞预警 | 灵当CRM文件上传漏洞  
浅安  浅安安全   2025-06-29 16:01  
  
**0x00 漏洞编号**  
- # 暂无  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
灵当CRM是一款专为中小企业打造的智能客户关系管理工具。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SVt7YFyTQQEfhb7U1ia1Eib9LbzN6IooEiaAu8gmJRoBbalGtmLHyIvibmIAvPanxUHCsPxmIasVyUNAA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
**0x03 漏洞详情**  
###   
  
**漏洞类型：**  
任意文件上传  
  
**影响：**  
写入后门  
  
****  
  
**简述：**  
灵当CRM的  
/crm/WeiXinApp/CallRecordLog/getLogInfo.php  
接口处存在文件上传漏洞，攻击者可以通过该漏洞上传恶意脚本文件到服务器，从而控制目标服务器。  
  
**0x04 影响版本**  
- 灵当CRM  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.51mis.com/  
  
  
  
