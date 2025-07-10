> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247492931&idx=1&sn=170a4a59b56d9bc4fbdc04e77da37999

#  【0day挖掘】怎么用“Rotor Goddess”轻松爆出过万资产的漏洞，以及其他小洞的出货方式与流程  
 神农Sec   2025-07-10 05:00  
  
“这里是雪山盟，感谢各位师傅长期的支持与帮助”  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhAzjS04W5sibB8eH3aic5Lhdiapj8Nc1YkFaS8UicBBqWic9lsoqrdCBmAXlg/640?wx_fmt=png&from=appmsg "")  
  
感谢名单：http://zhuanzi.com.cn/thank_you_list.html  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhAAPTzNib8EAhicFKicIekdxfbMrx5SN8GRJ1oOo5Sq5g0zkKiarBlO7otjA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
#------------------------------------------------------------  
  
距离上次发布1.1.0版本的转子女神工具以及过去了一周多，反响还是蛮不错的，用的师傅也不少，BUG也修了特别多，可以说是入不敷出了！  
  
版本也是成功从1.1.0更新到了1.1.6，师傅都称作“转子116”，因为116版本的稳定性比较强，扫描效果距离以前的版本可以说一个天一个地，废话讲完，初衷未变。  
  
“希望这个工具能够名扬四海！”  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhA6kDX0YtFlDldvVSSaC4wJCaWVN0j5f5P2ibdftqDAOfusgw0vJoPFlA/640?wx_fmt=gif&from=appmsg "")  
  
  
  
#------------------------------------------------------------  
  
  
①首先是0day的出货方式：  
  
说来这个出洞的方式，真是想象不到的简单和顺利  
  
HXW师傅在扫描一个站点的时候，抱着测试工具的心态，却发现了一个可疑的URL  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhA92to96JOCQf5p7m4yFt42FbwXj0gx9I6OSzewlZbmxBDdZb3iblrULw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhAC0k3ovdoaj7GrAYnAh2YayF4nOsmhDo74FAxcBvunnUjvy0VCib12Xw/640?wx_fmt=png&from=appmsg "")  
  
URL比较敏感，并且提示了“可能存在SQL注入”  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhACeZMwHicFEAibHVpJhjlsYcBAvDXWeK619klez2sgBaeXaicu1vyyGszA/640?wx_fmt=png&from=appmsg "")  
  
进入后却发现是信息泄露，这里可以水个低危洞，将type的值更改  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhA3XtEmlTvOoiaVrDP3JUB9ZQPDVfZYUiaFPrj1aFm3YcvEu9l0Nkv5TmA/640?wx_fmt=png&from=appmsg "")  
  
意外爆出了XSS漏洞，第二个低危到手，这位师傅又尝试了SQL注入  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhAw9I34t8yx0wKAIf1Z1A4vkBhIKmF8qyonO3kggvbY6q8dqQlofeGzA/640?wx_fmt=png&from=appmsg "")  
  
发现存在SQL延时注入  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhAQzwMs2hm4iatu49aodsVBMC5lPVg3YP0QOdb7fM1jKUGHmk07A6bZdA/640?wx_fmt=png&from=appmsg "")  
  
最终sqlmap一把梭  
  
后面审计框架的时候发现是个0day，意外之喜，一查fofa和quake  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhAKeLibNEETmtnv7eiagFReKaZDPMYpd06I4PfAjOmk7pGib4dyLttP5cGQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhAb3k49C3pGxQNAj22o8CiaAFE5v3QDk1iaqOtxyUtMw4534zfWTNEibaqw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhAdibwdcvuBc4R7RmNaOXfWibEpr7HqD1jjYZYXZyoU6NSeSmdiaHSRVfiaw/640?wx_fmt=png&from=appmsg "")  
  
  
发现影响的资产太多了，师傅正想提交到cnvd但是发现资产不够5000w，就此作罢，当作一次挖洞经验的增加吧！  
  
②第二位师傅的出货方式：  
  
来自。师傅的投稿  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhAz4niaSS5tG6LuTI91TPZfNq51U6JVUWaOnUicS9WemAwjIB440KiaBMwA/640?wx_fmt=png&from=appmsg "")  
  
本来在群里发布工具的相关事宜，聊到其他师傅的出货，这位师傅表示他也同样爆出了个JWT的漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhARgrRG20eHRGIib6u9Cul0RHNDPic07YsrmAXadVBest2HORev2jDhf5Q/640?wx_fmt=png&from=appmsg "")  
  
