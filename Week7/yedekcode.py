""" 
login.py
"""

#         self.pushbutton_login.clicked.connect(self.Login)
#         self.pushbutton_exit.clicked.connect(self.Exit)
    
#     def Login(self):
         
#         user_name = self.lineedit_user_login.text()
#         password = self.lineedit_password.text()
#         self.language = self.combobox_language.currentText()
#         if user_name == "admin" and password == "admin":
#             self.mw_main_menu = QtWidgets.QMainWindow()
#             self.ui = Ui_mw_main_menu()
#             self.ui.user = "admin"
#             self.ui.setupUi(self.mw_main_menu)
#             widgets.addWidget(self.mw_main_menu)
#             widgets.setCurrentIndex(widgets.currentIndex()+1)
#         elif user_name == "user" and password == "user":
#             self.mw_main_menu = QtWidgets.QMainWindow()
#             self.ui = Ui_mw_main_menu()
#             self.ui.user = "user"
#             self.ui.setupUi(self.mw_main_menu)
#             widgets.addWidget(self.mw_main_menu)
#             widgets.setCurrentIndex(widgets.currentIndex()+1)
#         else:
#             self.label_error = QtWidgets.QLabel(parent=self.frame)
#             self.label_error.setGeometry(QtCore.QRect(70, 110, 251, 31))
#             self.label_error.setStyleSheet("color: rgb(255, 0, 0);")
#             self.label_error.setText("User Name or Password is incorrect!")
#             self.label_error.setObjectName("label_error")
#             self.label_error
#     def Exit(self):
#         QtWidgets.QApplication.quit()
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ud_login = QtWidgets.QDialog()
#     ui = Ui_ud_login()
#     ui.setupUi(ud_login)
#     widgets= QtWidgets.QStackedWidget()
#     widgets.addWidget(ud_login)
#     widgets.show()
#     sys.exit(app.exec())

"""
MainMenu.py
"""
#           if self.user != "admin" :
#             self.pb_admin_menu.setVisible(False)

#       self.pb_exit.clicked.connect(self.Exit)

#     def Exit(self):
#         QtWidgets.QApplication.quit()

