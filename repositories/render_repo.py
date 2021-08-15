import config

import psutil
import ctypes


def crop_harvest_btn_screenshot(sct):
    config.HARVEST_BTN_BOUNDING_BOX = {
        'left': int((56 * int(config.SCREEN_WIDTH)) / 100),
        'top': int((27.2 * int(config.SCREEN_HEIGHT)) / 100),
        'width': 200,
        'height': 200
    }
    config.HARVEST_BTN_CENTER_X = int((65.52 * int(config.SCREEN_WIDTH)) /
                                      100) + (config.HARVEST_BTN_BOUNDING_BOX["width"] / 2)
    config.HARVEST_BTN_CENTER_Y = int((30.2 * int(config.SCREEN_HEIGHT)) /
                                      100) + (config.HARVEST_BTN_BOUNDING_BOX["height"] / 2)
    # แปลงสีภาพ
    config.FRAME_HARVEST_BTN = cv2.cvtColor(
        np.array(config.FRAME_EMULATOR), cv2.COLOR_BGR2RGB)
    gray_frame = cv2.cvtColor(config.FRAME_EMULATOR, cv2.COLOR_RGB2GRAY)


def crop_question_quiz_screenshot(sct):
    config.HARVEST_BTN_BOUNDING_BOX = {
        'left': int((56 * int(config.SCREEN_WIDTH)) / 100),
        'top': int((27.2 * int(config.SCREEN_HEIGHT)) / 100),
        'width': 200,
        'height': 200
    }
    config.HARVEST_BTN_CENTER_X = int((65.52 * int(config.SCREEN_WIDTH)) /
                                      100) + (config.HARVEST_BTN_BOUNDING_BOX["width"] / 2)
    config.HARVEST_BTN_CENTER_X = int((30.2 * int(config.SCREEN_HEIGHT)) /
                                      100) + (config.HARVEST_BTN_BOUNDING_BOX["height"] / 2)
    sct.get_pixels(config.HARVEST_BTN_BOUNDING_BOX)
    config.FRAME_HARVEST_BTN = Image.frombytes(
        'RGB', (sct.width, sct.height), sct.image)


def crop_question_answer_screenshot(sct):
    config.HARVEST_BTN_BOUNDING_BOX = {
        'left': int((56 * int(config.SCREEN_WIDTH)) / 100),
        'top': int((27.2 * int(config.SCREEN_HEIGHT)) / 100),
        'width': 200,
        'height': 200
    }
    config.HARVEST_BTN_CENTER_X = int((65.52 * int(config.SCREEN_WIDTH)) /
                                      100) + (config.HARVEST_BTN_BOUNDING_BOX["width"] / 2)
    config.HARVEST_BTN_CENTER_X = int((30.2 * int(config.SCREEN_HEIGHT)) /
                                      100) + (config.HARVEST_BTN_BOUNDING_BOX["height"] / 2)


def crop_question_btn_screenshot(sct):
    config.HARVEST_BTN_BOUNDING_BOX = {
        'left': int((56 * int(config.SCREEN_WIDTH)) / 100),
        'top': int((27.2 * int(config.SCREEN_HEIGHT)) / 100),
        'width': 200,
        'height': 200
    }
    config.HARVEST_BTN_CENTER_X = int((65.52 * int(config.SCREEN_WIDTH)) /
                                      100) + (config.HARVEST_BTN_BOUNDING_BOX["width"] / 2)
    config.HARVEST_BTN_CENTER_X = int((30.2 * int(config.SCREEN_HEIGHT)) /
                                      100) + (config.HARVEST_BTN_BOUNDING_BOX["height"] / 2)
    sct.get_pixels(config.HARVEST_BTN_BOUNDING_BOX)
    config.FRAME_HARVEST_BTN = Image.frombytes(
        'RGB', (sct.width, sct.height), sct.image)


def show():
    python_process = psutil.Process(config.PID)
    memoryUse = str("{:.2f}".format(
        python_process.memory_info().rss / 1024 ** 2))
    # Set title
    title = config.TITLE
    title += " - Status: " + str("Harvest" if not config.HOLD else "Stop")
    title += ", Limit: " + \
        str("No" if config.COOLDOWN == -1 else config.COOLDOWN)
    title += ", Cooldown: " + str(config.COOLDOWN)
    title += ", Count: " + str(config.COUNT)
    title += " | MemoryUse: " + memoryUse + " MB"
    ctypes.windll.kernel32.SetConsoleTitleW(title)
