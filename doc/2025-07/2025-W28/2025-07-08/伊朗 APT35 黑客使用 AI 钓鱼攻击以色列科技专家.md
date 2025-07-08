> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547036&idx=3&sn=538ef2224e912a425b55a46eed1c00e7

#  伊朗 APT35 黑客使用 AI 钓鱼攻击以色列科技专家  
龙猫  安小圈   2025-07-08 00:45  
  
**安小圈**  
  
  
第703期  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/jDxr6RVaB7vg2iaFhjMPt6AgOazbA1mP0RSD3zjTFfRPfjlUNTC5uwVMc1f6SZG3rR6RTEemOYPbmPiadyTBtquA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
![](http://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbMjDKCY2Lk2HcctzBYfqOcjU4Djy5iamYYkH1KlHltmMmibhVdKb0UKiaWm6EYfY9aRLtffwzUCl7FCg/640?wx_fmt=jpeg "")  
  
  
6 月 26 日消息，Check Point 周三发布的一份报告显示，与伊朗伊斯兰革命卫队（IRGC）有关联的一个伊朗国家支持的黑客组织，发起了一场鱼叉式网络钓鱼活动，目标直指以色列的记者、知名网络安全专家和计算机科学教授。  
  
在部分活动中，攻击者通过电子邮件和 WhatsApp 消息，伪装成科技高管或研究人员的虚构助理，与以色列的技术和网络安全专业人士接触，并将与之互动的受害者引导至伪造的 Gmail 登录页面或 Google Meet 邀请页面。  
  
这家网络安全公司将此次活动归因于一个被其追踪为 “Educated Manticore” 的威胁集群，该集群与 APT35（及其子集群 APT42）、CALANQUE、Charming Kitten 等多个组织存在重叠。  
  
这个高级持续性威胁（APT）组织长期以来一直有通过精心设计的诱饵策划社会工程攻击的历史，他们会在 Facebook 和 LinkedIn 等各种平台上使用虚构的人物角色接近目标，诱使受害者在其系统上部署恶意软件。  
  
Check Point 表示，在 2025 年 6 月中旬伊朗与以色列爆发战争后，观察到了新一轮的攻击。此次攻击针对以色列个人，使用了虚假的会议诱饵，通过电子邮件或 WhatsApp 消息发送，且这些消息专门针对目标定制。由于这些消息布局结构化且没有任何语法错误，据信是使用人工智能（AI）工具制作的。  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/jDxr6RVaB7vg2iaFhjMPt6AgOazbA1mP0m6lLQoPuDu0dnaH8lsOib8f65BUhg5B1hvUWVVexyQDQV4AcZRzLiceQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
  
该公司标记的一条 WhatsApp 消息，利用两国当前的地缘政治紧张局势，诱使受害者参加会议，声称需要他们立即协助一个基于人工智能的威胁检测系统，以应对自 6 月 12 日以来针对以色列的网络攻击激增。  
  
正如在之前的 Charming Kitten 活动中所观察到的，初始消息中没有任何恶意内容，主要目的是获取目标的信任。一旦威胁行为者在对话过程中与目标建立了融洽的关系，攻击就会进入下一阶段，他们会分享链接，将受害者引导至能够获取其 Google 账户凭据的虚假登录页面。  
  
Check Point 称：“在发送网络钓鱼链接之前，威胁行为者会询问受害者的电子邮件地址，然后该地址会预先填写在 credential 网络钓鱼页面上，以增加可信度，并模仿合法的 Google 身份验证流程。”  
  
这款定制的网络钓鱼工具包通过 React 单页应用程序（SPA）和动态页面路由等现代网络技术，紧密模仿谷歌等人们熟悉的登录页面，还利用实时 WebSocket 连接发送窃取的数据，其设计能够隐藏代码，避免被进一步审查。  
  
这个虚假页面是一个定制网络钓鱼工具包的一部分，该工具包不仅可以捕获受害者的凭据，还可以捕获双因素身份验证（2FA）代码，从而有效实施 2FA 中继攻击。该工具包还集成了一个被动键盘记录器，用于记录受害者输入的所有击键，并在用户中途放弃该过程时将其泄露。  
  
部分社会工程工作还涉及使用谷歌网站域名来托管虚假的 Google Meet 页面，页面上有一张模仿合法会议页面的图片，点击图片上的任何位置都会将受害者引导至触发身份验证过程的网络钓鱼页面。  
  
Check Point 表示：“在伊朗与以色列冲突升级阶段，Educated Manticore 继续构成持续且高影响的威胁，尤其是对以色列境内的个人。”“该组织继续稳步运作，其特点是积极的鱼叉式网络钓鱼、快速设置域名、子域名和基础设施，以及在被识别后迅速拆除。这种敏捷性使其在高度审查下仍能保持有效性。”  
  
  
  
END  
  
  
  
**【内容**  
**来源：星尘安全】**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/BWicoRISLtbMSrNYPzeZSs4X316kGV7UeeR4VInT56J0KCLD3HkiaRxjMLLV6rricOadHohJB1sOtPT02fETAxr4g/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/0YKrGhCM6DbI5sicoDspb3HUwMHQe6dGezfswja0iaLicSyzCoK5KITRFqkPyKJibbhkNOlZ3VpQVxZJcfKQvwqNLg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546898&idx=1&sn=2f16da5665014b4c07bcbd53e3d1c03e&scene=21#wechat_redirect)  
- [【HW】8个因护网被开除的网安人](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546898&idx=1&sn=2f16da5665014b4c07bcbd53e3d1c03e&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546898&idx=2&sn=e9578e62a475ac5c46b95ac81066d2a7&scene=21#wechat_redirect)  
- [HW应急溯源：50个高级命令实战指南](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546898&idx=2&sn=e9578e62a475ac5c46b95ac81066d2a7&scene=21#wechat_redirect)  
  
  
- [震惊全球！中国团队攻破RSA加密！RSA加密告急？](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546856&idx=1&sn=11b36f6fabde860e889e4ac2f4797bba&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbOugegrykhydnkHibcSWjpibTBZoK6jjGxJiax1BcwwctpA5SBric9aPdQFXsxFnn4LQJWdkYwbtPN0gg/640?wx_fmt=jpeg "")  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546815&idx=1&sn=99a4f3228f322ef92c93d23cee01f071&scene=21#wechat_redirect)  
- [2025年【护网】攻防演练时间已定！](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546815&idx=1&sn=99a4f3228f322ef92c93d23cee01f071&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546578&idx=1&sn=87cdf84e6fd7d35986b29acd90954c65&scene=21#wechat_redirect)  
  
[突发！小红书惊现后门......](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546578&idx=1&sn=87cdf84e6fd7d35986b29acd90954c65&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbPwt82pEdc2YwCDz6n3H3c2C0ibcMl4Tea8hM59iaZoR1FDMTCUswDiclc1icLoSywpkWbdqyb6uBNcnA/640?wx_fmt=jpeg "")  
- [2025年“净网”“护网”专项工作部署会在京召开，看看都说了哪些与你我相关的关键内容？](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546673&idx=1&sn=53fe0365785465d4ff6193a9ca639119&scene=21#wechat_redirect)  
  
  
- # 护网即将来临，这场网安盛会带给了我们打工人什么......  
  
- [护网在即，企业还有什么新思路可以应对吗？](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546698&idx=1&sn=55ab4ac8dffb5f7ccf02a4f759537acf&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbPwt82pEdc2YwCDz6n3H3c2Noz3ibYqNZ52uicBtuVVlFRg6vSuF8YFjPvCVma1ADrT1ViaKVE9URNOA/640?wx_fmt=jpeg "")  
- [HW必备：50个应急响应常用命令速查手册一（实战收藏）](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546304&idx=2&sn=45ef99e528ded7ff2e65e4d70e6d5181&scene=21#wechat_redirect)  
  
  
- [HW必备：50个应急响应常用命令速查手册二（实战收藏）](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546327&idx=2&sn=cf1ebbd2b511524ec965a3672b6fc3dd&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546530&idx=1&sn=4a2820b60102e538e87c956375f6fcdb&scene=21#wechat_redirect)  
- [网安同行们，你们焦虑了吗？](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546530&idx=1&sn=4a2820b60102e538e87c956375f6fcdb&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546466&idx=1&sn=a9d55d0b430dbf61dc219fd71ce25ae1&scene=21#wechat_redirect)  
- # 网安公司最后那点体面，还剩下多少？  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247545577&idx=1&sn=76a4dbd28d9c0e006b7790d89c2b1354&scene=21#wechat_redirect)  
- [2024年网安上市公司营收、毛利、净利润排行](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247545577&idx=1&sn=76a4dbd28d9c0e006b7790d89c2b1354&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247545311&idx=2&sn=bb8ff7cd42079bae40ab0a2e05ff37c1&scene=21#wechat_redirect)  
- [突发！数万台 Windows 蓝屏。。。。广联达。。。惹的祸。。。](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247545311&idx=2&sn=bb8ff7cd42079bae40ab0a2e05ff37c1&scene=21#wechat_redirect)  
  
  
#   
- # 权威解答 | 国家网信办就：【数据出境】安全管理相关问题进行答复  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247539649&idx=1&sn=8858b449c89d21240e1f522e92be4fbd&scene=21#wechat_redirect)  
- # 全国首位！上海通过数据出境安全评估91个，合同备案443个  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247544405&idx=2&sn=a961d43ca4a9ed667fccbbab758d9196&scene=21#wechat_redirect)  
- # 沈传宁：落实《网络数据安全管理条例》，提升全员数据安全意识  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247545156&idx=1&sn=ee5292e9838b2a2112a94a9c7c683925&scene=21#wechat_redirect)  
  
- [频繁跳槽，只为投毒](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247545156&idx=1&sn=ee5292e9838b2a2112a94a9c7c683925&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247545017&idx=1&sn=b513c15f91d5de7a8fa33c4b3725706a&scene=21#wechat_redirect)  
- [【高危漏洞】Windows 11：300毫秒即可提权至管理员](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247545017&idx=1&sn=b513c15f91d5de7a8fa33c4b3725706a&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247544601&idx=1&sn=e230574b0535e6005b830d086cdcf867&scene=21#wechat_redirect)  
- [针对网安一哥专门的钓鱼网站](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247544601&idx=1&sn=e230574b0535e6005b830d086cdcf867&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247544347&idx=1&sn=06311aa3f8aeba492f83224c652fe4a1&scene=21#wechat_redirect)  
  
- [为什么【驻场】网络安全服务已成为大多数网络安全厂商乙方不愿再触碰的逆鳞？](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247544347&idx=1&sn=06311aa3f8aeba492f83224c652fe4a1&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbOYPldtHVUmKQJ2WtL12GUnHRyzBiaKosLNicTZ2QkDFSRPUha2Eiaqk8R5fPdXc75zxprkTRB0ib5hUw/640?wx_fmt=jpeg "")  
- [HW流程以及岗位职责](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247544347&idx=3&sn=97e6083dbfbdd896680e24770a10d319&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247543989&idx=1&sn=2821b91efdd626e1a38ec6b2b439186b&scene=21#wechat_redirect)  
  
- # 网络安全【重保】| 实战指南：企业如何应对国家级护网行动？  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247542929&idx=1&sn=8cf6f15ddca44e343a494eea0fa619b2&scene=21#wechat_redirect)  
- **DeepSeek安全：AI网络安全评估与防护策略**  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247542701&idx=1&sn=567674aa12d861c3561d453268badb91&scene=21#wechat_redirect)  
- **虚拟机逃逸！VMware【高危漏洞】正被积极利用，国内公网暴露面最大******  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247542458&idx=1&sn=d81d049331d175a2176f0978d7f032a8&scene=21#wechat_redirect)  
- **挖矿病毒【应急响应】处置手册******  
  
****- **用Deepseek实现Web渗透自动化**  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247542225&idx=2&sn=244a465fab183f4fa91a284b92a920e6&scene=21#wechat_redirect)  
- **【风险】DeepSeek等大模型私有化服务器部署近九成在“裸奔”，已知漏洞赶紧处理！**  
  
****- **关于各大网安厂商推广「DeepSeek一体机」现象的深度分析**  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247541264&idx=1&sn=887bf392ba73e7c2c833a410e7168818&scene=21#wechat_redirect)  
- [Deepseek真的能搞定【安全运营】？](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247541264&idx=1&sn=887bf392ba73e7c2c833a410e7168818&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247540432&idx=1&sn=b9e7e6103e86b9966f29d7eacf8e3d1e&scene=21#wechat_redirect)  
- **【热点】哪些网络安全厂商接入了DeepSeek？**  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247540206&idx=2&sn=300737ad84f684e622fdde03da0fc1a7&scene=21#wechat_redirect)  
- **【2025】常见的网络安全服务大全（汇总详解）**  
  
[](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247540343&idx=1&sn=59d6f592f71a7f1e3a18fd082aa3de40&scene=21#wechat_redirect)  
- **AI 安全 |《人工智能安全标准体系(V1.0)》(征求意见稿)，附下载**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/BWicoRISLtbMbfUY7RtO1t6ZAxjoibZoZ8DSVPU0yI9v2nXpiat0oN8eLia5jiaoWOhlib5GiaPWQJeCsUmShI4QOqaGg/640?wx_fmt=png "")  
- **2025年 · 网络威胁趋势【预测】**  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbM09kF5tXEb8PRXicFibPic4un6rwDI2CBUxrVaDINuM8ChyotgWiag4icErAHniaYNYiccQiaVkyyJUTX13w/640?wx_fmt=jpeg "")  
- **【实操】常见的安全事件及应急响应处**  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbMASB7RibZ1nezrias4SvtcqzjvsJJPXhFiceJPEoVHVLhI2Soolaf8OhWQOVafycOibiaclJkT7NgG4Nw/640?wx_fmt=jpeg "")  
- **2024 网络安全人才实战能力白皮书安全测试评估篇**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/BWicoRISLtbMSrNYPzeZSs4X316kGV7UeOsnl5ayrQXc0wPVutL1dQXg7BugT7vAe8qkpfszTrlhUAq4DQZFaVA/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/BWicoRISLtbP7Bh21K85KEkXX7ibWmLdM2eafpPicoTqk37LEVMUKD1JuAic4FF4KB7jP4oFTricyMwvj5VUZZ824ww/640?wx_fmt=gif "")  
![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbNzlia8CP45sjgLJgia5Y22hx8khBeShnAzCPwsfqeIVKkpFDhUoMUWMicq6toR2TSUmgBpgzZQHEAHw/640?wx_fmt=jpeg "")  
![](https://mmbiz.qpic.cn/mmbiz_png/BWicoRISLtbPFKyibwduMibC35MsIhibgZEAibwSyVRz7FKt3xa1UK61fXXCCUKllCXFrLdnBqcmgiaKeSxGrWT0RtYw/640?wx_fmt=png "")  
  
