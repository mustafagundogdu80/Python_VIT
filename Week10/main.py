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
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QMessageBox, QVBoxLayout
from PyQt6.uic import loadUi
from MainMenu import Ui_mw_main_menu
from login import Ui_ud_login
from Application3 import Ui_ApplicationWindow
from interviews import Ui_interviews
from Mentor import Ui_Mentor
from AdminMenu import Ui_mwAdminMenu
from googledrive import GoogleDriveFileManager, GoogleCalendarManager
from mail import MailSender
from dbconnection import DatabaseConnection
import pandas as pd
import numpy as np  # Dosyanın en üstüne ekleyin

"""---------------------------------------------------------------------------------------"""
application_widgets_index = {"LoginWindow":0,"MainMenuWindow":-1,"ApplicationWindow":-1,"InterviewsWindow":-1,"MentorMeetingWindow":-1,"AdminMenuWindow":-1}
"""----------------------------------------------------------------------------------------"""
#Login Page Code Class
class LoginWindow(Ui_ud_login):
    def setupUi(self, ud_login):
        super().setupUi(ud_login)
        self.pushbutton_login.clicked.connect(self.login)
        self.pushbutton_exit.clicked.connect(self.exit_app)
    
    def login(self):
        # obj_gdfm = GoogleDriveFileManager("Kullanicilar")
        # obj_gdfm.getExcelFile()
        obj_db = DatabaseConnection()
        username = self.lineedit_user_login.text()
        password = self.lineedit_password.text()
        query = "SELECT kullaniciid, kullaniciadi, yetki FROM kullanicilar WHERE kullaniciadi = '" + username + "' AND parola = '" + password + "'"
        result = obj_db.db_select(query)
        if len(result) > 0:
            self.user = {"UserID":result[0][0],"Name":result[0][1],"Role":result[0][2]}
            self.lineedit_user_login.setText("")
            self.lineedit_password.setText("")
            self.lineedit_user_login.setFocus()
            if application_widgets_index["MainMenuWindow"] == -1:
                self.MainMenu = QtWidgets.QMainWindow()
                self.ui = MainMenuWindow(self.user)
                self.ui.setupUi(self.MainMenu)
                app.widgets.addWidget(self.MainMenu)
                application_widgets_index["MainMenuWindow"] = app.widgets.count() - 1
            else:
                self.ui.user = self.user
                self.ui.setupWindow()
            app.widgets.resize(600,500)
            app.widgets.setCurrentIndex(application_widgets_index["MainMenuWindow"])
        else:
            self.label_error.setText("User Name or Password is incorrect!")
            self.lineedit_user_login.setText("")
            self.lineedit_password.setText("")
            self.lineedit_user_login.setFocus()

    def exit_app(self):
        QtWidgets.QApplication.quit()
