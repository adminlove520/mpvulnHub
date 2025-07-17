> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkzNTYwMTk4Mw==&mid=2247489665&idx=1&sn=a19a72b885344786ec7047f7cc298f20

#  Shiro反序列化全版本漏洞原理详解  
网安探索员  网安探索员   2025-07-16 12:00  
  
原文链接：  
  
https://www.cnblogs.com/Smile3306/p/18984943  
  
# 前言  
  
Shiro反序列化漏洞原理详解，主要涉及Shiro认证的一些基础概念以及为什么能够这样进行攻击。文章削弱了具体代码以及反序列化部分，主要强调很多新手宝宝看不懂(面试常考)的漏洞版本划分即利用区别等内容。因为反序列化部分其实是一个攻击大类，在利用中也只是把对应攻击链Poc进行加密，Shiro反序列化的根本我认为还是在如何能让服务器**开始**  
反序列化这一步，即伪造明文这一步。反序列化相关的Sink、找链什么的其实专门去看Java反序列化漏洞比本文好。  
# Shiro认证：  
  
用户登录时如果点击“记住密码”，会发送请求包类似下面：  

```
POST /login HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

username=admin&password=123456&rememberMe=true          //大部分网站rememberMe都在请求体
```

  
登陆成功：响应包的响应头会有  
  
Set-Cookie: rememberMe=值  
  
，里面保存  
加密的  
用户登录信息  

```
HTTP/1.1 302 Found
Location: /home
Set-Cookie: rememberMe=YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXo=; Path=/; HttpOnly
Set-Cookie: JSESSIONID=xxx; Path=/; HttpOnly
```

  
之后的会话中请求头会携带该  
加密的  
登录信息的  
Cookie  

```
GET /home HTTP/1.1
Host: example.com
Cookie: rememberMe=YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXo=; JSESSIONID=xxx
```

  
登陆失败：  

```
HTTP/1.1 302 Found
Location: /home
Set-Cookie: rememberMe=deleteMe; Path=/; HttpOnly
Set-Cookie: JSESSIONID=xxx; Path=/; HttpOnly
```

## rememberMe值的可能情况：  
<table><tbody><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">情况</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">典型值示例</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">出现场景</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">rememberMe=登录信息</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><strong><span style="color: rgb(216, 59, 100);background-color: rgb(249, 242, 244);font-size: 14px;"><span leaf="">rememberMe=YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXo=</span></span></strong></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">用户登录成功并勾选“记住我”</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">deleteMe</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><strong><span style="color: rgb(216, 59, 100);background-color: rgb(249, 242, 244);font-size: 14px;"><span leaf="">rememberMe=deleteMe</span></span></strong></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">登录失败、Cookie 无效(</span></span><span style="color: #F36208;background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">密钥错误、填充校验失败</span></span><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">)、注销、主动清除</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">空值</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><strong><span style="color: rgb(216, 59, 100);background-color: rgb(249, 242, 244);font-size: 14px;"><span leaf="">rememberMe=</span></span></strong></code></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">某些框架或浏览器的特殊处理</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">无效值</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><strong><span style="color: rgb(216, 59, 100);background-color: rgb(249, 242, 244);font-size: 14px;"><span leaf="">rememberMe=invalid</span></span></strong></code></p><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"></span><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">或乱码</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">攻击者伪造失败、Cookie 损坏</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">无此 Cookie</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">（响应头中不出现</span></span><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"></span><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><strong><span style="color: rgb(216, 59, 100);background-color: rgb(249, 242, 244);font-size: 14px;"><span leaf="">rememberMe</span></span></strong></code></p><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">）</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">用户未勾选“记住我”，或者</span></span><span style="color: #F36208;background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">解出的明文不是用户信息</span></span></p></td></tr></tbody></table>## rememberMe登录信息格式  
  