师傅在进行站点扫描的时候，发现其中一个URL比较可疑，爆出了JWT令牌泄露  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhAhfdIY0wdw2vVKpgHrjyZ4zvOpX2MtxeoYq3qz4eJrTSOmhic2bZHIpQ/640?wx_fmt=png&from=appmsg "")  
  
就立马在威胁匹配里查看参数  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhA04TTZfoOgNtg7fF1wGkOdYD4LPYZxpZibiaVQtofeFU4RTqGVGkdNM9g/640?wx_fmt=png&from=appmsg "")  
  
发现泄露了JWT  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcewKQFGd2JvgS2u18V1ibOVhA3kNvR59lMoAxw19nxp6ph1j5FMm6pqMZ4BDFF5FwSmN3ZCDkNf3wJQ/640?wx_fmt=png&from=appmsg "")  
  
使用该JWT请求页面发现成功返回权限数据  
  
③第三位师傅的出货方式：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUceyG7X0leiaEZO1DX6b0xibar3m3GfCtqjxR6RUXOrQXmD51Xl2B5F5XIG0pjQzXDqiapcN8GvX18Gwkw/640?wx_fmt=png&from=appmsg "")  
  
来自NY师傅的投稿  
  
转子女神扫描站点的时候发现有很多的身份证泄露  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUceyG7X0leiaEZO1DX6b0xibar3sTH8ZGRfHWwLwavg8u2ukfquZajJgsGNXrvSBgHqhPic6TDG142jBlw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcezL4VPU9U05ghXZIM3QRRUiazsUR6kbmmmsXTfxgVp4icmHM3s5LRC5R6W5VHxeKrykmXKN9hFUnLicQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcezL4VPU9U05ghXZIM3QRRUiakz5RAhElvia1ce3eu7Im0wPE8TJBLyiaQDZHaic6zibJ3uibfLBQAAAK2qA/640?wx_fmt=png&from=appmsg "")  
  
无压力的出货信息泄露  
  
-----------------------------------------------------------  
  
以上就到此为止，有需要更详细更多的情报包括转子女神工具的都可以私信我，公众号不方便发太多  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MwxaTtRUcezL4VPU9U05ghXZIM3QRRUiaicujd9PTVZyricCq8WgI488vBgLnUnKBlcUFekrWRHs1gg8VO54fvEOQ/640?wx_fmt=jpeg&from=appmsg "")  
  
**内部小圈子详情介绍**  
  
  
  
我们是  
神农安全  
，点赞 + 在看  
 铁铁们点起来，最后祝大家都能心想事成、发大财、行大运。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mngWTkJEOYJDOsevNTXW8ERI6DU2dZSH3Wd1AqGpw29ibCuYsmdMhUraS4MsYwyjuoB8eIFIicvoVuazwCV79t8A/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
**内部圈子介绍**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap08Z60FsVfKEBeQVmcSg1YS1uop1o9V1uibicy1tXCD6tMvzTjeGt34qr3g/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
**圈子专注于更新src/红蓝攻防相关：**  
  

```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、知识星球专属微信“小圈子交流群”
3、微信小群一起挖洞
4、内部团队专属EDUSRC证书站漏洞报告
5、分享src优质视频课程（企业src/EDUSRC/红蓝队攻防）
6、分享src挖掘技巧tips
7、不定期有众测、渗透测试项目（一起挣钱）
8、不定期有工作招聘内推（工作/护网内推）
9、送全国职业技能大赛环境+WP解析（比赛拿奖）
```

  
  
  
  
**内部圈子**  
**专栏介绍**  
  
知识星球内部共享资料截屏详情如下  
  
（只要没有特殊情况，每天都保持更新）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibRSekfPpgmzg6Pn4yH440wEZhQZaJaxJds7olZp5H8Ma4PicQFclzGbQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibgpeLSDuggy2U7TJWF3h7Af8JibBG0jA5fIyaYNUa2ODeG1r5DoOibAXA/640?wx_fmt=png&from=appmsg "")  
  
  
**知识星球——**  
**神农安全**  
  
星球现价   
￥45元  
  
如果你觉得应该加入，就不要犹豫，价格只会上涨，不会下跌  
  
星球人数少于1000人 45元/年  
  
星球人数少于1200人 65元/年  
  
