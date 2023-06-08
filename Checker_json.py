import json
try:
    import pyperclip
except ImportError:
    import subprocess
    subprocess.getoutput(f"pip install pyperclip")
finally:
    import pyperclip


class JChecker:
    def __init__(self):
        self.file_name = "TestFile.json"
        self.file_output = "TestFile_roll_out.json"
        self.tmp_name = "tmp.json"
        self.blank = "\n\t\t"
        self.keyword_list = ["\\n", " ", "\\\\\\", "\\", "|"]
        self.replace_list = ['', '', "|", '', "\\\\\\"]

    def m_proc(self):
        self.load()
        self.format_js()
        self.checker()

    def load(self):
        with open(self.file_name, "r") as file:
            try:
                dict(json.load(file))
            #   Expected is error json
            except:
                file.close()
                with open(self.file_name, "r") as trs:
                    with open(self.file_output, "w") as roll_out:
                        raw_data = trs.read()
                        raw_json = raw_data[raw_data.find("{"):raw_data.rfind("}") + 1]
                        for raw, target in zip(self.keyword_list, self.replace_list):
                            raw_json = raw_json.replace(raw, target)
                        roll_out.write(raw_json)
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
                print(f"Response data:{self.blank}Device ID: {device_Id}{self.blank}Request ID: {requestId}")
            elif al_keys.get("inputs") is not None:
                device_Id = dict(list(
                    dict(dict(dict(list(al_keys.get("inputs"))[0]).get("payload")).get("commands")[0]).get(
                        "devices"))[0]).get("id")
                requestId = al_keys.get("requestId")
                temp = {"device_Id": device_Id, "requestId": requestId}
                with open(self.tmp_name, "w") as write_out:
                    write_out.write(json.dumps(temp, indent=2, sort_keys=True))
                    write_out.close()
                print(f"Response data:{self.blank}Device ID: {device_Id}{self.blank}Request ID: {requestId}")
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
                print(f"Response data:{self.blank}Device ID: {device_Id}{self.blank}Request ID: {requestId}")
                print(f"Device ID & Request ID:{self.blank}Request Data: {previous_data}{self.blank}Response Data: {temp}"
                      f"{self.blank}Result: {dict(temp) == previous_data}")
            else:
                print("No data found.")
        files.close()


if __name__ == '__main__':
    JChecker().m_proc()