该值为  
Base64  
编码值，解开后的格式与版本有关  
<table><tbody><tr style="height: 33px;"><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">情况</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">Shiro 版本</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">IV 类型</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">密钥类型</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">Cookie 结构</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">固定IV + Ciphertext</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">&lt;=1.2.4</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">固定（全 0）</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">固定</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><strong><span style="color: rgb(216, 59, 100);background-color: rgb(249, 242, 244);font-size: 14px;"><span leaf="">IV + Ciphertext</span></span></strong></code></p></td></tr><tr style="height: 33px;"><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">随机IV + Ciphertext</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">1.2.5-1.4.1</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">随机</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">随机</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><strong><span style="color: rgb(216, 59, 100);background-color: rgb(249, 242, 244);font-size: 14px;"><span leaf="">IV + Ciphertext</span></span></strong></code></p></td></tr><tr style="height: 33px;"><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">随机IV + Ciphertext + Tag</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">&gt;=1.4.2</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">随机</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">随机</span></span></p></td><td data-colwidth="150" width="150" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><code style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;background-color: rgba(0, 0, 0, 0.06);border: 1px solid rgba(0, 0, 0, 0.08);border-radius: 2px;padding: 0px 2px;"><strong><span style="color: rgb(216, 59, 100);background-color: rgb(249, 242, 244);font-size: 14px;"><span leaf="">IV + Ciphertext + Tag</span></span></strong></code></p></td></tr></tbody></table>## 反序列化点  
  
当服务器Base64解开Cookie的rememberMe值，将利用  
Cookie里的IV  
和  
服务器内存中Key  
(启动网站进程生成)解密  
Ciphertext  
后，会得到用户登录信息的**序列化值**  
，为了读取里面的登录信息具体值，服务器会进行反序列化。  
如果攻击者可以  
自定义  
该  
序列化值  
，让服务器最终能  
反序列化  
它，就能触发  
反序列化攻击  
。**注意：因为客户端Cookie正常是由服务器的Set-Cookie发来的，所以正确的用户Cookie里的IV就是服务器内存的IV(这里是为后续爆破密钥储备知识点)**  
## 加密方式  
### Shiro<=1.2.4  
  
登录信息用AES-128-CBC(分组链接)加密  
固定IV(
```
16个0x00
```

  
)作为初始向量，固定AES密钥(
```
kPH+bIxk5D2deZiIxcaaaA==
```

  
)。**Cookie格式：**
```
Cookie：rememberMe= base64_enc(IV + Ciphertext)
```

  
  
原理：  
- **密钥Key**  
：128 位（16 字节）  
- **初始向量IV**  
：128位（16 字节）  
- **加密模式**  
：CBC（Cipher Block Chaining）  
- **填充方式**  
：PKCS5Padding  
<table><tbody><tr style="height: 33px;"><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">项目</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">长度（位）</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">是否固定</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">说明</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">分组大小</span></span></strong></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">128</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">✅</span></span><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf=""> 固定</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">AES 标准定义，</span></span><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">永远 16 字节</span></span></strong></p></td></tr><tr style="height: 33px;"><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">密钥长度</span></span></strong></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">128/192/256</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">❌</span></span><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf=""> 可变</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">分别对应 AES-128、AES-192、AES-256</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">IV 长度</span></span></strong></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">128</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">✅</span></span><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf=""> 固定</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">与分组长度一致，</span></span><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">永远是 16 字节</span></span></strong></p></td></tr></tbody></table>  
**补充：Shiro支持长度分为128、196、256三种，考虑计算量效率等问题默认为128**  
#### PKCS5Padding填充  
  
以16字节为一个分组为例，不足部分  
差几个字节  
，就全部填充为  
该数字  
的  
16进制  
  
例如最后一个  
分组块  
为
```
user
```

  
,  
4  
个字节，那么后面全部填充
```
12
```

  
的16进制
```
0x0c
```

  
，即  
12  
个
```
0x0c
```

  
  
最终结果为：75 73 65 72 0C 0C 0C 0C 0C 0C 0C 0C 0C 0C 0C 0C  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/CSyEGWNz8ksiciboIruWcAKF7vF3N2G4RqBBR5umYoZdAuErQm3tUyWafq5mibmQdxr8ygnfknFbdDjXjUTP1iavrg/640?wx_fmt=png&from=appmsg "")  
  
#### 加密过程  
  
1、将明文按16字节分组，最后一组不足16字节按PKCS5Padding规则填充  
2、提取Cookie中的初始向量，将  
初始向量  
(**正常用户为16个**
```
0x00
```

  
)与  
第一块明文  
进行  
异或  
得到一个值我们称为  
中间值  
  
3、将  
中间值  
利用内存中的  
密钥  
(该版本为
```
kPH+bIxk5D2deZiIxcaaaA==
```

  
)进行AES加密，得到  
密文1  
  
4、将  
密文1  
与  
明文2  
进行异或，得到  
中间值2  
  
