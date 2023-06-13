import requests
import logging
from bs4 import BeautifulSoup


class PPC:
    def __init__(self, target_url):
        self.url = target_url
        self.visit_pass = 200
        self.raw_data = self._grv()

    def m_proc(self):
        if self.raw_data.status_code == self.visit_pass:
            logging.info(f"Privacy Policy link access is valid.")
        print(self.raw_data.text)

    def _grv(self):
        return requests.get(url=self.url)


if __name__ == '__main__':
    PPC(target_url="").m_proc()