# 说明：
飞书app群机器人发消息

# 安装：
```
git clone https://github.com/HowieShi/larkBot.git
cd larkBot
python setup.py install --user
```
# 使用：
```python
from lark_group_bot.lark_bot_msg import LarkBotMsg

url = "机器人url"
title = "标题"
content = "内容"
w = LarkBotMsg(url) # 初始化
w.txt_msg(content, at_all=True) # 发送文本消息
w.md_msg(title, content, at_all=True) # 发送markdown消息

```
