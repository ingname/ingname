import sys, os
from cfg import host, user, db_name, password, port
from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
from PyQt5.QtGui import QPixmap


class Ui_Dialog_2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Medic")
        Dialog.resize(1011, 637)
        icon = QtGui.QIcon("img/1.png")
        Dialog.setWindowIcon(icon)

        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1011, 581))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(810, 0, 161, 161))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(73, 140, 81);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setLineWidth(5)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(370, 0, 270, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(820, 500, 171, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(810, 170, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(810, 190, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(810, 220, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(73, 140, 81);")
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 161, 161))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(73, 140, 81);")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setLineWidth(0)
        self.label_8.setText("")
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 161, 161))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(73, 140, 81);")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setLineWidth(0)
        self.label_9.setText("")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(370, 0, 270, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(490, 400, 181, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setEnabled(True)
        self.label_15.setGeometry(QtCore.QRect(230, 200, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(710, 250, 221, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setEnabled(True)
        self.label_16.setGeometry(QtCore.QRect(230, 250, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setEnabled(True)
        self.label_17.setGeometry(QtCore.QRect(230, 300, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setTextFormat(QtCore.Qt.AutoText)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(460, 250, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(460, 300, 231, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setEnabled(True)
        self.label_19.setGeometry(QtCore.QRect(0, 460, 1011, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setTextFormat(QtCore.Qt.AutoText)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(460, 200, 231, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_12.setGeometry(QtCore.QRect(710, 150, 221, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setEnabled(True)
        self.label_22.setGeometry(QtCore.QRect(230, 150, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("")
        self.label_22.setTextFormat(QtCore.Qt.AutoText)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setEnabled(True)
        self.label_23.setGeometry(QtCore.QRect(460, 150, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("")
        self.label_23.setTextFormat(QtCore.Qt.AutoText)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(370, 40, 270, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(19)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 161, 161))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(73, 140, 81);")
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setLineWidth(0)
        self.label_12.setText("")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.tableView = QtWidgets.QTableView(self.tab_3)
        self.tableView.setGeometry(QtCore.QRect(10, 170, 991, 361))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.tableView.setFont(font)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 590, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setEnabled(True)
        self.label_13.setGeometry(QtCore.QRect(0, 580, 1011, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(73, 140, 81);")
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_13.close()
        self.label_19.close()

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.now = 600
        self.now_m = 20
        self.now_s = 0
        self.now2 = 59


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Medic"))
        self.label.setText(_translate("Dialog", "Главная"))
        self.pushButton_8.setText(_translate("Dialog", "Выйти"))
        self.label_3.setText(_translate("Dialog", "Владимиров"))
        self.label_5.setText(_translate("Dialog", "Кирилл"))
        self.label_7.setText(_translate("Dialog", "Лаборант"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Главная"))
        self.label_10.setText(_translate("Dialog", "Заказ"))
        self.pushButton_9.setText(_translate("Dialog", "Сформировать заказ"))
        self.label_15.setText(_translate("Dialog", "Перечень услуг"))
        self.pushButton_10.setText(_translate("Dialog", "Добавить пациента"))
        self.label_16.setText(_translate("Dialog", "Фамилия"))
        self.label_17.setText(_translate("Dialog", "Имя"))
        self.label_19.setText(_translate("Dialog", "Вы ввели не существующего пациента, проверьте данные или добавьте пациента"))
        self.pushButton_11.setText(_translate("Dialog", "Добавить услуги"))
        self.pushButton_12.setText(_translate("Dialog", "Сгенерировать шриткод"))
        self.label_22.setText(_translate("Dialog", "Шртихкод"))
        self.label_23.setText(_translate("Dialog", "Штрихкодик"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Заказ"))
        self.label_11.setText(_translate("Dialog", "Просмотреть отчет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Просмотреть отчет"))
        self.label_2.setText(_translate("Dialog", "10:24"))
        self.label_13.setText(_translate("Dialog", "Окончание времени сеанса"))
        self.label_23.setText('')


    def qrcode(self):
        pass

    def insert(self):
        connection = False

        with open('data_user.txt', 'r', encoding='utf-8') as f:
            data_user = f.read()

        with open('data_pass.txt', 'r', encoding='utf-8') as f:
            data_pass = f.read()

        login = str(data_user)
        passw = str(data_pass)

        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                port=port,
                database=db_name,
                password=password
            )

            with connection.cursor() as cursor:
                cursor.execute(
                    f"""SELECT name, lastname
    FROM public.users WHERE login = '{login}' AND password = '{passw}';"""
                )
                result = cursor.fetchall()

        except Exception as _ex:
            print("[ИНФО] Ошибка при работе с PostrgeSQL", _ex)
        finally:
            if connection:
                cursor.close()
                connection.close()

        self.label_5.setText(f'{result[0][0]}')
        self.label_3.setText(f'{result[0][1]}')
        self.pushButton_12.clicked.connect(lambda: self.qrcode())

        pixmap = QPixmap("img/1.png")
        self.label_8.setPixmap(pixmap)
        self.label_8.resize(pixmap.width(), pixmap.height())
        self.label_9.setPixmap(pixmap)
        self.label_9.resize(pixmap.width(), pixmap.height())
        self.label_12.setPixmap(pixmap)
        self.label_12.resize(pixmap.width(), pixmap.height())
        pixmap = QPixmap("img/laborant_1.jpg")
        self.label_4.setPixmap(pixmap)
        self.label_4.resize(pixmap.width(), pixmap.height())
        os.remove("data_pass.txt")
        os.remove("data_user.txt")


    def exits(self):
        try:
            print('[ИНФО] Приложение закрыто по кнопке')
            sys.exit(QtWidgets.QApplication(sys.argv))
        except Exception as _ex:
            print(f'[ИНФО] Следующая ошибка: {_ex}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
