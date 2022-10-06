import pyautogui
import time
'''
COLOQUE AS POSIÇÕES NECESSÁRIAS PARA O BOT FUNCIONAR
x, y = pyautogui.position() 
print(x,y)
'''
#ABA ZAPZAP
pyautogui.moveTo(947,12)
pyautogui.click()
time.sleep(2)

#BARRA DE BUSCA
pyautogui.moveTo(103, 153)
pyautogui.click()
time.sleep(2)

#NOME DO GRUPO, (NÃO PRECISA SER COMPLETO)
pyautogui.typewrite('')
time.sleep(4)
pyautogui.moveTo(216,288)
pyautogui.click()
time.sleep(2)

#MENSAGEM 1
pyautogui.typewrite('')
pyautogui.press('enter')
time.sleep(5)

#LOOP DE ENVIOS
for i in range(0,100):
    pyautogui.typewrite('')
    pyautogui.press('enter')
