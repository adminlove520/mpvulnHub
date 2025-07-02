> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzI3NzMzNzE5Ng==&mid=2247490353&idx=1&sn=c5470fd58355538b2dbea6a82e14b61a

#  【高危漏洞预警】sudo < 1.9.17p1 host&chroot本地提权漏洞  
cexlife  飓风网络安全   2025-07-02 10:17  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu022Xg5JNJt9GHOcIKoUKSkIHoRy6AzZePh7aOROLZF5fb8u6nNcQWC4RaBvqvJkOEibhia0MUL6ibDpg/640?wx_fmt=png&from=appmsg "")  
  
Linux sudo host 权限提升漏洞(CVE-2025-32462)   
  
漏洞描述:  
  
sudo是Linux系统发行版中的系统用户权限管理工具,2025年7月,互联网上披露CVE-2025-32462 sudo < 1.9.17p1 host选项本地提权漏洞,攻击者在已经获取到本地权限的情况下,若此时/etc/sudoers定义的Host或Host_Alias过于宽松,则攻击者可结合sudo的-h（--host）选项造成权限提升以root身份执行命令。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu022Xg5JNJt9GHOcIKoUKSkIicU1rfvolIY19Jf0PuicT4LytFl8XDgVNvLW9EuiaKkRZjiaIvxqAudHBA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu022Xg5JNJt9GHOcIKoUKSkI4ajdfakXVOvWVnvoic4Hsgp7tFvKic1dSF5Ls7PMocVC59HFRnN7AN6w/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu022Xg5JNJt9GHOcIKoUKSkI0F86F5QibbngWNE1z6U8bCmI85qxjt2KKQ9QTeWZcJ3PXic9JgdFuk6w/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu022Xg5JNJt9GHOcIKoUKSkI4ng46AVdoL4tib7L3ML0vPtgPRicnL1DWYtc0fibuKJ0uAQibwG6q0pr2A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu022Xg5JNJt9GHOcIKoUKSkI4ZCZMeiasq4yeZHV8RbMIZ0Gv9vVPClicc8zH4ibib9LQEA4CG9PjOowog/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu022Xg5JNJt9GHOcIKoUKSkIFntNxQ355VTvlKmIicEvZ0br09z5Sh0iciaTsEhJu68sFibTY82bjqm3WQ/640?wx_fmt=png&from=appmsg "")  
  
利用条件：  
  
1.本地低权限用户  
  
2.存在基于主机的权限规则:/etc/sudoers中定义Host或Host_Alias  
  
3.知道允许执行命令的远程主机名  
  
sudo影响范围:  
  
1.9.0 <= sudo <= 1.9.17  
  
1.8.8 <= sudo <= 1.8.32  
  
sudo安全版本:  
  
sudo 1.9.17p1  
  
修复建议:  
  
目前官方已发布安全更新,建议用户尽快升级至最新版本:  
  
ѕudо >= 1.9.17р1  
  
官方补丁下载地址:  
  
https://www.sudo.ws/security/advisories/host_any/  
  
https://www.sudo.ws/security/advisories/chroot_bug  
  
在环境中搜索任何使用了Host或Host_Alias选项的内容,检查/etc/sudoers中定义的所有Sudo规则以及/etc/sudoers.d下的文件,如果Sudo规则存储在LDAP中,请使用ldapsearch 等工具转储这些规则。   
  
参考链接:  
  
https://www.openwall.com/lists/oss-security/2025/06/30/2  
  
  
Linux sudo chroot 权限提升漏洞(CVE-2025-32463)   
  
漏洞描述:  
  
sudo是Linux系统发行版中的系统用户权限管理工具,2025年7月,互联网上披露CVE-2025-32463 sudo < 1.9.17p1 chroot 本地提权漏洞,自2023年发布的1.9.14版本开始,sudo的chroot机制实现存在缺陷,本地用户可通过利用用户控制目录下的/etc/nsswitch.conf 文件,通过chroot加载恶意动态链接库,从而以提权执行任意代码。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu022Xg5JNJt9GHOcIKoUKSkIFr09D2OIedmcKXLG0LsLlHzLcYVJ5bZUkW8g1518jcu3KcgtkWbianQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu022Xg5JNJt9GHOcIKoUKSkIEMC5OBA6SkBOuuXN8gHHXEUmROAGXX4ibWM7fGB7cXNEyx29IdK38wg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu022Xg5JNJt9GHOcIKoUKSkIBaQstGZy6y1RAp3rCHkmMrWxAOE8ic0ExJzzo2mvYLenOibrOC8ic563g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu022Xg5JNJt9GHOcIKoUKSkIGcF8Px2FV5iaiblWZWQ7wdNXew83AjhwNDgO7cCNExzsbJanyNicdkDmA/640?wx_fmt=png&from=appmsg "")  
  
攻击场景:  
  
攻击者可能通过使用用户控制目录中的/etc/nsswitch.conf文件与--chroot选项来获得root访问权限  
  
利用条件:  
  
本地低权限用户   
  
sudo影响范围:  
  
1.9.14 <= sudo <= 1.9.17  
  
sudo安全版本:  
  
sudo 1.9.17p1  
  
修复建议:  
  
目前官方已发布安全更新,建议用户尽快升级至最新版本:  
  
ѕudо >= 1.9.17р1  
  
官方补丁下载地址:  
  
https://www.sudo.ws/security/advisories/host_any/  
  
https://www.sudo.ws/security/advisories/chroot_bug   
  
参考链接:  
  
https://www.openwall.com/lists/oss-security/2025/06/30/3  
  
  
