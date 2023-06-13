import requests
import logging
from bs4 import BeautifulSoup


class PPC:
    def __init__(self, target_url):
        self.url = target_url
        self.visit_pass = 200
        self.raw_data = self._grv()
        self.raw_content = self.u_content()
        self.fo_list = {
            "userdata": "user data"
        }

    def m_proc(self):
        if self.raw_data.status_code == self.visit_pass:
            logging.info(f"Privacy Policy link access is valid.")
        for no, key in enumerate(self.fo_list.keys()):
            print(str(self.raw_content).lower().find(self.fo_list.get(key)))

    def u_content(self):
        return self.raw_data.text

    def _grv(self):
        return requests.get(url=self.url)


if __name__ == '__main__':
    PPC(target_url="").m_proc()