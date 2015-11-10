
import sys 
from Modelo_GUI import Modelogui
from gui_entrada import Ui_Form
from PyQt4 import QtCore, QtGui
from anlex import SimbolosAdmin
from  main_consola import principal
from config import DIR_SALIDA_CODIGO , PREFIJO_ARCHIVO_GEN
import os 
class MyForm(QtGui.QMainWindow):
    
    modelo_gui  = Modelogui()
    simbolos_admin = SimbolosAdmin()
    __listasimbolos = []
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        ######
        self.connect(self.ui.lineEdit_simbolo, QtCore.SIGNAL("returnPressed()"),self.simbolo_enter )
        self.ui.pushButton_Agregar.clicked.connect(self.agregar_alfabeto_click)
        self.ui.btn_procesar.clicked.connect(self.procesar_click)
        self.ui.btn_ejecutar.clicked.connect(self.ejecutar_click)
        self.llena_lista_alfabetos()

                     
    def simbolo_enter(self):
        simb = self.ui.lineEdit_simbolo.text()
        if len(simb ) > 0 and not simb in self.__listasimbolos :
            self.__listasimbolos.append(str(simb))
            self.ui.edt_lssimb.setText(str(self.__listasimbolos ))
            self.ui.lineEdit_simbolo.setText('')
        else:
            self.__msg("Ingrese el nuevo simbolo y presione enter")
    
    def agregar_alfabeto_click(self):
        nombre = str(self.ui.lineEdit_AlfabetoNombre.text())
        if len(nombre)>0:
            if self.simbolos_admin.agregar_alfabeto(nombre, self.__listasimbolos) :
                self.llena_lista_alfabetos()
                self.__listasimbolos = []
                print self.simbolos_admin.alfabetos
        else:
            self.__msg("Ingrese el nombre del alfabeto")
        
    def llena_lista_alfabetos(self):
        self.ui.listWidget_Alfabetos.clear()
        for alfabeto in self.simbolos_admin.alfabetos:
            item = QtGui.QListWidgetItem()
            item.setCheckState(True)
            item.setText(alfabeto  + "=" + str (self.simbolos_admin.alfabetos[alfabeto]) )
            
            self.ui.listWidget_Alfabetos.addItem(item)
    
    def __msg(self, mensaje):
        QtGui.QMessageBox.about(self, "Validacion", mensaje )
    
    """Metodo que activado por la emision del click en procesar """
    def procesar_click(self):
        defregular = str(self.ui.lineEdit.text())
        if len(defregular)> 0 :
            #selecciona solo los alfabetos marcados
            self.filtrar_marcados()
            
            try:
                #se llama al metodo principal, el que desencadena todas la acciones
                principal(self.simbolos_admin,defregular)
            except Exception as e:
                self.__msg(str(e))
        else:
            self.__msg("Ingrese la definicion regular")
    
    def filtrar_marcados(self):
        
        items = self.ui.listWidget_Alfabetos.selectedIndexes()
        nuevoalfab = SimbolosAdmin() 
        cont = 0 
        print "los items!! " , items
        for alfa in self.simbolos_admin.alfabetos :
            #si esta marcado se debe permitir usar el alfabeto
            if not cont in items:
                nuevoalfab.alfabetos[alfa]= self.simbolos_admin.alfabetos[alfa]
                cont +=1
        print "este es el que se va " , nuevoalfab.alfabetos
        return nuevoalfab
    
    def ejecutar_click(self):
        os.system("python ./" + DIR_SALIDA_CODIGO + os.sep + PREFIJO_ARCHIVO_GEN)
    
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
    
