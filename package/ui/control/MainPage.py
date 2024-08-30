from PyQt6 import QtCore
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from package.ui.control.InitUI import InitUI

class Browse_QPushButton(QtWidgets.QPushButton):
    def __init__(self, parent, connection_unit_obj:QtWidgets.QLineEdit,file_format_filter:str):
        super().__init__(parent)
        self.connection_unit_obj = connection_unit_obj
        self.file_format_filter = file_format_filter

    #slot function(use to be connect() with button
    def connect_open_file(self):
        #third para "directory": default path when open a file, "" is the program's path
        file_name, file_format = QtWidgets.QFileDialog.getOpenFileName(self,
                                "Please select a input file","",self.file_format_filter)

        self.connection_unit_obj.setText(file_name)
        self.connection_unit_obj.setStyleSheet("color:black")

    def connect_open_folder(self):
        fd = QtWidgets.QFileDialog.getExistingDirectory(self,"Please select a folder","")
        self.connection_unit_obj.setText(fd)
        self.connection_unit_obj.setStyleSheet("color:black")

class MainPage(InitUI):

    def __init__(self,Form:QtWidgets.QWidget,configPath):
        super().__init__(configPath)

        Form.setObjectName("Widget")
        Form.setFixedSize(698, 707)

        self.BigGroupBox = QtWidgets.QGroupBox(parent=Form)
        self.BigGroupBox.setGeometry(QtCore.QRect(20, 10, 551, 571))
        self.BigGroupBox.setObjectName("BigGroupBox")

        self.articleGroupBox = QtWidgets.QGroupBox(parent=self.BigGroupBox)
        self.articleGroupBox.setGeometry(QtCore.QRect(20, 30, 291, 521))
        self.articleGroupBox.setObjectName("articleGroupBox")

        self.articleInput = QtWidgets.QTextEdit(parent=self.articleGroupBox)
        self.articleInput.setGeometry(QtCore.QRect(13, 26, 261, 481))
        self.articleInput.setObjectName("articleInput")

        self.SearchWordsBox = QtWidgets.QGroupBox(parent=self.BigGroupBox)
        self.SearchWordsBox.setGeometry(QtCore.QRect(330, 30, 201, 521))
        self.SearchWordsBox.setObjectName("SearchWordsBox")

        self.SearchWordsInput = QtWidgets.QPlainTextEdit(parent=self.SearchWordsBox)
        self.SearchWordsInput.setGeometry(QtCore.QRect(20, 30, 161, 471))
        self.SearchWordsInput.setObjectName("SearchWordsInput")

        self.SearchButton = QtWidgets.QPushButton(parent=Form)
        self.SearchButton.setGeometry(QtCore.QRect(590, 140, 93, 28))
        self.SearchButton.setObjectName("DownloadButton")

        self.DownloadButton = QtWidgets.QPushButton(parent=Form)
        self.DownloadButton.setGeometry(QtCore.QRect(590, 180, 93, 28))
        self.DownloadButton.setObjectName("pushButton")

        self.StateLabel = QtWidgets.QLabel(parent=Form)
        self.StateLabel.setGeometry(QtCore.QRect(600, 210, 71, 20))
        self.StateLabel.setText("")
        self.StateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SettingGroupBox = QtWidgets.QGroupBox(parent=Form)
        self.SettingGroupBox.setGeometry(QtCore.QRect(20, 590, 551, 101))
        self.SettingGroupBox.setObjectName("SettingGroupBox")

        self.label = QtWidgets.QLabel(parent=self.SettingGroupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 19))
        self.label.setObjectName("label")

        self.SavePathInput = QtWidgets.QLineEdit(parent=self.SettingGroupBox)
        self.SavePathInput.setGeometry(QtCore.QRect(100, 20, 361, 25))
        self.SavePathInput.setObjectName("SavePathInput")
        self.SavePathInput.setText(self.config["SavePath"])

        self.SavePathBrowser = Browse_QPushButton(parent=self.SettingGroupBox,connection_unit_obj=self.SavePathInput,
                                                                          file_format_filter="Folder")
        self.SavePathBrowser.setGeometry(QtCore.QRect(470, 20, 71, 28))
        self.SavePathBrowser.setObjectName("SavePathBrowser")


        self.label_2 = QtWidgets.QLabel(parent=self.SettingGroupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 91, 19))
        self.label_2.setObjectName("label_2")

        self.ExpressionInput = QtWidgets.QLineEdit(parent=self.SettingGroupBox)
        self.ExpressionInput.setGeometry(QtCore.QRect(100, 60, 361, 25))
        self.ExpressionInput.setObjectName("ExpressionInput")
        self.ExpressionInput.setPlaceholderText("\((.*?)\)")
        self.ExpressionInput.setDisabled(True)

        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(590, 50, 111, 19))
        self.label_3.setObjectName("label_3")

        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(590, 70, 91, 25))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.BigGroupBox.setTitle(_translate("Widget", "Search Words Input"))
        self.articleGroupBox.setTitle(_translate("Widget", "Article"))
        self.SearchWordsBox.setTitle(_translate("Widget", "Search Words"))
        self.SearchButton.setText(_translate("Widget", "Search"))
        self.DownloadButton.setText(_translate("Widget", "Download"))
        self.SettingGroupBox.setTitle(_translate("Widget", "Setting"))
        self.label.setText(_translate("Widget", "Save into:"))
        self.SavePathBrowser.setText(_translate("Widget", "Browser"))
        self.label_2.setText(_translate("Widget", "Expression:"))
        self.label_3.setText(_translate("Widget", "Current/Jump to"))
