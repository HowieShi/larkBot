# 说明：
飞书app群机器人发消息，新增发送pandas数据框的数据

# 安装：

## 安装方式一：
```
git clone https://github.com/HowieShi/larkBot.git
cd larkBot
python setup.py install
```

## 安装方式二：
```
pip install git+https://github.com/HowieShi/larkBot.git
```

# 使用：
* 创建机器人的时候，选择关键词，文本和标题中要包含关键词。
<img width="630" alt="image" src="https://user-images.githubusercontent.com/25098399/229023350-8ccfb38d-443e-4676-954c-42b4a82bf8a0.png">


```python
from lark_group_bot.lark_bot_msg import LarkBotMsg

url = "webhook 地址"
title = "标题"
content = "内容"
w = LarkBotMsg(url) # 初始化
w.txt_msg(content, at_all=True) # 发送文本消息
w.md_msg(title, content, at_all=True) # 发送markdown消息
w.table_msg(title, data_frame, at_all=True) # 发送pandas数据框消息
```
