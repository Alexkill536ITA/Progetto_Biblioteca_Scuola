# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Panello_admin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import time
from PyQt5 import QtCore, QtGui, QtWidgets
import Connect_DB as cndb

type_modifica = 0
active_mod = False

class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.tableView = QtWidgets.QTableWidget(Form)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.cellDoubleClicked.connect(self.modifica)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.exit_Indietro = QtWidgets.QPushButton(Form)
        self.exit_Indietro.setMinimumSize(QtCore.QSize(130, 30))
        self.exit_Indietro.setMaximumSize(QtCore.QSize(130, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/igs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_Indietro.setIcon(icon)
        self.exit_Indietro.setObjectName("exit_Indietro")
        self.horizontalLayout_2.addWidget(self.exit_Indietro)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Inserisci_maestra = QtWidgets.QPushButton(Form)
        self.Inserisci_maestra.setMinimumSize(QtCore.QSize(110, 30))
        self.Inserisci_maestra.setMaximumSize(QtCore.QSize(110, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Icons/maestra.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inserisci_maestra.setIcon(icon1)
        self.Inserisci_maestra.setObjectName("Inserisci_maestra")
        self.horizontalLayout.addWidget(self.Inserisci_maestra)
        self.Inserisci_bimbo = QtWidgets.QPushButton(Form)
        self.Inserisci_bimbo.setMinimumSize(QtCore.QSize(110, 30))
        self.Inserisci_bimbo.setMaximumSize(QtCore.QSize(110, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Icons/bimbo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inserisci_bimbo.setIcon(icon2)
        self.Inserisci_bimbo.setObjectName("Inserisci_bimbo")
        self.horizontalLayout.addWidget(self.Inserisci_bimbo)
        self.Inserisci_libro = QtWidgets.QPushButton(Form)
        self.Inserisci_libro.setMinimumSize(QtCore.QSize(110, 30))
        self.Inserisci_libro.setMaximumSize(QtCore.QSize(110, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inserisci_libro.setIcon(icon3)
        self.Inserisci_libro.setObjectName("Inserisci_libro")
        self.horizontalLayout.addWidget(self.Inserisci_libro)
        self.Salva_modifice = QtWidgets.QPushButton(Form)
        self.Salva_modifice.setMinimumSize(QtCore.QSize(110, 30))
        self.Salva_modifice.setMaximumSize(QtCore.QSize(110, 30))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Icons/iconfinder_Compose_1891025.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Salva_modifice.setIcon(icon4)
        self.Salva_modifice.setObjectName("Salva_modifice")
        self.horizontalLayout.addWidget(self.Salva_modifice)
        self.Elimina = QtWidgets.QPushButton(Form)
        self.Elimina.setMinimumSize(QtCore.QSize(110, 30))
        self.Elimina.setMaximumSize(QtCore.QSize(110, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Icons/iconfinder_Close_1891023.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Elimina.setIcon(icon5)
        self.Elimina.setObjectName("Elimina")
        self.horizontalLayout.addWidget(self.Elimina)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Bambini")
        self.comboBox.addItem("Maestre")
        self.comboBox.addItem("Libri")
        self.comboBox.addItem("Prestiti")
        self.comboBox.currentTextChanged.connect(self.Table_Select_SQL)
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.Parametro_ricerca = QtWidgets.QComboBox(Form)
        self.Parametro_ricerca.setMinimumSize(QtCore.QSize(120, 25))
        self.Parametro_ricerca.setMaximumSize(QtCore.QSize(120, 25))
        self.Parametro_ricerca.setObjectName("Parametro_ricerca")
        self.horizontalLayout_3.addWidget(self.Parametro_ricerca)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.linedit = QtWidgets.QLineEdit(Form)
        self.linedit.setMinimumSize(QtCore.QSize(120, 25))
        self.linedit.setMaximumSize(QtCore.QSize(120, 25))
        self.linedit.setObjectName("Parametro_key")
        self.horizontalLayout_3.addWidget(self.linedit)
        self.Cerca = QtWidgets.QPushButton(Form)
        self.Cerca.setMinimumSize(QtCore.QSize(75, 25))
        self.Cerca.setMaximumSize(QtCore.QSize(75, 25))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Icons/iconfinder_icon-ios7-search-strong_211817.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cerca.setIcon(icon6)
        self.Cerca.setObjectName("Cerca")
        self.horizontalLayout_3.addWidget(self.Cerca)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.exit_Indietro.setText("Esci e Trona al Menu")
        self.Inserisci_maestra.setText("Inserisci Maestra")
        self.Inserisci_bimbo.setText("Inserisci Bimbo")
        self.Inserisci_libro.setText("Inserisci Libro")
        self.Salva_modifice.setText( "Modifica")
        self.Elimina.setText("Elimina")
        self.label.setText("Seleziona Tabella:")
        self.label_3.setText("Panello Gestione Database")
        self.label_4.setText("Data di oggi: "+time.strftime("%d/%m/%Y"))
        self.label_2.setText("Ricerca per:")
        self.label_5.setText("Parola chiave:")
        self.Cerca.setText("Cerca")
#        self.Inserisci_bimbo.clicked.connect(self.inserimento_new_profilo_C)
        # self.Inserisci_libro.clicked.connect(self.Inserimeto_libri)
        # self.Inserisci_maestra.clicked.connect(self.inserimento_new_profilo_A)
        self.Salva_modifice.clicked.connect(self.modifica)
 #       self.Elimina.clicked.connect(self.elimina)
        # self.exit_Indietro.clicked.connect(self.finestra1)
 #       self.Cerca.clicked.connect(self.cerca_per)

        self.Table_Select_SQL()
        self.centralWidget().setLayout(self.gridLayout)
        self.show()


    def Table_Select_SQL(self):
        global type_modifica
        sel_db = self.comboBox.currentText()
        if(sel_db == "Bambini"):
            self.Show_Table(cndb.show_client())
            self.Parametro_ricerca.clear()
            self.Parametro_ricerca.addItem("nome")
            self.Parametro_ricerca.addItem("cognome")
            self.Parametro_ricerca.addItem("classe")
            colum_text = ["","","","","",""]
            self.tableView.setHorizontalHeaderLabels(colum_text)
            colum_text = ["ID","COGNOME","NOME","CLASSE","ANNI","FOTO"]
            self.tableView.setHorizontalHeaderLabels(colum_text)
            type_modifica = 0
            return 0
        if(sel_db == "Maestre"):
            self.Show_Table(cndb.show_admin())
            self.Parametro_ricerca.clear()
            self.Parametro_ricerca.addItem("nome")
            self.Parametro_ricerca.addItem("cognome")
            colum_text = ["","","","","",""]
            self.tableView.setHorizontalHeaderLabels(colum_text)
            colum_text = ["ID","COGNOME","NOME","AMMINISTRETORE",]
            self.tableView.setHorizontalHeaderLabels(colum_text)
            type_modifica = 1
            return 0
        if(sel_db == "Libri"):
            self.Show_Table(cndb.show_book())
            self.Parametro_ricerca.clear()
            self.Parametro_ricerca.addItem("titolo")
            self.Parametro_ricerca.addItem("autore")
            self.Parametro_ricerca.addItem("disponibilità")
            colum_text = ["","","","","",""]
            self.tableView.setHorizontalHeaderLabels(colum_text)
            colum_text = ["ID","COGNOME","NOME","CLASSE","ANNI","FOTO"]
            self.tableView.setHorizontalHeaderLabels(colum_text)
            type_modifica = 3
            return 0
        if(sel_db == "Prestiti"):
            self.Show_Table(cndb.show_logs_book())
            colum_text = ["","","","","",""]
            self.tableView.setHorizontalHeaderLabels(colum_text)
            colum_text = ["ID","BAMBINO","LIBRO","DATA PRESTITO","DATA RESTITUITO"]
            self.tableView.setHorizontalHeaderLabels(colum_text)
            return 0
        else:
            print("ERROR")
              
    def Show_Table(self, table):
        result = table
        print(result)
        self.tableView.setColumnCount(6)
        self.tableView.setRowCount(0)
        for row_index, row_data in enumerate(result):
            self.tableView.insertRow(row_index)
            for colum_number, data in enumerate(row_data):
                self.tableView.setItem(row_index, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        cndb.close_db()
    
    def modifica(self):
        global type_modifica, active_mod
        id_linea = self.tableView.currentItem().row()
        id_Finale = self.tableView.item(id_linea,0).text()
        print(id_Finale)
        active_mod = True
        if(type_modifica == 0):
            self.inserimento_new_profilo_C(active_mod,id_Finale)
        elif(type_modifica == 1):
            self.inserimento_new_profilo_A(active_mod,id_Finale)
        elif(type_modifica == 2):
            self.Inserimeto_libri(active_mod,id_Finale)
        else:
            print("ERRORE")
        
        
    
    #def Cerca(self):
      #  cndb.


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
