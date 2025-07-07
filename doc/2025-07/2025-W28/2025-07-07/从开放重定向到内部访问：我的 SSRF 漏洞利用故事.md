> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkwOTE5MDY5NA==&mid=2247506926&idx=1&sn=20eed566beba200c7dd2651d3bca29b0

#  从开放重定向到内部访问：我的 SSRF 漏洞利用故事  
haidragon  安全狗的自我修养   2025-07-07 04:06  
  
# 官网：http://securitytech.cc/  
  
  
  
你好呀，  
  
我是 Pratik Dabhi，一名漏洞赏金猎人和渗透测试员。你们中的许多人可能已经认识我，但对于那些不认识我的人，请访问我的网站了解更多关于我的信息。  
  
在这篇博文中，我将分享我去年在一家跨国公司网站上发现的一个有趣的漏洞。该漏洞的核心在于我如何通过将其与第三方域名上的开放重定向漏洞相结合来绕过 SSRF 防护。正如我最近的博客文章中所述，我一直在详细介绍在侦察阶段发现的漏洞。同样，在这个案例中，我也是在侦察阶段发现了这个漏洞。  
# 什么是 SSRF？  
  
服务器端请求伪造 (SSRF) 是一种漏洞，攻击者可以诱骗服务器向攻击者通常无法访问的内部或外部系统发送 HTTP 请求。  
  
这可能导致：  
- 访问仅内部服务（例如数据库、管理面板）  
- 扫描内部网络并发现开放端口  
- 从云元数据服务中检索敏感数据  
- 绕过 IP 限制或防火墙  
公司通常会尝试通过阻止对特定主机名（
```
localhost
```

例如私有 IP 地址范围）的请求来防范 SSRF。但正如您所见，巧妙的漏洞链式攻击有时可以绕过这些防御措施。  
# 错误摘要  
  
目标正在运行以下服务：  

```
https://thumbnail.example.com/?url= <external_url>
```

  
该服务从外部 URL 获取图像以生成在其平台上显示的缩略图。  
  
他们有保护机制，阻止直接访问内部资源。例如，如果我尝试：  

```
https://thumbnail.example.com/?url=http://localhost:443
```

  
...服务器响应了如下错误消息：  
  
错误：localhost 被禁止。目前为止，一切看起来都很安全。  
# 开放重定向的发现  
  

```
blip.bizrate.com
```

在进行侦察时，我遇到了一个具有有趣端点的第三方域：  

```
https://blip.example.com/flip?u=https://evil.com
```

  
当我在浏览器中打开此 URL 时，它**会直接重定向到****https://evil.com** ，没有任何验证或限制。  
  
因此，确认
```
blip.example.com
```

端点容易受到通过参数进行的**开放重定向的**
```
u
```

攻击。  
# 将开放重定向链接到SSRF  
  
好戏就从这里开始了。我想：  
  
**如果我无法直接请求本地主机，那么如果我通过受信任的域进行重定向会怎样？**  
  
因此，我没有直接攻击
```
localhost
```

，而是制作了这个有效载荷：  

```
https://thumbnail.example.com/?url=https://blip.example.com/flip?u=http://localhost:80
```

  
以下是幕后发生的事情：  
  
1. thumbnail.example.com 获取了初始 URL：https://blip.example.com/flip? u=http://localhost:80  
  
2. blip.bizrate.com 的服务器发出 HTTP 302 重定向至：http://localhost:80 。  
  
3. thumbnail.example.com 按照重定向尝试连接到http://localhost:80 。  
  
**这就是尽管采取了保护措施，SSRF 仍然被触发的原因。**  
# 确认SSRF  
  
当我测试我精心设计的 URL 时，服务器响应如下：  
  
dial tcp   
127.0  
.  
0  
.  
1  
:  
80  
:   
connect  
: connection refused  

```


```

  
这清楚地表明服务器**尝试连接到 localhost**。由于在我的测试期间没有任何东西监听该端口，因此连接被拒绝。  
  
为了扫描其他端口，我只需更改有效载荷中的端口号：  

```
https://thumbnail.example.com/?url=https://blip.example.com/flip?u=http://localhost:443
```

  
如果该端口上有服务正在运行，我会收到不同的错误消息，甚至可能收到包含敏感数据的缩略图响应。  
  
通过这种方法，我可以执行内部端口扫描，并可能与未公开的服务进行交互。  
# 此漏洞为何发生  
  
该漏洞的存在是因为：  
- 开发人员正确地阻止了对内部主机的直接请求。  
- 然而，他们**信任外部域**并盲目遵循重定向。  
开放重定向允许我从受信任的外部域开始并最终到达内部资源 - 完全绕过保护逻辑。  
# 影响  
  
**严重程度：**中等  
  
利用此 SSRF 漏洞，攻击者可以：  
- 扫描内部服务并发现开放端口。  
- 访问内部端点，如管理面板或数据库。  
- 尝试利用内部服务上的其他漏洞。  
- 可能访问云元数据服务（例如 AWS、GCP、Azure），这可能会泄露敏感凭据。  
# 减轻  
  
解决此类问题的方法如下：  
  
✅**严格的允许列表**限制缩略图服务仅从受信任的域（例如
```
*.example.com
```

）获取图像。  
  
✅**验证最终目标：**检查URL 重定向后的**最终解析 IP 地址。阻止对内部 IP 地址范围或本地主机的请求。**  
  
✅**避免开放重定向**第三方服务应
```
blip.example.com
```

通过验证允许的目的地或实施严格的允许列表来修复开放重定向。  
## 利用这个漏洞，我能够赚到很多钱，我会向你们展示我的一些报告。  
  
  
   
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERGsKF9Uib4hYNxdVEdTJT3OTNDe44DiaCbEIJkbFfAbnibQnKVeTfOT90FJCesfxe74FDmDOGcdH1k9Q/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp "")  
  
-   
- 公众号:安全狗的自我修养  
  
- vx:2207344074  
  
- http://  
gitee.com/haidragon  
  
- http://  
github.com/haidragon  
  
- bilibili:haidragonx  
  
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
-   
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
****  
  
  
