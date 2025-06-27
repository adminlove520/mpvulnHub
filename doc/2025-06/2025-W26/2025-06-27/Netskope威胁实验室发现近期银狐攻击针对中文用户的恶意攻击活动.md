> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzAxMjYyMzkwOA==&mid=2247531404&idx=1&sn=de9a70dda8df8fcf23e2240fc118e7db

#  Netskope威胁实验室发现近期银狐攻击针对中文用户的恶意攻击活动  
 Ots安全   2025-06-27 04:08  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn7gtxSFZlfuCW6AdQib8Q1onbR0U2h9icP1eRO6wH0AcyJmqZ7USD0uOYncCYIH7ZEE8IicAOPxyb9IA/640?wx_fmt=gif "")  
  
概括  
  
Netskope 威胁实验室发现了一个利用虚假安装程序传播 Sainbox RAT 和 Hidden rootkit 的活动。在我们的威胁追踪活动中，我们发现了多个伪装成合法软件的安装程序，包括 WPS Office、搜狗和 DeepSeek。这些安装程序主要为 MSI 文件，通过钓鱼网站传播。钓鱼页面和安装程序均为中文，表明目标用户是中文使用者。根据 TTP（尤其是钓鱼网站、热门中文软件的虚假安装程序、Gh0stRAT 变种的使用以及针对中文使用者的攻击），我们可以中等程度地将此次攻击归咎于 Silver Fox（一个位于中国的恶意组织）。  
  
在这篇博文中，我们将探讨 MSI 有效载荷如何在受害者的机器中传递、加载和执行。  
  
主要发现  
- Netskope Threat Labs 发现了一项新的活动，该活动使用包括搜狗和 DeepSeek 在内的流行软件的虚假安装程序，向中文使用者发送恶意软件。  
  
- 恶意软件负载包括 Sainbox RAT、Gh0stRAT 的变种以及开源 Hidden rootkit 的变种。  
  
- 根据该活动的性质、所涉及的有效载荷以及目标用户，我们可以中等程度地将这些活动归咎于 Silver Fox 组织。  
  
细节  
  
当受害者访问钓鱼网站并从中下载虚假安装程序时，感染就开始了。以下示例展示了一个模仿WPS Office软件官方网站的网站。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacrQACC3Xuw5xIj9yoF2GT3ztfibxRbA3tok1rvcqmD9Kicaz9TkJAHRcJz7A917axJP0jIhpUdtEzg/640?wx_fmt=webp&from=appmsg "")  
  
钓鱼页面示例  
  
通过检查页面源代码，我们可以看到，当受害者点击下载按钮时，会从不同的 URL 下载文件。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tacrQACC3Xuw5xIj9yoF2GT325JiccXgEQq5O7iaePknOkViaFLnewVm0sgDRX0fWEuuZPdmCL0VlG1Vw/640?wx_fmt=png&from=appmsg "")  
  
钓鱼页面源代码片段  
  
在调查过程中，我们发现多个软件应用程序的虚假安装程序，包括搜狗、WPS Office 和 DeepSeek，它们出现在不同的假冒页面上。我们发现的大多数虚假安装程序都是 MSI 文件，只有 WPS Office 安装程序是 PE 格式。在本文中，我们将重点分析 MSI 文件。  
  
所有分析的 MSI 文件都包含几乎相同的行为，包括执行名为“Shine.exe”的合法文件，用于侧载恶意 DLL“libcef.dll”，以及执行正版安装程序软件。  
  
该恶意 DLL 是真实 libcef 库的伪造版本，该库是 Chromium 嵌入式框架 (CEF) 的一部分。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tacrQACC3Xuw5xIj9yoF2GT3icDzSRdEWEiahjSsibNoYOlsto67zfAtA79mSLQztU02DJ5y58qgJBuOw/640?wx_fmt=png&from=appmsg "")  
  
虚假安装程序操作  
  
在上述文件中，MSI 安装程序还会在同一目录中释放一个名为 1.txt 的文件。该文件包含 Shellcode 和恶意软件 Payload，稍后会加载并执行。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tacrQACC3Xuw5xIj9yoF2GT3Yw97Ep8yhT7YWQyibs0rDQhHIxe02FPUDDoyFuAO8twia54mSeZnU3BA/640?wx_fmt=png&from=appmsg "")  
  
