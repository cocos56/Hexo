---
title: Win10转换为政府版并激活400年的使用期限
categories: 资源分享
date: 2019-09-22 21:26
---
[TOC]

# 1. 按
本程序通过导入证书来转换1703+的Windows 10系统为Enterprise G，并且转换也是可逆的，例如原来是企业版，想要用回去企业版可以直接导入企业版的key即可，企业G有两个好处，一个是就是400年的kms宽限期，还有就是无法升级版本，对于不想让Windows更新升级的同学来说也方便，并且也能随时转换回去。

# 2. 下载方式
* [城通网盘](https://sn9.us/dir/13403389-34658217-ee6e79)
* [OneDrive网盘](https://www.cnblogs.com/coco56/p/11223189.html)
本工具在**大型软件/操作系统/激活工具**那里
![](https://img-blog.csdnimg.cn/20190703220203163.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NPQ081Ng==,size_16,color_FFFFFF,t_70)
* [蓝奏云](https://www.lanzous.com/b644737) 密码:`b4z4`


# 3. 使用方式
* 双击如图所示的cmd脚本以运行它。
![](https://img-blog.csdnimg.cn/20190703221614786.png)
* 最好右键单击然后选择以管理员身份运行，否则没法更换密钥，也就是说你之前用其他密钥激活过Windows，转成安装政府版的密钥需要把你之前的密钥删了，删除密钥是需要管理员权限的。如果不以管理员身份运行，则无法删除之前的密钥，进而导致没法安装政府版的密钥，因而也就没法转换成政府版的。
![](https://img-blog.csdnimg.cn/20190703223308405.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NPQ081Ng==,size_16,color_FFFFFF,t_70)
* 另外最好把文件放在桌面进行操作，我放在就G盘操作失败，放在桌面就成功了。
![](https://img-blog.csdnimg.cn/20190703224546886.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NPQ081Ng==,size_16,color_FFFFFF,t_70)
* 成功之后如下所示：
![](https://img-blog.csdnimg.cn/20190703224525204.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NPQ081Ng==,size_16,color_FFFFFF,t_70)
* 在设置里也可以看到版本为企业版G，即政府版，G是Government的意思。
![](https://img-blog.csdnimg.cn/20190703224834806.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NPQ081Ng==,size_16,color_FFFFFF,t_70)
* 双击运行里面的查看激活时长脚本可以查看激活到期时间。
![](https://img-blog.csdnimg.cn/20190704074601798.png)
* 400年可以把电脑当传家宝了。
![](https://img-blog.csdnimg.cn/20190704074547170.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NPQ081Ng==,size_16,color_FFFFFF,t_70)

# 4. 其他说明
* 逆转换回去企业版示例：
`slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43`
* 专业版
`slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX`
* 其他版本参考：https://docs.microsoft.com/zh-cn/windows-server/get-started/kmsclientkeys