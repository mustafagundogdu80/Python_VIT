# Form implementation generated from reading ui file 'Application.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1228, 805)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(1228, 805))
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet("\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.W_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.W_widget.setEnabled(True)
        self.W_widget.setGeometry(QtCore.QRect(12, 0, 305, 780))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.W_widget.setFont(font)
        self.W_widget.setAcceptDrops(False)
        self.W_widget.setStyleSheet("")
        self.W_widget.setObjectName("W_widget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.W_widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 265, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.PB_search_button = QtWidgets.QPushButton(parent=self.W_widget)
        self.PB_search_button.setGeometry(QtCore.QRect(20, 84, 265, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PB_search_button.setFont(font)
        self.PB_search_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.PB_search_button.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"")
        self.PB_search_button.setObjectName("PB_search_button")
        self.PB_all_applications_button = QtWidgets.QPushButton(parent=self.W_widget)
        self.PB_all_applications_button.setGeometry(QtCore.QRect(20, 180, 265, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PB_all_applications_button.setFont(font)
        self.PB_all_applications_button.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"")
        self.PB_all_applications_button.setObjectName("PB_all_applications_button")
        self.PB_mentor_meeting_defined_button = QtWidgets.QPushButton(parent=self.W_widget)
        self.PB_mentor_meeting_defined_button.setGeometry(QtCore.QRect(20, 245, 265, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PB_mentor_meeting_defined_button.setFont(font)
        self.PB_mentor_meeting_defined_button.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.PB_mentor_meeting_defined_button.setObjectName("PB_mentor_meeting_defined_button")
        self.PB_mentor_interview_undefined_button = QtWidgets.QPushButton(parent=self.W_widget)
        self.PB_mentor_interview_undefined_button.setGeometry(QtCore.QRect(20, 310, 265, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PB_mentor_interview_undefined_button.setFont(font)
        self.PB_mentor_interview_undefined_button.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"")
        self.PB_mentor_interview_undefined_button.setObjectName("PB_mentor_interview_undefined_button")
        self.PB_duplicate_record_button = QtWidgets.QPushButton(parent=self.W_widget)
        self.PB_duplicate_record_button.setGeometry(QtCore.QRect(20, 375, 265, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PB_duplicate_record_button.setFont(font)
        self.PB_duplicate_record_button.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.PB_duplicate_record_button.setObjectName("PB_duplicate_record_button")
        self.CB_combo_box = QtWidgets.QComboBox(parent=self.W_widget)
        self.CB_combo_box.setGeometry(QtCore.QRect(20, 450, 265, 55))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CB_combo_box.setFont(font)
        self.CB_combo_box.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.CB_combo_box.setObjectName("CB_combo_box")
        self.CB_combo_box.addItem("")
        self.CB_combo_box.addItem("")
        self.CB_combo_box.addItem("")
        self.CB_combo_box.addItem("")
        self.PB_return_to_preferences_screen_button = QtWidgets.QPushButton(parent=self.W_widget)
        self.PB_return_to_preferences_screen_button.setGeometry(QtCore.QRect(20, 710, 265, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PB_return_to_preferences_screen_button.setFont(font)
        self.PB_return_to_preferences_screen_button.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.PB_return_to_preferences_screen_button.setObjectName("PB_return_to_preferences_screen_button")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(325, 10, 900, 780))
        self.tableWidget.setSizeIncrement(QtCore.QSize(1228, 805))
        self.tableWidget.setBaseSize(QtCore.QSize(1228, 805))
        self.tableWidget.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APPLICATIONS"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "   Write a name or surname..."))
        self.PB_search_button.setText(_translate("MainWindow", "Search"))
        self.PB_all_applications_button.setText(_translate("MainWindow", "All Applications"))
        self.PB_mentor_meeting_defined_button.setText(_translate("MainWindow", "Mentor Interview Defined"))
        self.PB_mentor_interview_undefined_button.setText(_translate("MainWindow", "Mentor Interview Undefined"))
        self.PB_duplicate_record_button.setText(_translate("MainWindow", "Duplicate Record"))
        self.CB_combo_box.setCurrentText(_translate("MainWindow", "      Please make a choice..."))
        self.CB_combo_box.setItemText(0, _translate("MainWindow", "      Please make a choice..."))
        self.CB_combo_box.setItemText(1, _translate("MainWindow", "       Previous VIT Control"))
        self.CB_combo_box.setItemText(2, _translate("MainWindow", "         Different Records"))
        self.CB_combo_box.setItemText(3, _translate("MainWindow", "           Applying Filter"))
        self.PB_return_to_preferences_screen_button.setText(_translate("MainWindow", "Return to Preferences Screen"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Surname"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mentor Situation"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
