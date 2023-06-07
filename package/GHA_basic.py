import uiautomator2 as u2
from RawInfo import *


class GHABasic:
    def __init__(self):
        self.device = u2.connect()

    def verify(self):
        while True:
            if self.device.xpath(Verify_XPath).exists:
                self.device.xpath(Verify_XPath).click()

    def VerifyNext(self):
        self.device(resourceId="com.google.android.gms:id/sud_layout_template_content").child(text="Next").click()

    def UIElement(self):

        tmp = self.device.__call__()
        print(tmp)

    def power_key(self):
        print(self.device.current_app())

if __name__ == '__main__':
    GHABasic().power_key()