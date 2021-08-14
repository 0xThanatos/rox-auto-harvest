# -*- coding: utf-8 -*-
import os
import ctypes
from threading import Thread
import time
import numpy as np
import cv2
from mss import mss
from win32api import GetSystemMetrics

import config
from repositories import harvest_repo
from repositories import render_repo

config.PID = os.getpid()
config.SCREEN_WIDTH = int(GetSystemMetrics(0))
config.SCREEN_HEIGHT = int(GetSystemMetrics(1))

sct = mss()
ctypes.windll.kernel32.SetConsoleTitleW(config.TITLE)
# Clear console
os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print(config.TITLE)
print("Made by Thanapat Maliphan. (fb.com/thanatos1995)\n")

print("Screen resolution")
print("width = ", config.SCREEN_WIDTH)
print("height = ", config.SCREEN_HEIGHT)

print("\nPress 'R' button to reset limit.")
print("Press 'H' button to toggle harvest.")
print("Press 'Q' button to exit program.\n")


def main_function():
    while True:
        # ดักปุ่มกด
        key = cv2.waitKey(25)
        # Press "R" button to Reset
        if key & 0xFF == ord('r'):
            harvest_repo.set_cooldown()()
        # Press "H" button to Hold
        if key & 0xFF == ord('h'):
            config.HOLD ^= True
        # Press "Q" button to exit program
        if key & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        # เวลาปัจจุบัน
        config.CURRENT_TIME = time.time()

        # Crop harvest btn
        render_repo.crop_harvest_btn_screenshot(sct=sct)
        render_repo.crop_question_box_screenshot(sct=sct)

        # แปลงสีภาพ
        config.FRAME_HARVEST_BTN = cv2.cvtColor(
            np.array(config.FRAME_HARVEST_BTN), cv2.COLOR_BGR2RGB)
        hsv_frame = cv2.cvtColor(config.FRAME_HARVEST_BTN, cv2.COLOR_BGR2HSV)

        # Render window
        render_repo.show()

        # ระยะเวลาที่ห่างจากการคลิกครั้งล่าสุด
        last_click_sec = config.CURRENT_TIME - config.LAST_CLICK_TIME

        # Process
        if not config.HOLD and config.IS_HARVESTING and last_click_sec > config.COOLDOWN:  # รอ Cooldown เพื่อกดใหม่
            harvest_repo.harvest()


if __name__ == "__main__":
    harvest_repo.set_cooldown()
    thread = Thread(target=main_function)
    thread.start()
    thread.join()
