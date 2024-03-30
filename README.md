# 关于github仓库的建立
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## 注册github账号

- 略

## 创建仓库

- 在github上找到New repository(新仓库)并点击
- Repository name: 仓库名称（输入名字，最好不要使用中文）
- Description(可选): 仓库描述介绍
- Public, Private : 仓库权限（公开共享，私有或指定合作者）
- Initialize this repository with a README: 添加一个README.md
- gitignore: 不需要进行版本管理的仓库类型，对应生成文件.gitignore
- license: 证书类型，对应生成文件LICENSE
- 最后点击Create Repository

## 本地操作
- 在本地创建新文件夹
- 进入文件夹，右击鼠标找到Git Bash Here
- 输入命令git clone url （注意这里的url是指项目在网页上的url）
- 执行完后本地会出现一个新的文件夹（名字为github1上的仓库名字）
- 在终端上继续执行cd 新文件夹名
- 然后依次执行
```
git init
git add .（这里有一个.不可以忘记）
git commit -m "first commit"（-m后必须有一个参数，可酌情修改）
git pus
```


# 建立仓库可能出现的问题

- git SSL certificate problem: unable to get local issuer certificate
该问题是由于没有配置信任的服务器HTTPS验证。默认，cURL被设为不信任任何CAs，就是说，它不信任任何服务器验证。
解决方案为执行以下命令
```
git config --global http.sslVerify false
```
- OpenSSL SSL_read: Connection was reset, errno 10054或Failed to connect to github.com port 443: Timed out
该问题是因为git在拉取或者提交项目时，中间会有git的http和https代理，但是我们本地环境本身就有SSL协议了，所以取消git的https代理即可，不行再取消http的代理。
解决方案为执行以下命令
```
//取消http代理
git config --global --unset http.proxy
//取消https代理 
git config --global --unset https.proxy
```
- fatal: destination path ‘.‘ already exists and is not an empty directory.
该问题是因为目录已经存在了.git工程
最好的方案是新建一个文件夹再走一遍流程

- git commit时出现fatal: unable to auto-detect email address (got '******@.(none)')
这是由于没有配置用户名和邮箱的原因
解决方案为
```
git config --global user.email "daming17@163.com"
git config --global user.name "daming-Z"
```