# Luogu-Ac-Difficulties
统计你在洛谷通过的题目难度个数，并按照难度顺序输出详细题目信息（入门难度、普及- 只统计个数不输出明细）。

**请不要滥用爬虫，以免浪费洛谷流量。若被封 IP，后果自负。**

**请正确选择您 Python 语言版本对应程序运行。Python 2 用户请使用 main.py，Python 3 用户请使用 main3.py**

## 依赖的库：
+ requests
+ bs4
+ lxml

## 使用前提：
请确保你安装了以上三个库。安装方法：在命令行输入
```batch
pip install requests
pip install bs4
pip install lxml
```

## 使用方法：在 cmd 当中运行（不建议使用 IDLE）
```batch
python main(3).py
```
然后输入要获取对象的洛谷 uid，按下 `Enter` 即可。

**注意：如果获取对象开启了完全隐私保护，此脚本无法正常工作。**

## Badges
可以配合[该项目](https://github.com/Anguei/Luogu-Difficulties-Badge-Generator)生成 badges 代码
