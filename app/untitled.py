from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Medic")
        Dialog.resize(1011, 637)
        icon = QtGui.QIcon("img/1.png")
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(365, 40, 270, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(73, 140, 81);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 270, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 310, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(330, 230, 170, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 270, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(True)

        self.pushButton_2.clicked.connect(lambda: self.zvezda())
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 310, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 400, 600, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 440, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 180, 200, 200))
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
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(550, 270, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_2.close()
        self.label_3.close()
        self.pushButton_3.hide()
        self.lineEdit_3.hide()
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(True)

        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(550, 270, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("")
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_18.setText('')
        self.lineEdit_3.setText('')

        self.time_error = 0


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def zvezda(self):
        if self.pushButton_2.isChecked():
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Medic"))
        self.label.setText(_translate("Dialog", "Авторизация"))
        self.pushButton.setText(_translate("Dialog", "Войти"))
        self.pushButton_2.setText(_translate("Dialog", "*"))
        self.pushButton_3.setText(_translate("Dialog", "Заменить каптчу"))
        self.lineEdit.setText(_translate("Dialog", "chacking0"))
        self.lineEdit_2.setText(_translate("Dialog", "4tzqHdkqzo4"))
        self.label_2.setText(_translate("Dialog", "Вы ввели не правильные данные"))
        self.label_3.setText(_translate("Dialog", "10 сек."))
        self.label_5.setText(_translate("Dialog", "Показать пароль"))
