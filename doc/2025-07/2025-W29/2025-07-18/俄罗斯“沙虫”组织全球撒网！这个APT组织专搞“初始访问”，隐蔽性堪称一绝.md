> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzg3OTYxODQxNg==&mid=2247486447&idx=1&sn=1664fe8cf725ec27c3bcd2ed4b288d3b

#  俄罗斯“沙虫”组织全球撒网！这个APT组织专搞“初始访问”，隐蔽性堪称一绝  
原创 紫队  紫队安全研究   2025-07-18 03:59  
  
**大家好，我是紫队安全研究。建议大家把公众号“紫队安全研究”设为星标，否则可能就无法及时看到啦！因为公众号只对常读和星标的公众号才能大图推送。操作方法：先点击上面的“紫队安全研究”，然后点击右上角的【...】,然后点击【设为星标】即可。**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8TI2yicY7vMSLvoLUAox2nDd5yD373OGPZnzwvOrt798VOA9fIhSOdFdHmAeiaKpIwOzGSOODUa0JrQ/640?wx_fmt=png&from=appmsg "")  
  
俄罗斯顶级APT组织“沙虫”（Sandworm，又名Seashell Blizzard）的一个神秘分支，正在全球范围内悄悄布网。微软最新报告披露，这个专注于“初始访问与持久化”的子组，从2022年聚焦乌克兰，到2023年全球化扩张，再到2024年锁定美加澳英等国，其攻击范围横跨能源、军工、电信等关键行业，手法隐蔽到能绕过多数网络审计。    
  
一、从乌克兰到全球：攻击范围三年三级跳    
  
  
这个子组的“扩张路线图”清晰得令人心惊：    
  
2022年：主攻乌克兰，精准打击能源、零售、教育等民生领域，为俄乌冲突的“网络战场”铺路；    
  
2023年：全球化提速，在美国、欧洲、中亚、中东的数十个行业埋下“后门”，实现长期驻留；    
  
2024年：虽因漏洞曝光获取了更多访问权限，却开始“精准聚焦”，重点渗透美、加、澳、英的核心机构。    
  
  
微软研究员指出：“他们就像网络世界的‘先遣队’，不为即时破坏，只为给后续攻击预留‘隐形通道’。”    
  
  
  
二、技术拆解：漏洞+合法工具+Tor隐藏服务，三位一体的隐蔽术    
  
  
这个子组的攻击链堪称“教科书级”，每一步都在规避 detection：    
  
  
1. 漏洞利用：8大漏洞撕开防线    
  
从邮件服务器到远程控制软件，他们盯着全球网络的“软肋”下手：    
  
Exchange（CVE-2021-34473）、Zimbra（CVE-2022-41352）：通过邮件系统漏洞植入后门；    
  
Fortinet FortiClient（CVE-2023-48788）、Connectwise（CVE-2024-1709）：利用远程工具漏洞横向移动；    
  
甚至还有JBoss的未知零日漏洞，专门针对企业级应用平台。    
  
  
2. 持久化手段：从Webshell到“合法工具滥用”    
  
早期：用自定义Webshell（如LocalOlive）控制服务器，支持文件上传与命令执行；    
  
2024年升级：滥用Atera、Splashtop等正规远程监控（RMM）工具——这些工具本用于IT运维，却被黑客用来偷偷窃取凭证、部署二次攻击工具。    
  
  
3. ShadowLink：用Tor隐藏服务打造“永不关闭的后门”    
  
这是最令人头疼的技术：    
  
被攻陷的系统会注册为Tor隐藏服务，生成唯一的`.onion`地址，通过Tor网络远程访问；    
  
无需传统C2服务器，所有通信都像“隐形隧道”，网络管理员查日志都找不到异常——因为Tor的加密特性让 inbound 连接完全隐蔽。    
  
  
4. 凭证盗窃：修改登录页+DNS劫持    
  
篡改Outlook网页版（OWA）登录界面，植入恶意JavaScript，实时捕获账号密码；    
  
修改DNS配置，可能拦截关键服务的认证信息，为横向渗透铺路。    
  
  
  
三、“广撒网+精准打击”：攻击策略藏着俄罗斯的野心    
  
  
这个子组的战术透着明显的“战略意图”：    
  
“广撒网”：甚至会攻击与俄罗斯战略利益无关的组织，用微软的话说，“就像撒网捕鱼，捕到普通鱼就放着，捕到大鱼才收网”；    
  
“精准打击”：一旦攻陷能源、油气、军火制造、电信等关键行业，就会展开深度渗透，为后续行动（如数据窃取、破坏性攻击）做准备。    
  
  
目标清单里，既有乌克兰的电力公司，也有北美的军工企业，甚至中东的航运巨头——这些都是俄罗斯地缘博弈中“感兴趣的经济领域”。    
  
![](https://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8TI2yicY7vMSLvoLUAox2nDdBgyRMJP4yxs2tuJRInYLiaE2VwWFQKicbia5XnIUm9JlO7ntgDxldic4gw/640?wx_fmt=png&from=appmsg "")  
  
  
  
四、防御指南：如何堵住“沙虫”的入口？    
  
  
面对这个“全球猎手”，企业和机构必须升级防御：    
  
1. 漏洞清零：48小时内修复上述CVE漏洞，尤其Exchange、Fortinet等高频被利用的系统；    
  
2. 监控RMM工具：限制Atera、Splashtop的使用权限，审计异常操作（如深夜远程控制、批量文件传输）；    
  
3. 警惕Tor连接：部署网络监控，发现内部设备连接`.onion`地址立即隔离；    
  
4. 强化凭证保护：启用多因素认证（MFA），定期检查OWA登录页源码，防止被植入恶意脚本。    
  
  
  
结语：网络空间的“隐形驻军”    
  
  
这个子组的存在，印证了“沙虫”组织的全球化野心——它不仅是俄罗斯在乌克兰的“网络尖刀”，更在为全球范围内的战略目标“预埋伏笔”。正如微软所说：“他们的每一次渗透，都是在为未来的网络行动搭建舞台。”    
  
****  
****  
**加入知识星球，可继续阅读**  
  
**一、"全球高级持续威胁：网络世界的隐形战争"，总共26章，为你带来体系化认识APT，欢迎感兴趣的朋友****入圈交流。**  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/sUKKZDdVP8RRAic0GwkHmSw2QZes8kK1AfysU8oPBib56yJpTWxmMuHRQBk3DHtibEASDuO7FTia8jIpeYtMFicBy5A/640?wx_fmt=jpeg "")  
![](https://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8Sm53HIUuI9RNR5Vpk1TWmpt3dw7icrMOJchapl0qTHsxVnXHyicBmV2kNlgpt3WLGLgdBJKrWiaUGicw/640?wx_fmt=png&from=appmsg "")  
  
**二、"Deep****Seek：APT攻击模拟的新利器"，为你带来APT攻击的新思路。**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SmEmOb6eVreW81Qh8DCAQvT2jLpI7JoYFWHibP6wCCI2AicqKAgbc4GzoAafviavpdxGjBqGrs1nlibQ/640?wx_fmt=png&from=appmsg "")  
  
  
**喜欢文章的朋友动动发财手点赞、转发、赞赏，你的每一次认可，都是我继续前进的动力。**  
  
  
  
  