5、将  
中间值2  
进行AES加密，得到  
密文2  
  
6、重复  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/CSyEGWNz8ksiciboIruWcAKF7vF3N2G4RqJXicrBVaqkESJmZibNVvJRNBw4yYt35Nv5cJI2Rg5Fj4XMjJ6Yg3MEHw/640?wx_fmt=png&from=appmsg "")  
  
### 1.2.4 < Shiro < 1.4.2  
  
登录信息用AES-128-CBC(分组链接)加密，随机IV作为初始向量，随机AES密钥**Cookie格式：**
```
Cookie：rememberMe= base64_enc(IV + Ciphertext)
```

  
  
**注意：这里的随机是指程序启动随机生成一次存储在内存中，多用户时值都一样。**  
#### 加密过程  
  
加密过程与**Shiro<=1.2.4**  
相同，只是  
初始向量  
和  
密钥  
为  
随机值  
  
1、将明文按16字节分组，最后一组不足16字节按PKCS5Padding规则填充  
2、提取Cookie中的初始向量，将  
初始向量  
(该版本为随机值)与  
第一块明文  
进行  
异或  
得到一个值我们称为  
中间值  
  
3、将  
中间值  
利用内存中的  
密钥  
(**正常用户为服务器生成的固定随机值**  
)进行AES加密，得到  
密文1  
  
4、将  
密文1  
与  
明文2  
进行异或，得到  
中间值2  
  
5、将  
中间值2  
进行AES加密，得到  
密文2  
  
6、重复  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/CSyEGWNz8ksiciboIruWcAKF7vF3N2G4RqDkxu0sMflsd8VQSImaK4awTjq7jEVsX4OvJwxicFWPhkJianNaEImDPg/640?wx_fmt=png&from=appmsg "")  
  
### Shiro >=1.4.2  
  
登录信息用AES-128-GCM加密，随机IV作为初始向量，随机AES密钥。**Cookie格式：**
```
Cookie：rememberMe= base64_enc(IV + Ciphertext+Tag)
```

  
  
注意：Shiro官方将AES-GCM作为加密算法名称，但为兼容历史系统未遵循NIST的GCM标准。  
#### 标准GCM：  
- IV ： 12字节随机值  
- key： 16字节随机值  
- 计数器块 ：IV (12B) + 0x00000001 (4B) (0x00000001开始每次自增+1)  
- 密钥流：由计数器块生成的一串密钥，保证每次加密的使用的密钥都不同  
(**作用：保证密钥流唯一性、防止重放攻击)**  
- Tag ：16 字节计算值 (AES加密 + 伽罗瓦域乘法)  
(**作用：数据完整性和来源认证)**  
##### 生成密文  
1. **密钥流生成**  
：  
- 初始化计数器：
```
CTR₀ = IV + 0x00000001
```

  
（16字节）  
- 生成密钥流块：  

```
KS₁ = AES_Encrypt(Key, CTR₀)
        KS₂ = AES_Encrypt(Key, CTR₀ + 1)
        KS₃ = AES_Encrypt(Key, CTR₀ + 2)
```

1. **加密过程**  
：  

```
C₁ = P₁ ⊕ KS₁        // 明文与密钥流异或
		C₂ = P₂ ⊕ KS₂
		C₃ = P₃ ⊕ KS₃
```

1. **最终输出**  
：  

```
密文 = IV + C₁ + C₂ + ... + Cₙ
```

##### 生成Tag（简化表示）  
  
纯密码学计算，比较复杂，以下简写  
- 
```
key
```

  
: 加密密钥  
- 
```
iv
```

  
: 初始化向量（12字节）  
- 
```
aad
```

  
: 附加认证数据（在Shiro中通常为空）  
- 
```
ciphertext
```

  
: 生成的密文  

```
tag = generate_gcm_tag(key, iv, aad, ciphertext)            # 生成16字节认证标签
```

##### 最终输出  

```
输出 = IV(12字节) + C₁ + C₂ + ... + Cₙ + Tag
```

#### Shiro_GCM：  
- IV ： 16字节随机值   
**(不同处：为了兼容历史版本-CBC模式)**  
- key： 16字节随机值  
- 密钥流：由  
JDK内部方法  
生成的一串密钥，保证每次加密的使用的密钥都不同  
(**作用：保证密钥流唯一性、防止重放攻击)**  
- Tag ：16 字节计算值 (AES加密 + 伽罗瓦域乘法)  
(**作用：数据完整性和来源认证)**  
##### 生成密文  
1. **密钥流生成**  
：  
- 初始化计数器：
```
J₀ = GHASH(IV)
```

  
（16字节，JDK内部转换）  
- 生成密钥流块：  

