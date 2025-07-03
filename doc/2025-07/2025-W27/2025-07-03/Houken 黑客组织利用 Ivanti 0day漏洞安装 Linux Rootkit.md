> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzI2NzAwOTg4NQ==&mid=2649795612&idx=1&sn=bd2ec5afa78de18935e0be3b142b5f54

#  Houken 黑客组织利用 Ivanti 0day漏洞安装 Linux Rootkit  
会杀毒的单反狗  军哥网络安全读报   2025-07-03 01:01  
  
**导****读**  
  
  
  
法国国家信息系统安全局 (ANSSI) 披露一个名为“Houken”的威胁组织策划的一次复杂的网络攻击活动。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaGickubYlK8ErsXLiaUH79OYmz38jfXJS9O7ulGAabvF78IibVDD7noepmyQt4KpuEbO7OzZK7qqFVibw/640?wx_fmt=png&from=appmsg "")  
  
  
该组织涉嫌与 UNC5174 有关，利用 Ivanti 云服务设备 (CSA) 中的多个  
0day  
漏洞，未经授权访问法国政府、电信、媒体、金融和运输领域的网络。  
  
  
此次攻击始于 2024 年 9 月初，持续至 2024 年 11 月，利用了已识别为 CVE-2024-8190、CVE-2024-8963 和 CVE-2024-9380 的漏洞，可在易受攻击的系统上执行远程代码。  
  
  
这次攻击活动的特别之处在于部署了前所未见的Linux rootkit，展示了威胁组织先进的技术实力。  
  
  
ANSSI 的详细调查显示，Houken 是一个中等复杂的入侵装置，很可能作为初始访问代理运行。  
  
  
攻击者精心链接  
0  
day  
漏洞以渗透 Ivanti CSA 设备，执行 base64 编码的 Python 脚本来获取凭据并部署 PHP webshel  
  
l 以实现持久性。  
  
  
在法国国防部门发生的一起令人震惊的事件中，Houken 操作员安装了一个由内核模块（sysinitd.ko）和用户空间二进制文件（sysinitd）组成的 rootkit，旨在劫持 TCP 流量并以 root 权限执行远程命令。  
  
  
该 rootkit 的部署表了一种高价值目标策略，确保能够长期访问受感染的系统。  
  
### 0day漏洞的战略性使用  
###   
  
除了先进的恶意软件之外，攻击者还利用了一系列开源工具，和多样化的攻击基础设施。该基础设施包括 NordVPN 和 ExpressVPN 等商业 VPN、HostHatch 等提供商的专用服务器，合法  
  
ISP 的住宅 IP 地址。  
  
  
根据报告，ANSSI 的调查结果表明 Houken 的行动背后有双重动机。首先，该组织似乎专注于获取有价值的初始访问权，并可能将其转售给其他机构。  
  
  
部分数据泄露活动，则以经济利益为目标。例如 2025 年 3 月南美敏感机构发生的大规模电子邮件泄露事件以及在法国系统上部署门罗币挖矿木马。  
  
  
谷歌威胁情报小组此前记录了 UNC5174 的关联，该关联针对边缘设备并将访问权限转移到其他威胁组织，这强化了 Houken 是更广泛的网络间谍生态系统中间人的假设。  
  
  
技术报告：  
  
https://www.cert.ssi.gouv.fr/uploads/CERTFR-2025-CTI-009.pdf  
  
  
新闻链接：  
  
https://gbhackers.com/chinese-houken-group-exploits-ivanti-csa-zero-days/  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg "")  
  
**今日安全资讯速递**  
  
  
  
**APT事件**  
  
  
Advanced Persistent Threat  
  
国际刑事法院遭遇复杂网络攻击  
  
https://securityaffairs.com/179532/hacking/a-sophisticated-cyberattack-hit-the-international-criminal-court.html  
  
  
Kimsuky黑客利用ClickFix技术在受害机器上执行恶意脚本  
  
https://cybersecuritynews.com/kimsuky-hackers-using-clickfix-technique/  
  
  
Houken 黑客组织利用 Ivanti CSA   
0day  
漏洞安装 Linux Rootkit  
  
