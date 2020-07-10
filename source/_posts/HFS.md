---
layout: '[post]'
title: 我的HFS（HTTP File System）服务器
top: 1
categories: 资源分享
date: 2020-01-07 22:11:50
tags:
---

[toc]

# 1. 按

该HFS为新版本的HFS2，手机访问体验较好，如果您对相关下载操作不熟悉，请先查看[使用帮助](https://coco56.blog.csdn.net/article/details/100619737)，以解决如何**下载文件或文件夹**和**在线观看视频**等常见问题。

本应用为访问本人自建云的方式之一，当然还有更多其他方式，如通过：
<!-- * 通过我分享的[OneDrive网盘高速下载链接](https://coco56.gitee.io/blog/OneDrive/)来访问我分享的文件 -->
* [我的IIS（Internet Information Services）服务器](https://coco56.gitee.io/blog/IIS/)来访问我分享的文件
* [我分享的Windows共享文件夹](https://coco56.blog.csdn.net/article/details/105914768)来更好地访问我所分享的资源
需要您的机器安装的是Windows操作系统且支持IPv6

本文地址：

1. [博客园](https://www.cnblogs.com/coco56/p/13280891.html)
2. [Gitee博客](https://coco56.gitee.io/blog/HFS/)

# 2. IPv6协议

## 2.1. 协议介绍

[如何查看本机是否支持IPv6？：https://coco56.blog.csdn.net/article/details/103248395](https://coco56.blog.csdn.net/article/details/103248395)
一般普通手机卡的**流量**都支持IPv6上网（物联卡除外），电脑的话需要去网络连接那里看一下**IPv6连接**是否处于连通状态。
![图片若无法正常查看，请联系zj175@139.com](https://img-blog.csdnimg.cn/20200203182510793.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9jb2NvNTYuYmxvZy5jc2RuLm5ldA==,size_16,color_FFFFFF,t_70)

如需将家用宽带升级到支持IPv6，请参考：[个人或小微企业网络从IPv4升级到IPv6/v4硬件配置及注意事项](https://coco56.blog.csdn.net/article/details/105417342)

## 2.2. IPv6公网服务器地址列表

* [http://1.coco56.top/](http://1.coco56.top/)
解析的是一号机的IPv6地址，全世界范围内都可访问，40Mbps的带宽。
* [http://7.coco56.top/](http://7.coco56.top/)
解析的是五号机的IPv6地址，全世界范围内都可访问，60Mbps的带宽。

# 3. IPv4协议

注意：

* 以下这几个地址虽然全世界范围内都可以访问，但时延较高，还老是宕机无法访问，因此请访问服务器的IPv6地址，以享受更大的带宽、更低的时延。
这几台公网服务器说的都是1MbPS或者5MbPS的带宽，实际速度肯能稍微快一点儿，但也绝对是无法与40Mbps的IPv6网络可以比的。
* 强烈推荐用户将尽早尽快升级到支持IPv6的宽带，否则几年后一旦IPv6 Only，你可能就只能使用手机流量上网了（目前手机流量应该都是支持IPv6的）

## 3.1. IPv4公网服务器地址列表

1. [http://6.coco56.top](http://6.coco56.top)，6号机器（最高1MbPS，阿里云的四线BGP商用宽带，较稳定，但速度极慢）
2. [http://sz.coco56.top:16028](http://sz.coco56.top:16028)，保底5MbPS，专业穿透内网的服务器集群，速度较快。
3. [http://sz2.coco56.top:10720](http://sz2.coco56.top:10720)，保底5MbPS，专业穿透内网的服务器集群，速度较快。

## 3.2. IPv4局域网服务器地址列表

以下为局域网的IPv4地址，只有和我的机器连接的是同一个路由器或者在同一网段下才能访问，并非全世界的所有机器都能访问。

* [http://s.coco56.top/](http://s.coco56.top/)
解析的电脑的校园网IP，连接校园网后应该都可以用，如果不能用请访问下面路由器的域名，40Mbps的带宽
* [http://r.coco56.top/](http://r.coco56.top/)
解析的是路由器的校园网IP，连接校园网后应该都可以用，40Mbps的带宽
* [http://st.coco56.top/](http://st.coco56.top/)
50Mbps的带宽，科技楼的机子应该都能用

# 4. 打赏&支持&联系我

收集整理资源不易，如果感到帮助到了您，请打赏、支持我，我将会为大家发布和更新更多的内容：

* 微信
![图片若无法正常查看，请联系zj175@139.com](https://i.loli.net/2019/07/06/5d20bb02a413d45586.png)
* 支付宝
![图片若无法正常查看，请联系zj175@139.com](https://i.loli.net/2019/07/06/5d20bb5b090cf90572.jpg)

[关于&联系我](https://coco56.gitee.io/blog/about)
