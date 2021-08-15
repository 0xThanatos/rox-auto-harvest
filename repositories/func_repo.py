import config
from repositories import harvest_repo

import os
import sys
import pygetwindow
import re
from PIL import Image


def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')
    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)


def emulator_case(num):
    return {
        1: "BlueStacks App Player",
        2: "LDPlayer"
    }.get(num, 1)


def find_emulator():
    # Get titles of all specific window
    titles = pygetwindow.getAllTitles()

    # to get string with substring
    res = [x for x in titles if re.search(config.EMULATOR_TEXT, x)]
    if len(res) == 0:
        alert('Error', 'Emulator not found', kind='error')
        sys.exit(1)


def select_emulator():
    print("[Select your Andriod Emulator]")
    print("1) Bluestacks (Global & CN)")  # BlueStacks App Player
    print("2) LD Player")  # LDPlayer
    try:
        config.EMULATOR = int(
            input("\nEnter number\n(default is Bluestacks): ") or "1")
    except ValueError:
        print("Invalid number, set to Bluestacks.")
        config.EMULATOR = 1
    config.EMULATOR_TEXT = emulator_case(config.EMULATOR)
    print("Emulator is " + config.EMULATOR_TEXT)
    find_emulator()


def get_emulator_area(sct):
    try:
        window = pygetwindow.getWindowsWithTitle(config.EMULATOR_TEXT)[0]
    except IndexError:
        alert('Error', 'Can\'t get emulator bounding box', kind='error')
        sys.exit(1)
    config.EMULATOR_X = window.left
    config.EMULATOR_Y = window.top
    config.EMULATOR_WIDTH = window.width
    config.EMULATOR_HEIGHT = window.height
    sct.get_pixels(
        {'top': config.EMULATOR_Y, 'left': config.EMULATOR_X, 'width': config.EMULATOR_WIDTH, 'height': config.EMULATOR_HEIGHT})
    # Set emulator frame
    config.FRAME_EMULATOR = Image.frombytes(
        'RGB', (sct.width, sct.height), sct.image)


def mainmenu():
    while True:
        # Clear console
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        print("Made by Thanapat Maliphan. (fb.com/thanatos1995)\n")
        print("[Main Menu]\n")
        print("1) Change limit")
        print("2) Change cooldown")
        print("3) Toggle harvest or hold")
        print("4) Exit program\n")
        choice = input("Enter number: ")

        if choice == '1':
            harvest_repo.set_limit()
        if choice == '2':
            harvest_repo.set_cooldown()
        if choice == '3':
            config.HOLD ^= True
        if choice == '4':
            config.IS_RUNNING = False
            sys.exit(0)
