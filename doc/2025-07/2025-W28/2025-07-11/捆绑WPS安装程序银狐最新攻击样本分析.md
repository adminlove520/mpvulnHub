> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247492702&idx=1&sn=89ac40ba21680028bcdd90f498558299

#  捆绑WPS安装程序银狐最新攻击样本分析  
原创 pandazhengzheng  安全分析与研究   2025-07-10 00:30  
  
**安全分析与研究**  
  
  
专注于全球恶意软件的分析与研究  
  
前言概述  
  
安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。  
  
  
  
  
最近几年银狐类黑产团伙非常活跃，今年这些黑产团伙会更加活跃，而且仍然会不断的更新自己的攻击样本，采用各种免杀方式，逃避安全厂商的检测，此前大部分银狐黑产团伙使用各种修改版的Gh0st远控作为其攻击武器，远程控制受害者主机之后，进行相关的网络犯罪活动。  
  
  
除了银狐黑产团伙以外，还有一些其他黑产团伙也非常活跃，例如黑猫、GanbRun、暗蚊、金相狐、FaCai、DragonRank、夜枭等黑产团伙。  
  
  
今年银狐攻击活动非常频繁，基本上每天都有新的Loader变种出现，免杀方式多种多样，同时今年还有很多银狐攻击样本通过使用正常的数字签名来逃避安全厂商的检测，增肥技术也是银狐木马今年最常使用的免杀技术之一，通过将恶意样本体积增加到100M以上来逃避安全厂商的静态扫描。  
  
  
近日笔者又捕获到一例捆绑WPS安装程序银狐最新攻击样本，对该攻击样本进行了相关分析，文未提供该攻击样本的完整威胁情报。  
  
  
