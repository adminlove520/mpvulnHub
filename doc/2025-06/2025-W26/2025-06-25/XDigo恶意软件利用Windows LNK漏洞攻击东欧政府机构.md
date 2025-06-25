> **原文链接**: https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651323665&idx=4&sn=5cb47657df2c570bb3840e433f112670

#  XDigo恶意软件利用Windows LNK漏洞攻击东欧政府机构  
 FreeBuf   2025-06-24 11:03  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38LEqIgxpLGJtu8bNZDFVwZOTicmPvIZiaBPR0hT6iaEQSo2xUxUVrEuwicXgibEMl7OxCYQZ9ms7Rz0NA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
网络安全研究人员发现一款名为XDigo的Go语言恶意软件，该软件被用于2025年3月针对东欧政府实体的攻击活动。法国网络安全公司HarfangLab表示，攻击链利用了一系列Windows快捷方式(LNK)文件作为多阶段攻击流程的一部分来部署恶意软件。  
  
  
**Part01**  
### 历史背景与攻击手法  
  
  
自2011年以来，名为XDSpy的网络间谍组织一直以东欧和巴尔干地区的政府机构为目标。该组织最早由白俄罗斯CERT在2020年初记录在案。近年来，俄罗斯和摩尔多瓦的企业成为多起攻击活动的目标，攻击者投放了UTask、XDDown和DSDownloader等恶意软件家族，这些软件能够下载额外载荷并从受感染主机窃取敏感信息。  
  
  
HarfangLab观察到，攻击者利用了Microsoft Windows处理特制LNK文件时触发的远程代码执行漏洞（编号ZDI-CAN-25373）。该漏洞由趋势科技在今年3月初公开披露。  
  
  
趋势科技零日计划(ZDI)指出："特制的LNK文件数据可能导致文件中的危险内容对通过Windows用户界面检查文件的用户不可见。攻击者可利用此漏洞在当前用户上下文中执行代码。"  
  
  
**Part02**  
### 技术细节分析  
###   
  
对利用ZDI-CAN-25373漏洞的LNK文件样本分析发现，其中9个样本利用了微软未完全实现其MS-SHLLINK规范（8.0版）导致的LNK解析混淆漏洞。根据规范，LNK文件中字符串长度的理论最大值应为两个字节可编码的最大整数值（即65,535个字符），但Windows 11实际实现将存储的文本内容限制为259个字符（命令行参数除外）。  
  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38LEqIgxpLGJtu8bNZDFVwZ6Ny5CIutLqbnGC0uvm3XN8NUicezzvJCqsV7qeJngKmOFsUWCRYibkEA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
HarfangLab表示："这导致某些LNK文件在规范与Windows系统中的解析方式存在差异，甚至某些按规范应无效的LNK文件在微软Windows中实际有效。由于这种规范偏差，攻击者可精心构造LNK文件，使其在实现规范的第三方解析器中看似执行特定命令行或显示为无效，而在Windows中实际执行另一条命令行。"  
  
  
结合空白填充问题与LNK解析混淆漏洞，攻击者可隐藏Windows UI和第三方解析器中实际执行的命令。这9个LNK文件通过ZIP压缩包分发，每个压缩包内还包含第二个ZIP文件，其中有诱饵PDF文件、被重名的合法可执行文件以及通过二进制文件侧加载的恶意DLL。  
  
****  
**Part03**  
### 恶意软件功能与目标  
  
  
该DLL是第一阶段的下载器ETDownloader，其功能很可能是部署名为XDigo的数据收集植入程序。根据基础设施、受害者特征、时间节点、战术和工具重叠情况分析，XDigo被认为是卡巴斯基2023年10月报告的恶意软件"UsrRunVGA.exe"的新版本。  
  
  
XDigo具有窃取文件、提取剪贴板内容和截屏的功能，还支持通过HTTP GET请求从远程服务器获取命令或二进制文件并执行。数据外泄通过HTTP POST请求实现。已确认至少一个明斯克地区的目标，其他证据表明攻击还针对俄罗斯零售集团、金融机构、大型保险公司和政府邮政服务。  
  
  
HarfangLab指出："这一目标特征与XDSpy历史上针对东欧特别是白俄罗斯政府实体的攻击模式一致。XDSpy的针对性还体现在其定制化的规避能力上，据报道该组织的恶意软件是首个尝试规避俄罗斯网络安全公司PT Security沙箱解决方案检测的恶意软件，该公司为俄罗斯联邦的公共和金融组织提供服务。"  
###   
  
**参考来源：**  
  
XDigo Malware Exploits Windows LNK Flaw in Eastern European Government Attacks  
  
https://thehackernews.com/2025/06/xdigo-malware-exploits-windows-lnk-flaw.html  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651323514&idx=1&sn=0da8f04aecf7bbb0f3dca8f4bd1ff81f&scene=21#wechat_redirect)  
  
### 电台讨论  
  
****  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR3icF8RMnJbsqatMibR6OicVrUDaz0fyxNtBDpPlLfibJZILzHQcwaKkb4ia57xAShIJfQ54HjOG1oPXBew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
