> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkwMTQ0NDA1NQ==&mid=2247493546&idx=1&sn=d51a95f3597d55dc86040dcf83515674

#  漏洞预警 | WinRAR代码执行漏洞  
浅安  浅安安全   2025-07-01 00:00  
  
**0x00 漏洞编号**  
- # CVE-2025-6218  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
WinRAR是一款使用广泛、功能强大的压缩文件管理工具。该软件可用于备份数据，缩减电子邮件附件的大小，解压缩从Internet上下载的RAR、ZIP及其它类型文件，并且可以创建RAR及ZIP格式的压缩文件。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SV3C9JJP2zL1ehX4SBadI92Rvr56TxawrH7tUOibZqMdVxIX6QwYfvFx1Sa0lEYkILRxz4ZKMvVibCw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
**0x03 漏洞详情**  
  
**CVE-2025-6218**  
  
**漏洞类型：**  
代码执行  
  
**影响：**  
执行任意代码  
  
**简述：**  
由于WinRAR对文件路径的处理不当，攻击者可构造恶意的文件路径，诱使用户访问恶意页面或打开恶意文件，从而导致进程访问不该访问的目录，在当前用户上下文中执行恶意代码。  
   
  
**0x04 影响版本**  
- WinRAR <=   
7.11  
  
**0x05****POC状态**  
- 未公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.rarlab.com/  
  
  
  
