# 将成绩导入南京医科大学教务系统用脚本

## 安装方法
1. [安装 python](https://www.python.org)，注意安装 `pip`，注意添加 `pip` 到系统环境变量。

2. 使用 pip 安装 pandas
   打开终端（命令提示符/powershell），输入`pip install -r requirements.txt`

## 使用方法
1. 运行 extract.py，根据提示输入信息
2. 将 `paste_me_in_browser_console.js` 文件第 8 行 `data = {}` 中的 `{}` 替换为 extract.py 生成的文件内容
3. 打开浏览器控制台（通常按 F12 快捷键）
4. 将该文件复制粘贴至脚本最下方输入栏，回车。
