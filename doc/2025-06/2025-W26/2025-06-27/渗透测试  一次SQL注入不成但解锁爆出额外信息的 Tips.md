> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkwMzQyMTg5OA==&mid=2247488004&idx=1&sn=970f049279962698f02c1be4862e9dcc

#  渗透测试 | 一次SQL注入不成但解锁爆出额外信息的 Tips  
原创 Heihu577  Heihu Share   2025-06-26 16:00  
  
# 一次SQL注入不成但解锁爆出额外信息的 Tips  
  
- 前言  
- 基本介绍  
- 获取到数据库用户名步骤  
- 本地 MySQL 分析  
- 查看当前用户权限  
- 爆出库名【任意用户都可以】  
- Ending...  
## 前言  
  
一次渗透测试项目中朋友甩过来的疑似SQL注入点, 当时并没有注入成功, 并已经感觉几乎是没有概率造成 SQL 注入的. 随后第二天朋友通过一些手段拿到了数据库用户名称. 下面来看一下原因~  
## 基本介绍  
  
先来一个脱敏的报告吧, 来描述一下大致场景:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCsVAstYdHkZa9vhNLV44hGIYWWVnbjnODSlTcd2783g9Fic6tLK1nyu3Q/640?wx_fmt=png&from=appmsg "")  
  
这边通过单引号爆出语法错误, 那么按理来说是存在注入的, 并且通过字段名与直觉可以感觉到这是一个基于 ORDER BY 的注入, ORDER BY 注入我会啊, 只要 ORDER BY 一个不存在的列名就好了, 就能看出来是不是注入:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCstegrBicFDjuNibics21Lh3vQLNpp8SBF8Euh6nibOke8vjmtDmS8eXvHtA/640?wx_fmt=png&from=appmsg "")  
  
WTF？不应该啊, 为什么不会报错呢？正常情况应该这样:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCsoRgqQBqjVrXJDaeiciajhFIug4vIcZUWzPQuzGRqUj9GTGm2Dv0lpWpQ/640?wx_fmt=png&from=appmsg "")  
  
后来简单尝试了几下基于 ORDER BY 的 Payload 就没再看这个点了, 一方面不知道代码和SQL是怎么写的, 另一方面爆出来的错误有点模糊, 感觉很奇怪.  
## 获取到数据库用户名步骤  
  
再后来就听朋友说获取到了数据库名称？我有点不信, 步骤如下:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCsiawdFpOjlk26Ac6K92XNxYT5PicdwVIiaqDDLDbdiapr8zGfgicJmcmz4icg/640?wx_fmt=png&from=appmsg "")  
  
payload 中, 输入了
```
数字 + 字母
```

  
, 得到了
```
Unknown column
```

  
的错误, 这就有戏, 随后下面的 payload 如:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCsbLZ4ePhSVpiaicVf9IXibhsYHqdIWes9ibpFSicuBC7ES1JHo5jad9b44lQ/640?wx_fmt=png&from=appmsg "")  
  
就能够获得到用户名？到现在我还是有点晕, 为什么会这样...  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCs0a6J9yL63QlG5JibTQGepzXvFDgIswbtzCf6bgdCxf5BB79RIMFAKGw/640?wx_fmt=png&from=appmsg "")  
## 本地 MySQL 分析  
  
对于思考为什么
```
ORDER BY + 任意列名
```

  
都不会报错, 这里想到的是可能后端将其转为了字符串, 所以导致每次 ORDER BY 了一个常量, 并不会对排序进行发生实质性的改变:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCs1jKQTM2HvuxLvtucIUZhc7CHZnPcMI9qAEhu0hIicLkR0ics3icZr9v0A/640?wx_fmt=png&from=appmsg "")  
  
不过针对于这种情况, 后续可以通过往列名后面依次增加单引号来进行判断是否存在注入, 如下:  

```
package com.heihu577;

import java.sql.*;

public class MySQLConnectorTest {
    public static void main(String[] args) throws Exception {
        Connection connection =
                DriverManager.getConnection(&#34;jdbc:mysql://127.0.0.1:3306/docker_database?useSSL=false&useUnicode=true&characterEncoding=UTF-8&#34;, &#34;root&#34;, &#34;root&#34;);
        String sql = &#34;SELECT * FROM user ORDER BY 'hacker''&#34;;
        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery(sql);
    }
}

```

  
一个单引号, 打乱了SQL顺序, 包报错:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCsXqM0HLz4v5eK7wYr3D66EOsAtibjHSrv1xBCZQgDlfRkKt0icPNdu7oA/640?wx_fmt=png&from=appmsg "")  
  
