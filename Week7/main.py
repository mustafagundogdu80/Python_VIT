"""
Project Name: WeRHere Project
Description:
Author: Mustfa Gundogdu
        Kahraman Dal
        Neslihan Utuk
        Yasin Sinan
Start Date: 09-02-2025
End Date: 17-02-2025

"""
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from login import Ui_mw_main_menu
from MainMenu import Ui_MainWindow

class Edit_Ui_mw_main_menu(Ui_mw_main_menu):
    def setupUi(self, mw_main_menu):
        super().setupUi(mw_main_menu)
        self.pushbutton_login.clicked.connect(self.login)
        self.pushbutton_exit.clicked.connect(self.exit)
    
    def login(self):
        pass

    def exit(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Edit_Ui_mw_main_menu()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())
    