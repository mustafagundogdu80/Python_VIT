# Form implementation generated from reading ui file 'c:\Users\kahra\OneDrive\Masaüstü\PROGRAM\PYTHON\PROJECT\PYQT6_PROJECTS\TAMAMLANANLAR\PROJE\VIT_Project\AdminMenu.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mwAdminMenu(object):
    def setupUi(self, mwAdminMenu):
        mwAdminMenu.setObjectName("mwAdminMenu")
        mwAdminMenu.resize(1001, 601)
        mwAdminMenu.setBaseSize(QtCore.QSize(1050, 700))
        mwAdminMenu.setStyleSheet("QWidget {\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"        stop:0 rgba(173, 216, 230, 255), \n"
"        stop:1 rgba(255, 255, 255, 255));\n"
"};\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=mwAdminMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(8, 132))
        self.frame.setSizeIncrement(QtCore.QSize(7, 51))
        self.frame.setBaseSize(QtCore.QSize(37, 65))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbActionControl = QtWidgets.QPushButton(parent=self.frame)
        self.pbActionControl.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pbActionControl.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: #008CBA;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    margin: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #007B9E;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #005f73;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\kahra\\OneDrive\\Masaüstü\\PROGRAM\\PYTHON\\PROJECT\\PYQT6_PROJECTS\\TAMAMLANANLAR\\PROJE\\VIT_Project\\icons/calendar.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pbActionControl.setIcon(icon)
        self.pbActionControl.setIconSize(QtCore.QSize(40, 40))
        self.pbActionControl.setObjectName("pbActionControl")
        self.verticalLayout.addWidget(self.pbActionControl)
        self.pbSendMail = QtWidgets.QPushButton(parent=self.frame)
        self.pbSendMail.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pbSendMail.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: #008CBA;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    margin: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #007B9E;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #005f73;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\kahra\\OneDrive\\Masaüstü\\PROGRAM\\PYTHON\\PROJECT\\PYQT6_PROJECTS\\TAMAMLANANLAR\\PROJE\\VIT_Project\\icons/send-message.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pbSendMail.setIcon(icon1)
        self.pbSendMail.setIconSize(QtCore.QSize(40, 40))
        self.pbSendMail.setObjectName("pbSendMail")
        self.verticalLayout.addWidget(self.pbSendMail)
        self.pbPreferedAdmin = QtWidgets.QPushButton(parent=self.frame)
        self.pbPreferedAdmin.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pbPreferedAdmin.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: #008CBA;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    margin: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #007B9E;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #005f73;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\kahra\\OneDrive\\Masaüstü\\PROGRAM\\PYTHON\\PROJECT\\PYQT6_PROJECTS\\TAMAMLANANLAR\\PROJE\\VIT_Project\\icons/news.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pbPreferedAdmin.setIcon(icon2)
        self.pbPreferedAdmin.setIconSize(QtCore.QSize(40, 40))
        self.pbPreferedAdmin.setObjectName("pbPreferedAdmin")
        self.verticalLayout.addWidget(self.pbPreferedAdmin)
        self.pbExit = QtWidgets.QPushButton(parent=self.frame)
        self.pbExit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pbExit.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: #008CBA;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    margin: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #007B9E;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #005f73;\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\kahra\\OneDrive\\Masaüstü\\PROGRAM\\PYTHON\\PROJECT\\PYQT6_PROJECTS\\TAMAMLANANLAR\\PROJE\\VIT_Project\\icons/power.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pbExit.setIcon(icon3)
        self.pbExit.setIconSize(QtCore.QSize(50, 50))
        self.pbExit.setObjectName("pbExit")
        self.verticalLayout.addWidget(self.pbExit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    \n"
"    font-size: 14px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"    background-color: #f9f9f9;\n"
"    alternate-background-color: #e0e0e0;\n"
"    gridline-color: #ccc;\n"
"    border-radius: 10px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #008CBA;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(203)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_2.addWidget(self.frame_2)
        mwAdminMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=mwAdminMenu)
        self.statusbar.setObjectName("statusbar")
        mwAdminMenu.setStatusBar(self.statusbar)

        self.retranslateUi(mwAdminMenu)
        QtCore.QMetaObject.connectSlotsByName(mwAdminMenu)

    def retranslateUi(self, mwAdminMenu):
        _translate = QtCore.QCoreApplication.translate
        mwAdminMenu.setWindowTitle(_translate("mwAdminMenu", "Admin Menu Window"))
        self.pbActionControl.setText(_translate("mwAdminMenu", "Action Control"))
        self.pbSendMail.setText(_translate("mwAdminMenu", "Send Mail"))
        self.pbPreferedAdmin.setText(_translate("mwAdminMenu", "Main Menu"))
        self.pbExit.setText(_translate("mwAdminMenu", "Exit"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mwAdminMenu", "Action Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mwAdminMenu", "Start Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mwAdminMenu", "Participant Mail"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mwAdminMenu", "Organizer Mail"))
