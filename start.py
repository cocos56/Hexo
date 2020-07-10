import os

print("正在生成public")
os.system("hexo g")

os.system("start http://localhost:4000")

print("\n正在启动服务")
os.system("hexo s")