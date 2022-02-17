import requests
import json
from log_log import logging_log

def send_message(content):
    with open("kakao_code.json","r") as fp:
        tokens = json.load(fp)

    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # kapi.kakao.com/v2/api/talk/memo/default/send 

    headers={
        "Authorization" : "Bearer " + tokens["access_token"]
    }

    data={
        "template_object": json.dumps({
            "object_type": "text",
            "text": content,
            "link": {
                "web_url" : "https://finance.yahoo.com/quote/GOOGL?p=GOOGL",
                "mobile_web_url" : "https://finance.yahoo.com/quote/GOOG?p=GOOG",
            },
            "button_title" : content
        })
    }

    response = requests.post(url, headers=headers, data=data)
    if response.json().get('result_code') == 0:
        logging_log(f"Send message : {content}")
    else:
        logging_log('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))