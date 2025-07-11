> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzg4NTg5MDQ0OA==&mid=2247488265&idx=1&sn=5d4f61665320ae84e621d43683817245

#  高危警报！mcp-remote漏洞可完全控制你的电脑，43万次下载受影响  
原创 道玄安全  道玄网安驿站   2025-07-11 01:00  
  
**“**  
   
一次点击，全线崩溃——  
**AI开发工具正成为黑客入侵的新捷径**  
。**”**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L369x9IF3yPA9bic9zzTydWv4XTTHH2NAiamMp8Kxsh4s2lukPuyuwnia3NiaHkiaU8a3JGFhLvNnYvtLvHTFAd91Rw/640?wx_fmt=png&from=appmsg "")  
  
      
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L369x9IF3yPMwVHx9iaPDKDhBJiajRW2DIdq0Wxe7JcpgKDia3zMfgicaaD6Auwn6Q3GGm2vI0eNh1Qic6OUhHMjE7g/640?wx_fmt=png&from=appmsg "")  
  
  
  
PS：有内网web自动化需求可以私信  
  
  
  
  
01  
  
—  
  
  
  
导语  
  
  
    当您启动熟悉的LLM客户端连接远程服务器时，可能从未想过这会让攻击者获得您电脑的  
**完全控制权**  
。昨日披露的CVE-2025-6514漏洞证实了这种风险的真实存在——这个存在于mcp-remote工具中的致命缺陷，已影响超过  
**43.7万次下载**  
，威胁着全球AI开发环境的安全。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L369x9IF3yMDf7emB78IqKD0So0bS9InFCzEXOszZMQmrgNWTked9OdyAHImjibJ1AsHvuepzR6icYzVkJRKV0Ow/640?wx_fmt=png&from=appmsg "")  
## 01 漏洞核心：当连接服务器变成致命陷阱  
  
    网络安全研究人员近日曝光了一个  
**关键级漏洞**  
（CVE-2025-6514），CVSS评分高达9.6分（满分10分），存在于mcp-remote项目中。  
  
    mcp-remote是什么？它是一款代理工具，专门用于帮助大型语言模型（LLM）客户端（如Claude Desktop）与远程Model Context Protocol（MCP）服务器进行通信。简单来说，它是连接AI应用和外部服务的“桥梁”。  
  
**该漏洞的可怕之处在于攻击场景的隐蔽性**  
：  
- 当用户配置LLM客户端连接至  
**恶意或被劫持的MCP服务器**  
时（尤其是通过不安全的HTTP连接），攻击者可注入精心构造的恶意载荷。  
  
- 在Windows系统上，攻击者能够通过  
**PowerShell子表达式评估机制**  
实现  
**完整的命令注入**  
，直接执行任意操作系统命令。  
  
- 攻击者甚至不需要直接控制服务器——通过  
**中间人攻击（MitM）**  
 劫持HTTP流量，也能将连接重定向至恶意节点。  
  
    受影响版本明确界定为   
**mcp-remote v0.0.5 至 v0.1.15**  
。如果你正在使用这些版本中的任何一个，你的系统已经暴露在风险之下。  
## 02 攻击机制解析：恶意URL如何变成系统后门  
  
    漏洞的触发点隐藏在OAuth授权流程中。当mcp-remote向远程服务器请求OAuth元数据时，攻击者可构造一个特殊的 authorization_endpoint 值进行利用。  
  
    例如，攻击者发送形如   

```
“a：$（cmd.exe /c whoami > c：\\temp\\pwned.txt）”
```

  
 的恶意端点地址。当mcp-remote解析此地址时，由于未正确处理输入验证，该字符串会被传递给PowerShell执行。  
  
**关键攻击步骤**  
：  
- 恶意服务器响应OAuth发现请求，返回包含  
**恶意命令的authorization_endpoint URL**  
。  
  
- **mcp-remote工具调用系统命令处理该URL**  
，触发PowerShell执行。  
  
- 攻击者命令在用户机器上运行，  
**权限等同于mcp-remote进程权限**  
，通常意味着完全控制系统。  
  
    此攻击在Windows系统上危害最大，可实现  
**带参数控制的任意命令执行**  
。在macOS和Linux上虽然参数控制受限，仍可执行任意程序。  
## 03 紧急修复方案：升级与配置双管齐下  
  
    面对如此严重的漏洞，  
**Anthropic和JFrog团队已协作推出修复版本**  
。用户应立即采取以下措施：  
- **升级至mcp-remote v0.1.16**  
：该版本已修复命令注入漏洞，是阻断攻击的根本手段。  
  
- **强制使用HTTPS连接**  
：避免任何HTTP连接，防止中间人攻击篡改通信路径。  
  
- **严格限制MCP服务器信任列表**  
：仅连接已知可信的服务器源，屏蔽未知或公开MCP服务节点。  
  
    安全团队还建议企业立即  