```
KS₁ = AES_Encrypt(Key, J₀)
        KS₂ = AES_Encrypt(Key, J₀ + 1)
        KS₃ = AES_Encrypt(Key, J₀ + 2)
```

1. **加密过程（与标准GCM相同）**  
：  
注意：  
  
若明文不足 16 字节，不会填充 0，而是直接截取密钥流的对应长度进行异或。  

```
C₁ = P₁ ⊕ KS₁             例：8 字节明文 `P` → 仅取 `KS[0:8]` 异或生成 8 字节密文
        C₂ = P₂ ⊕ KS₂
        C₃ = P₃ ⊕ KS₃
```

##### 生成Tag（简化表示）  
  
纯密码学计算，比较复杂，以下简写  
- 
```
key
```

  
: 加密密钥  
- 
```
iv
```

  
: 初始化向量（12字节）  
- 
```
aad
```

  
: 附加认证数据（在Shiro中通常为空）  
- 
```
ciphertext
```

  
: 生成的密文  

```
tag = generate_gcm_tag(key, iv, aad, ciphertext)             // 注意iv是16字节
```

##### 最终输出  

```
输出 = IV(16字节) + C₁ + C₂ + ... + Cₙ + Tag
```

#### 标准GCM vs Shiro_GCM对比  
<table><tbody><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">特性</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">标准GCM</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">Shiro实现</span></span></strong></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">IV长度</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">12字节 (96位)</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">16字节 (128位)</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">IV结构</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">8字节固定 + 4字节计数器</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">完全随机</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">计数器管理</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">会话内严格递增</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">无状态</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">初始计数器(J₀)</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">IV + 0x00000001</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">GHASH(IV)计算</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">填充</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">无填充，最后块可不足 16 字节</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">无填充，最后块可不足 16 字节</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">重放防护</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">强制计数器验证</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">无</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">输出结构</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">12B IV + 密文 + 16B Tag</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">16B IV + 密文 + 16B Tag</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">性能</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">高效（直接计数器）</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">较低（GHASH计算）</span></span></p></td></tr></tbody></table>#### Shiro_GCM缺陷  
- 无限次执行同一恶意操作（如反复创建管理员账户）  
- 绕过单次执行防护机制  
- 触发分布式拒绝服务（重复执行高消耗操作）  
# Shiro 550漏洞  
  
**版本：Shiro <=1.2.4**  
**条件：1、硬编码密钥**  
**原理：**  
- Shiro 默认使用**硬编码的 AES 密钥**  
（
```
kPH+bIxk5D2deZiIxcaaaA==
```

  
）和**IV**  
(16个0x00)来加密  

```
rememberMe
```

  
  
Cookie。  
- 攻击者可以直接使用这个默认密钥和任意IV，根据AES-128-CBC加密方式构造恶意的序列化数据，加密后发送给服务器。  
- 服务器利用  
Cookie里的任意IV  
和  
服务器内存中Key  
解密后触发反序列化，导致远程代码执行（RCE）  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/CSyEGWNz8ksiciboIruWcAKF7vF3N2G4Rq8FftIDHSQFSAoOTIaW4KtlwpC3eHE3Dic2b5fhSib667hmcoYA0ADwIg/640?wx_fmt=png&from=appmsg "")  
  
**注意：这里是****任意IV****，虽然服务器用的IV(16个0x00)来加密，但服务器解密是提取的****请求包Cookie中的IV****，而我们不是破解原Cookie，所以随便输入一个IV都可以，只是反序列化后因为不是合法用户信息，服务器不会走判断账号逻辑，而是返回空**  
# Shiro 721漏洞  
  
**版本：Shiro <=1.4.1**  
**条件：1、需要一个正确的rememberMe值(无需知道密钥)**  
  
**缺陷：可以伪造任意长度(shiro上限)明文，但爆破时间会增加n**  
  
**原理：**  
  
Padding Oracle Attack：利用服务器对  
填充校验  
结果的返回值不同，爆破出  
最后一组  
密文块的  
中间值  
，从而直接伪造出明文。该方式算是对  
AES-128-CBC  
加密算法的明文伪造(非破解)  
  
