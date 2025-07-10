> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkzNjIzMjM5Ng==&mid=2247492767&idx=1&sn=f859ddce15279eae9d072ed1a9357c2a

#  微软紧急修复高危蠕虫级RCE漏洞，威胁全网Windows系统  
 信息安全大事件   2025-07-10 10:00  
  
微软已发布关键安全更新，修复编号为CVE-2025-47981的高危漏洞。该漏洞存在于SPNEGO扩展协商(NEGOEX)安全机制中，属于基于堆的缓冲区溢出漏洞，影响多个Windows和Windows Server版本。  
  
该漏洞CVSS评分为9.8分(满分10分)，属于最高危级别，可在无需用户交互的情况下实现远程代码执行。  
  
核心要点  
- Windows SPNEGO中存在基于堆的缓冲区溢出漏洞，CVSS评分9.8/10，可实现远程代码执行  
  
- 攻击者无需用户交互或特权，仅需向服务器发送恶意消息即可执行代码  
  
- 影响Windows 10(1607及以上)、Windows 11及Windows Server等33种系统配置  
  
- 微软于2025年7月8日发布更新，建议优先部署在面向互联网的系统及域控制器上  
  
该漏洞允许未经授权的攻击者通过网络连接执行任意代码，对企业环境构成严重威胁。  
  
可蠕虫传播的RCE漏洞(CVE-2025-47981)  
  
该漏洞存在于Windows SPNEGO扩展协商机制中，该机制是对简单且受保护的GSS-API协商机制的扩展。  
  
CVE-2025-47981被归类为CWE-122，属于可远程利用的基于堆的缓冲区溢出漏洞。其CVSS向量字符串CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C表明，该漏洞可通过网络发起攻击，复杂度低，无需特权或用户交互，但对机密性、完整性和可用性影响极大。  
  
安全研究人员评估该漏洞"极有可能被利用"，不过截至披露时尚未发现公开利用代码或实际攻击案例。该漏洞尤其影响运行Windows 10版本1607及更高版本的客户端计算机，这些系统默认启用了组策略对象"网络安全：允许PKU2U身份验证请求使用在线身份"。  
  
攻击者可通过向受影响服务器发送恶意消息来利用CVE-2025-47981，可能获得远程代码执行能力。基于堆的缓冲区溢出发生在NEGOEX处理机制中，允许攻击者覆盖内存结构并控制程序执行流程。这种可蠕虫传播的特性意味着漏洞可能通过网络连接的系统自动传播，无需用户干预。  
  
该漏洞由安全研究人员通过协调披露机制发现，包括匿名贡献者和Yuki Chen。微软对这些研究人员的致谢体现了负责任漏洞披露对维护企业安全态势的重要性。  
  
风险因素  
<table><tbody><tr><td data-colwidth="202" style="border-color:#000000;"><section style="text-indent: 0px;margin-top: 8px;margin-bottom: 8px;line-height: 2em;text-align: center;"><span leaf="" style="font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;font-weight: bold;">风险因素</span></span></section></td><td data-colwidth="370" style="border-color:#000000;"><section style="text-indent: 0px;margin-top: 8px;margin-bottom: 8px;line-height: 2em;text-align: center;"><span leaf="" style="font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;font-weight: bold;">详情</span></span></section></td></tr><tr><td data-colwidth="202" style="border-color:#000000;"><section style="text-indent: 0px;margin: 0px;line-height: 1em;"><span leaf="" style="font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;">受影响产品</span></span></section></td><td data-colwidth="370" style="border-color:#000000;"><section style="text-indent: 0px;margin: 0px;line-height: 1.5em;"><span leaf="" style="text-indent: 0px;font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;">- Windows 10(1607及以上版本)- Windows 11(23H2、24H2版本)- Windows Server 2008 R2至Server 2025- 包括x64、x86和ARM64架构- 包含Server Core安装</span></span></section></td></tr><tr><td data-colwidth="202" style="border-color:#000000;"><section style="text-indent: 0px;margin: 0px;line-height: 1em;"><span leaf="" style="text-indent: 0px;line-height: 1em;font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;">影</span></span><span leaf="" style="font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;">响</span></span></section></td><td data-colwidth="370" style="border-color:#000000;"><section style="text-indent: 0px;margin: 0px;line-height: 1em;"><span leaf="" style="text-indent: 0px;line-height: 1em;font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;">远程代码执行</span></span></section></td></tr><tr><td data-colwidth="202" style="border-color:#000000;"><section style="text-indent: 0px;margin: 0px;line-height: 1em;"><span leaf="" style="text-indent: 0px;line-height: 1em;font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;">利用前提  </span></span></section></td><td data-colwidth="370" style="border-color:#000000;"><section><span leaf="" style="text-indent: 2em;line-height: 2em;font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;">无</span></span><span leaf="" style="text-indent: 0px;line-height: 1em;font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;">需特权，无需用户交互</span></span></section></td></tr><tr><td data-colwidth="202" style="border-color:#000000;"><section style="text-indent: 0px;margin: 0px;line-height: 1em;"><span leaf="" style="text-indent: 0px;line-height: 1em;font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;">CVSS 3.1评分   </span></span></section></td><td data-colwidth="370" style="border-color:#000000;"><section style="text-indent: 0px;margin: 0px;line-height: 1em;"><span leaf="" style="text-indent: 0px;line-height: 1em;font-family: 宋体;font-size: 10.5pt;"><span textstyle="" style="font-size: 17px;">9.8(严重)</span></span></section></td></tr></tbody></table>  
补丁部署  
  
