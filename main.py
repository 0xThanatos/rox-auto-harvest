# -*- coding: utf-8 -*-
import config
from repositories import harvest_repo
from repositories import question_repo
from repositories import render_repo
from repositories import func_repo

import os
import sys
import ctypes
import time
import cv2
import numpy as np
from threading import Thread
from mss import mss
from pynput import keyboard

config.PID = os.getpid()
sct = mss()


def main_function():
    while config.IS_RUNNING:
        # เวลาปัจจุบัน
        config.CURRENT_TIME = time.time()

        # Reset when reaching the limit
        if config.COUNT - config.LIMIT == 0:
            harvest_repo.set_limit()

            # Get emulator areas
        func_repo.get_emulator_area(sct=sct)

        # Process screenshort
        render_repo.set_harvest_btn_bounding()
        render_repo.crop_question_quiz_screenshot(sct=sct)
        render_repo.set_question_answer_bounding()
        render_repo.set_question_btn_bounding()

        # Process
        last_click_sec = config.CURRENT_TIME - config.LAST_CLICK_TIME
        if not config.HOLD:
            if config.LOOP != 0:
                if not config.IS_HARVESTING:  # รอ Cooldown เพื่อกดใหม่
                    if last_click_sec > config.COOLDOWN:
                        harvest_repo.harvest()
                else:
                    # Check quiz
                    if not config.IS_QUIZ:
                        question_repo.get_quiz()

        # Show interface
        render_repo.show()

        # # Resize
        # scale_percent = 40  # percent of original size
        # width = int(config.FRAME_EMULATOR.shape[1] * scale_percent / 100)
        # height = int(config.FRAME_EMULATOR.shape[0] * scale_percent / 100)
        # resized = cv2.resize(config.FRAME_EMULATOR, (width, height))
        # # Render frame
        # cv2.imshow(
        #     config.TITLE,
        #     np.hstack([
        #         resized,
        #         # config.FRAME_QUESTION_TEXT
        #     ])
        # )
    # Thread terminate
    sys.exit(0)


if __name__ == "__main__":
    # Set title
    ctypes.windll.kernel32.SetConsoleTitleW(config.TITLE)
    print(config.TITLE)
    print("Made by Thanapat Maliphan. (fb.com/thanatos1995)\n")

    # pre-process
    func_repo.select_emulator()
    harvest_repo.set_limit()
    harvest_repo.set_cooldown()

    # Wait for ready
    input("\nPress Enter to start harvest...")
    config.HOLD = False
    config.LAST_CLICK_TIME = time.time() - config.COOLDOWN

    # Show menu function
    func_repo.mainmenu()

    # Create thread
    thread1 = Thread(target=main_function)
    thread2 = keyboard.Listener(on_press=func_repo.on_press)
    # Start thread
    thread1.start()
    thread2.start()  # start to listen on a separate thread
    # Thread terminate
    thread1.join()
    thread2.join()  # remove if main thread is polling self.keys

    # Exit program
    sys.exit(0)
