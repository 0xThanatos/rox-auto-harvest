IS_RUNNING = True
VERSION = '1.0'
TITLE = 'RO:X Next Generation - Auto Harvest Bot version ' + VERSION
PID = ''

EMULATOR = 1  # BlueStacks App Player
EMULATOR_TEXT = 'BlueStacks App Player'
EMULATOR_X = 0
EMULATOR_Y = 0
EMULATOR_WIDTH = 0
EMULATOR_HEIGHT = 0

IS_ACTIVE = False
IS_HARVESTING = False
HOLD = True

FRAME_EMULATOR = None
FRAME_QUESTION_TEXT = None

PREV_TIME = 0
CURRENT_TIME = 0
LAST_CLICK_TIME = 0
LIMIT = 0
COOLDOWN = 0
LOOP = 0
COUNT = 0

# ปุ่มกดเก็บเกี่ยว
HARVEST_BTN_BOUNDING_BOX = {'top': 0, 'left': 0, 'width': 0, 'height': 0}
HARVEST_BTN_CENTER_X = 0
HARVEST_BTN_CENTER_Y = 0

# โจทย์คำถาม
QUESTION_QUIZ_BOUNDING_BOX = {'top': 0, 'left': 0, 'width': 0, 'height': 0}
QUESTION_QUIZ_CENTER_X = 0
QUESTION_QUIZ_CENTER_Y = 0
FRAME_QUESTION_QUIZ = None
QUESTION_QUIZ_TEXT = ''

# ช่องใส่คำตอบ
QUESTION_ANS_BOUNDING_BOX = {'top': 0, 'left': 0, 'width': 0, 'height': 0}
QUESTION_ANS_CENTER_X = 0
QUESTION_ANS_CENTER_Y = 0
QUESTION_ANS_TEXT = ''

# ปุ่มส่งคำตอบ
QUESTION_BTN_BOUNDING_BOX = {'top': 0, 'left': 0, 'width': 0, 'height': 0}
QUESTION_BTN_CENTER_X = 0
QUESTION_BTN_CENTER_Y = 0
FRAME_QUESTION_BTN = None
