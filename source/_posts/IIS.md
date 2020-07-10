---
layout: '[post]'
title: 我的IIS（Internet Information Services）服务器
top: 1
categories: 资源分享
date: 2020-07-10 19:30:24
tags:
---

# 1. 按

微软出品，对流媒体支持更好，很多浏览器都能够在线播放使用IIS分享的视频文件。

# 2. IPv6协议

## 2.1. IPv6介绍

* [如何查看本机是否支持IPv6？：https://coco56.blog.csdn.net/article/details/103248395](https://coco56.blog.csdn.net/article/details/103248395)
一般普通手机卡的**流量**都支持IPv6上网（物联卡除外），电脑的话需要去网络连接那里看一下**IPv6连接**是否处于连通状态。
![图片若无法正常查看，请联系zj175@139.com](https://img-blog.csdnimg.cn/20200203182510793.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9jb2NvNTYuYmxvZy5jc2RuLm5ldA==,size_16,color_FFFFFF,t_70)

* 如需将家用宽带升级到支持IPv6，请参考：[个人或小微企业网络从IPv4升级到IPv6/v4硬件配置及注意事项](https://coco56.blog.csdn.net/article/details/105417342)

## 2.2. IPv6服务器

* [http://1.coco56.top:82/](http://1.coco56.top:82/)
解析的是一号机的IPv6地址，全世界范围内都可访问，40Mbps的带宽。
* [http://7.coco56.top:82/](http://7.coco56.top:82/)
解析的是五号机的IPv6地址，全世界范围内都可访问，60Mbps的带宽。

# 3. IPv4协议

## 3.1. 公网地址

<!-- 穿透内网的服务器已挂，推荐使用IPv6 -->
* [http://sz.coco56.top:16029](http://sz.coco56.top:16029)，专业穿透内网的服务器集群，速度较快，保底5MbPS
* [http://sz2.coco56.top:10726](http://sz2.coco56.top:10726)，专业穿透内网的服务器集群，速度较快，保底5MbPS
  对流媒体支持更好，使用很多浏览器都支持在线播放视频。

## 3.2. 局域网地址

以下为局域网的IPv4地址，只有连接同一个路由器或者在同一网段下才能访问，并非全世界的所有机器都能访问。

* [http://s.coco56.top:82/](http://s.coco56.top:82/)
解析的电脑的校园网IP，连接校园网后应该都可以用，如果不能用请访问下面路由器的域名，40Mbps的带宽
* [http://r.coco56.top:82/](http://r.coco56.top:82/)
解析的是路由器的校园网IP，连接校园网后应该都可以用，40Mbps的带宽
* [http://st.coco56.top:82/](http://st.coco56.top:82/)
50Mbps的带宽，科技楼的机子应该都能用