import pyautogui
import time


class MM:
    def __init__(self):
        self.delay = 1

    def trigger_flow(self):
        pyautogui.moveTo(100, 100)
        time.sleep(self.delay)


if __name__ == '__main__':
    MM().trigger_flow()