Shiro的服务器验证会校验两个东西：  
①账号密码是否正确  
，  
②填充是否正确  
  
明文分块 = 明文1+明文2+明文3  
密文分块 = 密文1+密文2+密文3  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/CSyEGWNz8ksiciboIruWcAKF7vF3N2G4RqKyHHVe1GBosLqKpHFiag1y40epJou2cMPRjvRqMHoibqbKH12aNbF5lg/640?wx_fmt=png&from=appmsg "")  
  
  
那么：  
密文1 = AES_enc(明文1 ^ IV)  
密文2 = AES_enc(明文2 ^ 密文1)  
密文3 = AES_enc(明文3 ^ 密文2)  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/CSyEGWNz8ksiciboIruWcAKF7vF3N2G4RqvrLbNz2HEvlyeaS9ApWmK1EjUfiaZxjn41C8HHFV4RShE3WR8ke4zAQ/640?wx_fmt=png&from=appmsg "")  
  
  
因为异或等式是  
任意两个  
相互  
异或  
都能得到  
第三个  
：  
AES_dec(密文3) = 密文2 ^ 明文3  
  
解密时，我们把  
AES_dec(密文3)  
  
称为  
密文3  
的  
中间值  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/CSyEGWNz8ksiciboIruWcAKF7vF3N2G4RqtpnBZQUOpUjIblCD1Os0xILqJxsfvghWAWsPzus3rTohsdPJCGF1XA/640?wx_fmt=png&from=appmsg "")  
##### 阶段一：得到中间值  
  
① 在服务器视角：  
解密流程：  
用  
密文3  
解出的  
中间值3  
与  
密文2  
异或，得到  
明文3  
，然后校验  
明文3  
填充  
是否正确  
  
那么：  
明文3  
  
=  
  
密文2  
  
异或  
  
中间值3  
  
而  
异或  
是  
一位对应一位  
的操作，可以得到：  
明文3[16]  
  
=  
  
密文2[16]  
  
异或  
  
中间值3[16]  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/CSyEGWNz8ksiciboIruWcAKF7vF3N2G4Rq6pcefmm8j1EapGofA2s0QSHGib7QGALuReoqwCnQFnf1u2YFoiawXyTA/640?wx_fmt=png&from=appmsg "")  
  
  
②同时可以利用填充校验是否正确  
服务器让  
密文2[16]  
与  
中间值3[16]  
异或，得到  
明文3[16]  
，这时服务器会校验  
明文3[16]  
是否符合  
PKCS5  
的填充规则。**爆破倒数第一位：**  
- 因为我们只控制了一位，所以要让它异或出  
0x01  
。由于密文是随便写的，肯定密码不正确，但我们不关心。只在乎填充校验是否正确。  
- 所以只要当遍历  
密文2[16]  
为某个值，服务器判断为“  
密钥正确，填充正确，非登录信息，静默处理  
”——即**无Set-Cookie或者deleteMe**  
- 那么  
有且只有一个值  
满足公式：  
0x01 =  
  
密文2[16]  
  
异或  
  
中间值3[16]  
- 然后已知  
0x01  
和  
密文2[16]  
  
，可以算出  
中间值3[16]  
的值  
- 整个过程最多需要  
256次  
爆破一个字节  

```
# 填充正确响应
HTTP/1.1 200 OK
Content-Type: text/html

# 填充错误响应
HTTP/1.1 500 Internal Server Error
Set-Cookie: rememberMe=deleteMe; Path=/; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:00 GMT

Shiro的特定行为：
    - 填充错误时，Shiro会强制设置`rememberMe=deleteMe`来清除客户端Cookie
    - 这是Shiro框架的**标准错误处理机制**
```

<table><tbody><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">场景</span><br/><br/></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">服务器响应特征</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">脚本判断逻辑</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">填充正确</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">无Set-Cookie头或内容不含deleteMe</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">返回成功</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">填充错误</span></span></strong></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">Set-Cookie头包含deleteMe</span></span></p></td><td data-colwidth="250" width="250" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">抛出异常</span></span></p></td></tr></tbody></table>  
**爆破倒数第二位：**  
  
然后我们修改  
密文2[15]  
和  
密文2[16]  
, 让他们与  
中间值3[15]  
和  
中间值3[16]  
进行两位的异或，当得到0x02 0x02时，服务器会返回“  
密钥正确，填充正确，非登录信息，静默处理  
”——即**无Set-Cookie或者deleteMe**  
，由于  
中间值3[16]  
是已知的，所以  
密文2[16]  
  
