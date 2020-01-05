# -*- coding: UTF-8 -*-
from sync import run
import os

if __name__ == "__main__":
    print("正在生成public")
    os.system("hexo g")
    
    li=[
        (r'H:\G\Hexo\public', r'H:\G\coco5666.github.io\blog')
    ]
    
    run(li)

    os.chdir(r"H:\G\coco5666.github.io")
    os.system("一键更新变动.bat")
    os.system("start https://github.coco56.top/blog/")
    input("同步已完成")