"""----------------------------------------------------------------------------------------"""
#Main Menu Code Class
class MainMenuWindow(Ui_mw_main_menu):
    def __init__(self, user ={}):
        super().__init__()
        self.user = user
    
    def setupUi(self, mw_main_menu):
        super().setupUi(mw_main_menu)
        self.setupWindow()
    
    def setupWindow(self):
        if self.user["Role"] == "admin":
            self.pushbutton_admin_menu.setVisible(True)
        else:
            self.pushbutton_admin_menu.setVisible(False)
        self.pushbutton_exit.clicked.connect(self.exit_app)
        self.pushbutton_applications.clicked.connect(self.open_applications)
        self.pushbutton_interviews.clicked.connect(self.open_Interviews)
        self.pushbutton_mentor_meeting.clicked.connect(self.open_mentor_meeting)
        self.pushbutton_admin_menu.clicked.connect(self.open_admin_menu)
        self.pushbutton_logout.clicked.connect(self.open_login)
    
    def open_applications(self):
        if application_widgets_index["ApplicationWindow"] == -1:
            self.ApplicationWindow = QtWidgets.QMainWindow()
            self.ui_applications = ApplicationsWindow()
            self.ui_applications.setupUi(self.ApplicationWindow)
            app.widgets.addWidget(self.ApplicationWindow)
            application_widgets_index["ApplicationWindow"] = app.widgets.count() - 1
        app.widgets.resize(1000,500)
        app.widgets.setCurrentIndex(application_widgets_index["ApplicationWindow"])

    def open_Interviews(self):
        if application_widgets_index["InterviewsWindow"] == -1:
            self.InterviewWindow = QtWidgets.QMainWindow()
            self.ui_interviews = InterviewsWindow(self.user)
            self.ui_interviews.setupUi(self.InterviewWindow)
            app.widgets.addWidget(self.InterviewWindow)
            application_widgets_index["InterviewsWindow"] = app.widgets.count()-1
        app.widgets.resize(1000,500)
        app.widgets.setCurrentIndex(application_widgets_index["InterviewsWindow"])

    def open_mentor_meeting(self):
        if application_widgets_index["MentorMeetingWindow"] == -1:
            self.MentorWindow = QtWidgets.QMainWindow()
            self.ui_mentor = MentorMeetingWindow(self.user)
            self.ui_mentor.setupUi(self.MentorWindow)
            app.widgets.addWidget(self.MentorWindow)
            application_widgets_index["MentorMeetingWindow"] = app.widgets.count()-1
        app.widgets.resize(1000,500)
        app.widgets.setCurrentIndex(application_widgets_index["MentorMeetingWindow"])
    
    def open_admin_menu(self):
        if application_widgets_index["AdminMenuWindow"] == -1:
            self.AdminWindow = QtWidgets.QMainWindow()
            self.ui_admin_menu = AdminMenuWindow(self.user)
            self.ui_admin_menu.setupUi(self.AdminWindow)
            app.widgets.addWidget(self.AdminWindow)
            application_widgets_index["AdminMenuWindow"] = app.widgets.count()-1
        app.widgets.resize(1000,500)
        app.widgets.setCurrentIndex(application_widgets_index["AdminMenuWindow"])

    def open_login(self):
        app.widgets.resize(600,500)
        app.widgets.setCurrentIndex(application_widgets_index["LoginWindow"])
   
    def exit_app(self):
        QtWidgets.QApplication.quit()

"""----------------------------------------------------------------------------------------"""
#Applications Window Code Class
# class ApplicationsWindow(Ui_ApplicationWindow):
#     def __init__(self, user = {}):
#         super().__init__()
#         self.user = user

#     def setupUi(self, mw_applications):
#         super().setupUi(mw_applications)
#         self.PB_return_to_preferences_screen_button.clicked.connect(self.return_preferences)
#         self.PB_exit.clicked.connect(self.exit_app)

