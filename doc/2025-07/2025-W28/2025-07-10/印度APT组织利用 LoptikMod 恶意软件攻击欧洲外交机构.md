> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzI2NzAwOTg4NQ==&mid=2649795670&idx=1&sn=d1d46021394a749b9db07a6b38594be5

#  印度APT组织利用 LoptikMod 恶意软件攻击欧洲外交机构  
会杀毒的单反狗  军哥网络安全读报   2025-07-10 01:01  
  
**导****读**  
  
  
  
据观察，一个与印度有关联的  
APT  
组织针对欧洲外交机构发起攻击，其恶意软件能够从受感染的主机中收集敏感数据。  
  
  
Trellix 高级研究中心已将该活动归咎于一个名为DoNot Team的高级持续性威胁 (APT) 组织，该组织又名APT-C-35、Mint Tempest、Origami Elephant、SECTOR02 和 Viceroy Tiger。据评估，该组织自 2016 年以来一直活跃。  
  
  
Trellix 研究人员 Aniket Choukde、Aparna Aripirala、Alisha Kadam、Akhil Reddy、Pham Duy Phuc 和 Alex Lanstein 表示：“DoNot APT 以使用定制的 Windows 恶意软件而闻名，包括 YTY 和 GEdit 等后门，通常通过鱼叉式网络钓鱼电子邮件或恶意文档传递。 ”  
  
  
“该威胁组织通常以政府实体、外交机构、国防单位和非政府组织为目标，重点是南亚和欧洲目标。”  
  
  
攻击链始于网络钓鱼电子邮件，旨在诱骗收件人点击 Google Drive 链接以触发下载 RAR 存档，然后为部署名为 LoptikMod 的恶意软件铺平道路，该恶意软件早在 2018 年就被该组织独家使用。  
  
  
据 Trellix 称，这些邮件来自 Gmail 地址，冒充国防官员，主题提到了意大利国防武官访问孟加拉国达卡的情况。  
  
  
Trellix 在对感染序列进行解构时指出：“该电子邮件使用了带有 UTF-8 编码的 HTML 格式，以正确显示‘Attaché’中的‘é’等特殊字符，这表明它注重细节以增加合法性。”  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaFJgxeo5hvrUX9OYPBYtpupPLKic480oXS3CPibkqZib88wdmjysLquopGDefDMtt8iaegmWKrjibP4uTw/640?wx_fmt=png&from=appmsg "")  
  
  
通过电子邮件分发的 RAR 存档包含一个模仿 PDF 文档的恶意可执行文件，打开后会导致执行 LoptikMod 远程访问木马，该木马可以通过计划任务在主机上建立持久性并连接到远程服务器以发送系统信息、接收进一步的命令、下载其他模块并窃取数据。  
  
  
它还采用了反虚拟机技术和 ASCII 混淆技术，以阻碍其在虚拟环境中的执行并逃避分析，从而使确定该工具的用途变得更加困难。此外，该攻击还会确保受感染系统上只有一个恶意软件实例在运行，以避免潜在的干扰。  
  
  
Trellix 表示，此次活动中使用的命令和控制 (C2) 服务器目前处于非活动状态，这意味着基础设施已被暂时禁用或不再运行，或者攻击者已转移到完全不同的服务器。  
  
  
C2 服务器的非活动状态还意味着目前无法确定传输到受感染端点的确切命令集以及作为响应发回的数据类型。  
  
  
研究人员表示：“他们的行动以持续监视、数据泄露和长期访问为特征，表明其具有强烈的网络间谍动机。虽然他们以往主要关注南亚，但此次针对南亚驻欧洲大使馆的事件，明显表明他们的兴趣已扩展到欧洲的外交通讯和情报领域。”  
  
  
技术报告：  
  
https://www.trellix.com/blogs/research/from-click-to-compromise-unveiling-the-sophisticated-attack-of-donot-apt-group-on-southern-european-government-entities/  
  
  
新闻链接：  
  
https://thehackernews.com/2025/07/donot-apt-expands-operations-targets.html  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg "")  
  
**今日安全资讯速递**  
  
  
  
**APT事件**  
  
  
Advanced Persistent Threat  
  
印度APT组织利用 LoptikMod 恶意软件攻击欧洲外交机构  
  
https://thehackernews.com/2025/07/donot-apt-expands-operations-targets.html  
  
  
黑客攻击针对俄罗斯民转军无人机改装生产系统  
  
https://therecord.media/cyberattack-russia-firmware-blow-hackers  
  
  
朝鲜黑客在 macOS 上部署罕见的基于 Nim 的恶意软件  
  
https://www.techrepublic.com/article/news-north-korea-nimdoor-macos-crypto-attack/  
  
  
APT36  
（透明部落）针对印度广泛采用的 BOSS Linux发行版  
  
