> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzU5MjgwMDg1Mg==&mid=2247485814&idx=1&sn=acfd188c5b16ac14d54620d554ba829f

#  数百款 Brother 打印机型号存在无法修补的漏洞 | 来看看你们公司的打印机有中招的吗？  
原创 NightTeam  夜组OSINT   2025-07-01 00:01  
  
数百款 Brother 打印机型号被发现存在严重安全漏洞，**攻击者可利用这些漏洞远程访问仍在使用默认密码的设备。安全公司 Rapid7 在 689 款 Brother 家用和企业打印机中发现了八个新漏洞，其中一个无法通过修补固件来修复。**  
  
![Brother](https://mmbiz.qpic.cn/sz_mmbiz_png/GLyX5CgG8A3w9xxficibQuOiaiba0UMmTwSwVGzFPgGc8VOFK8CF2icA0HwAW8E1xsZX8avjDEicSLFMfbzRPzfpLa3Q/640?wx_fmt=png&from=appmsg "")  
  
Brother  
  
这些漏洞还影响了富士、东芝、理光和柯尼卡美能达的 59 款打印机型号，但并非所有打印机型号都存在这些漏洞。  
## 受影响的打印机型号  
  
**如果您拥有 Brother 打印机，可以访问一下URL查看您的打印机型号是否受到影响。**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/GLyX5CgG8A3w9xxficibQuOiaiba0UMmTwSwEBUOkKSOPJlUk7OCqcvkO44oFxYfsjGyiatyOKS49Wh9484ZUBNF9rg/640?wx_fmt=png&from=appmsg "")  

```
https://support.brother.com/g/s/id/security/CVE-2017-9765.pdf

```

  
**最严重的安全漏洞在国家漏洞数据库中被标记为 CVE-2024-51978，CVSS 评级为 9.8 的“严重”级别。如果攻击者知道目标打印机的序列号，该漏洞可允许他们生成设备的默认管理员密码。这使得攻击者能够利用 Rapid7 发现的其他七个漏洞，包括检索敏感信息、导致设备崩溃、打开 TCP 连接、执行任意 HTTP 请求以及泄露已连接网络服务的密码。**  

```
https://nvd.nist.gov/vuln/detail/CVE-2024-51978

```

  
![NVD](https://mmbiz.qpic.cn/sz_mmbiz_png/GLyX5CgG8A3w9xxficibQuOiaiba0UMmTwSwD3pibZuBhLOogqoLoqlTy57TQbNvBzRZdeAyhLX7Tiaxk8tibn3NfEPNQ/640?wx_fmt=png&from=appmsg "")  
  
NVD  

```
https://www.cve.org/CVERecord?id=CVE-2024-51978

```

  
![CVE](https://mmbiz.qpic.cn/sz_mmbiz_png/GLyX5CgG8A3w9xxficibQuOiaiba0UMmTwSwibj2ibmNzDue5pKdMHVPqRGicickECz5tBaC7mLRjC2VtmqE0J9uEibyTAA/640?wx_fmt=png&from=appmsg "")  
  
CVE  
  
虽然其中七个安全漏洞可以通过Rapid7 报告中详述的固件更新进行修复，但 Brother 向公司表示，CVE-2024-51978 本身“无法通过固件完全修复”，将通过改进受影响打印机型号未来版本的制造工艺来修复。对于当前型号，Brother 建议用户通过设备的 Web 管理菜单更改打印机的默认管理员密码。  
## 安全建议  
  
买了新设备首先应该更改默认制造密码。  
  
