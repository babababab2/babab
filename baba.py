import time
import keyboard

# 3 saniye bekler
time.sleep(3)

# 50 kere "ss" yazıp Enter'a basar
for _ in range(50):
    keyboard.write("ss")
    keyboard.press_and_release("enter")
    time.sleep(0.1)  # Yazıların düzgün çıkması için kısa bir gecikme ekledim
