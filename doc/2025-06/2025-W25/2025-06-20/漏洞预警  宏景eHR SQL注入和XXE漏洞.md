> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkwMTQ0NDA1NQ==&mid=2247493458&idx=1&sn=c23bc486899927649e2245662abfb383

#  漏洞预警 | 宏景eHR SQL注入和XXE漏洞  
浅安  浅安安全   2025-06-20 00:00  
  
**0x00 漏洞编号**  
- # 暂无  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
宏景人力资源管理系统是一款由宏景软件研发的系统。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/7stTqD182SXhZfJGiaXfdjmnmnU9CcG6XajFjVjAA4Jno8LwWB1ia5Py19wpjxzZ7EOR0eoXNIfiaiceHt9Siby29Sg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
**0x03 漏洞详情**  
  
**漏洞类型：**  
SQL注入  
  
**影响：**  
敏感信息泄露****  
  
**简述：**  
宏景eHR的  
/servlet/XFireServlet/HrChangeInfoService:getChangeUsers  
接口处存在SQL注入漏洞，未经过身份认证的远程攻击者可利用此漏洞执行任意SQL指令，从而窃取数据库敏感信息。  
  
**漏洞类型：**  
XXE  
  
**影响：**  
执行代码****  
  
**简述：**  
宏景eHR的/servlet/XFireServlet/HrChangeInfoService:returnSynchroXml接口处存在  
XXE  
漏洞，  
未经身份验证的攻击者可以通过该漏洞远程执行代码，从而控制目标服务器。  
  
**0x04 影响版本**  
- 宏景eHR  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.hjehr.com/  
  
  
  
