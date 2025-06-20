import os
import re
import sys
import json
import platform
import tempfile
import shutil
import subprocess
import datetime


def write_json(path, data, encoding="utf8"):
    """写入json"""
    with open(path, "w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def read_json(path, default_data={}, encoding="utf8"):
    """读取json"""
    data = {}
    if os.path.exists(path):
        try:
            data = json.loads(open(path, "r", encoding=encoding).read())
        except:
            data = default_data
            write_json(path, data, encoding=encoding)

    else:
        data = default_data
        write_json(path, data, encoding=encoding)
    return data

def get_executable_path():
    '''获取可执行文件路径'''
    system = platform.system()
    if system == 'Windows':
        executable_path = './bin/wechatmp2markdown-v1.1.11_win64.exe'
    else:
        executable_path = './bin/wechatmp2markdown-v1.1.11_linux_amd64'
    # 添加执行权限
    os.chmod(executable_path, 0o755)
    # 返回可执行文件的完整路径
    return executable_path

def get_md_path(executable_path,url):
    '''获取md文件路径'''
    temp_directory = tempfile.mkdtemp()
    command = [executable_path, url, temp_directory, '--image=url']
    subprocess.check_output(command)
    for root, _, files in os.walk(temp_directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                yield file_path

def get_chainreactors_url():
    '''获取多日url，返回URL和对应日期的元组列表'''
    # 定义日期范围
    start_date = "2022-04-07"
    end_date = "2025-04-16"
    
    # 转换为datetime对象
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    
    url_date_pairs = []
    
    # 遍历每一天
    current_date = start
    while current_date <= end:
        date_str = current_date.strftime("%Y-%m-%d")
        # 本地文件路径
        local_path = os.path.join('archive', 'daily', date_str[:4], f"{date_str}.md")
        
        try:
            if os.path.exists(local_path):
                with open(local_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                urls = re.findall('(?:复现|漏洞|CVE-\d+|CNVD-\d+|CNNVD-\d+|XVE-\d+|QVD-\d+|POC|EXP|0day|1day|nday|RCE|代码执行|命令执行).*?(https://mp.weixin.qq.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', content, re.I)
                urls = [url.rstrip(')') for url in urls]
                # 存储URL和对应的日期
                url_date_pairs.extend([(url, date_str) for url in urls])
                print(f"成功获取 {date_str} 的文章URL: {len(urls)}条")
            else:
                print(f"{date_str} 无文章或文件不存在")
        except Exception as e:
            print(f"获取 {date_str} 文章时出错: {str(e)}")
        
        # 移动到下一天
        current_date += datetime.timedelta(days=1)
    
    # 去重，保留每个URL第一次出现的日期
    seen = set()
    unique_pairs = []
    for url, date in url_date_pairs:
        if url not in seen:
            seen.add(url)
            unique_pairs.append((url, date))
    return unique_pairs

    
def rep_filename(result_path):
    ''' 
    替换不能用于文件名的字符
    '''
    for root, _, files in os.walk(result_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                new_file = re.sub(r'[\/\\\:\*\?\"\<\>\|]', '', file)
                shutil.move(os.path.join(root, file), os.path.join(root, new_file))
                
def main():
    '''主函数'''
    data_file = 'data.json'
    data = {}
    executable_path = get_executable_path()
    base_result_path = 'doc'
    os.makedirs(base_result_path, exist_ok=True)
    
    # 读取历史记录
    data = read_json(data_file, default_data=data)
    
    if len(sys.argv) == 2:
        if sys.argv[1] == 'history':
            # 获取URL和日期对
            url_date_pairs = get_chainreactors_url()
            
            for url, date_str in url_date_pairs:
                if url in data:
                    continue
                
                # 创建按月份分类的目录 (yyyy-mm)
                year_month = date_str[:7]  # 提取年月部分
                month_dir = os.path.join(base_result_path, year_month)
                os.makedirs(month_dir, exist_ok=True)
                
                for file_path in get_md_path(executable_path, url):
                    name = os.path.splitext(os.path.basename(file_path))[0]
                    if name == '.md':
                        continue
                    
                    # 移动文件到对应月份目录
                    shutil.copy2(file_path, month_dir)
                    data[url] = name  # 保持JSON数据结构不变
                    write_json(data_file, data)
                    print(f"{name} (保存到 {year_month})", end='、')
    
    # 处理文件名中的非法字符（递归处理所有子目录）
    rep_filename(base_result_path)

if __name__ == '__main__':
    main()
