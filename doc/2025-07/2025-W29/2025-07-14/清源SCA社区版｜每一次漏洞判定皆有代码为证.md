> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzg3MDgyMzkwOA==&mid=2247491762&idx=1&sn=29ab889867f7d639faaa54a3dfc2ef2e

#  清源SCA社区版｜每一次漏洞判定皆有代码为证  
原创 安势信息  安势信息   2025-07-14 10:16  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01UNDy9laTbwiaibibABN1MUUe0avBT7AlJYBRPsOkWURB48A8WbrAlWr7Q/640?wx_fmt=gif "")  
  
利用【清源SCA社区版】进行漏洞判定  
  
  
  
  
**1**  
  
Step1：上传代码  
  
  
  
登陆【清源SCA社区版】之后创建扫描任务：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01vVHe7pEDlygFruibhYvqLBia8IIyl4DYul3ZT15EDQ3AObtFArs1k0kg/640?wx_fmt=png "")  
  
- 除本地源代码，部分二进制格式外，  
支持从git仓库直接拉取  
等方式进行代码上传；  
  
- 支持通过CLI命令行工具  
进行扫描。  
  
  
  
  
**2**  
  
Step2：触发扫描  
  
  
  
点击「开始扫描」即可。  
  
  
**3**  
  
Step3：查看扫描报告  
  
  
  
1分钟之后，我们完成了对这个开源项目的扫描，通过「查看」按钮展示扫描结果：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01dIhC0icNiaul7vN4YKibKxD1thiaSrO318uptxD5SHsJDhJmDl8R2VUgcw/640?wx_fmt=png "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01aB8ptTicOR0FxhrxibiaZ8KBfLibFYNtWjicC6Fy1uCY0XWT8WTRb1QKgfw/640?wx_fmt=png "")  
  
  
我们可以看到，目标开源项目中有很多“强烈建议修复”的漏洞，  
列表中展示了组件名称、版本、厂商、许可证及漏洞评估风险  
，针对有修复建议的情况，我们可以  
点击「修复建议」进行修复建议的查看。  
  
  
**4**  
  
Step4：查看漏洞详情  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01a0MXibxoGqzaOoXfYmM0ecSky1dj19AiavavXpHWccJiaQricicMn9ib9fVw/640?wx_fmt=png "")  
  
通过点击「定位」按钮即可展示漏洞可达信息  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01dy0luFOE4VEW6qpg79PwTicX0wianHthahz9ypAF6uqTG1nzpKPib4OjQ/640?wx_fmt=jpeg "")  
  
漏洞不可达情况  
  
- **显著标识：**  
✅ 可达漏洞（「定位」按钮出现）⚠️ 不可达漏洞（无「定位」按钮出现）。  
  
- **如有EOL**  
（End of Life，社区停止维护）组件，则会展示在修复建议中。  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01rBpegxibTKYon5icCNaqUkuic0mdGCT1LwY2frWyZnZ3RvLPhj3CAqrxg/640?wx_fmt=png "")  
  
  
至此，我们展示出了在本项目中与CVE-2022-25845漏洞相关的所有调用路径，研发/安全人员可以轻松确认该漏洞可达，进而进行版本升级/组件替换等修复行为。  
  
  
清源SCA社区版与Snyk社区版  
  
漏洞可达能力对比  
  
  
  
  
我们使用了10个测试项目，进行清源社区版SCA与Snyk社区版结果进行对比，得出如下结果：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01TlgQsvCR0wNk2C2icLyThB54jwBcV0DibS65jficHO8MUBlW4usnsvtibg/640?wx_fmt=png "")  
  
  
经过对测试项目中所有漏洞路径的人工复核验证，我们发现：在10个具备真实可达路径的漏洞案例中，Snyk社区版出现了70%的漏报情况。需要说明的是，尽管Snyk作为全球领先的SCA解决方案在业界享有盛誉，但其社区版在漏洞可达性分析这一高技术难度的功能模块上仍存在提升空间。  
  
  
以本文第一部分分析的CVE-2022-25845漏洞为例，该漏洞在测试项目中存在明确的可达路径，但Snyk社区版未能有效识别其可达性。这一现象也印证了我们的测试结论。  
  
  
接下来，我们将重点解析清源SCA社区版所采用的漏洞可达性分析技术，为大家深入探讨该领域的核心技术实现。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01ibDIFt5fibRZUhKSB1qhPnibXZKYJIY2oPxM0SmSd4KSicfhGyn8LWIk7w/640?wx_fmt=png "")  
  
Snyk社区版未能正确识别这一可达漏洞  
  
安势漏洞可达技术深度解析  
  
  
  
  
一  
  
为什么需要函数级分析？  
  
  
**传统组件级扫描的致命缺陷：**  
  
"项目中存在漏洞组件 ≠ 漏洞可被利用"，安全与研发人员消耗了大量的时间在定位漏洞上，而非修复漏洞。  
  
  
二  
  
技术原理与流程  
  
  
**1、核心原理如下：**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01mfVn7c86rka09cCSAKtOaoxMEl5lJurYIKwFOa4CZeY2V3aKbAlhgA/640?wx_fmt=png&from=appmsg "")  
  
****  
**关键逻辑：**  
若存在连续调用路径抵达漏洞函数（Sink），则漏洞存在被利用  
  
的可能性；反之若不可达，则几乎不可利用，可以降低相应修复的优先级。  
  
  
**2、流程框架**  
  
**2.1 标注漏洞函数（Sink）：**  
  
