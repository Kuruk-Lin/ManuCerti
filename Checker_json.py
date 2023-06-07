import json
import re
import sys
import pyperclip


class JChecker:
    def __init__(self):
        self.file_name = "TestFile.json"
        self.file_output = "TestFile_roll_out.json"
        self.tmp_name = "tmp.json"
        self.keyword_list = ["\\n", " ", "\\\\\\", "\\", "|"]
        self.replace_list = ['', '', "|", '', "\\\\\\"]

    def load(self):
        with open(self.file_name, "r") as file:
            try:
                dict(json.load(file))
            except:
                file.close()
                with open(self.file_name, "r") as trs:
                    with open(self.file_output, "w") as roll_out:
                        x = trs.read()
                        if x[0] == "\"" and x[-1] == "\"":
                            x = x[1:-1]
                        elif x[0] == "\"" and x[-1] != "\"":
                            x = x[1:]
                        elif x[0] != "\"" and x[-1] == "\"":
                            x = x[:-1]
                        for raw, target in zip(self.keyword_list, self.replace_list):
                            x = x.replace(raw, target)
                        roll_out.write(x)
                        roll_out.close()
                        trs.close()

    def format_js(self):
        with open(self.file_output, "r") as fi:
            with open(self.file_name, "w") as fw:
                js_format = json.dumps(json.load(fi), indent=2, sort_keys=True)
                fw.write(js_format)
                fw.close()
                fi.close()
                pyperclip.copy(js_format)

    def checker(self):
        with open(self.file_name, "r") as files:
            al_keys = dict(json.load(files))
            if al_keys.get("inputs") is not None and al_keys.get("inputs")[0].get("intent") == "action.devices.QUERY":
                device_Id = dict(list(al_keys.get("inputs"))[0]).get("payload").get("devices")[0].get("id")
                requestId = al_keys.get("requestId")
                temp = {"device_Id": device_Id, "requestId": requestId}
                with open(self.tmp_name, "w") as write_out:
                    write_out.write(json.dumps(temp, indent=2, sort_keys=True))
                    write_out.close()
                print(f"Response data:\n\t\tDevice ID: {device_Id}\n\t\tRequest ID: {requestId}")
            elif al_keys.get("inputs") is not None:
                device_Id = dict(list(
                    dict(dict(dict(list(al_keys.get("inputs"))[0]).get("payload")).get("commands")[0]).get(
                        "devices"))[0]).get("id")
                requestId = al_keys.get("requestId")
                temp = {"device_Id": device_Id, "requestId": requestId}
                with open(self.tmp_name, "w") as write_out:
                    write_out.write(json.dumps(temp, indent=2, sort_keys=True))
                    write_out.close()
                print(f"Response data:\n\t\tDevice ID: {device_Id}\n\t\tRequest ID: {requestId}")
            elif al_keys.get("payload") is not None:
                try:
                    device_Id = dict(list(dict(al_keys.get("payload")).get("commands"))[0]).get('ids')[0]
                except:
                    device_Id = list(dict(dict(dict(al_keys.get("payload"))).get("devices")).keys())[0]
                requestId = al_keys.get("requestId")
                temp = {"device_Id": device_Id, "requestId": requestId}
                with open(self.tmp_name, "r") as checker:
                    previous_data = dict(json.load(checker))
                    checker.close()
                print(f"Response data:\n\t\tDevice ID: {device_Id}\n\t\tRequest ID: {requestId}")
                print(f"Device ID & Request ID:\n\t\tPostData: {previous_data}\n\t\tResponseData: {temp}\n\t\tResult: {dict(temp) == previous_data}")
            else:
                print("No data found.")
        files.close()


if __name__ == '__main__':
    JChecker().load()
    JChecker().format_js()
    JChecker().checker()