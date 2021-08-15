# -*- coding: utf-8 -*-
import config
from repositories import harvest_repo
from repositories import render_repo
from repositories import func_repo

import os
import ctypes
import time
import cv2
import numpy as np
from PIL import Image
from threading import Thread
from mss import mss

config.PID = os.getpid()
sct = mss()


def main_function():
    while config.IS_RUNNING:
        # เวลาปัจจุบัน
        config.CURRENT_TIME = time.time()

        # Get emulator areas
        func_repo.get_emulator_area(sct=sct)

        # Process screenshort
        # thread1 = Thread(
        #     target=render_repo.crop_harvest_btn_screenshot(sct=sct))
        # thread2 = Thread(
        #     target=render_repo.crop_question_quiz_screenshot(sct=sct))
        # thread3 = Thread(
        #     target=render_repo.crop_question_answer_screenshot(sct=sct))
        # thread4 = Thread(
        #     target=render_repo.crop_question_btn_screenshot(sct=sct))
        # thread1.start()
        # thread2.start()
        # thread3.start()
        # thread4.start()
        # thread1.join()
        # thread2.join()
        # thread3.join()
        # thread4.join()

        # Process
        # if not config.HOLD and config.IS_HARVESTING and last_click_sec > config.COOLDOWN:  # รอ Cooldown เพื่อกดใหม่
        #     harvest_repo.harvest()

        # Render
        render_repo.show()


if __name__ == "__main__":
    # Set title
    ctypes.windll.kernel32.SetConsoleTitleW(config.TITLE)
    print(config.TITLE)
    print("Made by Thanapat Maliphan. (fb.com/thanatos1995)\n")

    # pre-process
    func_repo.select_emulator()
    harvest_repo.set_limit()
    harvest_repo.set_cooldown()

    # Create threads
    thread1 = Thread(target=main_function)
    thread2 = Thread(target=func_repo.mainmenu)

    # Start threads
    thread1.daemon = True
    thread1.start()
    thread2.start()

    # Thread terminates
    thread1.join()
    thread2.join()
