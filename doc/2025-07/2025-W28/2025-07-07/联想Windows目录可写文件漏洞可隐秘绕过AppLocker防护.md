> **原文链接**: https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651324515&idx=1&sn=e502828a52cb7663487c30f07c064387

#  联想Windows目录可写文件漏洞可隐秘绕过AppLocker防护  
 FreeBuf   2025-07-06 11:02  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR380mGfJnMjqmicdw8f31nCMVib4Axtqqs0jE8K3ugDKM9q7gicEiaUm5KV8L28n7OQXFSRGwp1gNjmBYg/640?wx_fmt=png&from=appmsg "")  
  
  
研究人员在联想预装Windows操作系统中发现一个安全漏洞——Windows目录下的可写文件 MFGSTAT 可使攻击者绕过微软AppLocker安全框架。该漏洞影响所有采用默认Windows安装的联想设备，对企业安全环境构成威胁。  
  
  
漏洞核心在于C:\Windows\目录下的MFGSTAT.zip文件存在错误权限配置，允许任何经过身份验证的用户对该位置进行写入和执行操作。  
  
  
关键发现：  
  
1. 联想Windows目录下可写的MFGSTAT.zip文件因权限配置错误可绕过AppLocker防护   
  
2. 利用NTFS备用数据流(ADS)在压缩文件中隐藏可执行文件，通过合法Windows进程运行   
  
3. 影响所有预装Windows的联想设备   
  
4. 可通过PowerShell命令或企业管理工具删除该文件  
  
  
**Part01**  
## 漏洞利用技术  
## NTFS备用数据流(ADS)  
  
  
攻击技术利用了NTFS备用数据流(ADS)这一鲜为人知的特性，攻击者可在看似无害的文件中隐藏可执行内容。TrustedSec公司的Oddvar Moe通过以下命令序列，将Microsoft Sysinternals的autoruns.exe工具嵌入存在漏洞的zip文件进行演示：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR380mGfJnMjqmicdw8f31nCMV7ndQe367ictR2HO3tL66PPmHEWVbJ0XLTEJ6IbTPMqsHfXFuAlfApAg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
数据流注入后，攻击者可通过合法的Microsoft Office应用程序加载器执行恶意载荷：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR380mGfJnMjqmicdw8f31nCMV5xOe7prhQhXE6kqjL4MTiaKBMB04jEIHYHjcwq8ZSR3THzUH8aKbkNQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
这种"利用合法二进制文件"(LOLBin)技术通过受信任的Windows进程执行未授权代码，可规避传统安全监控系统。由于完全使用合法系统组件，该攻击向量使安全团队的检测工作变得异常困难。  
  
  
**Part02**  
## 漏洞历史与厂商响应  
  
  
该漏洞最初于2019年常规安全评估中发现，但直到2025年Moe重新调查时才引起关注。在确认该问题影响多代联想设备后，研究人员联系了联想产品安全事件响应团队(PSIRT)。联想回应第一时间提供修复指南，客户可按照修复指南操作来保障安全。  
###   
  
**Part03**  
## 缓解措施  
  
  
企业可通过多种方法立即实施修复。最直接的方式是使用PowerShell删除漏洞文件：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR380mGfJnMjqmicdw8f31nCMVsDavVTyBeaO2bV7ricQVITqLOK6ep1cbiaU60YqOG8HesgANEFCkzjLw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
管理员也可使用带隐藏文件属性标志的命令提示符：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR380mGfJnMjqmicdw8f31nCMVreGatGJiaSVcnnCYXG0w9E25VcCibyyJnEibkbh3wzdy2kftibBX0uicu9A/640?wx_fmt=jpeg&from=appmsg "")  
  
  
企业环境应利用组策略首选项、System Center Configuration Manager(SCCM)等管理工具确保所有受影响系统完成统一清理。该事件凸显了实施AppLocker部署时全面文件系统审计的重要性，即使微小疏忽也可能造成可绕过基础访问控制的安全漏洞。  
  
  
**参考来源：**  
  
Writable File in Lenovo’s Windows Directory Enables a Stealthy AppLocker Bypass  
  
https://cybersecuritynews.com/writable-file-in-lenovos-windows-directory/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651324107&idx=1&sn=f89429997e0347cfe1580cc8ca6e858b&scene=21#wechat_redirect)  
  
### 电台讨论  
  
****  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
   
  
