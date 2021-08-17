import config
from repositories import func_repo

import re
import numpy as np
import argparse
import time
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def get_quiz():
    # Text recognition process...
    text = pytesseract.image_to_string(
        config.FRAME_QUESTION_TEXT
    )
    text = text.replace(" ", "")
    text = text.strip()
    # print("[SYSTEM]: Text = '" + text + "'")
    # Check string can solve math
    if re.match(r"[\w\s]*[\d\+\-\*\/]+[\w\s]*", text):
        config.QUESTION_QUIZ_TEXT = text.strip()
    #     config.IS_QUIZ = True
        print("[SYSTEM]: Set to quiz mode")
        print("[SYSTEM]: Question is '" + config.QUESTION_QUIZ_TEXT + "'")
        # Solve math
        get_answer()
        # Key answer process
        open_numpad()
        time.sleep(0.4)
        key_answer_to_numpad(config.QUESTION_ANS_TEXT)
        # Send confirm
        time.sleep(0.5)
        confirm_btn_click()
        time.sleep(0.5)
    else:
        if config.CURRENT_TIME > config.LAST_CLICK_TIME + config.COOLDOWN:
            config.IS_HARVESTING = False


def get_answer():
    quiz = config.QUESTION_QUIZ_TEXT.strip()
    config.QUESTION_ANS_TEXT = str(eval(quiz))
    print("[SYSTEM]: Answer = " + config.QUESTION_ANS_TEXT)


def open_numpad():
    func_repo.mouse_left_click(
        config.QUESTION_ANS_CENTER_X, config.QUESTION_ANS_CENTER_Y)
    print("[SYSTEM]: Click to answer input for open the numpad")


def set_position_of_numpad_btn():
    # Numpad 1
    config.NUMPAD_BTN_1_CENTER_X = int(
        (config.EMULATOR_X + (65 * config.EMULATOR_WIDTH) / 100))
    config.NUMPAD_BTN_1_CENTER_Y = int(
        (config.EMULATOR_Y + (58 * config.EMULATOR_HEIGHT) / 100))
    # Numpad 2
    config.NUMPAD_BTN_2_CENTER_X = int(
        (config.EMULATOR_X + (70.5 * config.EMULATOR_WIDTH) / 100))
    config.NUMPAD_BTN_2_CENTER_Y = int(
        (config.EMULATOR_Y + (58 * config.EMULATOR_HEIGHT) / 100))
    # Numpad 3
    config.NUMPAD_BTN_3_CENTER_X = int(
        (config.EMULATOR_X + (76 * config.EMULATOR_WIDTH) / 100))
    config.NUMPAD_BTN_3_CENTER_Y = int(
        (config.EMULATOR_Y + (58 * config.EMULATOR_HEIGHT) / 100))
    # Numpad 4
    config.NUMPAD_BTN_4_CENTER_X = int(
        (config.EMULATOR_X + (65 * config.EMULATOR_WIDTH) / 100))
    config.NUMPAD_BTN_4_CENTER_Y = int(
        (config.EMULATOR_Y + (68 * config.EMULATOR_HEIGHT) / 100))
    # Numpad 5
    config.NUMPAD_BTN_5_CENTER_X = int(
        (config.EMULATOR_X + (70.5 * config.EMULATOR_WIDTH) / 100))
    config.NUMPAD_BTN_5_CENTER_Y = int(
        (config.EMULATOR_Y + (68 * config.EMULATOR_HEIGHT) / 100))
    # Numpad 6
    config.NUMPAD_BTN_6_CENTER_X = int(
        (config.EMULATOR_X + (76 * config.EMULATOR_WIDTH) / 100))
    config.NUMPAD_BTN_6_CENTER_Y = int(
        (config.EMULATOR_Y + (68 * config.EMULATOR_HEIGHT) / 100))
    # Numpad 7
    config.NUMPAD_BTN_7_CENTER_X = int(
        (config.EMULATOR_X + (65 * config.EMULATOR_WIDTH) / 100))
    config.NUMPAD_BTN_7_CENTER_Y = int(
        (config.EMULATOR_Y + (78 * config.EMULATOR_HEIGHT) / 100))
    # Numpad 8
    config.NUMPAD_BTN_8_CENTER_X = int(
        (config.EMULATOR_X + (70.5 * config.EMULATOR_WIDTH) / 100))
    config.NUMPAD_BTN_8_CENTER_Y = int(
        (config.EMULATOR_Y + (78 * config.EMULATOR_HEIGHT) / 100))
    # Numpad 9
    config.NUMPAD_BTN_9_CENTER_X = int(
        (config.EMULATOR_X + (76 * config.EMULATOR_WIDTH) / 100))
    config.NUMPAD_BTN_9_CENTER_Y = int(
        (config.EMULATOR_Y + (78 * config.EMULATOR_HEIGHT) / 100))
    # Numpad 0
    config.NUMPAD_BTN_0_CENTER_X = int(
        (config.EMULATOR_X + (82 * config.EMULATOR_WIDTH) / 100))
    config.NUMPAD_BTN_0_CENTER_Y = int(
        (config.EMULATOR_Y + (68 * config.EMULATOR_HEIGHT) / 100))
    # Numpad OK
    config.NUMPAD_BTN_OK_CENTER_X = int(
        (config.EMULATOR_X + (82 * config.EMULATOR_WIDTH) / 100))
    config.NUMPAD_BTN_OK_CENTER_Y = int(
        (config.EMULATOR_Y + (78 * config.EMULATOR_HEIGHT) / 100))