（新人优惠卷20，扫码或者私信我即可领取）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXYSHg6L72Acqz6CcxdTTR72ic6bOSuMibJkYgVvibYfvrIwxESqR5TL8qrZhUQicKTUGeOic4VMibicF6Mw/640?wx_fmt=png&from=appmsg "")  
  
欢迎加入星球一起交流，券后价仅45元！！！ 即将满1000人涨价  
  
长期  
更新，更多的0day/1day漏洞POC/EXP  
  
  
  
**内部知识库--**  
**（持续更新中）**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFu12KTxgSfI69k7BChztff43VObUMsvvLyqsCRYoQnRKg1ibD7A0U3bQ/640?wx_fmt=png&from=appmsg "")  
  
  
**知识库部分大纲目录如下：**  
  
知识库跟  
知识星球联动，基本上每天保持  
更新，满足圈友的需求  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFhXF33IuCNWh4QOXjMyjshticibyeTV3ZmhJeGias5J14egV36UGXvwGSA/640?wx_fmt=png&from=appmsg "")  
  
  
知识库和知识星球有师傅们关注的  
EDUSRC  
和  
CNVD相关内容（内部资料）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFKDNucibvibBty5UMNwpjeq1ToHpicPxpNwvRNj3JzWlz4QT1kbFqEdnaA/640?wx_fmt=png&from=appmsg "")  
  
  
还有网上流出来的各种  
SRC/CTF等课程视频  
  
量大管饱，扫描下面的知识星球二维码加入即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFxYMxoc1ViciafayxiaK0Z26g1kfbVDybCO8R88lqYQvOiaFgQ8fjOJEjxA/640?wx_fmt=png&from=appmsg "")  
  
  
  
不会挖CNVD？不会挖EDURC？不会挖企业SRC？不会打nday和通杀漏洞？  
  
直接加入我们小圈子：  
知识星球+内部圈子交流群+知识库  
  
快来吧！！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJ5wUOL9GnsxoXibKezHTjL6Yvuw6y8nm5ibyL388DdDFvuAtGypahRevg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJO0FHgdr6ach2iaibDRwicrB3Ct1WWhg9PA0fPw2J1icGjQgKENYDozpVJg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
  
神农安全知识库内部配置很多  
内部工具和资料💾，  
玄机靶场邀请码+EDUSRC邀请码等等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXjm2h60OalGLbwrsEO8gJDNtEt0PfMwXQRzn9EDBdibLWNDZXVVjog7wDlAUK1h3Y7OicPQCYaw2eA/640?wx_fmt=png&from=appmsg "")  
  
  
快要护网来临，是不是需要  
护网面试题汇总  
？  
问题+答案（超级详细🔎）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXjm2h60OalGLbwrsEO8gJDbLia1oCDxSyuY4j0ooxgqOibabZUDCibIzicM6SL2CMuAAa1Qe4UIRdq1g/640?wx_fmt=png&from=appmsg "")  
  
  
最后，师傅们也是希望找个  
好工作，那么常见的  
渗透测试/安服工程师/驻场面试题目，你值得拥有！！！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXjm2h60OalGLbwrsEO8gJDicYew8gfSB3nicq9RFgJIKFG1UWyC6ibgpialR2UZlicW3mOBqVib7SLyDtQ/640?wx_fmt=png&from=appmsg "")  
  
  
内部小圈子——  
圈友反馈  
（  
良心价格  
）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0s5638ehXF2YQEqibt8Hviaqs0Uv6F4NTNkTKDictgOV445RLkia2rFg6s6eYTSaDunVaRF41qBibY1A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0s5638ehXF2YQEqibt8HviaRhLXFayW3gyfu2eQDCicyctmplJfuMicVibquicNB3Bjdt0Ukhp8ib1G5aQ/640?wx_fmt=png&from=appmsg "")  
  
  
****  
**神农安全公开交流群**  
  
有需要的师傅们直接扫描文章二维码加入，然后要是后面群聊二维码扫描加入不了的师傅们，直接扫描文章开头的二维码加我（备注加群）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXYSHg6L72Acqz6CcxdTTR7Fotibpcs8XRn33xic5cMHaRIVPPBX9pJynCUQ7II1kBnsQCfzwXSToMw/640?wx_fmt=jpeg&from=appmsg "")  
  
    

```
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

```

  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/b7iaH1LtiaKWW8vxK39q53Q3oictKW3VAXz4Qht144X0wjJcOMqPwhnh3ptlbTtxDvNMF8NJA6XbDcljZBsibalsVQ/640?wx_fmt=gif "")  
  
  
