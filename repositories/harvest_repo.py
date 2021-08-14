import cv2
import pyautogui

import config


def set_cooldown():
    # ปิดจอแสดงผล
    cv2.destroyAllWindows()
    # เปลี่ยนสถานะเป็นรอ
    config.HOLD = True
    try:
        config.COOLDOWN = int(
            input("\nNumber of cooldown harvest\n(default = 3): ") or "3")
    except ValueError:
        print("Invalid number, set to unlimit.")
        config.COOLDOWN = 3
    # เริ่มนับใหม่
    config.COUNT = 0
    print("[SYSTEM] Running...\n")


def action_click():
    print("[EVENT] Mouse left click!")
    config.LAST_CLICK_TIME = config.CURRENT_TIME
    pyautogui.click(config.CENTER_X, config.CENTER_Y)


def harvest():
    print('Gotcha!')
    action_click()
    config.COUNT += 1
    if config.LOOP > 0:
        config.LOOP -= 1
    # เข้าสู่สถานะรอเก็บเกี่ยว
    config.IS_HARVESTING = False
