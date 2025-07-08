> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247495212&idx=1&sn=00ae3354296be75c719f7c2bda855410

#  效率翻倍 | 集成化BurpSuite漏洞探测插件实战演示  
Tsojan  星落安全团队   2025-07-07 16:00  
  
现在只对常读和星标的公众号才展示大图推送，建议大家能把  
**星落安全团队**  
“  
**设为星标**  
”，  
否则可能就看不到了啦  
！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllkXnsUODwVWmlxAHuHu4dBuwIlu707ZfPdbNTYyibYzQHA0xn0p2hTbQAiba04SOnDiadxVExZ53nfog/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
**工具介绍**  
  
TsojanScan是  
一款集成的BurpSuite漏洞探测插件。  
本着市面上各大漏洞探测插件的功能比较单一，因此与  
TsojanSecTeam  
成员决定在已有框架的基础上修改并增加常用的漏洞探测POC，它会以最少的数据包请求来准确检测各漏洞存在与否，你只需要这一个足矣。  
  
功能介绍  
  
1、加载插件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCbJd3fiaYWxvwBeibb1UxVtWia7aPGHZwM0sLoT7uXAUibjVFlZYgYfX43Q/640?wx_fmt=png&from=appmsg "")  
#### 2、功能介绍  
#### 1. 面板  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCl3U69T7t5ibRicsEiaaiczbqOdpgyk91It752T13N6W0StQ7IMExJOGQ2Q/640?wx_fmt=jpeg "")  
  
自定义黑名单，插件不扫描黑名单的url列表，进行Reg匹配优先级第一。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaChZTh98ia9D9HrjuYh30z07qQx41El7ic4picAWYwSFQHlFibqeeIAHzP5w/640?wx_fmt=jpeg "")  
#### 2. 主动探测  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCWUk2uUMSS2fyamIjpSvtx1shn9SyiaByIP3XcZ5oKB8gtTo9Q6ibV6NA/640?wx_fmt=png&from=appmsg "")  
  
比如探测非根目录/，目录下面需要加/  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCKls7g5JUNxoxtJOVLXp0DhBZicjgKL19P5HNwOXViaypCVmCuhWI8NEA/640?wx_fmt=png&from=appmsg "")  
#### 3、fastjson >=1.2.80探测  
#### 1. 本地环境  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCkibLjfSAOliab0r00J5zsMA0BIYgZssHbjwicGKFxCnA2t60Nbos86VlA/640?wx_fmt=png&from=appmsg "")  
#### 2. 预查询DNSlog接口  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCjz73cqyafO3NiaIXFMKHTyBPcwFXNrtwnba0AX5vYtazOglMvfCNKSQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCaRrVQ8ib6zuCp2l6h2ID8COTx2c7bKeRvVNxNws3kFWYmWYpasPRJfQ/640?wx_fmt=png&from=appmsg "")  
#### 3. 扫描  
####   
#### 4. 判断准确版本  
  
1.2.80版本探测如果收到了两个dns请求，则证明使用了1.2.83版本，如果收到了一个 dns 请求，则证明使用了1.2.80版本。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCVhZfHC49UZWnWNn2C8G7M49wcDsQwdwvyDsu1VBahIdzgyVNjHxgkg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCCia6TxwvsVydgnf3Crhh2p0ib0aPhZ3Ddw6yQXBrvLuIqARUEM72aMUQ/640?wx_fmt=png&from=appmsg "")  
#### 4、DNSLog查询漏报  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCgAlXRrIhtygrTibicic6oHEMdcicJumePiaMiayFmtsFBUJIBaGLbbpKUwIA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCBrMYWYskTP02uhpvHpZjIl3eDNPaFCnwzSO9icRp879BQxSJxTowwkQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaChqNeHZZyeOCcTw9ribf6Lrw0ucnWwuCMQV1Q1z5hNOCTvr2N8sFVgzg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaCS8DtI5eBfqWLchwGTGdEibRr0lQ7yjao7eoB6UTibD2uMhVdqpULWN1Q/640?wx_fmt=png&from=appmsg "")  
  