**审计现有MCP配置**  
，检查是否存在未加密连接或来源不明的服务器配置，并尽快移除。  
## 04 MCP生态安全警报：这只是冰山一角  
  
    令人担忧的是，CVE-2025-6514并非孤例。  
**MCP生态系统在短时间内暴露出多个严重漏洞**  
，形成一波针对AI工具链的攻击浪潮：  
- **MCP Inspector漏洞（CVE-2025-49596）**  
：CVSS 9.4分，允许攻击者通过诱使用户访问恶意网站，在开发者机器上实现  
**远程代码执行**  
。即便服务绑定在localhost，仍可利用浏览器的“0.0.0.0-day”缺陷发起攻击。  
  
- **GitHub MCP服务器漏洞**  
：攻击者通过  
**恶意议题注入隐藏指令**  
，诱骗AI代理泄露私有代码库数据，无需入侵系统本身。  
  
- **数据库泄露漏洞**  
：恶意用户提交伪装成正常请求的指令，当高权限代理（如service_role）处理时，会  
**绕过权限限制直接导出敏感数据**  
。  
  
    这些漏洞共同揭示了一个严峻现实：在AI开发工具快速普及的背景下，  
**安全设计未能跟上功能迭代的步伐**  
。许多工具默认配置缺乏认证、加密和权限隔离，成为攻击者眼中的“低垂果实”。  
## 05 未来防护：构建AI开发生命周期安全体系  
  
面对不断进化的攻击手法，单纯修补已不够。开发团队需重新审视整个AI工具链的安全架构：  
- **权限最小化**  
：避免MCP工具或关联进程（如数据库访问角色service_role）拥有过高权限，  
**强制执行只读模式**  
 处理外部数据。  
  
- **输入过滤机制**  
：在MCP客户端或代理层部署  
**对抗提示注入（Prompt Injection）的过滤模块**  
，识别并清除可疑指令。  
  
- **纵深防御**  
：包括实施服务认证（如MCP Inspector v0.14.1引入的会话令牌机制）、请求来源校验（防御CSRF）、以及网络隔离策略。  
  
    正如JFrog漏洞研究团队负责人Or Peles所强调：“在管理环境内，远程MCP服务器是扩展AI能力的有效工具，但用户必须警惕——只应连接可信的MCP服务器并使用HTTPS等安全连接方式。”  
  
    随着MCP协议在AI开发领域的普及，其安全性已关系到整个智能应用生态的根基。企业开发团队应立即检查自身使用的MCP相关组件版本，建立MCP服务器白名单制度，并推动HTTPS全面覆盖。  
**技术发展的速度，永远不该超越安全防御的底线**  
。  
  