微软于2025年7月8日发布了全面的安全更新，针对不同Windows配置修复了该漏洞。关键更新包括Windows Server 2025(版本10.0.26100.4652)、Windows 11 24H2版(版本10.0.26100.4652)、Windows Server 2022 23H2版(版本10.0.25398.1732)以及Windows Server 2008 R2(版本6.1.7601.27820)等旧系统的补丁。  
  
企业应优先为面向互联网的系统和域控制器部署这些安全更新。补丁可通过Windows Update、Microsoft更新目录和Windows Server更新服务(WSUS)获取。系统管理员应通过核对微软安全公告中的版本号来验证补丁是否成功安装，并考虑在部署补丁期间实施网络分段作为额外防御措施。  
  
  
<table><tbody><tr><td data-colwidth="576"><p style="text-indent: 0px;margin-top: 8px;margin-bottom: 8px;line-height: 2em;" data-pm-slice="4 4 []"><span style="font-family: 宋体;font-size: 10.5pt;"><font face="宋体"><span leaf=""><span textstyle="" style="font-size: 17px;">江苏国骏可为客户提供：</span></span></font></span></p><p data-pm-slice="0 0 []"><span style="mso-spacerun:&#39;yes&#39;;font-family:宋体;font-size:10.5000pt;mso-font-kerning:1.0000pt;"><font face="宋体"><span leaf=""><span textstyle="" style="font-size: 15px;">安全评估与咨询：快速扫描客户网络环境，精准识别所有受此漏洞影响的</span></span></font><font face="宋体"><span leaf=""><span textstyle="" style="font-size: 15px;">Windows 系统（特别是域控制器、Web服务器、文件服务器、VPN网关等面向互联网或关键的系统），并评估其暴露面和风险等级。</span></span></font></span><span style="mso-spacerun:&#39;yes&#39;;font-family:宋体;font-size:10.5000pt;mso-font-kerning:1.0000pt;"><o:p></o:p></span></p><p><span style="mso-spacerun:&#39;yes&#39;;font-family:宋体;font-size:10.5000pt;mso-font-kerning:1.0000pt;"><font face="宋体"><span leaf=""><span textstyle="" style="font-size: 15px;">安全网关</span></span></font><font face="宋体"><span leaf=""><span textstyle="" style="font-size: 15px;">(下一代防火墙、IPS/IDS)：实时检测并</span></span></font></span><span style="mso-spacerun:&#39;yes&#39;;font-family:宋体;font-size:10.5000pt;mso-font-kerning:1.0000pt;"><font face="宋体"><span leaf=""><span textstyle="" style="font-size: 15px;">拦截尝试利用漏洞的恶意网络流量</span></span></font></span></p><section><span style="color: rgba(0, 0, 0, 0.9);font-family: 宋体;font-size: 15px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 700;letter-spacing: 0.544px;orphans: 2;text-align: justify;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;background-color: rgb(255, 255, 255);text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;display: inline !important;float: none;" data-pm-slice="0 0 []"><span leaf="">如需进一步定制化方案，欢迎联系江苏国骏技术团队，联系电话：400-6776-989/13338963885</span></span></section></td></tr></tbody></table>  
  
  
  
