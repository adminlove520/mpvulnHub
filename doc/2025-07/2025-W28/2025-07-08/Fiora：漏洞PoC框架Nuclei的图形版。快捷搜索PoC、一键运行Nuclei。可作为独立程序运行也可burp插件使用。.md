> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247494699&idx=1&sn=69f6bcf949f34426d14e3cb19a6128ed

#  Fiora：漏洞PoC框架Nuclei的图形版。快捷搜索PoC、一键运行Nuclei。可作为独立程序运行也可burp插件使用。  
bit4woo  夜组安全   2025-07-08 00:00  
  
免责声明  
  
由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
**所有工具安全性自测！！！VX：**  
**baobeiaini_ya**  
  
朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把  
**夜组安全**  
“**设为星标**  
”，  
否则可能就看不到了啦！  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg "")  
  
## 工具介绍  
  
Fiora是LoL中的无双剑姬的名字，她善于发现对手防守弱点，实现精准打击。该项目为PoC框架nuclei提供图形界面，实现快速搜索、一键运行等功能，提升nuclei的使用体验。  
## 安装运行  
### 一、作为burp插件运行  
  
1、访问https://github.com/bit4woo/Fiora/releases  
  
2、下载最新jar包  
  
3、如下方法安装插件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UoMfH0BInAJyGYB6oXJvzPTWV1xtRlTF1P6GPuowHvvPEwjKa33eLQwbWGficwq6OlkGlOzichOFYg/640?wx_fmt=png&from=appmsg "")  
### 二、作为独立程序运行  
  
该程序即可作为burp插件运行，也可以作为独立程序运行。命令行下通过java启动程序的命令：  

```
java -jar Fiora-202100220-jar-with-dependencies.jar      

```

  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UoMfH0BInAJyGYB6oXJvzPgvk2Dg2C8tNAzcAQZibMbspywE66xUoRSMc5exBGE0cwh6YTYr4fUuA/640?wx_fmt=png&from=appmsg "")  
## 使用方法  
  
以grafana的PoC为例。  
### 搜索PoC  
  
程序会自动扫描nuclei-templates目录下的所有PoC文件，并加载进程序中，可以通过关键词搜索来找到想要的PoC。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UoMfH0BInAJyGYB6oXJvzPmY1ODUov9QYxeHaO0dIABh1Evz146ZRxpcFqNR6cZvAXBXPasUrlXw/640?wx_fmt=png&from=appmsg "")  
### 生成PoC命令  
  
选中想要的PoC，右键选择“generate Command Of This PoC”即可。命令会写入剪切板，直接粘贴运行即可。优点是可以对命令行进行再次编辑，但是需要自行粘贴后运行。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UoMfH0BInAJyGYB6oXJvzPEpclWFblxeryv1tRA7FtibC4kKVh8S0UhCib5VUaoboe997bD51yfR3Q/640?wx_fmt=png&from=appmsg "")  

```
#生产的单个PoC 
nuclei -t C:\Users\P52\nuclei-templates\vulnerabilities\grafana\grafana-file-read.yaml -u http://example.com -proxy http://127.0.0.1

#生产workflow PoC
nuclei -w C:\Users\P52\nuclei-templates\workflows\grafana-workflow.yaml -u http://example.com -proxy http://127.0.0.1


nuclei -tags grafana -u http://example.com -proxy http://127.0.0.1

```

### 直接执行PoC  
  
和生成PoC命令类似，但是它会直接执行生成的命令，不需要粘贴。优点是更便捷，但是无法编辑命令行。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2UoMfH0BInAJyGYB6oXJvzPEpclWFblxeryv1tRA7FtibC4kKVh8S0UhCib5VUaoboe997bD51yfR3Q/640?wx_fmt=png&from=appmsg "")  
  
  
## 工具获取  
  
  
  
点击关注下方名片  
进入公众号  
  
回复关键字【  
250708  
】获取  
下载链接  
  
  
## 往期精彩  
  
  
往期推荐  
  
[一个用于 Burp Suite 的插件，专为检测和分析 SQL 注入漏洞而设计。](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247494698&idx=1&sn=47fe75c62630836696f6a32f42bef890&chksm=c36ba8d2f41c21c4fb95dbebe76e1974b261c8850be5da2969c90a9c0a2d6079c7072fedfe6b&scene=21#wechat_redirect)  
  
  
[十款免费的恶意样本分析工具](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247494690&idx=1&sn=32c119203374701411a8d9572174b5dc&chksm=c36ba8daf41c21cc7ec7d636f92bfbaaab079f8a55292cb65b31395bfbe9b79d2ae45613ec0d&scene=21#wechat_redirect)  
  
  
[一个专为数字钱包助记词本地安全备份设计的加密工具。助记词数据加密 & 解密](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247494661&idx=1&sn=347e22606381188baf5cf640a969e519&chksm=c36ba8fdf41c21eb792672415d86141a93ad6e8a9abbd9b0b852a7cddd966b2cf40db99d8e4d&scene=21#wechat_redirect)  
  
  
[PassGuard是一个轻量级安全工具，专为防护Linux系统中的脏牛(Dirty COW)内核漏洞而设计。](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247494660&idx=1&sn=aa557759e534cc95f47181c56432377b&chksm=c36ba8fcf41c21ea800497d928fd66778c5f035328a0f138321d4624c7ae409129e60997c5bc&scene=21#wechat_redirect)  
  
  
[为渗透测试工程师设计的纯前端工具集，专注于信息收集和文本处理，提供 URL 处理、路径分析、信息收集等功能。](http://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247494659&idx=1&sn=cc30a929b1d60d6cf79279fd545f7e77&chksm=c36ba8fbf41c21edc6aa3c62eaddc47d292c113b1f0c662bbe2b42a71da842914ab6b5e5c529&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp "")  
  
