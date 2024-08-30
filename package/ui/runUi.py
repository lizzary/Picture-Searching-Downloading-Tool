from package.ui.control.connect import Connect
from PyQt6 import QtWidgets
import sys
import os
class runUi(Connect):

    def __init__(self,Form:QtWidgets.QWidget,configPath):
        super().__init__(Form,configPath)

def run():
    configPath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\config.json"
    print(configPath)

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    UiInit = runUi(Form,configPath)
    Form.show()
    sys.exit(app.exec())



