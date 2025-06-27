> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzI5NTUzNzY3Ng==&mid=2247489137&idx=1&sn=e53ef16afa60551407e420378ec99419

#  漏洞预警|兄弟牌（Brother）打印机曝八个新漏洞  
 SecHub网络安全社区   2025-06-27 01:43  
  
****  
****  
****  
**点击蓝字 关注我们**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwuh8LP87lPQLxMwiceAsv3TurmE7zZOulOhMELnQ2OulwFIJkbmB3bRg/640?wx_fmt=png "")  
  
  
**免责声明**  
  
本文发布的工具和脚本，仅用作测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。  
  
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关内容。  
  
文中所涉及的技术、思路及工具等相关知识仅供安全为目的的学习使用，任何人不得将其应用于非法用途及盈利等目的，间接使用文章中的任何工具、思路及技术，我方对于由此引起的法律后果概不负责。  
## 🌟简介  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZqJEAQJgdFlIK4Re45FnKY8NHT6PE9BwhHSIUAvDbSKgRDwfznol5ZzhBItOBWuAOEfjfMRN5hMKg/640?wx_fmt=png&from=appmsg "")  
  
**数百款 Brother 和其他供应商的打印机被网络安全公司 Rapid7 的研究人员发现的可能严重的漏洞影响。**  
  
该网络安全公司在表示，其研究人员发现了影响 Brother 制造的多功能打印机的八个漏洞。  
  
这些安全漏洞已被发现影响 Brother 的 689 款打印机、扫描仪和标签打印机型号，其中一些或所有缺陷也影响了 46 款富士胶片商业创新（Fujifilm Business Innovation）的46款、理光（Ricoh）的5款、柯尼卡美能达（Konica Minolta）的6款及东芝（Toshiba）的2款打印机  
  
总体而言，数百万台企业和家用打印机被认为由于这些漏洞而暴露于黑客攻击之下。  
  
最严重的漏洞之一，CVE-2024-51978，被评为“严重”，允许远程未身份验证的攻击者通过获取设备的默认管理员密码来绕过身份验证。  
  
注意事项  
  
CVE-2024-51978 可以与一个信息泄露漏洞 CVE-2024-51977 链式利用，该漏洞可以被用来获取设备的序列号。这个序列号是生成默认管理员密码所必需的。  
  
“这是由于发现了 Brother 设备使用的默认密码生成程序，”Rapid7 解释道。“该程序将序列号转换为默认密码。受影响的设备在制造过程中根据每个设备的唯一序列号设置了默认密码。”  
  
拥有管理员密码使攻击者能够重新配置设备或滥用为认证用户设计的功能。  
  
其余漏洞的严重性评级为“中等”和“高”，可被用于 DoS 攻击，迫使打印机打开 TCP 连接，获取配置的外部服务密码，触发堆栈溢出，并执行任意 HTTP 请求。Rapid7 发现的八个漏洞中有六个无需身份验证即可利用。  
  
该网络安全公司通过日本的 JPCERT/CC 向 Brother 报告了其发现，大约一年前，供应商已发布公告通知客户这些漏洞。  
  
Brother 已修复了大部分漏洞，但表示 CVE-2024-51978 无法在固件中完全修复。新的制造工艺将确保未来设备不会存在漏洞。对于现有设备，提供了一种解决方案。  
  
JPCERT/CC及理光、富士胶片、东芝、柯尼卡美能达等厂商也同步发布了相关安全公告。  
  
  
  
欢迎关注SecHub网络安全社区，SecHub网络安全社区目前邀请式注册，邀请码获取见公众号菜单【邀请码】  
  
**#**  
  
  
**企业简介**  
  
  
**赛克艾威 - 网络安全解决方案提供商**  
  
****  
       北京赛克艾威科技有限公司（简称：赛克艾威），成立于2016年9月，提供全面的安全解决方案和专业的技术服务，帮助客户保护数字资产和网络环境的安全。  
  
  
安全评估|渗透测试|漏洞扫描|安全巡检  
  
代码审计|钓鱼演练|应急响应|安全运维  
  
重大时刻安保|企业安全培训  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwuh8LP87lPQLxMwiceAsv3TurmE7zZOulOhMELnQ2OulwFIJkbmB3bRg/640?wx_fmt=png "")  
  
  
**联系方式**  
  
电话｜010-86460828   
  
官网｜https://sechub.com.cn  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FW5uwU0BZtn2lmMrLPwpibCeCVbtBFDRkbFb7n7ibhPRxg20spUo9mUIiakmRYABB88Idl81IpGuXfw/640?wx_fmt=gif "")  
  
**关注我们**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SUZ43ICubr4mWJcUARDKYbQooQjbjbmqZTerAIXqDX9CaVxXbB7pyWwnMRklrCJias9r59PhnJAxZ4e3gYjyqVQ/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SUZ43ICubr4mWJcUARDKYbQooQjbjbmqZTerAIXqDX9CaVxXbB7pyWwnMRklrCJias9r59PhnJAxZ4e3gYjyqVQ/640?wx_fmt=png "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwyhlWCYDVqK38BA5dbjKkH7icWmAew7SYRA7ao1bFibialrMvmQ9ib0TBvw/640?wx_fmt=jpeg "")  
  
  
**公众号：**  
sechub安全  
  
**哔哩号：**  
SecHub官方账号  
  
  
  
