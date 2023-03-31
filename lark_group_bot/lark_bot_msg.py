import requests
import json


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


if __name__ == '__main__':
    t = 'test, 这个是石伟的测试消息'
