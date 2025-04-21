import requests
import threading 
from colorama import Fore 

webhook = input('Discord server webhook :')
num_thread = int(input('Number of times to send the message :'))
message = input('Message You Wanna spam :')
def send_request():
    try:
        r = requests.post(webhook , json={
            'content': message
        })
        if r.status_code == 204:
            print(Fore.GREEN + '[SUCCESS] Message Sent !' + Fore.WHITE)
        elif r.status_code == 429:
            print(Fore.RED + '[FAILED] Rate Limit !' + Fore.WHITE)
    except Exception as e:
        print(Fore.RED + f'[ERROR] {e}' + Fore.WHITE)
for x in range(num_thread):
    threading.Thread(target=send_request).start()
