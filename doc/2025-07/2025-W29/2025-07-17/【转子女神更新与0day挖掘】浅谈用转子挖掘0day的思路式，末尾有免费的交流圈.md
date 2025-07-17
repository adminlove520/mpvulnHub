> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247493493&idx=1&sn=b7596ba5e416cbb4fa3627f1f8cb1d0f

#  【转子女神更新与0day挖掘】浅谈用转子挖掘0day的思路式，末尾有免费的交流圈  
 神农Sec   2025-07-17 05:00  
  
“海内存知己，天涯若比邻”  
  
”这里是雪山盟，承蒙各位师傅的厚爱和支持“  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcezg7oLRsEA2L4yJUpMDznXGcJNeVezzpfbH3G1ajicvk8OWDzen1bZCQvWoxQ9IcAC9OoN2ia7nuGTw/640?wx_fmt=png&from=appmsg "")  
  
感谢名单：http://zhuanzi.com.cn/thank_you_list.html  
  
非常感谢所有在转子女神工具上给予帮助的每一位师傅  
  
#------------------------------------------------------------  
  
“”“  
  
历经10余天，转子女神来到了1.1.7版本，更改了扫描的方式，可选的1-3次迭代的扫描，新增了代理，延时等等功能，修复了众多的BUG，再次感谢各位师傅的支持  
  
”“”  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MwxaTtRUcezg7oLRsEA2L4yJUpMDznXGicLyHkRVCQ4cnuccRY8khE69sRDklwSR3DHvAXqJmAgxHWyBic9V9fTw/640?wx_fmt=jpeg&from=appmsg "")  
  
更新内容：  

```
# 2025/7/11-16 更新
# 1.更改路径拼接写法
# 2.修复出现两个url合并拼接的问题
# 3.增加敏感页面字典
# 4.对URL进行解码,解决URL存在中文显示过长的问题
# 5.去除URL末尾的->符号
# 6.增强脏数据的过滤
# 7.增加SSRF的字典
# 8.新增迭代扫描功能:JS文件的三次迭代扫描--scan=x 上限为3次 默认为1
# 9.更改整体写法,提升代码效率
# 10.修复自定义拼接的问题
# 11.对JS文件的收集进行总结输出
# 12.对重复内容进行颜色区分标记
# 13.新增扫描的睡眠时间设置,适合扫描存在WAF的站点
# 14.增加代理功能
# 15.增加自动更新的开关,防止内网环境下出网外连
# 16.域名后缀过滤
# 17.修复JS文件取消分析依然会要求输入数量的问题
# 18.增加POST请求功能
# 19.填充过滤字典
# 20.优化批量扫描时需要反复输入y/n的问题
```

  
  
接下来是使用方法：  
  
--cer : 过证书  
  
--time=5 : 超时设置  
  
--url : 自定义URL的拼接  
  
--proxy=http://1.1.1.1:8080 : 自定义代理  
  
--sleep=5 : 请求的睡眠时间  
  
--scan=3 : 迭代扫描的深度，最高为3，默认为1  
  
#------------------------------------------------------------  
  
接下来是关于  
0day的出货方式与思路  
  
来自【落樱时】师傅的投稿：  
  
这位师傅在进行黑盒测试的时候，扫描的过程中发现了一个敏感的页面  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcezg7oLRsEA2L4yJUpMDznXGLCwqSmAPTs2lUETQqfZkWAqn0y3lCTzPVMAdJXq6oXRDlxSnibkdrfQ/640?wx_fmt=png&from=appmsg "")  
  
经过查看，该厂商的资产超过1.5e  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcezg7oLRsEA2L4yJUpMDznXGniaxNibIMp7hllwyOUpUflDWwnxiamBx93Y7HJIolaeUY9fn4G8icSMXTA/640?wx_fmt=png&from=appmsg "")  
  
请求后是这样的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcezg7oLRsEA2L4yJUpMDznXGjTGgX4ibQqhMvnb2icqQ1ibw7MQhiaC1gE6RwZzZkQOwDDkLs02V81giaqg/640?wx_fmt=png&from=appmsg "")  
  
查看响应头会发现拿到了session，将session填入到这个请求下，进行fuzzer，并遍历包中的ROLE_ID，成功拿到管理员的账号密码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcezg7oLRsEA2L4yJUpMDznXGJw7dibcHadXxuKfDZvI7e5Ze0oRdO2zZ8eAVeYd4Zib41ZeD5FwdCTtA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcezg7oLRsEA2L4yJUpMDznXGXXianJBaI5a8iaIlVia4XNkCrT65zEWoKHTVSwV5Gw58wIpxRbkickYXmQ/640?wx_fmt=png&from=appmsg "")  
  
成功登陆进后台系统，该漏洞已由今天，提交至CNVD国家漏洞平台  
  
需要key或者更多挖掘思路和情报的师傅，欢迎添加我的微信：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MwxaTtRUcezg7oLRsEA2L4yJUpMDznXGRGoOX2zwibWxF3tFibGBTm6TbonGdgHsGI1W8xo5ecZtOV90dPgEAz9A/640?wx_fmt=png "")  
  
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
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXWwRdxNQnWo5Eq7BzgsIKogHTNRKIZQVcM0QQE3wbFrFciafzrEaRcia7gkRFb4vujBubqic3sPIN1g/640?wx_fmt=png&from=appmsg "")  
  
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
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXWwRdxNQnWo5Eq7BzgsIKovBgx57dc6Ql2yRSPBJGA5fde4sQJzOomD1GURVibZeCNzXM6iaGrSe8Q/640?wx_fmt=jpeg&from=appmsg "")  
  
    

```
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

```

  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/b7iaH1LtiaKWW8vxK39q53Q3oictKW3VAXz4Qht144X0wjJcOMqPwhnh3ptlbTtxDvNMF8NJA6XbDcljZBsibalsVQ/640?wx_fmt=gif "")  
  
  
