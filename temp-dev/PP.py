import requests
import logging


class PPC:
    def __init__(self, target_url):
        self.url = target_url
        self.visit_pass = 200

    def capture_desc(self):
        raw_data = requests.get(url=self.url)
        #   visit url
        if raw_data.status_code == self.visit_pass:
            logging.info(f"Privacy Policy link access is normal ({raw_data.status_code == self.visit_pass})")
        #   get description
        print(raw_data.text)



if __name__ == '__main__':
    PPC(target_url="https://www.iguzzini.com/privacy-statement/").capture_desc()