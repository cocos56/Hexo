import os

print("正在生成public")
os.system("hexo g")

print("\n正在启动服务")
os.system("hexo s")