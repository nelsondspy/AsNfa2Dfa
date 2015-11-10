# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui_entrada.ui'
#
# Created: Tue Oct 22 12:56:08 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

"""Clase que tratara con la intefaz grafica a fin modificar lo menos posible el codigo generado 
por la herramienta de qt 
"""


"""
Codigo generado por la herramienta de pyqt4
"""


class Ui_Form(object):
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(620, 375)
        
        self.listWidget_Alfabetos = QtGui.QListWidget(Form)
        self.listWidget_Alfabetos.setGeometry(QtCore.QRect(80, 120, 421, 71))
        self.listWidget_Alfabetos.setObjectName(_fromUtf8("listWidget_Alfabetos"))
        
        self.lineEdit_AlfabetoNombre = QtGui.QLineEdit(Form)
        self.lineEdit_AlfabetoNombre.setGeometry(QtCore.QRect(170, 70, 113, 20))
        self.lineEdit_AlfabetoNombre.setObjectName(_fromUtf8("lineEdit_AlfabetoNombre"))
        
        self.pushButton_Agregar = QtGui.QPushButton(Form)
        self.pushButton_Agregar.setGeometry(QtCore.QRect(290, 70, 75, 23))
        
        
        
        self.pushButton_Agregar.setObjectName(_fromUtf8("pushButton_Agregar"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.lineEdit_simbolo = QtGui.QLineEdit(Form)
        self.lineEdit_simbolo.setGeometry(QtCore.QRect(170, 90, 40, 20))
        self.lineEdit_simbolo.setObjectName(_fromUtf8("lineEdit_simbolo"))
        
        
        #lista de simbolos 
        self.edt_lssimb = QtGui.QLineEdit(Form)
        self.edt_lssimb.setGeometry(QtCore.QRect(220, 90, 120, 20))
        self.edt_lssimb.setObjectName(_fromUtf8("edt_lssimb"))
        
        
        
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 90, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        
        
        
        self.label_defregular = QtGui.QLabel(Form)
        self.label_defregular.setGeometry(QtCore.QRect(30, 50, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_defregular.setFont(font)
        self.label_defregular.setObjectName(_fromUtf8("label_defregular"))
        self.label_alfabetos = QtGui.QLabel(Form)
        self.label_alfabetos.setGeometry(QtCore.QRect(30, 220, 115, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_alfabetos.setFont(font)
        self.label_alfabetos.setObjectName(_fromUtf8("label_alfabetos"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 240, 420, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.btn_procesar = QtGui.QPushButton(Form)
        self.btn_procesar.setGeometry(QtCore.QRect(80, 300, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_procesar.setFont(font)
        self.btn_procesar.setStyleSheet(_fromUtf8("color:rgb(27, 27, 81)\n"
""))
        self.btn_procesar.setObjectName(_fromUtf8("btn_procesar"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 403, 30))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btn_acercade = QtGui.QPushButton(Form)
        self.btn_acercade.setGeometry(QtCore.QRect(580, 0, 40, 23))
        self.btn_acercade.setObjectName(_fromUtf8("btn_acercade"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Reg-Tool", None))
        self.pushButton_Agregar.setText(_translate("Form", "Agregar", None))
        self.label_2.setText(_translate("Form", "Nombre Alfabeto:", None))
        self.label.setText(_translate("Form", "Simbolo:", None))
        self.label_defregular.setText(_translate("Form", "Alfabetos", None))
        self.label_alfabetos.setText(_translate("Form", "Definición regular", None))
        self.btn_procesar.setText(_translate("Form", "Procesar", None))
        self.label_3.setText(_translate("Form", "1-Defina nuevos alfabetos  2-seleccione los que utilizara  \n3-Ingrese la expresion regular  4-Procesar", None))
        self.btn_acercade.setText(_translate("Form", "...?", None))
        self.edt_lssimb.setText(_translate("Form", "", None))
        
        ############
        self.btn_ejecutar = QtGui.QPushButton(Form)
        self.btn_ejecutar.setGeometry(QtCore.QRect(430, 295, 90, 26))
        self.btn_ejecutar.setText("Ejecutar codigo")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_ejecutar.setFont(font)        
        ############
        
        
        #self.listWidget_Alfabetos.addItems( self.lineEdit_simbolo.text())
    
    def buttonClicked(self):
        nombre = self.lineEdit_AlfabetoNombre.text()
        #modelo_gui.nuevo_alfabeto(nombre )
        item = QtGui.QListWidgetItem()
        item.setText(nombre)
        self.listWidget_Alfabetos.addItem(item)
    
####################################################################
class MyLineEdit(QtGui.QLineEdit):
    def __init__(self, *args):
        QtGui.QLineEdit.__init__(self, *args)

    def event(self, event):
        if (event.type()==QtCore.QEvent) and (event.key()==QtCore.Qt.Key_Enter):
            self.emit(QtCore.SIGNAL("enterPressed"))
            return True
        return QtGui.QLineEdit.event(self, event)

############################################################        


