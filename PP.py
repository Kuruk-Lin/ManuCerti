import requests
import logging
import threading
from package.website_screenshot import website_sh
from bs4 import BeautifulSoup


class PPC:
    def __init__(self, target_url):
        self.url = target_url
        self.visit_pass = 200
        self.logger = logging.getLogger(__name__)
        self.raw_data = self._grv()
        self.raw_content = self.u_content()
        self.fo_list = {
            "user_data": "user data",
            "personal_data": "personal data",
            "personal_info": "personal information"
        }
        self.logging_pre()

    def m_proc(self):
        self.visit_proc()
        self.keyword_proc()
        self.site_sh()

    def keyword_proc(self):
        for no, key in enumerate(self.fo_list.keys()):
            self.logger.info(f"[{no}]: {key} ({str(self.raw_content).lower().find(self.fo_list.get(key))})")

    def visit_proc(self):
        if self.raw_data.status_code == self.visit_pass:
            self.logger.info(f"Privacy Policy link access is passed.")

    def logging_pre(self):
        self.logger.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(console_handler)

    def u_content(self):
        return self.raw_data.text

    def _grv(self):
        return requests.get(url=self.url)

    def site_sh(self):
        return website_sh(target_url=self.url)


if __name__ == '__main__':
    PPC(target_url="").m_proc()