两个单引号可正常发送数据:  

```
package com.heihu577;

import java.sql.*;

public class MySQLConnectorTest {
    public static void main(String[] args) throws Exception {
        Connection connection =
                DriverManager.getConnection(&#34;jdbc:mysql://127.0.0.1:3306/docker_database?useSSL=false&useUnicode=true&characterEncoding=UTF-8&#34;, &#34;root&#34;, &#34;root&#34;);
        String sql = &#34;SELECT * FROM user ORDER BY 'hacker'''&#34;;
        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery(sql);
        while (resultSet.next()) {
            System.out.println(resultSet.getString(&#34;user&#34;));
            /**
             * admin
             * guest
             */
        }
    }
}

```

  
为什么
```
数字 + 字母
```

  
前面会增加
```
r.
```

  
, 
```
r.
```

  
通常是 SQL 语句中的别名, 如下:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCsibM73hC1JCCtpH4PWoptu6hvv1UFe8MaqQarw50SYFmt2KPadA2niaGg/640?wx_fmt=png&from=appmsg "")  
  
可能是开发者调试某些数据的原因, 做了这么一个判断与转换. 那么接下来看一下之前抛出的异常:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCs9OutNmyelgl10owcPstzicDr8iaEhbRfNhDiaCS9ubuu2eW8C5au03oaw/640?wx_fmt=png&from=appmsg "")  
  
去搜了一下, 发现这篇文章: https://wenku.csdn.net/answer/4xfnmxod5k  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCsD2qAM97zKZJxnGx9Q5KtAhE9DTUdCRTKibIsksSwA04L999iaicTTMiaMg/640?wx_fmt=png&from=appmsg "")  
  
所以这边是触发了函数调用导致的, 当一个用户不存在某些函数的具体权限的话, 则会抛出异常信息, 将用户名带出来, 为了验证这个说法, 先在本地创建一个普通用户:  

```
mysql> create user 'heihu577'@'%' identified by 'heihu577';
Query OK, 0 rows affected (0.00 sec)

mysql> grant all privileges on docker_database.* to 'heihu577'@'%' identified by 'heihu577' with grant option;
Query OK, 0 rows affected, 1 warning (0.00 sec)

```

  
并且给予这个用户
```
docker_database
```

  
这个数据库下的操作权限, 首先是正常的函数调用:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCsKP3xN3YSQVsQznnhoaicqqhqibYJias7iaO4G3C5cf7U2ibowa0m2gKduSw/640?wx_fmt=png&from=appmsg "")  
  
看起来其实没什么大问题, 不过怎么样将用户名暴露出来呢？  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCs4UkE29YArj6vANfpJPgo0gdmiaksHxKHol1gY1vdVc73wtachWBozKw/640?wx_fmt=png&from=appmsg "")  
  
由于当前
```
heihu577
```

  
这个用户只存在
```
docker_database
```

  
下的权限, 当调用
```
abcdefg.1()
```

  
时会发生歧义, 误以为会去
```
abcdefg中调用函数
```

  
:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCskIMNnVlQeOAiczL6uiadz7F8HeuZcZIRV9O989j0HGpyz1KSjOMmLoIA/640?wx_fmt=png&from=appmsg "")  
### 查看当前用户权限  
  
除了可以爆出用户名以外, 也可以用来判断当前用户的权限, 如果是 root 这种权限比较大的用户, 如图:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCs6ISC0zDvPbQGvYHtGrWsqT6uZHeh3nzjd6q1vMibcoDb4RwJicdjVSlg/640?wx_fmt=png&from=appmsg "")  
  
会爆出函数不存在, 如果是普通用户 (或权限较小的用户), 会爆出具体的用户名:  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCsrM8JJ4ZIHhSGosk4yWtgzt8tGmkvMmhRGnKbKzyQxI56E7wlkZHY2A/640?wx_fmt=png&from=appmsg "")  
### 爆出库名【任意用户都可以】  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tiaKRx8m4Wn6uT0Y9G3mhXadKvVPGSmCsUTHZdp01jS1wztwc0VkQSicGhdjrSwDzgnzndtHg1SeicXf6KYe1QvXw/640?wx_fmt=png&from=appmsg "")  
## Ending...  
  
  
  
