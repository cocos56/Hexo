# -*- coding: UTF-8 -*-
from sync import run
import os

if __name__ == "__main__":
    print("正在生成public")
    os.system("hexo g")
    
    li=[
        (r'H:\G\Hexo\public', r'H:\G\blog.coco56.top\blog')
    ]
    
    run(li)

    cwd = os.getcwd()
    os.chdir(r"H:\G\blog.coco56.top")
    os.system("一键更新变动.bat")

    os.chdir(cwd)
    os.system("一键更新变动.bat")

    os.system("start https://blog.coco56.top/blog/")