是已知的，只需要遍历  
密文2[15]  
，满足公式：  
0x02 0x02 =  
  
密文2[15]  
  
密文2[16]  
  
异或  
  
中间值3[15]  
  
中间值3[16]  
  
然后已知0x02 0x02、  
密文2[15]  
  
密文2[16]  
和  
中间值3[16]  
，可以算出  
中间值3[15]  
的值  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/CSyEGWNz8ksiciboIruWcAKF7vF3N2G4RqxG9fIvmArYMzlldPiadvWKtjEdFDOFyk4CKX3HYr7jspppm9U6MGoVQ/640?wx_fmt=png&from=appmsg "")  
  
**以此类推得到**  
最后一个密文块的中间值的每一位  
  
**同理：**  
  
我们可以  
去掉密文3  
然后  
固定密文2  
的值，也就是**让下一个要爆破的分组密文作为最后一个分组**  
然后遍历  
密文1  
的每个字节，得到  
倒数第二个密文块的中间值的每一位  
  
整个分组的  
第一个密文块  
用的异或的前一个密文块是  
初始向量  
，所以爆破中间值1就改变初始向量  
整个过程需要最多需要  
256*密文分组  
次爆破所有分组的中间值  
  
**流程总结：**  
**截断(最后一组不用)——>爆破中间值——>构造新的前一组密文，伪造明文——>截断**  
###### 误判：  
  
这种判断方式可能存在误判  
因为我们只知道服务器校验填充是否合法。假如在爆破  
中间值3[16]  
时，我只修改了  
密文2[16]  
为了找到符合以下公式的值：  
0x01 =  
  
遍历的密文2[16]  
  
异或  
  
中间值3[16]  
  
但如果运气好，此时满足  
0x02 0x02 =  
  
未遍历密文2[15]  
  
遍历的密文2[16]  
  
异或  
  
中间值3[15]  
  
中间值3[16]  
  
服务器也会返回填充正确，这样的误判直到0x0f 0x0f ... 0x0f 总共  
16种  
情况  
最终误判概率为：  
P(0x0n 误判)=(1/256)^n  
等于  
P(总误判)≈1/(256×255)=1/65280  
##### 阶段二：伪造明文  
  
**构造明文3：**  
  
因为解密时的公式：  
明文3  
  
=  
  
密文2  
  
异或  
  
中间值3  
  
现在已经通过爆破获得  
  
中间值3  
，只需要修改  
密文2  
，就能构造出想让服务器解析的  
明文3  
**构造明文2：**  
  
因为解密公式：  
明文2 = 密文1 异或 中间值2  
##### 阶段三：扩容明文分组  
  
上面描述的原理只能控制  
256(密文分组-1)个字符，对攻击来说远远不够。所以我们需要对分组进行扩容我们伪造一个密文4，无论他是否合理，服务器都会对这个分组密文进行解密，得到中间值4。由于密文4不合理，中间值4可能也不合理，但我们不关心是否合理，只需要修改密文3，通过填充校验爆破出中间值4就行这样我们就从原本的：IV+C1+C2+C3 （可控值：明文2+明文3 16
```
*
```

2=32字节）变为(扩容1组)IV+新C1+新C2+新C3+C4 （可控值：明文2+明文3+明文4 16
```
*
```

3=48字节）同理(扩容2组)IV+新C1+新C2+新C3+新C4+C5（可控值：明文2+明文3+明文4+明文5 16
```
*
```

4=64字节）理论可以扩容到shiro上限，但每扩容一个分组，增加16  
256  
次爆破  
#### 举例：  
  
假如我们原本登录成功得到一个正确Cookie:  
Set-Cookie：  
rememberMe=Base64(IV+密文)  
  
rememberMe=Base64(0x00 ... 0x00 0x01 ... 0x01 0x02 ... 0x02)  
通过分组得到：  
IV = 0x00 0x00 ... 0x00  
C1 = 0x01 0x01 ... 0x01  
C2 = 0x02 0x02 ... 0x02  
现在按扩容到C4构造：  
IV = 0x00 0x00 ... 0x00  
C1 = 0x01 0x01 ... 0x01  
C2 = 0x02 0x02 ... 0x02  
C3 = 0x03 0x03 ... 0x03 (写任意值AES都能解密)  
C4 = 0x04 0x04 ... 0x04 (写任意值AES都能解密)  
将rememberMe=Base64(IV+C1+C2+C3+C4)作为**请求头**  
发送给服务器  
服务器会先解密  
C4  
，假设得到**C4的中间值4**  
(  
攻击者未知  
)：**中间值4 = F1 F2 F3 F4 F5 F6 F7 F8 F9 FA FB FC FD FE********FF**  
##### 1、获取中间值  
  