基于   
CVE  
信息分析受影响组件  
源码  
去识别漏洞触发函数。  
  
  
**2.2 构建全量调用图（Call Graph）：**  
  
静态分析项目代码 + 依赖，生成跨模块函数调用关系图。  
  
  
**2.3 路径可达性验证：**  
  
通过调用路径来验证从项目中代码到依赖组件中漏洞函数的可达性。  
  
  
**2.4 风险判定与排序：**  
  
结合可达性结果 + 威胁情报（POC/攻击事件）输出修复优先级。  
  
  
三  
  
漏洞可达的技术难点与挑战  
  
  
**难点1：漏洞函数标注**  
  
****  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01nNTZavJ9wa8kxnsecSKeTmLTY9hf8eF11P8WrIdDxrcGlamp7qL12g/640?wx_fmt=png "")  
  
****  
**关键结论：**  
当前需人工+工具结合，标注准确性直接影响可达分析有效性。  
  
  
**难点2：调用图构建（Call Graph）**  
  
  
**挑战1：多态与动态绑定（面向对象语言）**  
- **问题：**  
父类函数调用在运行时可能指向任意子类重写方法。  
  
  
- 描述：  
由于 java 语言中的多态特性，一个抽象类或者父类存在多个子类和实现类，在构造调用图的时候需要权衡全面性以及准确性，单纯使用 CHA 算法会存在包含了大量无用路径的问题，而基于 SPARK 的算法又会漏掉一些客观可能的路径。清源 SCA的自研算法有效的平衡了调用图构建过程中的覆盖率与准确性。  
  
**挑战2：动态语言特性（反射/运行时加载）**  
  
****- **例如：**  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01P33ibo2OHXq48ib4alWnpuatezcxR8bv1UehsdpwM5L70m2cUEdQGkQw/640?wx_fmt=png "")  
  
这种代码在编译时完全不知道会调用哪些类和方法，因为这里的 className 依赖于运行时的实际传入的值。  
  
  
**挑战3：跨模块调用**  
- 项目依赖多组件时，需拼接多个模块的调用图 → 存储与计算复杂度指数级增长。  
  
- 例：Python项目中多个.py文件相互调用；Java项目中跨JAR包交互。  
  
****  
**本质矛盾：**  
静态分析无法覆盖动态行为，导致调用图完整性与准确性难以兼得。  
  
  
四  
  
总结：漏洞可达技术的价值  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01Xk2pn2YCeEibYMzH6oeag03HdWias30D7JoW8yXD5ZbG17hFDl3qlbMw/640?wx_fmt=png "")  
  
  
**技术演进意义：**  
  
**从“有漏洞即报”升级为“能利用才报”**  
，将安全团队从告警噪音中解放，聚焦真实风险。  
  
  
立即体验【清源SCA社区版】  
  
  
  
**【清源SCA社区版】注册登陆：**  
  
**https://cleansource-ce.sectrend.com.cn:9988/login**  
  
**或点击文章底部的【阅读原文】**  
  
****  
**用户操作手册：**  
  
https://cleansource-ce.sectrend.com.cn:9988/document  
  
****  
**让安全告警回归真实威胁，让开发者告别无效警报。**  
  
****  
清源SCA社区版｜每一次漏洞判定皆有代码为证。  
  
  
  
  
  
  
  
  
  
  
扫下方**【安势信息小助手】**  
二维码，第一时间获取**【清源SCA社区版】**  
最新信息  
  
扫一扫｜安势信息小助手  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01dUy9l8yLryGnlhg9hXOoypE6y8VERk2kahXjFhP5RO0gyElh1JjUFQ/640?wx_fmt=jpeg "")  
  
  
  
扫码下方二维码加入官方交流群，每日获取安势信息在官网交流群和公众号中发布的：  
  
- CVE未收录高危漏洞提前感知  
  
- CVE热点漏洞精选  
  
- 投毒情报  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01dLq0RkoGG9p0uia1weobPHMokTE50LRh50G3qLoRBEnpydWs9r7f8iaQ/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0HJalXIBXGXSBFLMk2TZAqh23iaHwLpprUov8bNQ95dWDVMTq4qGicM3G6cmsZcCF6RsKyn9p8eQA3Q/640?wx_fmt=png "")  
  
清源SCA社区版交流群  
  
**扫码入群**  
  
获取每日最新 漏洞和投毒情报  
  
****  
**关于安势信息**  
  
  
上海安势信息技术有限公司是国内先进的软件供应链安全治理解决方案提供商，核心团队来自Synopsys、华为、阿里巴巴、腾讯、中兴等国内外企业。安势信息始终坚持DevSecOps的理念和实践，以AI、多维探测和底层引擎开发等技术为核心，提供包括清源CleanSource SCA（软件成分分析）、清源SCA社区版、清正CleanBinary (二进制代码扫描)、清流PureStream（AI风险治理平台）、清本CleanCode SAST（企业级白盒静态代码扫描）、可信开源软件服务平台、开源治理服务等产品和解决方案，覆盖央企、高科技、互联网、ICT、汽车、高端制造、半导体&软件、金融等多元化场景的软件供应链安全治理最佳实践。  
  
  
欢迎访问安势信息官网www.sectrend.com.cn或发送邮件至 info@sectrend.com.cn垂询。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibSWU7ian1thv4sZU2nEqe6mxS7I2dRP01wARmjF5AbMS7uwUyfWr7kmaeDYEDOicju7FVvqTJ0ibcU57wh8k6KKKA/640?wx_fmt=gif "")  
  
  