<table><thead><tr style="box-sizing: border-box;break-inside: avoid;break-after: auto;border: 1px solid rgb(223, 226, 229);margin: 0px;padding: 0px;"><th style="box-sizing: border-box;padding: 6px 13px;font-weight: bold;border-width: 1px 1px 0px;border-top-style: solid;border-right-style: solid;border-left-style: solid;border-top-color: rgb(223, 226, 229);border-right-color: rgb(223, 226, 229);border-left-color: rgb(223, 226, 229);border-image: initial;border-bottom-style: initial;border-bottom-color: initial;margin: 0px;text-align: left;"><span cid="n68" mdtype="table_cell" style="box-sizing: border-box;display: inline-block;min-width: 1ch;width: 205.479px;min-height: 10px;"><span md-inline="strong" style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">关键行动项</span></span></strong></span></span></th><th style="box-sizing: border-box;padding: 6px 13px;font-weight: bold;border-width: 1px 1px 0px;border-top-style: solid;border-right-style: solid;border-left-style: solid;border-top-color: rgb(223, 226, 229);border-right-color: rgb(223, 226, 229);border-left-color: rgb(223, 226, 229);border-image: initial;border-bottom-style: initial;border-bottom-color: initial;margin: 0px;text-align: left;"><span cid="n69" mdtype="table_cell" style="box-sizing: border-box;display: inline-block;min-width: 1ch;width: 703.521px;min-height: 10px;"><span md-inline="strong" style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">执行说明</span></span></strong></span></span></th></tr></thead><tbody><tr style="box-sizing: border-box;break-inside: avoid;break-after: auto;border: 1px solid rgb(223, 226, 229);margin: 0px;padding: 0px;"><td style="box-sizing: border-box;padding: 6px 13px;border: 1px solid rgb(223, 226, 229);margin: 0px;min-width: 32px;text-align: left;"><span cid="n71" mdtype="table_cell" style="box-sizing: border-box;display: inline-block;min-width: 1ch;width: 205.479px;min-height: 10px;"><span md-inline="strong" style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">升级mcp-remote</span></span></strong></span></span></td><td style="box-sizing: border-box;padding: 6px 13px;border: 1px solid rgb(223, 226, 229);margin: 0px;min-width: 32px;text-align: left;"><span cid="n72" mdtype="table_cell" style="box-sizing: border-box;display: inline-block;min-width: 1ch;width: 703.521px;min-height: 10px;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">立即升级至v0.1.16或更高版本</span></span></span></td></tr><tr style="box-sizing: border-box;break-inside: avoid;break-after: auto;border: 1px solid rgb(223, 226, 229);margin: 0px;padding: 0px;background-color: rgb(248, 248, 248);"><td style="box-sizing: border-box;padding: 6px 13px;border: 1px solid rgb(223, 226, 229);margin: 0px;min-width: 32px;text-align: left;"><span cid="n74" mdtype="table_cell" style="box-sizing: border-box;display: inline-block;min-width: 1ch;width: 205.479px;min-height: 10px;"><span md-inline="strong" style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">禁用HTTP连接</span></span></strong></span></span></td><td style="box-sizing: border-box;padding: 6px 13px;border: 1px solid rgb(223, 226, 229);margin: 0px;min-width: 32px;text-align: left;"><span cid="n75" mdtype="table_cell" style="box-sizing: border-box;display: inline-block;min-width: 1ch;width: 703.521px;min-height: 10px;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">仅允许HTTPS连接至MCP服务器，防止中间人攻击</span></span></span></td></tr><tr style="box-sizing: border-box;break-inside: avoid;break-after: auto;border: 1px solid rgb(223, 226, 229);margin: 0px;padding: 0px;"><td style="box-sizing: border-box;padding: 6px 13px;border: 1px solid rgb(223, 226, 229);margin: 0px;min-width: 32px;text-align: left;"><span cid="n77" mdtype="table_cell" style="box-sizing: border-box;display: inline-block;min-width: 1ch;width: 205.479px;min-height: 10px;"><span md-inline="strong" style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">审计服务器信任源</span></span></strong></span></span></td><td style="box-sizing: border-box;padding: 6px 13px;border: 1px solid rgb(223, 226, 229);margin: 0px;min-width: 32px;text-align: left;"><span cid="n78" mdtype="table_cell" style="box-sizing: border-box;display: inline-block;min-width: 1ch;width: 703.521px;min-height: 10px;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">移除配置中任何未知或公开MCP服务器，仅保留可验证的信任节点</span></span></span></td></tr><tr style="box-sizing: border-box;break-inside: avoid;break-after: auto;border: 1px solid rgb(223, 226, 229);margin: 0px;padding: 0px;background-color: rgb(248, 248, 248);"><td style="box-sizing: border-box;padding: 6px 13px;border: 1px solid rgb(223, 226, 229);margin: 0px;min-width: 32px;text-align: left;"><span cid="n80" mdtype="table_cell" style="box-sizing: border-box;display: inline-block;min-width: 1ch;width: 205.479px;min-height: 10px;"><span md-inline="strong" style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">检查关联组件</span></span></strong></span></span></td><td style="box-sizing: border-box;padding: 6px 13px;border: 1px solid rgb(223, 226, 229);margin: 0px;min-width: 32px;text-align: left;"><span cid="n81" mdtype="table_cell" style="box-sizing: border-box;display: inline-block;min-width: 1ch;width: 703.521px;min-height: 10px;"><span md-inline="plain" style="box-sizing: border-box;"><span leaf="">同时排查MCP Inspector等工具，升级至安全版本（如v0.14.1）</span></span></span></td></tr></tbody></table>  
免责声明：  
### 本人所有文章均为技术分享，均用于防御为目的的记录，所有操作均在实验环境下进行，请勿用于其他用途，否则后果自负。  
  
第二十七条：任何个人和组织不得从事非法侵入他人网络、干扰他人网络正常功能、窃取网络数据等危害网络安全的活动；不得提供专门用于从事侵入网络、干扰网络正常功能及防护措施、窃取网络数据等危害网络安全活动的程序和工具；明知他人从事危害网络安全的活动，不得为其提供技术支持、广告推广、支付结算等帮助  
  
第十二条：  国家保护公民、法人和其他组织依法使用网络的权利，促进网络接入普及，提升网络服务水平，为社会提供安全、便利的网络服务，保障网络信息依法有序自由流动。  
  
任何个人和组织使用网络应当遵守宪法法律，遵守公共秩序，尊重社会公德，不得危害网络安全，不得利用网络从事危害国家安全、荣誉和利益，煽动颠覆国家政权、推翻社会主义制度，煽动分裂国家、破坏国家统一，宣扬恐怖主义、极端主义，宣扬民族仇恨、民族歧视，传播暴力、淫秽色情信息，编造、传播虚假信息扰乱经济秩序和社会秩序，以及侵害他人名誉、隐私、知识产权和其他合法权益等活动。  
  
第十三条：  国家支持研究开发有利于未成年人健康成长的网络产品和服务，依法惩治利用网络从事危害未成年人身心健康的活动，为未成年人提供安全、健康的网络环境。  
  
  
  
  
  