**爆破倒数第一位**  
  
保持C4不变，首先改变C3的最后一个字节  
C3[16]  
，比如改为  
0xDD  
  
令rememberMe=Base64(00 ... 00|01 ... 01|02 ... 02|03 ...  
  
DD  
|04 ... 04)**服务器视角：**  
  
判断错误：  
让  
0xDD  
与  
中间值4[16]  
的  
0xFF  
异或(**攻击者不可视**  
)，结果得到的不是  
0x01  
，所以返回 “  
密码不正确、校验不合格  
”的相关内容(**不考虑误报**  
)，如状态码  
500  
  
(**攻击者只能看到响应信息**  
）  
判断正确：  
而当  
C3[16]  
遍历到  
  
0xFE  
  
时：  
0x01 =  
  
中间值4[16]  
  
异或  
  
0xFE  
  
服务器返回“  
密码不正确、校验合格  
”的相关内容，如状态码  
301  
，那么就得到：  
中间值4[16]  
  
= 0x01 异或  
  
0xFE  
  
= 0xFF**接着爆破倒数第二位**  
  
由于上一步算出了  
中间值4[16]  
等于  
0xFF  
，可以得到  
新C3[16]  
  
= 0x02 异或 0xFF  
= 0xFD  
那么改变  
C3[15]  
，比如改为  
0xEE  
  
令rememberMe=Base64(00 ... 00|01 ... 01|02 ... 02|03 ...  
  
EE FD  
|04 ... 04)**服务器视角：**  
  
判断错误：  
让  
0xEE  
  
0xFD  
与  
中间值4[15]  
和  
中间值4[16]  
的  
0xFE 0xFF  
异或(**攻击者不可视**  
)，结果得到的不是  
0x02 0x02  
，所以返回 “  
密码不正确、校验不合格  
”的相关内容  
判断正确：  
当  
C3[15]  
遍历到  
  
0xFC  
  
时：  
0x02 0x02 =  
  
中间值4[15]  
  
中间值4[16]  
  
异或 0xFC 0xFD  
服务器返回“  
密码不正确、校验合格  
”的相关内容，如状态码  
301  
，那么就得到：  
中间值4[15]  
  
= 0x02 异或  
  
0xFC  
  
= 0xFE  
最终得到完整的**中间值4**  
：**中间值4 = F1 F2 F3 F4 F5 F6 F7 F8 F9 FA FB FC FD FE FF**  
##### 2、伪造明文  
  
因为公式：  
明文 =  
  
C3  
  
异或  
  
中间值4  
  
而  
中间值4  
是已知的，所以公式：  
新C3 =  
  
伪造明文4  
  
异或  
  
中间值4  
  
我们伪造一个明文：
```
helloword
```

  
**步骤 1：**  
  
把“helloword”变成 16 字节明文  
伪造明文  
：
```
helloword
```

  
（9 字节）  
PKCS5Padding：再补 7 个  

```
0x07
```

  
  
明文4  
  
= 68 65 6C 6C 6F 77 6F 72 64 07 07 07 07 07 07 07**步骤 2：**  
  
计算新 C3（16 字节）  
已知：  
中间值4  
  
= F1 F2 F3 F4 F5 F6 F7 F8 F9 FA FB FC FD FE FF  
逐字节异或：  
新C3[i]  
  
=  
  
明文4[i]  
  
异或  
  
中间值4[i  
  
得到（示例值，按位计算即可）：  
新C3  
  
= 97 93 9F 9F 9A 81 9A 8E 9B F8 F8 F8 F8 F8 F8 F8  
##### 3、截断  
  
得到**新的C3**  
，现在要进行**C3位置**  
的爆破操作，  
改变C2  
，  
固定新C3  
，  
去掉C4  
  
该过程发送的Cookie值  
去掉C4  
  
原Cookie：  
IV + C1 + C2 + C3 + C4  
00 ... 00 01 ... 01 02 ... 02 03 ... 03 04 04 ... 04  
该阶段Cookie：  
IV + C1 + C2 + 新C3  
00 ... 00 01 ... 01 02 ... 02 97 93 9F 9F 9A 81 9A 8E 9B F8 F8 F8 F8 F8 F8 F8  
##### 4、重复获取中间值  
  
该阶段  
固定  
伪造出C4位置明文的  
新C3  
，遍历C2的值，去获取  
新C3  
的  
中间值  
，从而伪造C3位置的明文  
# Shiro GCM漏洞(高版本)  
  
版本：Shiro >=1.4.2  
原理：GCM不存在填充机制，所以只能用全版本通用方式——爆破密钥，详情见下一章。  
# 爆破密钥漏洞(全版本)  
  
**版本：全版本**  
**条件：密钥在爆破字典中**  
  
原理：在讨论算法中其实很清楚知道，无论AES-CBC还是AES-GCM的  
加解密算法  
都是  
公开已知  
的。而解密时需要的两个变量  
IV  
和  
Key  
，解密时服务器是使用  
Cookie中提取的IV  
，所以也就只存在一个变量  
Key  
，我们可以利用：  
1、密钥错误，服务器解密失败，返回deleteMe  
2、密钥正确，服务器解密成功，但明文不是登陆信息，静默处理，返回null**解密处理流程：**  

```
1. 请求进入 → `ShiroFilter` 读取所有 Cookie。
2. 发现 `rememberMe=...` → 调用 `AbstractRememberMeManager#getRememberedPrincipals()`。
3. 里面先做 `decrypt()`：  
    • 密钥错 → 抛异常 → catch 住 → 立即添加 `Set-Cookie: rememberMe=deleteMe` 并返回 null。  
    • 密钥对 → 解密成功 → 继续反序列化。
4. 反序列化后拿到的是一个“伪造的”或“空的” PrincipalCollection。  
    Shiro 判断“这不是合法用户” → 直接返回 null，既不再 set 任何 Cookie，也不再追加 deleteMe。
5. 请求继续走，但当前 Subject 是匿名，后续若访问受限资源会被重定向到登录页；我们做的只是普通 GET，没有受限资源，于是最终响应头里完全没有 Set-Cookie 字段。
```

  
所以关键就是我们根据对应版本加密算法，遍历密钥伪造密文，利用服务器是否返回
```
Set-Cookie: rememberMe=deleteMe
```

  
  
字段，从而爆破出密钥。  
  
这也是为什么工具中会出现对应的  
GCM选项  
，因为加密方式完全不同  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/CSyEGWNz8ksiciboIruWcAKF7vF3N2G4RqwpGF3CZL2Q21CiczveUUu1KDXbIia8H2NsticG7qRbRcibfibbGKtweLibyw/640?wx_fmt=png&from=appmsg "")  
  
  
比如以  
1.2.4  
版本漏洞来看，虽然是默认密钥，但本质也能走爆破流程。而1.2.4属于AES-CBC加密，就不能勾选AES-GCM。  
如果勾选了就爆破不出来  
。  
# 总结  
<table><tbody><tr style="height: 33px;"><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">漏洞</span></span></strong></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">影响版本</span></span></strong></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">漏洞成因</span></span></strong></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;background-color: rgb(238, 240, 246);"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">利用</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">Shiro550</span></span></strong></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">Shiro&lt;=1.2.4</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">硬编码固定值Key和IV(16个0x00)</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">默认值</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">Shiro721</span></span></strong></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">Shiro &lt;=1.4.1</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">利用服务器对填充校验爆破末尾分组的中间值，从而伪造明文</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">爆破中间值</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><strong><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">Shiro_GCM版本</span></span></strong></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">&gt;=1.4.2</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">如果爆破出密钥Key，可以根据算法伪造密文(rememberMe=)</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">爆破密钥</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">爆破密钥</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">全版本</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">如果爆破出密钥Key，可以根据版本所对应算法伪造密文(rememberMe=)</span></span></p></td><td data-colwidth="187" width="187" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;text-align: left;"><span style="color: rgb(34, 34, 34);background-color: rgba(255, 255, 255, 0.9);font-size: 14px;"><span leaf="">爆破密钥</span></span></p></td></tr></tbody></table># 后续注意事项  
  
1、如今高版本开发Cookie传递的参数是自定义的，而不是常见的rememberMe，需要注意。  
##   
  
##   
  
  
  
  
  
  
  
