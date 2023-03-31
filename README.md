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
from larkBot.lark_group_bot import LarkBotMsg

url = "机器人url"
title = "标题"
content = "内容"
w = LarkBotMsg(url) # 初始化
w.txt_msg(content, at_all=True)
w.md_msg(title, content, at_all=True)


```