伪造的安装程序文件  
  
执行时，MSI 文件会以常规安装程序的形式显示，并安装实际软件。同时，Shine.exe 文件也会执行，并侧载恶意 DLL。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tacrQACC3Xuw5xIj9yoF2GT3gt9x39CY1rLXIIEOIMLDW7XaajmUquzmwo9qNlA28P5jViaaVVOyLKg/640?wx_fmt=png&from=appmsg "")  
  
DeepSeek 虚假安装示例  
  
恶意 DLL 代码从名为“cef_api_hash”的导出函数开始，该函数由 Shine.exe 文件本身在执行期间调用。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tacrQACC3Xuw5xIj9yoF2GT3GuIzKrgCeN4skicWlG08CqvOR5FLycRprrK2O30q13lO5dfPyHibXEWA/640?wx_fmt=png&from=appmsg "")  
  
主要有效载荷依赖项  
  
被调用函数主要执行三个任务。首先，它将正在执行的主二进制文件（在本例中为 Shine.exe）的路径设置为名为“Management”的 Windows 注册表 Run 键，以保持其在系统中的持久性。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacrQACC3Xuw5xIj9yoF2GT3Hb4year33BSs1DTEKH5xQcfuReH6tysKmGyODP7GiahprCNfvSvz9KQ/640?wx_fmt=webp&from=appmsg "")  
  
Libcef DLL 代码片段设置运行键  
  
之后，它将“1.txt”文件的内容读入缓冲区，分配内存，并将读取的内容写入其中。最后一步是将控制流重定向到读取文件的第一个字节，也就是shellcode有效载荷的开始。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacrQACC3Xuw5xIj9yoF2GT3TXXpeA0pY305rXoUAyeRNmkkVfibPNaC7oGVSEeRgn2ysE5yiaH57ib1w/640?wx_fmt=webp&from=appmsg "")  
  
Libcef 代码片段读取 1.txt 文件并调用 shellcode  
  
在所有分析的文件中，shellcode 的大小均为 0xc04 字节。shellcode 中使用的代码基于开源sRDI工具。该工具的原理是将 DLL 反射加载到内存中，调用其 DllMain 函数，然后调用导出函数，恶意负载的操作由此开始。  
  
加载的 DLL 位于 1.txt 文件的偏移量 0xc04 处，并且其 DOS 签名（“MZ”字节）已被删除，以试图绕过取证工具。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tacrQACC3Xuw5xIj9yoF2GT3V9pTom5s4MsW7DJcsNHeQzH5GeZX2micUgqXLaD8uQh1L9lUkJOpT5A/640?wx_fmt=png&from=appmsg "")  
  
Shellcode 结尾和 RAT DLL 开头的十六进制视图  
  
在分析的样本中，DLL名称为“Install.dll”，执行的导出函数为“Shellex”。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tacrQACC3Xuw5xIj9yoF2GT3yJibWNS3hSaulhBUWOUfyAFP3rV3aYNrD4Lha25YljnicWuap76Rvq7g/640?wx_fmt=png&from=appmsg "")  
  
RAT DLL名称和导出函数  
  
在分析过程中，我们发现 DLL 有效载荷是 Sainbox RAT，它是开源 Gh0stRAT 的变体。   
  
分析的有效载荷的 .data 部分包含另一个 PE 二进制文件，该二进制文件可能根据恶意软件的配置被执行。嵌入的文件是基于开源项目Hidden的 rootkit 驱动程序。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacrQACC3Xuw5xIj9yoF2GT3lncaYadldn1Kibs4gOMcJeXTciaJG9ziacu0PlL1VRNIFvkbYpaGbdrEA/640?wx_fmt=webp&from=appmsg "")  
  
包含 rootkit 驱动程序有效载荷的 RAT .data 块  
  
该 RAT 为 rootkit 创建了一个名为“Sainbox”的服务，并使用 NtLoadDriver 函数加载它。rootkit 的主要目标是隐藏进程、文件以及注册表项和值等项目。它通过使用微过滤器和内核回调来实现这一点。它还可以保护自身和特定进程，并包含一个可通过 IOCTL 访问的用户界面。  
  
