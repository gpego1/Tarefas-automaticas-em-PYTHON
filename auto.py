import pyautogui as pa
import time
import pyperclip
pa.PAUSE = 1

pa.press('win')
pa.write("edge")
pa.press('ENTER')
pa.write("youtube.com")
pa.press('ENTER')
time.sleep(4)
pa.click(x=716, y=151)
pyperclip.copy("spiderman 2 gameplay")
pa.hotkey('ctrl','v')
pa.press('enter')
time.sleep(4)
pa.click(x=642, y=712)
pa.click(x=826, y=968)

