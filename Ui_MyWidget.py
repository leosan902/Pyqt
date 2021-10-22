# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import requests
import xmltodict

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")    
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 90, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 340, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 340, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 290, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(540, 290, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(510, 240, 141, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 240, 141, 31))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Converter)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #Pegar nomes        
        url = 'https://economia.awesomeapi.com.br/xml/available/uniq'
        data= requests.get(url)
        doc = xmltodict.parse(data._content)
        self.comboBox.addItems(doc['xml'].keys())
        self.comboBox_2.addItems(doc['xml'].keys())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Converter"))
        self.label.setText(_translate("MainWindow", "Converter de Moeda"))
        self.label_2.setText(_translate("MainWindow", "Moeda 1"))
        self.label_3.setText(_translate("MainWindow", "Moeda 2"))
        
    def Converter(self):
        try:
            self.lineEdit.clear()
            url = 'https://economia.awesomeapi.com.br/json/last/'
            valConv = requests.get(url+self.comboBox.currentText()+"-"+self.comboBox_2.currentText()).json()
            valConv = valConv[self.comboBox.currentText()+self.comboBox_2.currentText()]["ask"]
            self.lineEdit.setText(str(float(valConv)*float(self.textEdit.toPlainText())))
        except Exception as err:
            url = 'https://economia.awesomeapi.com.br/xml/available'
            data= requests.get(url)
            doc = xmltodict.parse(data._content)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText("A Api nao aceita essa conversao Use Essas:\n" +str(doc['xml'].keys()) )
            msg.setWindowTitle("Error")
            msg.exec_()

    
        

