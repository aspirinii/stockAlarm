from datetime import datetime


def logging_log(text="text 미입력"):
    now = datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    print("/////log/////",text)

    with open("log.txt","a+") as fp:
        fp.write(f"{nowDatetime} {text}\n")
        