https://gbhackers.com/chinese-houken-group-exploits-ivanti-csa-zero-days/  
  
  
曹县黑客利用 macOS 恶意软件  
  
NimDoor  
  
攻击 Web3  
  
相关目标  
  
https://thehackernews.com/2025/07/north-korean-hackers-target-web3-with.html  
  
  
俄罗斯 APT28 组织利用 Signal 攻击乌克兰  
  
https://www.cysecurity.news/2025/07/russian-apt28-targets-ukraine-using.html  
  
  
TA829 黑客利用新的 TTP 和增强型 RomCom 后门来逃避检测  
  
https://gbhackers.com/ta829-hackers-use-new-ttps-and-enhanced-romcom-backdoor/  
  
  
美国捣毁29家笔记本电脑农场，打击朝鲜IT工人计划  
  
https://www.securityweek.com/us-storms-29-laptop-farms-in-crackdown-on-north-korean-it-worker-schemes/  
  
  
伊朗与以色列冲突期间，黑客组织对 20 多个关键部门发动攻击  
  
https://gbhackers.com/hacktivist-group-launches-attacks-on-20-critical-sectors/  
  
  
  
**一般威胁事件**  
  
  
General Threat Incidents  
  
夏威夷航空公司遭黑客攻击，航空业警告称可能存在Scattered Spider袭击  
  
https://www.securityweek.com/hawaiian-airlines-hacked-as-aviation-sector-warned-of-scattered-spider-attacks/  
  
  
澳航遭受网络攻击，大量客户数据被盗  
  
https://therecord.media/qantas-airline-data-breach  
  
  
数十款假钱包插件涌入 Firefox 商店，盗取加密货币  
  
https://www.bleepingcomputer.com/news/security/dozens-of-fake-wallet-add-ons-flood-firefox-store-to-drain-crypto/  
  
  
Ahold Delhaize 报告重大数据泄露事件，影响美国超过 200 万员工  
  
https://www.cysecurity.news/2025/07/ahold-delhaize-reports-major-data.html  
  
  
黑客利用恶意 PDF 冒充 Microsoft、DocuSign 和 Dropbox 进行有针对性的网络钓鱼攻击  
  
https://gbhackers.com/cybercriminals-use-malicious-pdfs/  
  
  
黑客瞄准 Linux SSH 服务器部署 TinyProxy 和 Sing-Box 代理工具  
  
https://gbhackers.com/hackers-target-linux-ssh-servers/  
  
  
DCRat 针对 Windows 系统进行远程控制、键盘记录、屏幕捕获和数据窃取  
  
https://gbhackers.com/dcrat-targets-windows-systems/  
  
  
TA829 黑客采用新的 TTP 和升级的 RomCom 后门来逃避检测  
  
https://cybersecuritynews.com/ta829-hackers-employs-new-ttps/  
  
  
Snake 键盘记录器利用 Java 实用程序逃避安全工具的检测  
  
https://gbhackers.com/snake-keyloggers-exploit-java-utilities/  
  
  
**漏洞事件**  
  
  
Vulnerability Incidents  
  
CISA 警告两个 TeleMessage 漏洞可能被利用  
  
https://www.securityweek.com/cisa-warns-of-two-exploited-telemessage-vulnerabilities/  
  
  
Forminator WordPress 插件中存在一个漏洞，允许攻击者删除任意文件并接管网站  
  
https://www.securityweek.com/forminator-wordpress-plugin-vulnerability-exposes-400000-websites-to-takeover/  
  
  
德国工业巨头Microsens 产品中存在严重身份验证绕过和远程代码执行漏洞  
  
https://www.securityweek.com/critical-microsens-product-flaws-allow-hackers-to-go-from-zero-to-hero/  
  
  
数千个 Citrix NetScaler 实例未修复被利用的漏洞  
  
https://www.securityweek.com/thousands-of-citrix-netscaler-instances-unpatched-against-exploited-vulnerabilities/  
  
  
Windows 上的 Nessus 漏洞可导致任意系统文件覆盖  
  
https://gbhackers.com/nessus-vulnerabilities-on-windows/  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
