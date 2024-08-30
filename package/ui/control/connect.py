from package.ui.control.slot import Slot
from PyQt6 import QtWidgets

class Connect(Slot):

    def __init__(self,Form:QtWidgets.QWidget,configPath):
        super().__init__(Form,configPath)

        self.articleInput.textChanged.connect(self.ArticleInputEvent)
        self.SearchWordsInput.textChanged.connect(self.SearchWordsInputEvent)
        self.ExpressionInput.textChanged.connect(self.ExpressionInputEvent)
        self.SavePathInput.textChanged.connect(self.SavePathInputEvent)

        self.SearchButton.clicked.connect(self.search)
        self.DownloadButton.clicked.connect(self.downLoad)

        self.comboBox.activated.connect(self.comboBoxSelectedEvent)

        self.SavePathBrowser.clicked.connect(self.SavePathBrowser.connect_open_folder)