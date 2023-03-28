import pyautogui
import time

# COMANDOS E COORDENADAS
from comandos import *

while True:
  img = pyautogui.locateOnScreen('imagem.png', confidence=0.6)
  if img == None:
    time.sleep(sleepFixo)
    print('Imagem não encontrada')
  else:
    pyautogui.click(img)
    time.sleep(sleepFixo)
    # click1
    pyautogui.rightClick(click1,duration=0.2)
    time.sleep(sleepFixo)
    # click2
    pyautogui.click(click2,duration=0.2)
    time.sleep(sleepFixo)
    # click3
    pyautogui.click(click3,duration=0.2)
    time.sleep(sleepFixo)
    # click4
    pyautogui.click(click4,duration=0.2)
    time.sleep(sleepFixo)
    # click5
    pyautogui.rightClick(click5,duration=0.2)
    time.sleep(sleepFixo)
    # click6
    pyautogui.click(click6,duration=0.2)
    time.sleep(sleepFixo)
    pyautogui.hotkey('enter')
    time.sleep(sleepFixo)
    # click7
    pyautogui.click(click7,duration=0.2)
    time.sleep(sleepFixo)
    # click8
    pyautogui.rightClick(click8,duration=0.2)
    time.sleep(sleepFixo)
    # click9
    pyautogui.click(click9,duration=0.2)
    time.sleep(sleepFixo)
    pyautogui.hotkey('enter')
    time.sleep(sleepFixo)
    pyautogui.click(ocultaAbas,duration=0.2)
    img = None