class ApplicationsWindow(QtWidgets.QMainWindow, Ui_ApplicationWindow):
    def __init__(self):
        super().__init__()
        #self.user = user
        self.df = DatabaseConnection()
        # self.vit1_df = None
        # self.vit2_df = None
    
    def setupUi(self, mw_applications):
        super().setupUi(mw_applications)
        # Buton click eventlerini bağla
        self.PB_search_button.clicked.connect(self.search_applications)
        self.PB_all_applications_button.clicked.connect(self.show_all_applications)
        self.PB_mentor_meeting_defined_button.clicked.connect(self.show_mentor_assigned)
        self.PB_mentor_interview_undefined_button.clicked.connect(self.show_mentor_unassigned)
        self.PB_duplicate_record_button.clicked.connect(self.show_duplicates)
        self.PB_return_to_preferences_screen_button.clicked.connect(self.return_preferences)
        self.PB_EXIT.clicked.connect(self.exit_app)
    

        # ComboBox için işlevler
        self.CB_combo_box.currentIndexChanged.connect(self.handle_combo_selection)


    def initialize_table(self):


        self.tableWidget.setRowCount(len(self.df))

        # **Verileri tabloya doldur**
        for row in range(len(self.df)):
            for col in range(len(self.df[row])):  # Tüm sütunlar için
                value = str(self.df.iloc[row, col])  # Satır ve sütundaki değeri al
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(value))  # Tabloya ekle


    # 1. Arama işlevi
    def search_applications(self):
        search_text = self.LE_search_input.text().strip().lower()
        if not search_text:
            return

        # Arama filtresi
        mask = self.df['Adınız Soyadınız'].str.lower().str.contains(search_text, na=False)
        filtered_df = self.df[mask]

        # **Tabloyu temizle**
        self.tableWidget.setRowCount(0)
        
        # **Yeni sütunları belirle ve tablo başlıklarını güncelle**
        self.tableWidget.setColumnCount(len(filtered_df.columns))
        self.tableWidget.setHorizontalHeaderLabels(filtered_df.columns)

        # **Yeni verileri tabloya ekle**
        for row_index, row_data in filtered_df.iterrows():
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)  # Yeni satır ekle

            for col_index, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_position, col_index, item)


    # 2. Tüm Başvurular
    def show_all_applications(self):
        self.DataObject = DatabaseConnection()
        query = "SELECT k.adsoyad, projegonderilistarihi, projeningelistarihi FROM projetakiptablosu as p INNER JOIN kursiyerler k ON p.kursiyerid = k.kursiyerid "
        if self.lineEdit.text() != "":
            query += "WHERE adsoyad LIKE '%" + self.lineEdit.text() + "%' "
        query += "ORDER BY p.kursiyerid"
        write_data = self.DataObject.db_select(query)



        # **Verileri tabloya ekle**
        for row_index, row_data in filtered_df.iterrows():
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)  # Yeni satır ekle

            for col_index, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_position, col_index, item)

       
       

    # 3. Mentor Atananlar
    def show_mentor_assigned(self):
        filtered_df = self.df[self.df['Mentor gorusmesi'].str.strip().str.upper() == 'OK']
        
        # Tabloyu temizle
        self.tableWidget.setRowCount(0)
        
        # Yeni başlıkları ayarla
        self.tableWidget.setColumnCount(len(filtered_df.columns))
        self.tableWidget.setHorizontalHeaderLabels(filtered_df.columns.tolist())
        
        # Yeni verileri tabloya ekle
        for row_index, row_data in filtered_df.iterrows():
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)  # Yeni satır ekle
            
            for col_index, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_position, col_index, item)

    # 4. Mentor Atanmayanlar
    def show_mentor_unassigned(self):
        filtered_df = self.df[self.df['Mentor gorusmesi'].str.strip().str.upper() != 'OK']
        
        # Tabloyu temizle
        self.tableWidget.setRowCount(0)
        
        # Yeni başlıkları ayarla
        self.tableWidget.setColumnCount(len(filtered_df.columns))
        self.tableWidget.setHorizontalHeaderLabels(filtered_df.columns.tolist())
        
        # Yeni verileri tabloya ekle
        for row_index, row_data in filtered_df.iterrows():
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)  # Yeni satır ekle
            
            for col_index, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_position, col_index, item)

    
    def show_duplicates(self):
        # Aynı isim-soyisim veya aynı mail adresine sahip kayıtları bul
        mask = self.df.duplicated(subset='Adınız Soyadınız', keep=False) | self.df.duplicated(subset='Mail adresiniz', keep=False)
        duplicates = self.df[mask]
        
        # Tabloyu temizle
        self.tableWidget.setRowCount(0)
        
        # Yeni başlıkları ayarla
        self.tableWidget.setColumnCount(len(duplicates.columns))
        self.tableWidget.setHorizontalHeaderLabels(duplicates.columns.tolist())
        
        # Yeni verileri tabloya ekle
        for row_index, row_data in duplicates.iterrows():
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)  # Yeni satır ekle
            
            for col_index, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_position, col_index, item)

    # 6. ComboBox

    def handle_combo_selection(self):
        selection = self.CB_combo_box.currentText()

        # 'Previous VIT Control' seçildiğinde vit1 ve VIT2 olanları yazdır
        if selection == "    Previous VIT Control":
            filtered_df = self.df[self.df['Basvuru Donemi'].isin(['VIT1', 'VIT2'])]
        
        
        elif selection == "      Different Records":
             # 'Adınız Soyadınız' ve 'Basvuru Donemi' sütunlarını kontrol et
            vit1_vit2_names = self.df[self.df['Basvuru Donemi'].isin(['VIT1', 'VIT2'])]['Adınız Soyadınız'].unique()

            # 'Adınız Soyadınız' sütununda, 'VIT1' ve 'VIT2' olmayanları filtrele
            filtered_df = self.df[~self.df['Adınız Soyadınız'].isin(vit1_vit2_names) | (self.df['Basvuru Donemi'] == 'VIT3')]
            # 'Applying Filter' seçildiğinde, mükerrer isimler olmadan filtreleme işlemi yap
        elif selection == "        Applying Filter":
            # 'Adınız Soyadınız' sütununda benzersiz olanları al
            filtered_df = self.df.drop_duplicates(subset=['Adınız Soyadınız'])
        # Tabloyu temizle
        self.tableWidget.setRowCount(0)

        # Yeni başlıkları ayarla
        self.tableWidget.setColumnCount(len(filtered_df.columns))
        self.tableWidget.setHorizontalHeaderLabels(filtered_df.columns.tolist())

        # Yeni verileri tabloya ekle
        for row_index, row_data in filtered_df.iterrows():
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)  # Yeni satır ekle

            for col_index, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_position, col_index, item)
        
        



    def return_preferences(self):
        app.widgets.resize(600,500)
        app.widgets.setCurrentIndex(application_widgets_index["MainMenuWindow"])

    def exit_app(self):
        QtWidgets.QApplication.quit()