Sainbox RAT 使攻击者能够完全控制受害者的设备，从而下载并执行其他有效载荷、窃取敏感数据等。Hidden Rootkit 则提供了一定的隐身能力，可以隐藏有效载荷、保护进程免遭终止，并试图阻止安全和监控软件检测到 RAT 及其活动。  
  
结论  
  
这篇博文是攻击者利用人工智能的流行进行恶意攻击的又一例证。攻击者利用钓鱼网站作为诱饵，并将有效载荷隐藏在合法安装程序中，这种技术旨在避免引起怀疑。攻击者使用 Gh0stRAT 等商用 RAT 变种和 Hidden 等开源内核 rootkit，无需进行大量自定义开发即可实现控制和隐身。Netskope 威胁实验室将继续监测 Sainbox RAT 的演变以及 Silver Fox 组织的 TTP 策略。  
  
归因  
  
将活动归因于特定的敌对团体并非易事。敌对团体试图隐瞒其真实身份，或故意发动假旗行动，试图使其攻击看起来像是来自其他团体。多个团体通常采用相同的策略和技术，有些甚至使用完全相同的工具或共享基础设施。随着团体不断发展或成员在团体之间流动，甚至定义敌对团体也变得十分困难。因此，敌对团体归因是一个持续的过程，会随着新信息的出现和形势的变化而不断发展。  
  
Netskope 采用三个级别的归因：  
- 高置信度：该归因有来自多个来源的强有力佐证。虽然这是最高级别的置信度，但该归因仍有可能存在错误。  
  
- 中等置信度：有几条证据指向特定对手，但仍可能存在一些模糊之处。这些归因依赖于一致的 TTP、基础设施、工具和上下文。   
  
- 低置信度：一些证据表明存在特定的对手，但存在重大信息差距，或者证据可能很容易被伪造。  
  
IOCs  
  
C2 addresses  
- 45.207.12.71  
  
- 154.23.221.136  
  
- 206.119.124.126  
  
MSI files (MD5)  
- F0893BBA522061E58299C295F5838DFC  
  
- BA6A4699F59E557537BCB6463B4BA75B  
  
- BB43584E3308237BD97FB2CD483898A0  
  
- 8C6DF59659D4407FA4A07CC094F46DD5  
  
- 6442971B32BAD1F3B30306B60544FAEA  
  
- 0056D6F321A87CAF26EE800933BA4BCF  
  
- 78F0F18CDDF3D9FF82D001A2B5EAA429  
  
- C4582684928195F0EE6D2411BDF5DFAD  
  
DLL files (MD5)  
- FE56BCA80C57480CD68C43C192FCA295  
  
- C08B995F8A76F1059BA188DC862C98A2  
  
- 1B1EBDB45ED02695370227E7C897910E  
  
- 966310F10069F8443FE4D8ADF4A7BD80  
  
- 487FB061ED51046206E69B9C8F41E935  
  
- E59062D8AB72D71A9B9BA8B4152E730D  
  
1.txt files (MD5)  
- D65853C14A5652B91F154E72CD1D4979  
  
- DAD8C653F11F49DF5CCB429B3F1B65BB  
  
- AB9AB337C4F4284B1176FA65817DF5FE  
  
- A04C9630ADF4EADF3AC896BFF8D9EAD8  
  
- C12F28D8A2E5726C8125C5738D97D478  
  
  
  
感谢您抽出  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycNnFvFYVgXoExRy0gqCkqvrAghf8KPXnwQaYq77HMsjcVka7kPcBDQw/640?wx_fmt=gif "")  
  
.  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycd5KMTutPwNWA97H5MPISWXLTXp0ibK5LXCBAXX388gY0ibXhWOxoEKBA/640?wx_fmt=gif "")  
  
.  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycU99fZEhvngeeAhFOvhTibttSplYbBpeeLZGgZt41El4icmrBibojkvLNw/640?wx_fmt=gif "")  
  
来阅读本文  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWge7Mibiad1tV0iaF8zSD5gzicbxDmfZCEL7vuOevN97CwUoUM5MLeKWibWlibSMwbpJ28lVg1yj1rQflyQ/640?wx_fmt=gif "")  
  
**点它，分享点赞在看都在这里**  
  