注意⚠️  
：扫描结束后才会在BurpSuite的Target、Dashboard模块显示高危漏洞，进程扫描中无法进行同步，但可以在插件中查看（涉及到DoPassive方法问题）。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllKFBfOWicicqiavuwBd6fTXaC05CBnjVKDmLBBuib1ncfh7BHwc6cicibiaHBiazqkAFCbTP3fCswblTMEyw/640?wx_fmt=png&from=appmsg "")  
  
  
**相关地址**  
  
**关注微信公众号后台回复“入群”，即可进入星落安全交流群！**  
  
关注微信公众号后台回复“  
20250708  
**”，即可获取项目下载地址！**  
  
****  
  
  
**圈子介绍**  
  
博主介绍  
：  
  
  
目前工作在某安全公司攻防实验室，一线攻击队选手。自2022-2024年总计参加过30+次省/市级攻防演练，擅长工具开发、免杀、代码审计、信息收集、内网渗透等安全技术。  
  
  
目前已经更新的免杀内容：  
- 部分免杀项目源代码  
  
- 一键击溃360+核晶  
  
- 一键击溃windows defender  
  
- 一键击溃火绒进程  
  
-    
CobaltStrike4.9.1Linux星落专版   
  
-    
CobaltStrike免杀加载器  
  
- 数据库直连工具免杀版  
  
- aspx文件自动上线cobaltbrike  
  
- jsp文件  
自动上线cobaltbrike  
  
- 哥斯拉免杀工具   
XlByPassGodzilla  
  
- 冰蝎免杀工具 XlByPassBehinder  
  
- 冰蝎星落专版 xlbehinder  
  
- 正向代理工具 xleoreg  
  
- 反向代理工具xlfrc  
  
- 内网扫描工具 xlscan  
  
- CS免杀加载器 xlbpcs  
  
- Todesk/向日葵密码读取工具  
  
- 导出lsass内存工具 xlrls  
  
- 绕过WAF免杀工具 ByPassWAF  
  
- 等等...  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
目前星球已满600人，价格由208元  
调整为  
218元(  
交个朋友啦  
)，700名以后涨价至268元！  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/rlSBJ0flllmXEGfK9uB8VibWo8ZLL8nficA1BJXW90bric2w266yxOaAYQZAhXLsrFTqunYhbUDibVuicc465WzvFEA/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/MuoJjD4x9x3siaaGcOb598S56dSGAkNBwpF7IKjfj1vFmfagbF6iaiceKY4RGibdwBzJyeLS59NlowRF39EPwSCbeQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
     
往期推荐  
     
  
  
1.   
[学不会全额退款 | 星落免杀第一期，助你打造专属免杀武器库](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247494072&idx=1&sn=e46a6d176a8fad2aa4b4c055de3607da&scene=21#wechat_redirect)  
  
  
  
2.   
[【干货】你不得不学习的内网渗透手法](http://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489483&idx=1&sn=0cbeb449e56db1ae48abfb924ffd0b43&chksm=c0e2bc74f79535622f39166c8ed17d5fe5a2bbc3f622d20491033b6aa61d26d789e59bab5b79&scene=21#wechat_redirect)  
  
  
  
3.   
[【免杀】CobaltStrike4.9.1二开 | 自破解 免杀 修复BUG](http://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247488486&idx=1&sn=683083d38a58de4a95750673d9cb725d&chksm=c0e2b859f795314f3b7bc980a5d4114508ee2c286bc683cdfd25eefa4fb59f26adfe5483690b&scene=21#wechat_redirect)  
[！](http://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247486966&idx=1&sn=3f144d5936d5cdc11178004549384ace&chksm=c0e2a649f7952f5f7557dde6e9cca53ecee7b5e2f7ff23395250e8fe47acb102902d9727185d&scene=21#wechat_redirect)  
  
  
  
4.   
[【免杀】原来SQL注入也可以绕过杀软执行shellcode上CoblatStrike](http://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489950&idx=1&sn=a54e05e31a2970950ad47800606c80ff&chksm=c0e2b221f7953b37b5d7b1a8e259a440c1ee7127d535b2c24a5c6c2f2e773ac2a4df43a55696&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
  
【  
声明  
】本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统以及盈利等目的，一切后果由操作者自行承担！！！  
  
