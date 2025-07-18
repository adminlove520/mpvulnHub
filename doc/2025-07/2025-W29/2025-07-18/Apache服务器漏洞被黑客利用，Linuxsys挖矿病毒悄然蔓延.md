> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkzMDQ0NzQwNA==&mid=2247487007&idx=1&sn=970c607c01da42be4e8fd7696b20cd75

#  Apache服务器漏洞被黑客利用，Linuxsys挖矿病毒悄然蔓延  
原创 ralap  网络个人修炼   2025-07-18 03:03  
  
网络安全研究人员发现了一个新的攻击活动，该活动利用 Apache HTTP 服务器存在的一个已知安全漏洞，分发一种名为  
 Linuxsys 的挖矿病毒。  
  
此次涉及的漏洞是   
CVE-2021-41773（CVSS 评分：7.5），这是 Apache HTTP Server 2.4.49 版本中存在的一个高严重性路径遍历漏洞，可能导致远程代码执行。  
  
VulnCheck 在给《黑客新闻》的一份报告中表示：“攻击者利用被入侵的合法网站分发恶意软件，实现了隐蔽交付并规避检测。”  
  
本月早些时候观察到的这一攻击序列源自印度尼西亚的一个 IP 地址   
103.193.177.152，其设计目的是通过 curl 或 wget 工具从   
repositorylinux.org下载下一阶段的有效载荷。  
  
该有效载荷是一个 shell 脚本，负责从 5 个不同的合法网站下载 Linuxsys 挖矿病毒，这表明该攻击活动背后的黑客已经成功入侵了第三方基础设施，以协助分发恶意软件。  
  
VulnCheck 指出：“这种方法很巧妙，因为受害者连接的是带有有效 SSL 证书的合法主机，这使得检测难度加大。此外，由于恶意软件本身并不托管在那里，这为下载器网站（  
repositorylinux.org）提供了一层隔离保护。”  
  
这些网站还托管了另一个名为   
cron.sh的 shell 脚本，该脚本确保矿工在系统重启时自动启动。这家网络安全公司表示，在被黑客攻击的网站上还发现了两个 Windows 可执行文件，这意味着攻击者可能也在针对微软的桌面操作系统。  
  
值得注意的是，此前分发 Linuxsys 病毒攻击曾利用过 OSGeo GeoServer GeoTools 中的一个严重安全漏洞（CVE-2024-36401，CVSS 评分：9.8），这一点已由 Fortinet FortiGuard 实验室在 2024 年 9 月记录在案。  
  
有趣的是，利用该漏洞后下载的 shell 脚本来自 “  
repositorylinux .com”，其源代码中的注释是用印尼语编写的。早在 2021 年 12 月，就已在实际环境检测到这个相同的 shell 脚本。  
  
近年来，用于分发该矿工的其他一些漏洞包括：  
  
CVE-2023-22527，Atlassian Confluence 数据中心和 Confluence 服务器中的模板注入漏洞  
  
CVE-2023-34960，Chamilo 学习管理系统（LMS）中的命令注入漏洞  
  
CVE-2023-38646，Metabase 中的命令注入漏洞  
  
CVE-2024-0012 和   
CVE-2024-9474，  
Palo Alto Networks  
防火墙中的身份验证绕过和权限提升漏洞  
  
VulnCheck 表示：“所有这些都表明，攻击者一直在进行长期的攻击活动，采用了一致的技术，如利用 n-day 漏洞、在被入侵的主机上存放内容以及在受害者机器上进行加密货币挖矿。”“他们的部分成功源于精准的目标定位。他们  
似乎会避开低交互蜜罐，且需要高交互才能观察到他们的活动。再加上利用被入侵的主机分发恶意软件，这种方法在很大程度上帮助攻击者避开了审查。”  
  
  
参考链接  
  
https://thehackernews.com/2025/07/hackers-exploit-apache-http-server-flaw.html  
  
  
相关阅读  
  
[CVE-2021-41773 漏洞复现：从失败到成功的探索](https://mp.weixin.qq.com/s?__biz=MzkzMDQ0NzQwNA==&mid=2247486827&idx=1&sn=a25724a950ba87c0352ab769c3f88bb2&scene=21#wechat_redirect)  
  
  
  
-End-  
  
  
  
**如果觉得我的分享有用**  
  
**[点赞+分享****+关注]**  
  
  
