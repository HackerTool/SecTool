# Chos Mac安全工具集

## Created By jiexian©asuri.co





基础环境

--------

Xcode

> 请务必从AppStore安装最新版的Xcode

Python

> 需要安装python2.7.x （Mac OS X 10.11自带python 2.7.10）

Ruby

> 需要安装Ruby 2.2.0以上，2.3.0以下版本(Mac OS X 10.11自带 Ruby 2.2.2p95)

Perl

> 需要perl 5.18.x （Mac OS X10.11自带Perl 5.18.2）

PHP

> 需要php5.5.x （Mac OS X 10.11 自带php5.5.29）

JRE/JDK

> 需要安装jre1.6以上。推荐安装jdk1.8u60



基础软件

----

Hombrew/MacPorts

> Homebrew和MacPorts不兼容，二选一即可。
> 
> > Homebrew安装方法如下：
> 
> 
> 
> > MacPorts安装方法如下:
> 
> 如果在其他软件的安装或使用过程中发现缺少某些模块，请使用brew install soft 或port install soft进行安装，库文件尽量避免自编译安装。

Mac原生应用

-----

SQLDeveloper  

> Oracle官方提供的OracleDatabase管理工具

vSSH

> SSH管理工具，可以记住密码，可以使用ICloud保存连接信息

MySQLWorkbench

> Mysql官方提供的工具，用户数据库设计、管理和调试

Navicat Premium

> 商业版的数据库开发工具，支持多种数据库的远程管理，稳定性较差

Cakebrew

> 图形化的brew管理工具，便于查看哪些软件可以升级或已经过时

CoRD

> 用于远程连接Windows RDP的软件 

SnippetsLab

> 代码片段管理工具，用于记录常用的命令行、配置或代码片段，本工具集中使用的大量命令行工具将保存在SnippetsLab中

代码编辑器

> TextMate/Visual Studio Code/vim/sublime或其他
> 
> 推荐至少以上一种编辑器

端口扫描器

> nmap/Zenamp/Angry IP Scanner等，至少选择一款扫描器

mysql

> 部分安全工具需要使用mysql进行数据存储，建议使用mysql官方提供的pkg安装包进行安装

postgresql

> metasploit、beef等工具需要使用

逆向工具

-------

JD-GUI

> 用于反编译java程序的工具

Hopper Disassembler

> 用于静态反编译的工具

0xED

> 短小精悍的十六进制编辑器

安全工具

-----

metasploit-framework

> 全球最强大的渗透测试框架，

exploit-db

> exploit-db.com中所有漏洞信息的离线版

sqlmap

> 强大的数据库注入工具，可以配合msf或其他工具进行定向攻击

lobotomy

> Android测试框架，集成了多种Android相关的安全工具

mitmproxy/BurpSuite/Proxy

> mitmproxy是python开发的代理工具，在Mac运行良好，可用于进行中间人攻击
> 
> BurpSuite是Java开发的商业测试工具，功能丰富，易于使用
> 
> Proxy是原生的Mac代理工具，功能较少，目前版本还不稳定
> 
> 以上工具，选取其中之一即可

代理工具

-----

SSH proxy/SSH tunnel

> SSH隧道代理可以使用命令行实现，图形化工具只是简化了某些操作，这两款软件服药付费

Proxifier

> 类似于Proxychain，用于多个代理并存的情况下，为不同的访问请求选择不同的路径。

安装和运行

-------

​	cd ~

​	git clone https://github.com/jiexian/SecTool.git

​	cd ~/Sectool

​	sudo ./install.sh



