import config

import cv2
import numpy as np
import psutil
import ctypes
import random
from PIL import Image


def set_harvest_btn_bounding():
    config.HARVEST_BTN_BOUNDING_BOX = {
        'left': int(config.EMULATOR_X + (round(random.uniform(57, 59), 2) * int(config.EMULATOR_WIDTH)) / 100),
        'top': int(config.EMULATOR_Y + (round(random.uniform(35, 38), 2) * int(config.EMULATOR_HEIGHT)) / 100),
        'width': 100,
        'height': 100
    }
    config.HARVEST_BTN_CENTER_X = config.HARVEST_BTN_BOUNDING_BOX["left"] + (
        config.HARVEST_BTN_BOUNDING_BOX["width"] / 2)
    config.HARVEST_BTN_CENTER_Y = config.HARVEST_BTN_BOUNDING_BOX["top"] + (
        config.HARVEST_BTN_BOUNDING_BOX["height"] / 2)


def crop_question_quiz_screenshot(sct):
    config.QUESTION_QUIZ_BOUNDING_BOX = {
        'left': int(config.EMULATOR_X + (41 * int(config.EMULATOR_WIDTH)) / 100),
        'top': int(config.EMULATOR_Y + (49.75 * int(config.EMULATOR_HEIGHT)) / 100),
        'width': 200,
        'height': 30
    }
    config.QUESTION_QUIZ_CENTER_X = config.QUESTION_QUIZ_BOUNDING_BOX["left"] + (
        config.QUESTION_QUIZ_BOUNDING_BOX["width"] / 2)
    config.QUESTION_QUIZ_CENTER_Y = config.QUESTION_QUIZ_BOUNDING_BOX["top"] + (
        config.QUESTION_QUIZ_BOUNDING_BOX["height"] / 2)
    # Question image processing
    sct.get_pixels(config.QUESTION_QUIZ_BOUNDING_BOX)
    config.FRAME_QUESTION_TEXT = Image.frombytes(
        'RGB', (sct.width, sct.height), sct.image)
    config.FRAME_QUESTION_TEXT = cv2.cvtColor(
        np.array(config.FRAME_QUESTION_TEXT), cv2.COLOR_BGR2RGB)
    # Get local maximum:
    kernelSize = 5
    maxKernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (kernelSize, kernelSize)
    )
    localMax = cv2.morphologyEx(
        config.FRAME_QUESTION_TEXT, cv2.MORPH_CLOSE, maxKernel, None, None, 1, cv2.BORDER_REFLECT101
    )
    # Perform gain division
    gainDivision = np.where(
        localMax == 0, 0, (config.FRAME_QUESTION_TEXT/localMax)
    )
    # Clip the values to [0,255]
    gainDivision = np.clip((255 * gainDivision), 0, 255)
    # Convert the mat type from float to uint8:
    gainDivision = gainDivision.astype("uint8")
    # Convert RGB to grayscale:
    grayscaleImage = cv2.cvtColor(gainDivision, cv2.COLOR_BGR2GRAY)
    # Get binary image via Otsu:
    _, config.FRAME_QUESTION_TEXT = cv2.threshold(
        grayscaleImage, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # Flood fill (white + black):
    cv2.floodFill(config.FRAME_QUESTION_TEXT, mask=None, seedPoint=(
        int(0), int(0)), newVal=(255))
    # Invert image so target blobs are colored in white:
    config.FRAME_QUESTION_TEXT = 255 - config.FRAME_QUESTION_TEXT


def set_question_answer_bounding():
    config.QUESTION_ANS_BOUNDING_BOX = {
        'left': int(config.EMULATOR_X + (41 * int(config.EMULATOR_WIDTH)) / 100),
        'top': int(config.EMULATOR_Y + (55.5 * int(config.EMULATOR_HEIGHT)) / 100),
        'width': 200,
        'height': 30
    }
    config.QUESTION_ANS_CENTER_X = config.QUESTION_ANS_BOUNDING_BOX["left"] + (
        config.QUESTION_ANS_BOUNDING_BOX["width"] / 2)
    config.QUESTION_ANS_CENTER_Y = config.QUESTION_ANS_BOUNDING_BOX["top"] + (
        config.QUESTION_ANS_BOUNDING_BOX["height"] / 2)


def set_question_btn_bounding():
    config.QUESTION_BTN_BOUNDING_BOX = {
        'left': int(config.EMULATOR_X + (41 * int(config.EMULATOR_WIDTH)) / 100),
        'top': int(config.EMULATOR_Y + (68.65 * int(config.EMULATOR_HEIGHT)) / 100),
        'width': 200,
        'height': 30
    }
    config.QUESTION_BTN_CENTER_X = config.QUESTION_BTN_BOUNDING_BOX["left"] + (
        config.QUESTION_BTN_BOUNDING_BOX["width"] / 2)
    config.QUESTION_BTN_CENTER_Y = config.QUESTION_BTN_BOUNDING_BOX["top"] + (
        config.QUESTION_BTN_BOUNDING_BOX["height"] / 2)


def render_question_box_bounding():
    # Harvest button
    cv2.rectangle(config.FRAME_EMULATOR,
                  (config.HARVEST_BTN_BOUNDING_BOX["left"],
                   config.HARVEST_BTN_BOUNDING_BOX["top"]),
                  (config.HARVEST_BTN_BOUNDING_BOX["left"] + config.HARVEST_BTN_BOUNDING_BOX["width"],
                   config.HARVEST_BTN_BOUNDING_BOX["top"] + config.HARVEST_BTN_BOUNDING_BOX["height"]),
                  (255, 255, 255), 1)  # BGR
    # Quiz text
    cv2.rectangle(config.FRAME_EMULATOR,
                  (config.QUESTION_QUIZ_BOUNDING_BOX["left"],
                   config.QUESTION_QUIZ_BOUNDING_BOX["top"]),
                  (config.QUESTION_QUIZ_BOUNDING_BOX["left"] + config.QUESTION_QUIZ_BOUNDING_BOX["width"],
                   config.QUESTION_QUIZ_BOUNDING_BOX["top"] + config.QUESTION_QUIZ_BOUNDING_BOX["height"]),
                  (0, 255, 255), 1)
    # Quiz answer input
    cv2.rectangle(config.FRAME_EMULATOR,
                  (config.QUESTION_ANS_BOUNDING_BOX["left"],
                   config.QUESTION_ANS_BOUNDING_BOX["top"]),
                  (config.QUESTION_ANS_BOUNDING_BOX["left"] + config.QUESTION_ANS_BOUNDING_BOX["width"],
                   config.QUESTION_ANS_BOUNDING_BOX["top"] + config.QUESTION_ANS_BOUNDING_BOX["height"]),
                  (0, 255, 0), 1)
    # Quiz confirm button
    cv2.rectangle(config.FRAME_EMULATOR,
                  (config.QUESTION_BTN_BOUNDING_BOX["left"],
                   config.QUESTION_BTN_BOUNDING_BOX["top"]),
                  (config.QUESTION_BTN_BOUNDING_BOX["left"] + config.QUESTION_BTN_BOUNDING_BOX["width"],
                   config.QUESTION_BTN_BOUNDING_BOX["top"] + config.QUESTION_BTN_BOUNDING_BOX["height"]),
                  (255, 0, 0), 1)


def render_numpad_position():
    # Numpad 1
    cv2.circle(config.FRAME_EMULATOR,
               (config.NUMPAD_BTN_1_CENTER_X, config.NUMPAD_BTN_1_CENTER_Y),
               20,
               (255, 255, 255), thickness=1, lineType=8, shift=0)
    # Numpad 2
    cv2.circle(config.FRAME_EMULATOR,
               (config.NUMPAD_BTN_2_CENTER_X, config.NUMPAD_BTN_2_CENTER_Y),
               20,
               (255, 255, 255), thickness=1, lineType=8, shift=0)
    # Numpad 3
    cv2.circle(config.FRAME_EMULATOR,
               (config.NUMPAD_BTN_3_CENTER_X, config.NUMPAD_BTN_3_CENTER_Y),
               20,
               (255, 255, 255), thickness=1, lineType=8, shift=0)
    # Numpad 4
    cv2.circle(config.FRAME_EMULATOR,
               (config.NUMPAD_BTN_4_CENTER_X, config.NUMPAD_BTN_4_CENTER_Y),
               20,
               (255, 255, 255), thickness=1, lineType=8, shift=0)
    # Numpad 5
    cv2.circle(config.FRAME_EMULATOR,
               (config.NUMPAD_BTN_5_CENTER_X, config.NUMPAD_BTN_5_CENTER_Y),
               20,
               (255, 255, 255), thickness=1, lineType=8, shift=0)
    # Numpad 6
    cv2.circle(config.FRAME_EMULATOR,
               (config.NUMPAD_BTN_6_CENTER_X, config.NUMPAD_BTN_6_CENTER_Y),
               20,
               (255, 255, 255), thickness=1, lineType=8, shift=0)
    # Numpad 7
    cv2.circle(config.FRAME_EMULATOR,
               (config.NUMPAD_BTN_7_CENTER_X, config.NUMPAD_BTN_7_CENTER_Y),
               20,
               (255, 255, 255), thickness=1, lineType=8, shift=0)
    # Numpad 8
    cv2.circle(config.FRAME_EMULATOR,
               (config.NUMPAD_BTN_8_CENTER_X, config.NUMPAD_BTN_8_CENTER_Y),
               20,
               (255, 255, 255), thickness=1, lineType=8, shift=0)
    # Numpad 9
    cv2.circle(config.FRAME_EMULATOR,
               (config.NUMPAD_BTN_9_CENTER_X, config.NUMPAD_BTN_9_CENTER_Y),
               20,
               (255, 255, 255), thickness=1, lineType=8, shift=0)
    # Numpad 0
    cv2.circle(config.FRAME_EMULATOR,
               (config.NUMPAD_BTN_0_CENTER_X, config.NUMPAD_BTN_0_CENTER_Y),
               20,
               (255, 255, 255), thickness=1, lineType=8, shift=0)
    # Numpad OK
    cv2.circle(config.FRAME_EMULATOR,
               (config.NUMPAD_BTN_OK_CENTER_X, config.NUMPAD_BTN_OK_CENTER_Y),
               20,
               (255, 255, 255), thickness=1, lineType=8, shift=0)


def show():
    # Initialize
    python_process = psutil.Process(config.PID)
    memoryUse = str("{:.2f}".format(
        python_process.memory_info().rss / 1024 ** 2))
    # Set title
    config.FULL_TITLE = config.TITLE
    config.FULL_TITLE += " - Status: " + \
        str("Harvest" if not config.HOLD else "Stop")
    config.FULL_TITLE += ", Limit: " + \
        str("No" if config.COOLDOWN == -1 else config.LIMIT)
    config.FULL_TITLE += ", Cooldown: " + str(config.COOLDOWN)
    config.FULL_TITLE += ", Count: " + str(config.COUNT)
    config.FULL_TITLE += " | MemoryUse: " + memoryUse + " MB"
    ctypes.windll.kernel32.SetConsoleTitleW(config.FULL_TITLE)

    # # Show bounding box
    # render_question_box_bounding()
    # # Show numpad postions
    # render_numpad_position()
