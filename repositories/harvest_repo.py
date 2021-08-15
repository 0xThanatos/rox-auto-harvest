import config


def set_limit():
    # เปลี่ยนสถานะเป็นรอ
    config.HOLD = True
    try:
        config.LIMIT = int(
            input("\n[Unlimit is -1]\nEnter number of limit: ") or "-1")
    except ValueError:
        print("Invalid number, set to unlimit.")
        config.LIMIT = -1
    # เริ่มนับใหม่
    config.COUNT = 0


def set_cooldown():
    # เปลี่ยนสถานะเป็นรอ
    config.HOLD = True
    try:
        config.COOLDOWN = int(
            input("\n[default is 3]\nEnter number of cooldown: ") or "3")
    except ValueError:
        print("Invalid number, set to 3 seconds.")
        config.COOLDOWN = 3
    # เริ่มนับใหม่
    config.COUNT = 0


def mouse_left_click(x, y):
    pyautogui.click(x, y)


def harvest():
    print('Gotcha!')
    mouse_left_click()
    config.COUNT += 1
    if config.LOOP > 0:
        config.LOOP -= 1
    # เข้าสู่สถานะรอเก็บเกี่ยว
    config.IS_HARVESTING = False
