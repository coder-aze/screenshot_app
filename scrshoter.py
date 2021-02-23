import pyautogui  #pip install pyautogui
import time
import random
numbers=random.choices(["a","b","c","d","e","f","g","h","i"],k=6)
time.sleep(2)
screen=pyautogui.screenshot()
screen.save(str(numbers)+".png")

