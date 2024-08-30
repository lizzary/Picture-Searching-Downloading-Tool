import json

from package.ui.control.MainPage import MainPage
from PyQt6 import QtWidgets
from DrissionPage import ChromiumOptions,WebPage
import re
import os
from PIL import Image

class Slot(MainPage):
    searchWordCount:int = -1
    searchWordList:list = ['']
    page = None

    def __init__(self,Form:QtWidgets.QWidget,configPath):
        super().__init__(Form,configPath)

    def __isLegalSearch(self,keyword):
        if (
            keyword == '' or
            keyword == ' ' or
            keyword == '\n'
        ):
            return False
        else:
            return True

    def __convert_to_jpg(self,path:str):
        lowerCase = path.lower()
        if not "gif" in lowerCase or not "png" in lowerCase:
            return

        img = Image.open(path)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        os.remove(path)
        img.save(path, "JPEG")

    '''change: self.searchWordList
    '''
    def ArticleInputEvent(self):
        text = self.articleInput.toPlainText()
        if len(text) > 0:
            if text[0] == "$":
                if "set expression" in text:
                    self.ExpressionInput.setDisabled(False)
                if "config" in text:
                    self.articleInput.setPlainText(json.dumps(self.config))
                else:
                    self.ExpressionInput.setDisabled(True)
            else:
                self.ExpressionInput.setDisabled(True)

        self.searchWordList = re.findall(pattern=self.config["Expression"], string=text)
        str = ""
        for word in self.searchWordList:
            str += word + '\n'
        self.SearchWordsInput.setPlainText(str)

    '''change: self.searchWordList
               self.comboBox
    '''
    def SearchWordsInputEvent(self):
        text = self.SearchWordsInput.toPlainText()
        text = text.split("\n")
        self.searchWordList = [word for word in text if self.__isLegalSearch(word)]
        print(self.searchWordList)

        self.comboBox.clear()
        for i in text:
            if self.__isLegalSearch(i):
                self.comboBox.addItem(i)
        self.searchWordCount = -1


    def comboBoxSelectedEvent(self):
        self.searchWordCount = self.comboBox.currentIndex()-1

    def SavePathInputEvent(self):
        self.config["SavePath"] = self.SavePathInput.text()

    def ExpressionInputEvent(self):
        self.config["Expression"] = self.ExpressionInput.text()

    '''change: self.comboBox
    '''
    def search(self):
        if not os.path.exists(self.config["BrowserPath"]):
            self.articleInput.setPlainText("ERROR: CANNOT find your google browser in path: " + self.config["BrowserPath"])
            return

        self.SearchButton.setDisabled(True)
        self.searchWordCount += 1

        if self.searchWordCount >= len(self.searchWordList) :
            self.SearchButton.setDisabled(False)
            return

        print(self.comboBox.currentIndex())
        keyword = self.searchWordList[self.searchWordCount]
        self.comboBox.setCurrentIndex(self.searchWordCount)
        if not self.__isLegalSearch(keyword):
            self.SearchButton.setDisabled(False)
            # self.searchWordCount += 1
            return

        search_request = (
            self.config["UrlPrefix"] + keyword + self.config["UrlSuffix"]
        )
        co = ChromiumOptions()
        co.set_browser_path(self.config["BrowserPath"])
        print(self.config["BrowserPath"])
        self.page = WebPage(mode='d', chromium_options=co)
        self.page.get(search_request)

        self.SearchButton.setDisabled(False)


    def downLoad(self):
        self.DownloadButton.setDisabled(True)
        try:
            pic_link_list = self.page.eles(self.config["DownloadSelectedRule"])
            pic_link = None
            for i in pic_link_list:
                if "jsaction" in i.html:
                    pic_link = i
                    break

            print(pic_link)
            source = pic_link.parent(1)
            title = pic_link.attr('alt')
            print(pic_link.link)
            print(source.link)
            print(title)
            print(self.searchWordList[self.searchWordCount])
            self.page.set.download_path(self.config["SavePath"])
            print(self.page.download(rename=self.searchWordList[self.searchWordCount],
                                      file_url=pic_link.link))


            f = open(self.config["SavePath"]+"\pictureInfo.txt","a+",encoding='utf-8')
            f.write(title+"。"+source.link+'\n')

            self.StateLabel.setText("Success")
            self.StateLabel.setStyleSheet("color:green")
        except Exception as e:
            self.DownloadButton.setDisabled(False)
            self.StateLabel.setText("Fail")
            self.StateLabel.setStyleSheet("color:red")
            return

        self.DownloadButton.setDisabled(False)