https://gbhackers.com/how-apt36-targets-boss-linux/  
  
  
恶意 Firefox 扩展程序使用户面临凭证盗窃和监视的风险  
  
https://gbhackers.com/eight-malicious-firefox-extensions-expose-users/  
  
  
与伊朗结盟的黑客组织瞄准中东政府机构  
  
https://www.infosecurity-magazine.com/news/iran-hacking-group-targets-middle/  
  
  
新型 Batavia 间谍软件瞄准俄罗斯工业企业  
  
https://securityaffairs.com/179699/uncategorized/new-batavia-spyware-targets-russian-industrial-enterprises.html  
  
  
  
**一般威胁事件**  
  
  
General Threat Incidents  
  
黑客利用合法 Shellter 渗透测试工具传播 Lumma Stealer 和 SectopRAT 恶意软件  
  
https://thehackernews.com/2025/07/hackers-use-leaked-shellter-tool.html  
  
  
Anatsa Android 银行木马利用 Google Play 上的虚假 PDF 应用感染 9 万用户  
  
https://thehackernews.com/2025/07/anatsa-android-banking-trojan-hits.html  
  
  
黑客利用  
SEO  
投毒传播PuTTY和WinSCP木马版本，攻击针对IT专业人士  
  
https://gbhackers.com/hackers-manipulate-search-results-to-target-it-pros/  
  
  
恶意  
 Pull   
请求通过易受攻击的  
 Ethcode VS Code   
扩展程序攻击  
 6,000   
多名开发人员  
  
https://thehackernews.com/2025/07/malicious-pull-request-infects-6000.html  
  
  
新日铁子公司将数据泄露归咎于  
0  
day  
攻击  
  
https://www.securityweek.com/nippon-steel-subsidiary-blames-data-breach-on-zero-day-attack/  
  
  
加拿大电力公司称电表数据通信系统遭网络攻击  
  
https://www.securityweek.com/canadian-electric-utility-says-power-meters-disrupted-by-cyberattack/  
  
  
SparkKitty 恶意软件窃取 iOS 和 Android 设备照片  
  
https://gbhackers.com/sparkkitty-malware-steals-photos/  
  
  
黑客利用 Shellter 红队工具传播信息窃取程序  
  
https://securityaffairs.com/179745/malware/hackers-weaponize-shellter-red-teaming-tool-to-spread-infostealers.html  
  
  
Firefox 附加组件商店发现 40 多个恶意加密钱包扩展程序  
  
https://www.cysecurity.news/2025/07/over-40-malicious-crypto-wallet.html  
  
  
新的 Android TapTrap 攻击可使恶意应用绕过权限管理并执行破坏性操作  
  
https://cybersecuritynews.com/android-taptrap-attack/  
  
  
18  
个恶意扩展程序感染 230 万 Chrome、Edge 用户  
  
https://www.theregister.com/2025/07/08/browser_hijacking_campaign/  
  
  
**漏洞事件**  
  
  
Vulnerability Incidents  
  
AMD 警告称新的 Meltdown、Spectre 漏洞可能会影响 CPU  
  
https://www.theregister.com/2025/07/09/amd_tsa_side_channel/  
  
  
Apache Tomcat 多个漏洞可导致攻击者触发 DoS 攻击  
  
https://cybersecuritynews.com/apache-tomcat-dos-vulnerabilities/  
  
  
FortiWeb SQL注入漏洞允许攻击者执行恶意SQL命令  
  
https://gbhackers.com/fortiweb-sql-injection-vulnerability/  
  
  
未修补的 Ruckus 漏洞允许黑客入侵无线网络环境  
  
https://www.securityweek.com/unpatched-ruckus-vulnerabilities-allow-wireless-environment-hacking/  
  
  
Adobe 修补关键代码执行漏洞  
  
https://www.securityweek.com/adobe-patches-critical-code-execution-bugs/  
  
  
Ivanti、Fortinet、Splunk 发布安全更新  
  
https://www.securityweek.com/ivanti-fortinet-splunk-release-security-updates/  
  
  
西门子、施耐德、菲尼克斯电气修复工业控制系统漏洞  
  
https://www.securityweek.com/ics-patch-tuesday-vulnerabilities-addressed-by-siemens-schneider-phoenix-contact-2/  
  
  
Citrix 漏洞（CVE-2025-6759）使攻击者获得 SYSTEM 权限  
  
https://cybersecuritynews.com/citrix-windows-virtual-delivery-agent-vulnerability/  
  
  
微软修复 Windows 和服务器中可蠕虫的远程代码执行漏洞  
  
https://gbhackers.com/microsoft-fixes-wormable-remote-code-execution-flaw/  
  
  
微软 2025 年 7 月补丁日修复 130 个漏洞，其中包括 SQL Server 中的  
0day  
漏洞  
  
https://www.securityweek.com/microsoft-patches-130-vulnerabilities-for-july-2025-patch-tuesday/  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
