import json
import os
import sys

class InitUI(object):
    urlPrefix: str = None
    urlSuffix: str = None
    config: dict = None
    configPath: str = None
    write_json_obj = None

    def __init__(self,configPath):
        self.configPath = configPath
        try:
            f = open(self.configPath, 'r', encoding='utf-8')
            self.config = json.load(f)
        except Exception as e:
            os.remove(self.configPath) if os.path.exists(self.configPath) else False
            self.reBulidConfig()
            f = open(self.configPath, 'r', encoding='utf-8')
            self.config = json.load(f)

        if self.config["BrowserPath"] == "None":
            self.config["BrowserPath"] = os.path.dirname(os.path.realpath(sys.argv[0]))
            self.config["BrowserPath"] += "\google\chrome.exe"

        if self.config["SavePath"] == "None":
            self.config["SavePath"] = os.path.dirname(os.path.realpath(sys.argv[0]))
            self.config["SavePath"] += "\picture"

        if self.config["Expression"] == "None":
            self.config["Expression"] = "\((.*?)\)"

        if self.config["UrlPrefix"] == "None":
            self.config["UrlPrefix"] = "https://www.google.com.hk/search?as_st=y&hl=zh-TW&as_q="

        if self.config["UrlSuffix"] == "None":
            self.config["UrlSuffix"] = "&as_epq=&as_oq=&as_eq=&imgsz=l&imgar=w&imgcolor=&imgtype=&cr=countryJP&as_sitesearch=&as_filetype=&tbs=&udm=2"

        if self.config["DownloadSelectedRule"] == "None":
            self.config["DownloadSelectedRule"] = "t:img@|src:jpg@|src:jpeg@|src:webp@|src:png@|src:JPG@|src:gif"

        self.write_json_obj = open(self.configPath, 'w', encoding='utf-8')

    def __del__(self):
        json.dump(self.config, self.write_json_obj, ensure_ascii=False, indent=2)


    def reBulidConfig(self):

        f = open(self.configPath,'w+',encoding='utf-8')
        file = {
            "BrowserPath": "None",
            "SavePath": "None",
            "Expression": "None",
            "UrlPrefix": "None",
            "UrlSuffix": "None",
            "DownloadSelectedRule": "None"
        }
        json.dump(file,f,ensure_ascii=True,indent=2)
        f.close()
