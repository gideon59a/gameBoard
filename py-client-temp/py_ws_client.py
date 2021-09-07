# ref: https://pypi.org/project/websocket-client/
# Note that the are some links to test per https://www.youtube.com/watch?v=Xpc-pPA55GM :
#    wss://ws-postman.eu-gb.mybluemix.net/ws/echo
#    wss://ws-postman.eu-gb.mybluemix.net/ws/iot
#    wss://chatroom-pm-ws.herokuapp.com


import websocket  # Must also pip install websocket-client
import _thread
import time

def on_message(ws, message):
    print(f'message: {message}')

def on_error(ws, error):
    print(f'error: {error}')

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    _thread.start_new_thread(run, ())

def test_AmazonS3_websocket_conn():
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    aa = ws.run_forever()
    return aa


if __name__ == "__main__":
    websocket.enableTrace(True)
    aa = test_AmazonS3_websocket_conn()
    print(f'aa: {type(aa)} {aa}')
