import requests
import json
import pandas as pd


class LarkBotMsg:
    def __init__(self, url):
        self.url = url

    def txt_msg(self, txt, at_all=False):
        headers = {'Content-Type': 'application/json'}
        text = txt
        if at_all is True:
            text = txt + '\n<at user_id="all">所有人</at>'
        data = {
            "msg_type": "text",
            "content": {
                "text": text
            }
        }
        data = json.dumps(data)
        res = requests.post(url=self.url, data=data, headers=headers)
        res_text = res.text
        print(res_text)

    def md_msg(self, title, md, at_all=False):
        headers = {'Content-Type': 'application/json'}
        md_txt = md
        if at_all is True:
            md_txt = md + '\n<at id=all></at>'
        data = {
            "msg_type": "interactive",
            "card": {
                "elements": [{
                    "tag": "div",
                    "text": {
                        "content": md_txt,
                        "tag": "lark_md"
                    }
                }],
                "header": {
                    "title": {
                        "content": title,
                        "tag": "plain_text"
                    }
                }
            }
        }
        data = json.dumps(data)
        res = requests.post(url=self.url, data=data, headers=headers)
        res_text = res.text
        print(res_text)

    def __card_msg(self, title, data_frame):
        """
        将pandas的data-frame转换为飞书消息卡片的函数
        """
        col_info = []
        for col_name in data_frame.columns:
            col_value = "\n".join([str(i) for i in data_frame[col_name]])
            col_temp = {
                "tag": "column",
                "width": "auto",
                "elements": [{"tag": "markdown", "content": f"**{col_name}**\n" + col_value}]
            }
            col_info.append(col_temp)

        card_info = {
            "elements": [
                {
                    "tag": "markdown",
                    "content": title
                },
                {
                    "tag": "column_set",
                    "flex_mode": "none",
                    "background_style": "default",
                    "horizontal_spacing": "default",
                    "columns": col_info
                }]
        }
        return card_info

    def table_msg(self, title, data_frame, at_all=False):
        """
        发送table的消息卡片信息
        """
        if at_all is True:
            title = title + '\n<at id=all></at>'
        _card_info = self.__card_msg(title, data_frame)
        card = json.dumps(_card_info)
        headers = {"Content-Type": "application/json"}
        body = json.dumps({"msg_type": "interactive", "card": card})
        res = requests.post(url=self.url, data=body, headers=headers)
        res_text = res.text
        print(res_text)


if __name__ == '__main__':
    t = 'test, 这个是石伟的测试消息'
    data_frame = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 5], "col3": [4, 5, 5]})