def key_answer_to_numpad(answer):
    for ch in answer:
        time.sleep(0.4)
        numpad_click(ch)
        print("[SYSTEM]: Click to numpad '" + ch + "'")
    # Send OK
    time.sleep(0.4)
    func_repo.mouse_left_click(
        config.NUMPAD_BTN_OK_CENTER_X, config.NUMPAD_BTN_OK_CENTER_Y)
    print("[SYSTEM]: Click to numpad 'OK'")


def numpad_click(btn):
    if btn == '1':
        func_repo.mouse_left_click(
            config.NUMPAD_BTN_1_CENTER_X, config.NUMPAD_BTN_1_CENTER_Y)
    elif btn == '2':
        func_repo.mouse_left_click(
            config.NUMPAD_BTN_2_CENTER_X, config.NUMPAD_BTN_2_CENTER_Y)
    elif btn == '3':
        func_repo.mouse_left_click(
            config.NUMPAD_BTN_3_CENTER_X, config.NUMPAD_BTN_3_CENTER_Y)
    elif btn == '4':
        func_repo.mouse_left_click(
            config.NUMPAD_BTN_4_CENTER_X, config.NUMPAD_BTN_4_CENTER_Y)
    elif btn == '5':
        func_repo.mouse_left_click(
            config.NUMPAD_BTN_5_CENTER_X, config.NUMPAD_BTN_5_CENTER_Y)
    elif btn == '6':
        func_repo.mouse_left_click(
            config.NUMPAD_BTN_6_CENTER_X, config.NUMPAD_BTN_6_CENTER_Y)
    elif btn == '7':
        func_repo.mouse_left_click(
            config.NUMPAD_BTN_7_CENTER_X, config.NUMPAD_BTN_7_CENTER_Y)
    elif btn == '8':
        func_repo.mouse_left_click(
            config.NUMPAD_BTN_8_CENTER_X, config.NUMPAD_BTN_8_CENTER_Y)
    elif btn == '9':
        func_repo.mouse_left_click(
            config.NUMPAD_BTN_9_CENTER_X, config.NUMPAD_BTN_9_CENTER_Y)
    elif btn == '0':
        func_repo.mouse_left_click(
            config.NUMPAD_BTN_0_CENTER_X, config.NUMPAD_BTN_0_CENTER_Y)


def confirm_btn_click():
    func_repo.mouse_left_click(
        config.QUESTION_BTN_CENTER_X, config.QUESTION_BTN_CENTER_Y)
    config.IS_QUIZ = False
    config.QUESTION_QUIZ_TEXT = ''
    config.QUESTION_ANS_TEXT = ''
    print("[SYSTEM]: Confirm button clicked")
