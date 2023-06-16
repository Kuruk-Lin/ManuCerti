import uiautomator2


class TTM:
    def __init__(self):
        self.device = uiautomator2.connect()

    def flow_task(self):
        print(self.device().info['packageName'])


if __name__ == '__main__':
    TTM().flow_task()