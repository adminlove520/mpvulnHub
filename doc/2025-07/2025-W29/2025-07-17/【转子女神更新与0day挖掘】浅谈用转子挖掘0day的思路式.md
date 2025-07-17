> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzg3NzkwMTYyOQ==&mid=2247489680&idx=1&sn=37eee459a55b76471119db69d6b93f58

#  【转子女神更新与0day挖掘】浅谈用转子挖掘0day的思路式  
 不秃头的安全   2025-07-17 07:09  
  
# 谈用转子挖掘0day的思路式  

```
声明：本文中涉及到的相关技术或工具仅限技术研究与讨论，严禁用于非法用途，否则产生的一切后果自行承担，如有侵权请私聊删除。
需要2025hvv情报群私聊我拉，需要加交流群在最下方。
知识星球在最下方，续费也有优惠私聊~~
考安全证书请联系vx咨询

```

  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVomYdKlDu5UciaUE1VCluxZZRibVLr3f2Csye8IQxXH5ic6XXWibuGN1jV6n5icJQ8wBjXNoqiavN0z66Q/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
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
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWdezx59b2Q6Yiaibicdkb39G47ZbqBuYrOqvibqdMzutCwS4Qc1KuZrg6uMPrTHe3rbxCvhL7okaTwMg/640?wx_fmt=png&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
往期推荐：  
  
[渗透骚思路 | 从某音泄露到全站信息获取](https://mp.weixin.qq.com/s?__biz=Mzg3NzkwMTYyOQ==&mid=2247489675&idx=1&sn=64bd32314348f9a75be67851c4e687b9&scene=21#wechat_redirect)  
  
  
[SRC实战 | 供应链攻击某src某游戏控制台](https://mp.weixin.qq.com/s?__biz=Mzg3NzkwMTYyOQ==&mid=2247489669&idx=1&sn=24f32f9e8bfc22531976a69e090a10d6&scene=21#wechat_redirect)  
  
  
[【SRC】某选课小程序任意用户登录漏洞深度剖析](https://mp.weixin.qq.com/s?__biz=Mzg3NzkwMTYyOQ==&mid=2247489664&idx=1&sn=df572e4cbef72a5ed6c4de877b52b935&scene=21#wechat_redirect)  
  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVomYdKlDu5UciaUE1VCluxZiaftqQJFoGRnaDnzFRfwZibRHymU9kXP3Aw9hxD0KVicsjJV7icXuZibjFQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp "")  
  
**关于我们:**  
  
感谢各位大佬们关注-不秃头的安全，后续会坚持更新渗透漏洞思路分享、安全测试、好用工具分享以及挖掘SRC思路等文章，同时会组织不定期抽奖，希望能得到各位的关注与支持，考证请加联系vx咨询。  
  
  
## 1. 需要考以下各类安全证书的可以联系  
  
cn*d\cnn*d(量少)中高证书，学生pte超低价，绝对低价绝对优惠，CISP、PTE/PTS、DSG、IRE/IRS、NISP、PMP、CCSK、CISSP、ISO27001、IT服务项目经理等等巨优惠，想加群下方链接：  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DicRqXXQJ6fVomYdKlDu5UciaUE1VCluxZTHtdmBXXGzQnOp21Nktia69klGUoZpIIES20WjVKMj5iaGL80XcWRp7A/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVomYdKlDu5UciaUE1VCluxZcu3vkO9qNeYOq3794Kvy1ZB7rfJeicfnu8C4ZiaI0qqCtRvXOkyX9eoQ/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DicRqXXQJ6fVomYdKlDu5UciaUE1VCluxZvsDmvs9bg9lI0NdC6f09xfIA5fzOSF1y8BrqGnHmGC6q3MibDsYP40g/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp "")  
## 2. 需要入星球的可以私聊优惠  
  
星球里有什么？  

```
1、维护更新src、cnxd、cnnxd专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、fafo/零零信安/QUAKE 高级会员key
3、POC及CXXD及CNNXD通用报告详情分享思路
4、知识星球专属微信“内部圈子交流群”
5、分享src挖掘技巧tips
6、最新新鲜工具分享
7、不定期有工作招聘内推（工作/护网内推）
8、攻防演练资源分享(免杀，溯源，钓鱼等)
9、19个专栏会持续更新~提前续费有优惠，好用不贵很实惠

```

  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DicRqXXQJ6fVomYdKlDu5UciaUE1VCluxZZgmjdkCWSjWdrgrFRpF8Rm09pnVHTkUWJzoCEMxtNYvnb3PrWSicsuw/640?wx_fmt=jpeg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp "")  
  
## 3、其他合作（合法合规）  
  
1、承接各种安全项目（须有授权），需要攻防团队或岗位招聘都可代发、代招（灰黑勿扰）；  
  
2、各位安全老板需要文章推广的请私聊，承接合法合规推广文章发布，可直发、可按产品编辑推广；  
合作、推广代发、安全项目、岗位代招均可发布  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DicRqXXQJ6fVomYdKlDu5UciaUE1VCluxZASr6eck3cQtkVVJ5uZg2ufysuWznFTOZS2UsyFYJkmkgXRMFMIfzkA/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp "")  
  
  
