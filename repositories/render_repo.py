import psutil
import ctypes
import cv2
import numpy as np
from PIL import Image

import config


def tracking_info(curTime):
    # Initialize FPS variables
    sec = curTime - config.PREV_TIME
    config.PREV_TIME = curTime
    fps = 1 / sec
    count_str = "%d time" % config.COUNT
    fps_str = "FPS: %0.1f" % fps
    # Right side
    cv2.rectangle(config.FRAME, (config.BOUNDING_BOX['width'] - (
        65 if not config.HOLD else 40), config.BOUNDING_BOX['width'] - 15), (config.BOUNDING_BOX['width'] - (
            30 if not config.HOLD else 40) + 70, config.BOUNDING_BOX['height']), (0, 255, 0) if not config.HOLD else (0, 0, 255), -1)
    cv2.putText(config.FRAME, str("Harvest..." if not config.HOLD else "Stop"), (config.BOUNDING_BOX['width'] - (
        60 if not config.HOLD else 35), config.FRAME.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0) if not config.HOLD else (255, 255, 255), 1)
    # Left side
    cv2.putText(config.FRAME, str("Cooldown: " + str("No" if config.COOLDOWN == -1 else config.COOLDOWN)), (0,
                config.FRAME.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    cv2.putText(config.FRAME, str("Count: " + count_str), (0,
                config.FRAME.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    cv2.putText(config.FRAME, str(
        fps_str), (0, config.FRAME.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)


def render_harvest_btn_center_point():
    cv2.circle(config.FRAME_HARVEST_BTN, (0 + int(config.HARVEST_BTN_BOUNDING_BOX['width'] / 2), 0 + int(
        config.HARVEST_BTN_BOUNDING_BOX['height'] / 2)), config.HARVEST_BTN_RADIUS, (255, 255, 255), thickness=1, lineType=8, shift=0)
    cv2.rectangle(config.FRAME_HARVEST_BTN, (0 + int(config.HARVEST_BTN_BOUNDING_BOX['width'] / 2), 0 + int(config.HARVEST_BTN_BOUNDING_BOX['height'] / 2)),
                  (0 + int(config.HARVEST_BTN_BOUNDING_BOX['width'] / 2),
                   0 + int(config.HARVEST_BTN_BOUNDING_BOX['height'] / 2)),
                  (255, 255, 255), 5)


def crop_harvest_btn_screenshot(sct):
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


def crop_question_box_screenshot(sct):
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
    title = config.TITLE + " - Status: " + str("Harvest" if not config.HOLD else "Stop") + ", Cooldown: " + str(
        config.COOLDOWN) + ", Count: " + str(config.COUNT) + " | MemoryUse: " + memoryUse + " MB"
    ctypes.windll.kernel32.SetConsoleTitleW(title)

    # แสดงรายละเอียดบนจอ
    # tracking_info(config.CURRENT_TIME)

    # Harvest button center point
    render_harvest_btn_center_point()

    # Rendering
    cv2.imshow('RO:X - Auto Harvest v%s' % config.VERSION,
               np.hstack([config.FRAME_HARVEST_BTN]))
