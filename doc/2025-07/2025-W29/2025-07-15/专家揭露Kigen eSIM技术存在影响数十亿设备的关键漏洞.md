> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzg3OTc0NDcyNQ==&mid=2247494252&idx=1&sn=276563e9f1cb87023e8012c699e3829b

#  专家揭露Kigen eSIM技术存在影响数十亿设备的关键漏洞  
鹏鹏同学  黑猫安全   2025-07-15 01:13  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/8dBEfDPEceib4aqsQibvD4Ahuqriauc28MibMACDTTm7EtUtfoVpeArauscSjJSTInYibIBdQB73lq4s2TIXUtadaiag/640?wx_fmt=png&from=appmsg "")  
  
安全研究团队Security Explorations发现一种新型攻击手段，可利用Kigen公司eSIM技术漏洞入侵数十亿物联网设备。eSIM（嵌入式SIM卡）作为传统物理SIM卡的数字化形态，直接内置于智能手机、平板、智能手表及物联网设备中，其核心eUICC（嵌入式通用集成电路卡）软件标准由GSMA制定，支持远程下载管理多运营商配置文件并实现无缝切换。  
  
研究人员成功攻破经过安全认证的Kigen eUICC芯片，证实该芯片既无法有效隔离存储的eSIM配置文件与Java Card应用，也缺乏基本防护机制。此次攻击基于2019年被Oracle驳回的Java Card研究成果，首次公开证实了以下三大领域存在可被攻破的实例：  
1. 消费级GSMA eUICC标准  
  
1. Kigen eSIM技术（该公司宣称其安全SIM操作系统支撑超20亿张SIM卡）  
  
1. 经EAL(**)认证的GSMA安全芯片（采用英飞凌32位ARM SecurCore SC300处理器）  
  
尽管攻击需物理接触设备并知晓内部密钥，但远程攻击可能性未被排除。研究团队成功从被入侵的Kigen eUICC中提取ECC私钥，彻底击穿其加密体系。2025年3月17日提交证据后，Kigen于3月20日确认漏洞存在。概念验证视频显示，攻击者既能模拟空中下载恶意应用，又可窃取芯片身份证书与私钥。  
  
该漏洞导致GSMA消费者证书失窃将引发连锁反应：攻击者能直接下载各运营商加密的eSIM配置文件，获取包含用户配置、认证密钥(OPc/AMF)等敏感数据，并可任意篡改后植入其他eUICC芯片而不被运营商察觉，从根本上动摇了eSIM安全架构的信任基础。  
  
2025年3月31日，Kigen向研究人员支付3万美元奖金并设立90天保密期。该公司披露漏洞源于GSMA TS.48通用测试配置文件(v6.0及更早版本)，该文件被广泛用于eSIM射频合规测试时可能加载未验证恶意程序。新版TS.48 v7.0已禁用测试配置功能，Kigen同步向所有客户推送了操作系统补丁。  
  
"此次攻破证明eSIM配置文件和Java应用毫无安全隔离，eUICC存储内容完全暴露。"Security Explorations在公告中强调，"虽然基于我们2019年Java Card研究，但本次突破需要开发全新攻击技术。希望促使运营商、厂商和安全机构重新审视eSIM安全风险。"  
  
  