"""----------------------------------------------------------------------------------------"""
#Interviews Window Code Class
class InterviewsWindow(Ui_interviews):
    def __init__(self, user = {}):
        super().__init__()
        self.user = user

    def setupUi(self, mw_applications):
        super().setupUi(mw_applications)
        self.PB_preferences.clicked.connect(self.return_preferences)
        self.PB_interrview_exit.clicked.connect(self.exit_app)
        self.PB_interviews_find.clicked.connect(self.interviews_find)
        self.pb_submittedProjects.clicked.connect(self.submitted_projects)
        self.pb_incomingprojects.clicked.connect(self.incoming_projects)

    
    def interviews_find(self):
        self.DataObject = DatabaseConnection()
        query = "SELECT k.adsoyad, projegonderilistarihi, projeningelistarihi FROM projetakiptablosu as p INNER JOIN kursiyerler k ON p.kursiyerid = k.kursiyerid "
        if self.lineEdit.text() != "":
            query += "WHERE adsoyad LIKE '%" + self.lineEdit.text() + "%' "
        query += "ORDER BY p.kursiyerid"
        write_data = self.DataObject.db_select(query)
        self.fill_table(write_data)

    def submitted_projects(self):
        self.DataObject = DatabaseConnection()
        query = "SELECT k.adsoyad, projegonderilistarihi, projeningelistarihi FROM projetakiptablosu as p INNER JOIN kursiyerler k ON p.kursiyerid = k.kursiyerid "
        query += "WHERE projegonderilistarihi IS NOT NULL "
        query += "ORDER BY p.kursiyerid "
        write_data = self.DataObject.db_select(query)
        self.fill_table(write_data)

    def incoming_projects(self):
        self.DataObject = DatabaseConnection()
        query = "SELECT k.adsoyad, projegonderilistarihi, projeningelistarihi FROM projetakiptablosu as p INNER JOIN kursiyerler k ON p.kursiyerid = k.kursiyerid "
        query += "WHERE projeningelistarihi IS NOT NULL "
        query += "ORDER BY p.kursiyerid "
        write_data = self.DataObject.db_select(query)
        self.fill_table(write_data)

    def fill_table(self, data):
                                           
        self.tw_interviews.setRowCount(len(data))

        for row in range(len(data)):
            for col in range(len(data[row])):
                value = str(data[row][col])
                self.tw_interviews.setItem(row, col,QtWidgets.QTableWidgetItem(value))

    def return_preferences(self):
        app.widgets.resize(600,500)
        app.widgets.setCurrentIndex(application_widgets_index["MainMenuWindow"])
    
    
    def exit_app(self):
        QtWidgets.QApplication.quit()
    

