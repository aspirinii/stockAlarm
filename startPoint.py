from run_systemtray import make_wintray
from send_kakao_message import send_message
from reretrieve_token import reissuance



if __name__ == '__main__':
    try:
        make_wintray()
    finally:
        reissuance()
        send_message("--Message APP STOP--")
