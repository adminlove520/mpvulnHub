> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzI2NzAwOTg4NQ==&mid=2649795710&idx=3&sn=52208912e929c701e1fe746d0a6cbada

#  WinRAR 0day漏洞在暗网以 8 万美元的价格出售  
会杀毒的单反狗  军哥网络安全读报   2025-07-15 01:01  
  
**导****读**  
  
  
  
暗网市场出现针对WinRAR 的复杂  
0day  
漏洞，以“zeroplayer”为假名的黑客成员以 80,000 美元的价格提供独家远程代码执行 (RCE)漏洞，这代表着地下漏洞利用市场显著升级。  
  
### RCE漏洞技术分析  
###   
  
根据 ThreatMon 的报告，该  
0day  
漏洞表明 WinRAR 的文件处理机制存在一个严重的安全漏洞，可能允许攻击者在目标系统上执行任意代码。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaF0OrLAXuWLVIZawcTXcTstMIWkfyA3CUHRVicFsRQ6VHxZzysooazeJoao2Rw6nh9yklrPuAo99iaw/640?wx_fmt=png&from=appmsg "")  
  
  
与之前披露的CVE-2025-6218漏洞不同，这个新发现的漏洞代表了一种独特的攻击媒介，会影响软件的当前版本和旧版本。  
  
  
远程代码执行使攻击者能够利用 WinRAR 解析引擎中的缓冲区溢出条件或内存损坏漏洞来完全控制受感染的系统。  
  
  
安全研究人员强调，RCE 漏洞非常危险，因为它们可以通过看似无辜的文件操作触发。  
  
  
当受害者试图提取或查看恶意存档文件时，漏洞可以利用与运行 WinRAR 的用户相同的权限执行有效载荷代码，从而可能导致系统受损、数据盗窃或恶意软件安装。  
  
  
80,000 美元的价格反映了该漏洞在网络犯罪生态系统中的价值，  
0day  
漏洞根据其目标软件的普遍性和发现的难度来标价。  
  
  
WinRAR 拥有广泛的用户群，估计全球安装量超过 5 亿，这使得这一漏洞对于寻求最大影响潜力的威胁组织特别有吸引力。  
  
  
由于目前尚无官方补丁，组织和个人用户面临着此未公开漏洞的直接风险。  
  
  
该漏洞与多个 WinRAR 版本的兼容性表明存在一个根本性的架构缺陷，可能需要进行大量代码重组才能正确解决。  
  
  
新闻链接：  
  
https://cyberpress.org/winrar-0-day-exploit/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