"""---------------------------------------------------------------------------------------"""
#Mentor Meeting Window Code Class
class MentorMeetingWindow(Ui_Mentor):
    def __init__(self, user = {}):
        super().__init__()
        self.user = user
        self.DataObject = DatabaseConnection()
    
    def setupUi(self, mw_applications):
        super().setupUi(mw_applications)
        self.PB_mentor_preferences.clicked.connect(self.return_preferences)
        self.PB_mentor_exit.clicked.connect(self.exit_app)
        self.PB_Mentor_Find.clicked.connect(self.mentor_find)
        self.PB_mentor_all_interviews.clicked.connect(self.mentor_all_interview)
        self.comboBox_Mentor.currentTextChanged.connect(self.mentor_find_status)

    def mentor_all_interview(self):
        write_data =  self.DataObject.db_select("""
                                                SELECT k.adsoyad, gorusmetarihi, mentoradsoyad, bilgisahibimi, yogunlukdurumu, yorumlar 
                                                FROM mentortablosu m
                                                    INNER JOIN kursiyerler k ON m.kursiyerid = k.kursiyerid
                                            """)
        self.tableWidget.setRowCount(len(write_data))
        for row in range(len(write_data)):
            for col in range(len(write_data[row])):
                if col == 0:
                    value = str(write_data[row][col]).split(" ")[0]
                    self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(value))
                    value = str(write_data[row][col]).split(" ")[1]
                    self.tableWidget.setItem(row, col+1, QtWidgets.QTableWidgetItem(value))
                else :    
                    value = str(write_data[row][col])
                    self.tableWidget.setItem(row, col+1, QtWidgets.QTableWidgetItem(value))
    
    def mentor_find(self):
        query = "SELECT k.adsoyad, gorusmetarihi, mentoradsoyad, bilgisahibimi, yogunlukdurumu, yorumlar "
        query += "FROM mentortablosu m INNER JOIN kursiyerler k ON m.kursiyerid = k.kursiyerid "
        query += "WHERE k.adsoyad LIKE '%" + self.lineEdit.text() + "%'"
        write_data =  self.DataObject.db_select(query)
        self.tableWidget.setRowCount(len(write_data))
        for row in range(len(write_data)):
            for col in range(len(write_data[row])):
                if col == 0:
                    value = str(write_data[row][col]).split(" ")[0]
                    self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(value))
                    value = str(write_data[row][col]).split(" ")[1]
                    self.tableWidget.setItem(row, col+1, QtWidgets.QTableWidgetItem(value))
                else :    
                    value = str(write_data[row][col])
                    self.tableWidget.setItem(row, col+1, QtWidgets.QTableWidgetItem(value))
        

    
    def mentor_find_status(self):
        selection = self.comboBox_Mentor.currentText()
        if selection == "All":
             write_data =  self.DataObject.db_select("""
                                                SELECT k.adsoyad, gorusmetarihi, mentoradsoyad, bilgisahibimi, yogunlukdurumu, yorumlar 
                                                FROM mentortablosu m
                                                    INNER JOIN kursiyerler k ON m.kursiyerid = k.kursiyerid
                                            """)
        else:
            query = "SELECT k.adsoyad, gorusmetarihi, mentoradsoyad, bilgisahibimi, yogunlukdurumu, yorumlar "
            query += "FROM mentortablosu m INNER JOIN kursiyerler k ON m.kursiyerid = k.kursiyerid "
            query += "WHERE yogunlukdurumu = '" + self.comboBox_Mentor.text() + "'"
            write_data =  self.DataObject.db_select(query)
        
        self.tableWidget.setRowCount(len(write_data))
        for row in range(len(write_data)):
            for col in range(len(write_data[row])):
                if col == 0:
                    value = str(write_data[row][col]).split(" ")[0]
                    self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(value))
                    value = str(write_data[row][col]).split(" ")[1]
                    self.tableWidget.setItem(row, col+1, QtWidgets.QTableWidgetItem(value))
                else :    
                    value = str(write_data[row][col])
                    self.tableWidget.setItem(row, col+1, QtWidgets.QTableWidgetItem(value))
        
        
    def return_preferences(self):
        app.widgets.resize(600,500)
        app.widgets.setCurrentIndex(application_widgets_index["MainMenuWindow"])
    
    def exit_app(self):
        QtWidgets.QApplication.quit()
   

