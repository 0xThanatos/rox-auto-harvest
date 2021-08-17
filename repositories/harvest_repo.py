import config
from repositories import func_repo


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
    print("[SYSTEM]: Set limit to " + str(config.LIMIT))
    config.HOLD = False
    config.COUNT = 0
    config.LOOP = config.LIMIT


def set_cooldown():
    # เปลี่ยนสถานะเป็นรอ
    config.HOLD = True
    try:
        config.COOLDOWN = int(
            input("\n[default is 5]\nEnter number of cooldown: ") or "5")
    except ValueError:
        print("Invalid number, set to 5 seconds.")
        config.COOLDOWN = 5
    # เริ่มนับใหม่
    print("[SYSTEM]: Set cooldown to " + str(config.COOLDOWN))
    config.HOLD = False
    config.COUNT = 0


def harvest():
    # Click to start harvest
    func_repo.mouse_left_click(
        config.HARVEST_BTN_CENTER_X, config.HARVEST_BTN_CENTER_Y)
    config.COUNT += 1
    if config.LOOP > 0:
        config.LOOP -= 1
    # เข้าสู่สถานะรอเก็บเกี่ยว
    print("[SYSTEM]: Harvesting...")
    config.IS_HARVESTING = True
    config.LAST_CLICK_TIME = config.CURRENT_TIME
