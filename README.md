# 微信公众号安全漏洞文章归档

[![GitHub Actions](https://github.com/adminlove520/mpVulnHub/actions/workflows/update_today.yml/badge.svg)](https://github.com/adminlove520/mpVulnHub/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)


## ✨ 项目功能

自动抓取微信公众号安全漏洞文章，转换为Markdown格式并建立本地知识库，每日持续更新。

## 📰 数据来源

数据来自以下渠道的公众号文章：
- [chainreactors/picker](https://github.com/chainreactors/picker) 每日归档
- [BruceFeIix/picker](https://github.com/BruceFeIix/picker) 每日归档
- [Doonsec](https://doonsec.com) RSS订阅源
- 从GitHub Issues中提取的公众号链接
- [yarb](https://github.com/Vu1nT0tal/yarb) RSS订阅源

## 🔍 内容筛选规则

系统会自动识别包含以下关键词的文章：
复现|漏洞|信息泄漏|威胁情报|注入|XSS|内网|域控|安全运营|漏洞运营|情报运营|SRC|应急响应|APT|银狐|勒索病毒|CWE-\d+|CVE-\d+|CNVD-\d+|CNNVD-\d+|XVE-\d+|QVD-\d+|POC|EXP|0day|1day|nday|RCE|代码执行|命令执行

## 🛠️ 技术实现

- 使用 [wechatmp2markdown](https://github.com/fengxxc/wechatmp2markdown) 将公众号文章转为Markdown格式
- 智能处理特殊字符，生成合规文件名
- 按年月分类存储：`doc/yy-mm/week_dir/daily_dir`
- 通过`data.json`记录已处理链接，避免重复

## ⚙️ 使用方法

### 自动运行
- GitHub Actions 每1小时自动执行

### 手动运行
```bash
# 抓取当日新文章
python run.py today

# 抓取历史文章（更改脚本后使用）
python run_history.py history