"""---------------------------------------------------------------------------------------"""
#Admin Menu Window Code Class
class AdminMenuWindow(Ui_mwAdminMenu):
    def __init__(self, user = {}):
        super().__init__()
        self.user = user
    
    def setupUi(self, mw_applications):
        super().setupUi(mw_applications)
        self.pbPreferedAdmin.clicked.connect(self.open_preferences)
        self.pbExit.clicked.connect(self.exit_app)
        self.pbActionControl.clicked.connect(self.open_action_control)
        self.pbSendMail.clicked.connect(self.open_send_mail)

    def open_action_control(self):
        self.obj_calendar = GoogleCalendarManager("seracc_calendar.json")
        self.obj_calendar.get_calendar_events()
        
        if not self.obj_calendar.events:
            print('No upcoming events found.')
        else:
            self.tableWidget.setRowCount(len(self.obj_calendar.events))
            self.tableWidget.setColumnCount(4)
            row_count = 0
            for event in self.obj_calendar.events:
                 for event in self.obj_calendar.events:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    participant = []
                    organizer = event['organizer']['email']
                    if "attendees" in event:
                        for attendee in event['attendees']:
                            if organizer != attendee["email"] and attendee["email"] not in participant:
                                participant.append(attendee["email"])
                    action_name = event["summary"]
                    self.tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(action_name))
                    self.tableWidget.setItem(row_count, 1, QtWidgets.QTableWidgetItem(start))
                    if len(participant) == 0:
                        self.tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(""))
                    else:
                        self.tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(participant[0])))
                    self.tableWidget.setItem(row_count, 3, QtWidgets.QTableWidgetItem(organizer))
                    row_count += 1
    
    def open_send_mail(self):
        object_mail = MailSender()
        summary = self.obj_calendar.events[self.tableWidget.currentRow()]["summary"]
        start = self.obj_calendar.events[self.tableWidget.currentRow()]["start"]["dateTime"]
        end = self.obj_calendar.events[self.tableWidget.currentRow()]["end"]["dateTime"]
        sender_email = self.obj_calendar.events[self.tableWidget.currentRow()]["organizer"]["email"]
        location = "Google Meet"
        description = "VIT Appointment"
        if self.obj_calendar.events[self.tableWidget.currentRow()]["attendees"]:
            recipient_email = self.obj_calendar.events[self.tableWidget.currentRow()]["attendees"][1]["email"]
        else:
            return False
        object_mail.create_ics_file(summary, start, end, description, location)
        subject = f"Appointment: {summary}"
        mail_content = f"""Hello,

                    We invite you to "{summary}" event.

                    Start: {start}
                    Finish: {end}
                    Location: {location}

                    Please accept the invitation and add it to your calendar.

                    Kind regards,
                    {sender_email}
                    """
        if object_mail.send_appointment_email(recipient_email, subject, mail_content):
            #QMessageBox.information(self, "Information", "Email sent successfully!")
            self.statusbar.showMessage("Email sent successfully!")
            #print("Email sent successfully!")            
        else:
            #QMessageBox.information(self, "Information", "Failed to send email.")
            #print("Failed to send email.")
            self.statusbar.showMessage("Failed to send email.")
        
    def open_preferences(self):
        app.widgets.resize(600,500)
        app.widgets.setCurrentIndex(application_widgets_index["MainMenuWindow"])

    def exit_app(self):
        QtWidgets.QApplication.quit() 
        

"""----------------------------------------------------------------------------------------"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = LoginWindow()
    ui.setupUi(MainWindow)
    app.widgets = QtWidgets.QStackedWidget()
    app.widgets.addWidget(MainWindow)
    app.widgets.show()
    sys.exit(app.exec())
