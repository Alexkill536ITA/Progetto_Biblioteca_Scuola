import sys
import os
import time
from PyQt5 import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QEvent, QObject, pyqtSignal
import shutil
import sqlite3
from sqlite3 import Error
import Connect_DB as cndb


#Variabli Globali
client = True
admin = False
Root = os.getcwd()
nome = ""
cognome = ""
id_libro = ""
id_bimbo = ""
id_Maestra = ""
id_log = ""
New_Patch_avatar = ""
New_Patch_Cover = ""
genere = ""
type_modifica = 0
active_mod = False
rest = False

#Widget To Make Clickable
def clickable(widget):
    class Filter(QObject): 
        clicked = pyqtSignal()
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


class MainWindow(QtWidgets.QMainWindow):

#init main run    
    def  __init__(self,parent = None):
        super().__init__()

        #creazione barra del menu
        bar = self.menuBar()

        #aggiunta sezione file
        file = bar.addMenu("File")

        #comando nuovo utente
        new_user_action = QtWidgets.QAction("Nuovo utente", self)
        new_user_action.setShortcut('Ctrl+N')
        file.addAction(new_user_action)

        #comando cancella utente
        del_user_action = QtWidgets.QAction("Cancella utente", self)
        del_user_action.setShortcut('Ctrl+D')
        file.addAction(del_user_action)

        #comando esci dal programma
        quit_action = QtWidgets.QAction('Esci', self)
        quit_action.setShortcut('Ctrl+Q')
        file.addAction(quit_action)
        quit_action.triggered.connect(self.quit_trigger)

        #aggiunta sezione opzioni
        opzioni = bar.addMenu("Opzioni")

        #sottosezione tema
        theme = opzioni.addMenu("Cambia tema")

        #comando colori
        grey = QtWidgets.QAction("Grigio", self)
        theme.addAction(grey)
        coral = QtWidgets.QAction("Corallo", self)
        theme.addAction(coral)
        pink = QtWidgets.QAction("Rosa", self)
        theme.addAction(pink)

        #richiamo delle funzioni per colorare lo sfondo
        grey.triggered.connect(self.color_theme)
        coral.triggered.connect(self.color_theme)
        pink.triggered.connect(self.color_theme)

        #aggiunta sezinone info
        info = bar.addMenu("Info")

        #sottosezione creatori
        creators = QtWidgets.QAction("Creatori", self)
        info.addAction(creators)

        creators.triggered.connect(self.credits)

        #stylesheet della barra menu
        bar.setStyleSheet('background-color: white; color: black')

        # risoluzione della finestra e posizione nel monitor
        screen_resolution = app.desktop().screenGeometry()
        self.width = screen_resolution.width()
        self.height = screen_resolution.height()
        self.setGeometry(self.width // 2 - 1280 // 2,
                         self.height // 2 - 720 // 2, 1280, 720)

        self.font_size = self.width // 1000

        # colore di sfondo
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor('#41383C'))
        self.setPalette(p)

        self.finestra1()

#Clear Variabili Globali
    def Clear_Variabili_Glogals(self):
        global client,admin,nome,cognome,id_libro,id_libro,id_Maestra,New_Patch_avatar,New_Patch_Cover,genere,type_modifica, active_mod
        client = True
        admin = False
        nome = ""
        cognome = ""
        id_libro = ""
        id_bimbo = ""
        id_Maestra = ""
        New_Patch_avatar = ""
        New_Patch_Cover = ""
        genere = ""
        type_modifica = 0
        active_mod = False
        rest = False

#Main Windows
    def finestra1(self):
        #QWidget presenti nella finestra
        self.Clear_Variabili_Glogals()
        self.log_button = QtWidgets.QPushButton("Accedi")
        self.log_button.setMaximumWidth(100)
        self.log_button.setStyleSheet('width: '+str(self.font_size*100)+'px; font-size: '+str(self.font_size*15)+'px')
        self.type_profile_label = QtWidgets.QLabel("Bambino")
        self.textEditor = QtWidgets.QLineEdit(self)
        self.textEditor.setPlaceholderText("Inserisci il nome:")
        self.textEditor.setMaximumWidth(300)
        self.textEditor.setStyleSheet('font-size: '+str(15*self.font_size)+'px')
        self.textEditor_pass = QtWidgets.QLineEdit(self)
        self.textEditor_pass.setPlaceholderText("Inserisci il cognome:")
        self.textEditor_pass.setMaximumWidth(300)
        self.textEditor_pass.setStyleSheet('font-size: '+str(15*self.font_size)+'px')
        self.image_profile = QtWidgets.QLabel()
        self.other_profile = QtWidgets.QPushButton("Accedi come maestra")

        #immagine profilo background al QLabel
        pixmap = QtGui.QPixmap('Icons/bimbo.png')
        pixmap = pixmap.scaledToWidth(250)
        pixmap = pixmap.scaledToHeight(250)
        self.image_profile.setPixmap(pixmap)

        #titolo della finestra
        self.setWindowTitle("Biblioteca")

        #icona della finestra
        self.setWindowIcon(QtGui.QIcon('Icons/logo.png'))

        #impostazione del layout principale
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.v_box1 = QtWidgets.QVBoxLayout()
        self.v_box1.addStretch()

        #creazione layout con LineEdit
        self.h_box1 = QtWidgets.QHBoxLayout()
        self.h_box1.addStretch()
        self.h_box1.addWidget(self.textEditor)
        self.h_box1.addWidget(self.textEditor_pass)
        self.h_box1.addStretch()

        #creazione layout con pulsante accedi
        self.h_box2 = QtWidgets.QHBoxLayout()
        self.h_box2.addStretch()
        self.h_box2.addWidget(self.log_button)
        self.h_box2.addStretch()
        self.h_box2.setContentsMargins(0, 15, 0, 0)

        #creazione layout con immagine profilo
        self.h_box3 = QtWidgets.QHBoxLayout()
        self.h_box3.addStretch()
        self.h_box3.addWidget(self.image_profile)
        self.h_box3.addStretch()

        #h_box4 = QtWidgets.QHBoxLayout()
        #h_box4.addStretch()
        #h_box4.addWidget(self.type_profile_label)
        #self.type_profile_label.setStyleSheet('color: #7E2217; font-size: 20px')
        #h_box4.addStretch()
        #h_box4.setContentsMargins(0, 10, 0, 10)

        #creazione layout con pulsante accedi come...
        self.h_box5 = QtWidgets.QHBoxLayout()
        self.h_box5.addStretch()
        self.h_box5.addWidget(self.other_profile)
        self.other_profile.setStyleSheet("color: black; background-color: #ff7f50; padding: 5px; font-size:"+str(15*self.font_size)+"px")

        #richiamo funzione 'cambia profilo' al click del bottone
        self.other_profile.clicked.connect(self.change_profile)

        #richiamo funzione 'accedi' al click del bottone
        self.log_button.clicked.connect(self.log)

        self.v_box1.addLayout(self.h_box3)
        #self.v_box1.addLayout(h_box4)
        self.v_box1.addLayout(self.h_box1)
        self.v_box1.addLayout(self.h_box2)
        self.v_box1.addStretch()
        self.v_box1.addLayout(self.h_box5)

        #impostazione layout principale nella finestra
        self.centralWidget().setLayout(self.v_box1)

        #mostra il tutto
        self.show()

#funzione 'cambia profilo'
    def change_profile(self):
        global client
        sender = self.sender()
        if sender.text() == 'Accedi come maestra':
            #self.type_profile_label.setText("Maestra")
            self.other_profile.setText("Accedi come bambino")
            self.textEditor_pass.clear()
            self.textEditor_pass.setPlaceholderText("Inserisci il password:")
            self.textEditor_pass.setEchoMode(QtWidgets.QLineEdit.Password)
            pixmap = QtGui.QPixmap('Icons/maestra.png')
            pixmap = pixmap.scaledToWidth(250)
            pixmap = pixmap.scaledToHeight(250)
            self.image_profile.setPixmap(pixmap)
            client = False
        else:
            pixmap = QtGui.QPixmap('Icons/bimbo.png')
            pixmap = pixmap.scaledToWidth(250)
            pixmap = pixmap.scaledToHeight(250)
            self.image_profile.setPixmap(pixmap)
            #self.type_profile_label.setText("Bambino")
            self.other_profile.setText("Accedi come maestra")
            self.textEditor_pass.clear()
            self.textEditor_pass.setPlaceholderText("Inserisci il cognome:")
            self.textEditor_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
            client = True
    
#funzione 'login'
    def log(self):
        global client, nome, cognome, admin
        if(client == True):
            nome = self.textEditor.text()
            cognome = self.textEditor_pass.text()
            if(len(nome)>0 and len(cognome)>0):
                crsr = cndb.filter_Login_Client(nome,cognome)
                if len(crsr.fetchall())>0:
                    self.Dati_Bimbo()
                    cndb.close_db()
                else:
                    mes =QtWidgets.QMessageBox()
                    mes.setWindowTitle("ERROR")
                    mes.setWindowIcon(QtGui.QIcon("Icons/iconfinder_Close_1891023.png"))
                    mes.setIcon(QtWidgets.QMessageBox.Critical)
                    mes.setText("Il Nome o il Cognome inseriti non sono corretti")
                    mes.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    mes.exec_()
                    cndb.close_db()
        else:
            nome = self.textEditor.text()
            password = self.textEditor_pass.text()
            if(len(nome)>0 and len(password)>0):
                crsr = cndb.filter_Login_maestre(nome,password)
                data = tuple(crsr.fetchall())
                if len(data)>0:
                    if(data[0][4] == 1):
                        admin = True
                    else:
                        admin = False
                    self.Pannello_amministrativo()
                    cndb.close_db()
                else:
                    mes =QtWidgets.QMessageBox()
                    mes.setWindowTitle("ERROR")
                    mes.setWindowIcon(QtGui.QIcon("Icons/iconfinder_Close_1891023.png"))
                    mes.setText("Il Nome o il Password inseriti non sono coretti")
                    mes.setIcon(QtWidgets.QMessageBox.Critical)
                    mes.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    mes.exec_()
                    self.textEditor.clear()
                    self.textEditor_pass.clear()
                    cndb.close_db()

            

    #def new(self, evt):
    #    self.textEditor.setFocus()
    #    self.textEditor.keyPressEvent(evt)

#funzione per uscire dal programma
    def quit_trigger(self):
        sys.exit()

#funzione per cambiare il tema
    def color_theme(self):
        sender = self.sender()
        if (sender.text() == "Grigio"):
            color = "#41383C"
        elif (sender.text() == "Corallo"):
            color = "#ff7f50"
        elif (sender.text() == "Rosa"):
            color = "#FAAFBE"

        #colore di sfondo
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor(color))
        self.setPalette(p)

#Finestra di crediti
    def credits(self):
        #pulsante indietro
        self.redo = QtWidgets.QPushButton()

        #creatori interfaccia grafica
        self.gui_title = QtWidgets.QLabel("Interfaccia grafica:")
        self.gui_title.setStyleSheet('color: white; font-size: '+str(35*self.font_size)+'px')
        self.gui_guy = QtWidgets.QLabel("Michael Toscano \n"
                                        "Lorenzo Ferro \n"
                                        "Simone Vetere \n"
                                        "Marco Alberto Vicentin")
        self.gui_guy.setStyleSheet('color: darkorange; font-size:'+str(20*self.font_size)+'px; padding-left: 10px')

        #creatori connessione query e scripting
        self.conn_query_title = QtWidgets.QLabel("Connessione database e scripting:")
        self.conn_query_title.setStyleSheet('color: white; font-size:'+str(35*self.font_size)+'px')
        self.conn_query_guy = QtWidgets.QLabel("Alessandro Alizzi \n"
                                        "Wissam Soudassi")
        self.conn_query_guy.setStyleSheet('color: darkorange; font-size:'+str(20*self.font_size)+'px; padding-left: 10px')

        #creatori database
        self.database_title = QtWidgets.QLabel("Creatori database:")
        self.database_title.setStyleSheet('color: white; font-size:'+str(35*self.font_size)+'px')
        self.database_guy = QtWidgets.QLabel("Enrico Carena \n"
                                                "Andrea Fontana \n"
                                                "Mattia Marengo")
        self.database_guy.setStyleSheet('color: darkorange; font-size:'+str(20*self.font_size)+'px; padding-left: 10px')

        #creatori query
        self.database_query_title = QtWidgets.QLabel("Creatori query:")
        self.database_query_title.setStyleSheet('color: white; font-size:'+str(35*self.font_size)+'px')
        self.database_query_guy = QtWidgets.QLabel("Patrizio Marasso \n"
                                                   "Roberto Monticone")
        self.database_query_guy.setStyleSheet('color: darkorange; font-size:'+str(20*self.font_size)+'px; padding-left: 10px')

        #impostazione del nuovo layout principale
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.credit_box= QtWidgets.QVBoxLayout()

        #layout pulsante indietro
        self.undo_box = QtWidgets.QHBoxLayout()
        self.undo_box.addStretch()
        self.undo_box.addWidget(self.redo)
        self.redo.setObjectName("Indietro")
        self.redo.setStyleSheet("background-image: url(Icons/igs.png); width: 32px; height: 32px; border: none")

        self.redo.clicked.connect(self.finestra1)

        #layout e soto layout con gli elementi
        self.h_box_creator = QtWidgets.QHBoxLayout()
        self.h_box_creator.addStretch()

        self.v_box_creators = QtWidgets.QVBoxLayout()
        self.v_box_creators.addStretch()
        self.v_box_creators.addWidget(self.gui_title)
        self.v_box_creators.addWidget(self.gui_guy)

        self.v_box_creators.addWidget(self.conn_query_title)
        self.conn_query_title.setContentsMargins(0, 20, 0, 0)
        self.v_box_creators.addWidget(self.conn_query_guy)

        self.v_box_creators.addWidget(self.database_title)
        self.database_title.setContentsMargins(0, 20, 0, 0)
        self.v_box_creators.addWidget(self.database_guy)

        self.v_box_creators.addWidget(self.database_query_title)
        self.database_query_title.setContentsMargins(0, 20, 0, 0)
        self.v_box_creators.addWidget(self.database_query_guy)

        self.v_box_creators.addStretch()


        self.h_box_creator.addLayout(self.v_box_creators)
        self.h_box_creator.addStretch()

        self.credit_box.addLayout(self.undo_box)
        self.credit_box.addLayout(self.h_box_creator)

        #impostazione layout principale
        self.centralWidget().setLayout(self.credit_box)

        #mostra il tutto
        self.show()
    
#finzione mostra dati bimbo-----------------------------------------------------ATENZIONE-BUGS
    def Dati_Bimbo(self):
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Img_avatar = QtWidgets.QLabel()
        self.Img_avatar.setMinimumSize(QtCore.QSize(250, 250))
        self.Img_avatar.setMaximumSize(QtCore.QSize(250, 250))
        self.Img_avatar.setStyleSheet("background-color:white;")
        self.Img_avatar.setText("")
        self.Img_avatar.setObjectName("Img_avatar")
        self.Img_avatar.setScaledContents(True)
        self.verticalLayout_7.addWidget(self.Img_avatar)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.indietro_2 = QtWidgets.QPushButton()
        self.indietro_2.setObjectName("indietro_2")
        self.indietro_2.clicked.connect(self.finestra1)
        self.horizontalLayout_5.addWidget(self.indietro_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label_nome = QtWidgets.QLabel()
        self.label_nome.setMinimumSize(QtCore.QSize(530, 30))
        self.label_nome.setObjectName("label_nome")
        self.verticalLayout_2.addWidget(self.label_nome)
        self.label_cognome = QtWidgets.QLabel()
        self.label_cognome.setMinimumSize(QtCore.QSize(530, 30))
        self.label_cognome.setObjectName("label_cognome")
        self.verticalLayout_2.addWidget(self.label_cognome)
        self.label_classe = QtWidgets.QLabel()
        self.label_classe.setMinimumSize(QtCore.QSize(530, 30))
        self.label_classe.setObjectName("label_classe")
        self.verticalLayout_2.addWidget(self.label_classe)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.scrollArea_libri_inpossesso = QtWidgets.QScrollArea()
        self.scrollArea_libri_inpossesso.setMinimumSize(QtCore.QSize(400, 300))
        self.scrollArea_libri_inpossesso.setStyleSheet("background-color:grey;")
        self.scrollArea_libri_inpossesso.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_libri_inpossesso.setWidgetResizable(True)
        self.scrollArea_libri_inpossesso.setObjectName("scrollArea_libri_inpossesso")
        self.scrollAreaWidgetContents_INT = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_INT.setGeometry(QtCore.QRect(0, 0, 381, 298))
        self.scrollAreaWidgetContents_INT.setObjectName("scrollAreaWidgetContents_INT")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_INT)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_libri_inpossesso.setWidget(self.scrollAreaWidgetContents_INT)
        self.verticalLayout_3.addWidget(self.scrollArea_libri_inpossesso)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel()
        self.label_6.setMinimumSize(QtCore.QSize(0, 30))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.scrollArea_Libri_Disponibili = QtWidgets.QScrollArea()
        self.scrollArea_Libri_Disponibili.setMinimumSize(QtCore.QSize(400, 300))
        self.scrollArea_Libri_Disponibili.setStyleSheet("background-color:grey;")
        self.scrollArea_Libri_Disponibili.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_Libri_Disponibili.setWidgetResizable(True)
        self.scrollArea_Libri_Disponibili.setObjectName("scrollArea_Libri_Disponibili")
        self.scrollAreaWidgetContents_DSP = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_DSP.setGeometry(QtCore.QRect(0, 0, 381, 298))
        self.scrollAreaWidgetContents_DSP.setObjectName("scrollAreaWidgetContents_DSP")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_DSP)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_Libri_Disponibili.setWidget(self.scrollAreaWidgetContents_DSP)
        self.verticalLayout_4.addWidget(self.scrollArea_Libri_Disponibili)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.indietro_2.setText("← indietro")
        self.label_2.setText("Libri in Possesso")
        self.label_6.setText("Libri Disponibili")

        self.Load_sheda_bimbo()


    def Load_sheda_bimbo(self):
        global Root, nome, cognome, id_bimbo
        self.label_nome.setText("Nome: "+nome)
        self.label_cognome.setText("Cognome: "+cognome)
        result_1 = cndb.filter_Login_Client(nome,cognome)
        data = tuple(result_1.fetchall())
        cndb.close_db()
        self.label_classe.setText("Classe: "+data[0][3])
        if(data[0][5]== None):
            img = "Icons/bimbo.png"
        else:
            img = Root+data[0][5]
        self.Img_avatar.setPixmap(QtGui.QPixmap(img))
        id_temp = str(data[0][0])
        id_bimbo = str(data[0][0])
    
    #Seletore Libri da Restituire
        result_2 = cndb.show_libri_inpossesso(id_temp)
        data_2 = tuple(result_2.fetchall())
        self.NUM_BOX_INT = [""]
        self.Cover_INT = [""]
        self.label_INT = [""]
        self.Id_INT = [""]
        self.Id_log_INT = [""]
        for y in range(len(data_2)):
            result_3 = cndb.show_book_by_ID(str(data_2[y][2]))
            data_3 = tuple(result_3.fetchall())
            if data_2[y][4] == None:
                self.NUM_BOX_INT.insert(y,QtWidgets.QHBoxLayout())
                self.NUM_BOX_INT[y].setObjectName("BOX_INT_"+str(y))
                self.Cover_INT.insert(y, QtWidgets.QLabel(self.scrollAreaWidgetContents_INT))
                self.Cover_INT[y].setMinimumSize(QtCore.QSize(160, 0))
                self.Cover_INT[y].setMaximumSize(QtCore.QSize(160, 95))
                self.Cover_INT[y].setStyleSheet("background-color:white;")
                self.Cover_INT[y].setText("")
                self.Cover_INT[y].setObjectName("Cover_INT_"+str(y))
                if(data_3[0][4] == None):
                    img = "Icons/book.png"
                else:
                    img = Root+data_3[0][4]
                self.Cover_INT[y].setPixmap(QtGui.QPixmap(img))
                self.Cover_INT[y].setScaledContents(True)
                self.NUM_BOX_INT[y].addWidget(self.Cover_INT[y])
                self.label_INT.insert(y, QtWidgets.QLabel(self.scrollAreaWidgetContents_INT))
                self.label_INT[y].setMinimumSize(QtCore.QSize(170, 50))
                self.label_INT[y].setMaximumSize(QtCore.QSize(16777215, 95))
                self.label_INT[y].setObjectName("label_INT_"+str(y))
                self.label_INT[y].setText(data_3[0][1])
                self.NUM_BOX_INT[y].addWidget(self.label_INT[y])
                self.Id_INT.insert(y, QtWidgets.QLabel(self.scrollAreaWidgetContents_DSP))
                self.Id_INT[y].setMinimumSize(QtCore.QSize(16777215, 50))
                self.Id_INT[y].setMaximumSize(QtCore.QSize(16777215, 95))
                self.Id_INT[y].setObjectName("Id_INT"+str(y))
                self.Id_INT[y].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Id_INT[y].setText(str(data_3[0][0]))
                self.NUM_BOX_INT[y].addWidget(self.Id_INT[y])
                self.Id_log_INT.insert(y, QtWidgets.QLabel(self.scrollAreaWidgetContents_DSP))
                self.Id_log_INT[y].setMinimumSize(QtCore.QSize(16777215, 50))
                self.Id_log_INT[y].setMaximumSize(QtCore.QSize(16777215, 95))
                self.Id_log_INT[y].setObjectName("Id_Log_INT"+str(y))
                self.Id_log_INT[y].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.Id_log_INT[y].setText(str(data_2[y][0]))
                self.NUM_BOX_INT[y].addWidget(self.Id_log_INT[y])
                self.verticalLayout_5.addLayout(self.NUM_BOX_INT[y])
                
                clickable(self.Cover_INT[y]).connect(lambda: self.Get_Id_Libro_INT(self.Id_INT,y,self.Id_log_INT))
                clickable(self.label_INT[y]).connect(lambda: self.Get_Id_Libro_INT(self.Id_INT,y,self.Id_log_INT))
                clickable(self.Id_INT[y]).connect(lambda: self.Get_Id_Libro_INT(self.Id_INT,y,self.Id_log_INT))
        cndb.close_db()

    #Seletore Libri Disponibili    
        result_4 = cndb.show_book_Disponibili()
        data_4 = tuple(result_4.fetchall())
        self.NUM_BOX_DSP = [""]
        self.NUM_Cover_DSP = [""]
        self.NUM_Label_DSP = [""]
        self.NUM_Id_DSP = [""]
        self.NUM_Buton_DSP = [""]
        for x in range(len(data_4)):
            self.NUM_BOX_DSP.insert(x, QtWidgets.QHBoxLayout())
            self.NUM_BOX_DSP[x].setObjectName("BOX_DSP_"+str(x))
            self.NUM_Cover_DSP.insert(x, QtWidgets.QLabel(self.scrollAreaWidgetContents_DSP))
            self.NUM_Cover_DSP[x].setMinimumSize(QtCore.QSize(160, 0))
            self.NUM_Cover_DSP[x].setMaximumSize(QtCore.QSize(160, 95))
            self.NUM_Cover_DSP[x].setStyleSheet("background-color:white;")
            self.NUM_Cover_DSP[x].setText("")
            self.NUM_Cover_DSP[x].setObjectName("Cover_DSP_"+str(x))
            self.NUM_Cover_DSP[x].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            if(data_4[x][4] == None):
                img = "Icons/book.png"
            else:
                img = Root+data_4[x][4]
            self.NUM_Cover_DSP[x].setPixmap(QtGui.QPixmap(img))
            self.NUM_Cover_DSP[x].setScaledContents(True)
            self.NUM_BOX_DSP[x].addWidget(self.NUM_Cover_DSP[x])
            self.NUM_Label_DSP.insert(x, QtWidgets.QLabel(self.scrollAreaWidgetContents_DSP))
            self.NUM_Label_DSP[x].setMinimumSize(QtCore.QSize(170, 50))
            self.NUM_Label_DSP[x].setMaximumSize(QtCore.QSize(16777215, 95))
            self.NUM_Label_DSP[x].setObjectName("label_DSP_"+str(x))
            self.NUM_Label_DSP[x].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.NUM_Label_DSP[x].setText(data_4[x][1])
            self.NUM_BOX_DSP[x].addWidget(self.NUM_Label_DSP[x])
            self.NUM_Id_DSP.insert(x, QtWidgets.QLabel(self.scrollAreaWidgetContents_DSP))
            self.NUM_Id_DSP[x].setMinimumSize(QtCore.QSize(16777215, 50))
            self.NUM_Id_DSP[x].setMaximumSize(QtCore.QSize(16777215, 95))
            self.NUM_Id_DSP[x].setObjectName("id_DSP_"+str(x))
            self.NUM_Id_DSP[x].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.NUM_Id_DSP[x].setText(str(data_4[x][0]))
            self.NUM_BOX_DSP[x].addWidget(self.NUM_Id_DSP[x])
            self.verticalLayout_6.addLayout(self.NUM_BOX_DSP[x])
            self.INT_ID_Libro = self.NUM_Id_DSP[x].text()
            clickable(self.NUM_Cover_DSP[x]).connect(lambda: self.Get_Id_Libro(self.INT_ID_Libro))
            clickable(self.NUM_Label_DSP[x]).connect(lambda: self.Get_Id_Libro(self.INT_ID_Libro))
            clickable(self.NUM_Id_DSP[x]).connect(lambda: self.Get_Id_Libro(self.INT_ID_Libro))

        cndb.close_db()
        
        self.centralWidget().setLayout(self.gridLayout)
        self.show()

    def Get_Id_Libro_INT(self,_ogetto,_hit,_ogetto2):
        global id_libro, id_log, rest
        id_libro = _ogetto[_hit].text()
        id_log = _ogetto2[_hit].text()
        rest = True
        self.Info_prestito()

    def Get_Id_Libro(self,_ogetto):
        global id_libro,rest
        id_libro = _ogetto
        rest = False
        self.Info_prestito()      

#Vilsualizza Informazione libro per il prestito
    def Info_prestito(self):
        global Root, id_libro, rest
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 5, 1, 1)
        self.indietro = QtWidgets.QPushButton()
        self.indietro.setObjectName("indietro")
        self.indietro.clicked.connect(self.Dati_Bimbo)
        self.gridLayout.addWidget(self.indietro, 4, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 2, 1, 1)
        self.frame = QtWidgets.QFrame()
        self.frame.setMinimumSize(QtCore.QSize(700, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(10)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Img_cover = QtWidgets.QLabel(self.frame)
        self.Img_cover.setMinimumSize(QtCore.QSize(346, 400))
        self.Img_cover.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Img_cover.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.Img_cover.setStyleSheet("Background-color:rgb(255, 255, 255)")
        self.Img_cover.setFrameShape(QtWidgets.QFrame.Box)
        self.Img_cover.setLineWidth(2)
        self.Img_cover.setText("")
        self.Img_cover.setScaledContents(True)
        self.Img_cover.setObjectName("Img_cover")
        self.verticalLayout.addWidget(self.Img_cover)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(200, 30))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 30))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.verticalLayout_2.addWidget(self.frame_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        if rest == True:
            self.restituisci = QtWidgets.QPushButton(self.frame)
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(14)
            font.setBold(False)
            font.setWeight(50)
            self.restituisci.setFont(font)
            self.restituisci.setStyleSheet("border-radius:15px;border:1px solid white;background-color:green;")
            self.restituisci.setObjectName("restituisci")
            self.restituisci.setText("Restituisci")
            self.restituisci.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.verticalLayout_2.addWidget(self.restituisci)
            self.restituisci.clicked.connect(self.restituisci_libro)
        else:
            self.prendi = QtWidgets.QPushButton(self.frame)
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(14)
            font.setBold(False)
            font.setWeight(50)
            self.prendi.setFont(font)
            self.prendi.setStyleSheet("border-radius:15px;border:1px solid white;background-color:green;")
            self.prendi.setObjectName("prendi")
            self.prendi.setText("Prendi")
            self.prendi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.prendi.clicked.connect(self.prendi_libro)
            self.verticalLayout_2.addWidget(self.prendi)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 3, 3, 1, 1)
    
        result = cndb.show_book_by_ID_all(id_libro)
        data = tuple(result.fetchall())
        self.label_3.setText("Titolo: "+data[0][1])
        self.label_4.setText("Autore: "+data[0][2])
        if(data[0][3] == 0):
            self.label_5.setText("Genere: SENTIMENTI")
        elif(data[0][3] == 2):
            self.label_5.setText("Genere: SCIENZE")
        elif(data[0][3] == 3):
            self.label_5.setText("Genere: ANIMALI")
        elif(data[0][3] == 4):
            self.label_5.setText("Genere: RACCONTI")
        elif(data[0][3] == 5):
            self.label_5.setText("Genere: STORIE")
        elif(data[0][3] == 6):
            self.label_5.setText("Genere: CIBO")
        else:
            self.label_5.setText("Genere: Non Specificato")
        if(data[0][4] == None):
            img = "Icons/book.png"
        else:
            img = Root+data[0][4]
        self.Img_cover.setPixmap(QtGui.QPixmap(img))
        cndb.close_db()

        self.indietro.setText("← Indietro")
        self.label.setText("copertina del libro")
        self.label_2.setText("Informazini sul libro")

        self.centralWidget().setLayout(self.gridLayout)
        self.show()


    def prendi_libro(self):
        global id_bimbo, id_libro
        cndb.add_logs_book(id_bimbo,id_libro)
        self.Dati_Bimbo()
    
    def restituisci_libro(self):
        global id_libro, id_log, rest
        cndb.romve_logs_book(id_log,id_libro)
        rest = False
        self.Dati_Bimbo()

#Inserimento Profili dei Bambini
    def inserimento_new_profilo_C(self):
        global active_mod
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame()
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(10)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, 30)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Avatar = QtWidgets.QLabel(self.frame)
        self.Avatar.setMinimumSize(QtCore.QSize(300, 200))
        self.Avatar.setMaximumSize(QtCore.QSize(300, 200))
        self.Avatar.setStyleSheet("background-color:white;")
        self.Avatar.setText("")
        self.Avatar.setScaledContents(True)
        self.Avatar.setObjectName("Avatar")
        self.horizontalLayout_2.addWidget(self.Avatar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.caricafotoprofilo = QtWidgets.QPushButton(self.frame)
        self.caricafotoprofilo.setMinimumSize(QtCore.QSize(200, 0))
        self.caricafotoprofilo.setMaximumSize(QtCore.QSize(200, 16777215))
        self.caricafotoprofilo.setAutoFillBackground(False)
        self.caricafotoprofilo.setStyleSheet("border-radius:2px;background-color:white;border:1px solid grey;")
        self.caricafotoprofilo.setObjectName("caricafotoprofilo")
        self.caricafotoprofilo.clicked.connect(self.getAvatar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/iconfinder_ic_filter_48px_352349.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.caricafotoprofilo.setIcon(icon)
        self.horizontalLayout_2.addWidget(self.caricafotoprofilo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Edit_nome = QtWidgets.QLineEdit(self.frame)
        self.Edit_nome.setMinimumSize(QtCore.QSize(300, 0))
        self.Edit_nome.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Italic")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Edit_nome.setFont(font)
        self.Edit_nome.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Edit_nome.setAutoFillBackground(False)
        self.Edit_nome.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.Edit_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.Edit_nome.setObjectName("Edit_nome")
        self.verticalLayout.addWidget(self.Edit_nome)
        self.Edit_cognome = QtWidgets.QLineEdit(self.frame)
        self.Edit_cognome.setMinimumSize(QtCore.QSize(300, 0))
        self.Edit_cognome.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Italic")
        font.setPointSize(12)
        font.setKerning(False)
        self.Edit_cognome.setFont(font)
        self.Edit_cognome.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Edit_cognome.setAutoFillBackground(False)
        self.Edit_cognome.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.Edit_cognome.setAlignment(QtCore.Qt.AlignCenter)
        self.Edit_cognome.setObjectName("Edit_cognome")
        self.verticalLayout.addWidget(self.Edit_cognome)
        self.Edit_classe = QtWidgets.QLineEdit(self.frame)
        self.Edit_classe.setMinimumSize(QtCore.QSize(300, 0))
        self.Edit_classe.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Italic")
        font.setPointSize(12)
        font.setKerning(False)
        self.Edit_classe.setFont(font)
        self.Edit_classe.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Edit_classe.setAutoFillBackground(False)
        self.Edit_classe.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.Edit_classe.setAlignment(QtCore.Qt.AlignCenter)
        self.Edit_classe.setObjectName("Edit_classe")
        self.verticalLayout.addWidget(self.Edit_classe)
        self.Edit_anni = QtWidgets.QLineEdit(self.frame)
        self.Edit_anni.setMinimumSize(QtCore.QSize(300, 0))
        self.Edit_anni.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Italic")
        font.setPointSize(12)
        font.setKerning(False)
        self.Edit_anni.setFont(font)
        self.Edit_anni.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Edit_anni.setAutoFillBackground(False)
        self.Edit_anni.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.Edit_anni.setAlignment(QtCore.Qt.AlignCenter)
        self.Edit_anni.setObjectName("Edit_anni")
        self.verticalLayout.addWidget(self.Edit_anni)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.conferma = QtWidgets.QPushButton(self.frame)
        self.conferma.setMinimumSize(QtCore.QSize(100, 20))
        self.conferma.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.conferma.setFont(font)
        self.conferma.setStyleSheet("border-radius:2px;background-color:white;border:1px solid grey;")
        self.conferma.setObjectName("conferma")
        if(active_mod == True):
            self.conferma.clicked.connect(self.modifica_bambino)
        else:
            self.Clear_Variabili_Glogals()
            self.conferma.clicked.connect(self.inserimento_nuovo_bambino)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/iconfinder_Checkmark_1891021.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.conferma.setIcon(icon1)
        self.horizontalLayout.addWidget(self.conferma)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        self.indietro = QtWidgets.QPushButton()
        self.indietro.setMinimumSize(QtCore.QSize(100, 20))
        self.indietro.setMaximumSize(QtCore.QSize(100, 20))
        self.indietro.setObjectName("indietro")
        self.indietro.clicked.connect(self.Pannello_amministrativo)
        self.gridLayout.addWidget(self.indietro, 6, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)

 
        self.Edit_nome.clear()
        self.Edit_cognome.clear()
        self.Edit_classe.clear()
        self.Edit_anni.clear()
        self.caricafotoprofilo.setText("carica foto profilo")
        self.Edit_nome.setPlaceholderText("nome")
        self.Edit_cognome.setPlaceholderText("cognome")
        self.Edit_classe.setPlaceholderText("classe")
        self.Edit_anni.setPlaceholderText("anni")
        self.conferma.setText("conferma")
        self.indietro.setText("← indietro")

        if(active_mod == True):
            self.Carica_items()
        
        self.centralWidget().setLayout(self.gridLayout)
        self.show()
    
    def Carica_items(self):
        global Root, id_bimbo
        result = cndb.filter_ID_to_Client(id_bimbo)
        data = tuple(result.fetchall())
        self.Edit_nome.setText(data[0][1])
        self.Edit_cognome.setText(data[0][2])
        self.Edit_classe.setText(data[0][3])
        self.Edit_anni.setText(str(data[0][4]))
        if(data[0][5] == None):
            Patch_avatar = "Icons/bimbo.png"
        else:
            Patch_avatar = Root+str(data[0][5])
        self.pixMap = QtGui.QPixmap(Patch_avatar)
        self.Avatar.setPixmap(QtGui.QPixmap(self.pixMap))
        cndb.close_db()


    def getAvatar(self):
        global New_Patch_avatar
        options = QFileDialog.Options()
        img,_ = QFileDialog.getOpenFileName(None, 'QFileDialog.getOpenFileName()', '', 'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        FullName_Avatar = img.split('/')
        Ultimo = len(FullName_Avatar)-1
        shutil.copy(img, Root+"\\Avatar\\"+FullName_Avatar[Ultimo])
        New_Patch_avatar = "\\Avatar\\"+FullName_Avatar[Ultimo]
        self.pixMap = QtGui.QPixmap(img)
        self.Avatar.setPixmap(QtGui.QPixmap(self.pixMap))

    def inserimento_nuovo_bambino(self):
        global New_Patch_avatar
        nome = self.Edit_nome.text()
        cognome = self.Edit_cognome.text()
        classe = self.Edit_classe.text()
        anni = self.Edit_anni()
        if (len(nome)>0 and len(cognome)>0 and len(classe) and len(anni)>0):
            cndb.insert_client(cognome,nome,classe,anni,New_Patch_avatar)
        else:
            self.error
    
    def modifica_bambino(self,id_Client):
        global New_Patch_avatar,active_mod
        cognome = self.Edit_cognome.text()
        nome = self.Edit_nome.text()
        classe = self.Edit_classe.text()
        anni = self.Edit_anni.text()
        cndb.edit_client(cognome,nome,classe,anni,New_Patch_avatar,id_Client)
        active_mod = False
    
#Inserimento dei libri
    def Inserimeto_libri(self):
        global active_mod
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame()
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(10)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, 30)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Avatar = QtWidgets.QLabel(self.frame)
        self.Avatar.setMinimumSize(QtCore.QSize(300, 200))
        self.Avatar.setMaximumSize(QtCore.QSize(300, 200))
        self.Avatar.setStyleSheet("background-color:white;")
        self.Avatar.setText("")
        self.Avatar.setScaledContents(True)
        self.Avatar.setObjectName("Avatar")
        self.horizontalLayout_2.addWidget(self.Avatar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.caricafotoprofilo = QtWidgets.QPushButton(self.frame)
        self.caricafotoprofilo.setMinimumSize(QtCore.QSize(200, 0))
        self.caricafotoprofilo.setMaximumSize(QtCore.QSize(200, 16777215))
        self.caricafotoprofilo.setAutoFillBackground(False)
        self.caricafotoprofilo.setStyleSheet("border-radius:2px;background-color:white;border:1px solid grey;")
        self.caricafotoprofilo.setObjectName("caricafotoprofilo")
        self.caricafotoprofilo.clicked.connect(self.getCover)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/iconfinder_ic_filter_48px_352349.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.caricafotoprofilo.setIcon(icon)
        self.horizontalLayout_2.addWidget(self.caricafotoprofilo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Edit_titolo = QtWidgets.QLineEdit(self.frame)
        self.Edit_titolo.setMinimumSize(QtCore.QSize(300, 0))
        self.Edit_titolo.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Italic")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Edit_titolo.setFont(font)
        self.Edit_titolo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Edit_titolo.setAutoFillBackground(False)
        self.Edit_titolo.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.Edit_titolo.setAlignment(QtCore.Qt.AlignCenter)
        self.Edit_titolo.setObjectName("Edit_titolo")
        self.verticalLayout.addWidget(self.Edit_titolo)
        self.Edit_autore = QtWidgets.QLineEdit(self.frame)
        self.Edit_autore.setMinimumSize(QtCore.QSize(300, 0))
        self.Edit_autore.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Italic")
        font.setPointSize(12)
        font.setKerning(False)
        self.Edit_autore.setFont(font)
        self.Edit_autore.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Edit_autore.setAutoFillBackground(False)
        self.Edit_autore.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.Edit_autore.setAlignment(QtCore.Qt.AlignCenter)
        self.Edit_autore.setObjectName("Edit_autore")
        self.verticalLayout.addWidget(self.Edit_autore)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("Sentimentale")
        self.comboBox.addItem("Scienze")
        self.comboBox.addItem("Animali")
        self.comboBox.addItem("Racconti")
        self.comboBox.addItem("Storie")
        self.comboBox.addItem("Cibo")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.conferma = QtWidgets.QPushButton(self.frame)
        self.conferma.setMinimumSize(QtCore.QSize(100, 20))
        self.conferma.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.conferma.setFont(font)
        self.conferma.setStyleSheet("border-radius:2px;background-color:white;border:1px solid grey;")
        self.conferma.setObjectName("conferma")
        if(active_mod == True):
            self.conferma.clicked.connect(self.modifica_libro)
        else:
            self.conferma.clicked.connect(self.inserimento_nuovo_libro)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/iconfinder_Checkmark_1891021.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.conferma.setIcon(icon1)
        self.horizontalLayout.addWidget(self.conferma)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        self.indietro = QtWidgets.QPushButton()
        self.indietro.setMinimumSize(QtCore.QSize(100, 20))
        self.indietro.setMaximumSize(QtCore.QSize(100, 20))
        self.indietro.setObjectName("indietro")
        self.indietro.clicked.connect(self.Pannello_amministrativo)
        self.gridLayout.addWidget(self.indietro, 6, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)

        self.Edit_titolo.clear()
        self.Edit_autore.clear()
        self.caricafotoprofilo.setText("carica foto profilo")
        self.Edit_titolo.setPlaceholderText("Titolo")
        self.Edit_autore.setPlaceholderText("autore")
        self.conferma.setText("conferma")
        self.indietro.setText("← indietro")

        if(active_mod == True):
            self.Carica_items_libro()

        self.centralWidget().setLayout(self.gridLayout)
        self.show()
    
    def getCover(self):
        global New_Patch_Cover
        options = QFileDialog.Options()
        img,_ = QFileDialog.getOpenFileName(None, 'QFileDialog.getOpenFileName()', '', 'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        FullName_Cover = img.split('/')
        Ultimo = len(FullName_Cover)-1
        shutil.copy(img, Root+"\\Cover\\"+FullName_Cover[Ultimo])
        New_Patch_Cover = "\\Cover\\"+FullName_Cover[Ultimo]
        self.pixMap = QtGui.QPixmap(img)
        self.Avatar.setPixmap(QtGui.QPixmap(self.pixMap))
    
    def Select_genere(self):
        global genere
        sel = self.comboBox.currentText()
        if(sel == "Sentimentale"):
            genere = "Sentimentale"
            return 0
        if(sel == "Scienze"):
            genere = "Scienze"
            return 0
        if(sel == "Animali"):
            genere = "Animali"
            return 0
        if(sel== "Racconti"):
            genere = "Racconti"
            return 0
        if(sel == "Storie"):
            genere = "Storie"
            return 0
        if(sel == "Cibo"):
            genere = "Cibo"
            return 0
        if(sel == ""):
            genere = ""
        else:
            print("ERROR")
    
    def inserimento_nuovo_libro(self):
        global New_Patch_Cover, genere
        titolo = self.Edit_nome.text()
        autore = self.Edit_autore.text()
        if (len(titolo)>0 and len(autore)>0 and len(genere)):
            cndb.insert_book(titolo,autore,genere,New_Patch_Cover)
        else:
            self.error
    
    def Carica_items_libro(self):
        global New_Patch_Cover, Root, id_libro
        result = cndb.filter_ID_book(id_libro)
        data = tuple(result.fetchall())
        self.Edit_titolo.setText(data[0][1])
        self.Edit_autore.setText(data[0][2])
        if(data[0][3] == "Sentimentale"):
            self.comboBox.itemText(1)
        elif(data[0][3] == "Scienze"):
            self.comboBox.itemText(2)
        elif(data[0][3] == "Animali"):
            self.comboBox.itemText(3)
        elif(data[0][3] == "Racconti"):
            self.comboBox.itemText(4)
        elif(data[0][3] == "Storie"):
            self.comboBox.itemText(5)
        elif(data[0][3] == "Cibo"):
            self.comboBox.itemText(6)
        else:
            self.comboBox.itemText(0)
        if(data[0][4]==None):
            img = Root+"\\Icons\\book.png"
        else:
            img = Root+str(data[0][4])
        self.pixMap = QtGui.QPixmap(img)
        self.Avatar.setPixmap(QtGui.QPixmap(self.pixMap))
        cndb.close_db()

    def modifica_libro(self):
        global New_Patch_Cover, id_libro
        titolo = self.Edit_titolo.text()
        autroe = self.Edit_autore.text()
        genere = self.comboBox.currentText()
        cndb.edit_book(titolo,autroe,genere,New_Patch_Cover,id_libro)

#Inserimento profilo Maestre
    def inserimento_new_profilo_A(self):
        global active_mod, Root
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame()
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(10)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, 30)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Avatar = QtWidgets.QLabel(self.frame)
        self.Avatar.setMinimumSize(QtCore.QSize(300, 200))
        self.Avatar.setMaximumSize(QtCore.QSize(300, 200))
        self.Avatar.setStyleSheet("")
        self.Avatar.setText("")
        self.Avatar.setPixmap(QtGui.QPixmap("Icons/maestra.png"))
        self.Avatar.setScaledContents(True)
        self.Avatar.setObjectName("Avatar")
        self.horizontalLayout_2.addWidget(self.Avatar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Edit_nome = QtWidgets.QLineEdit(self.frame)
        self.Edit_nome.setMinimumSize(QtCore.QSize(300, 0))
        self.Edit_nome.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Italic")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Edit_nome.setFont(font)
        self.Edit_nome.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Edit_nome.setAutoFillBackground(False)
        self.Edit_nome.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.Edit_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.Edit_nome.setObjectName("Edit_nome")
        self.verticalLayout.addWidget(self.Edit_nome)
        self.Edit_cognome = QtWidgets.QLineEdit(self.frame)
        self.Edit_cognome.setMinimumSize(QtCore.QSize(300, 0))
        self.Edit_cognome.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Italic")
        font.setPointSize(12)
        font.setKerning(False)
        self.Edit_cognome.setFont(font)
        self.Edit_cognome.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Edit_cognome.setAutoFillBackground(False)
        self.Edit_cognome.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.Edit_cognome.setAlignment(QtCore.Qt.AlignCenter)
        self.Edit_cognome.setObjectName("Edit_cognome")
        self.verticalLayout.addWidget(self.Edit_cognome)
        self.Edit_Password = QtWidgets.QLineEdit(self.frame)
        self.Edit_Password.setMinimumSize(QtCore.QSize(300, 0))
        self.Edit_Password.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Italic")
        font.setPointSize(12)
        font.setKerning(False)
        self.Edit_Password.setFont(font)
        self.Edit_Password.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Edit_Password.setAutoFillBackground(False)
        self.Edit_Password.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.Edit_Password.setAlignment(QtCore.Qt.AlignCenter)
        self.Edit_Password.setObjectName("Edit_Password")
        self.verticalLayout.addWidget(self.Edit_Password)

        self.Edit_Password_ver = QtWidgets.QLineEdit(self.frame)
        self.Edit_Password_ver.setMinimumSize(QtCore.QSize(300, 0))
        self.Edit_Password_ver.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Italic")
        font.setPointSize(12)
        font.setKerning(False)
        self.Edit_Password_ver.setFont(font)
        self.Edit_Password_ver.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Edit_Password_ver.setAutoFillBackground(False)
        self.Edit_Password_ver.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.Edit_Password_ver.setAlignment(QtCore.Qt.AlignCenter)
        self.Edit_Password_ver.setObjectName("Edit_Password_ver")
        self.verticalLayout.addWidget(self.Edit_Password_ver)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setMinimumSize(QtCore.QSize(300, 23))
        self.checkBox.setMaximumSize(QtCore.QSize(300, 23))
        self.checkBox.setStyleSheet("border-radius:5px;border:1px solid grey;background-color:white;")
        self.checkBox.setObjectName("checkBox")
        if(admin == True):
            self.checkBox.setEnabled
        else:
            self.checkBox.setDisabled
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.conferma = QtWidgets.QPushButton(self.frame)
        self.conferma.setMinimumSize(QtCore.QSize(100, 20))
        self.conferma.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeue-Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.conferma.setFont(font)
        self.conferma.setStyleSheet("border-radius:2px;background-color:white;border:1px solid grey;")
        self.conferma.setObjectName("conferma")
        if(active_mod == True):
            self.conferma.clicked.connect(self.modifica_maestra)
        else:
            self.conferma.clicked.connect(self.inserimento_nuovo_maestra)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/iconfinder_Checkmark_1891021.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.conferma.setIcon(icon1)
        self.horizontalLayout.addWidget(self.conferma)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        self.indietro = QtWidgets.QPushButton()
        self.indietro.setMinimumSize(QtCore.QSize(100, 20))
        self.indietro.setMaximumSize(QtCore.QSize(100, 20))
        self.indietro.setObjectName("indietro")
        self.indietro.clicked.connect(self.Pannello_amministrativo)
        self.gridLayout.addWidget(self.indietro, 6, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)

        self.Edit_nome.clear()
        self.Edit_cognome.clear()
        self.Edit_Password.clear()
        self.Edit_Password_ver.clear()
        self.Edit_nome.setPlaceholderText("nome")
        self.Edit_cognome.setPlaceholderText("cognome")
        self.Edit_Password.setPlaceholderText("Password")
        self.Edit_Password_ver.setPlaceholderText("Ripetere Password")
        self.checkBox.setText("Amministratore")
        self.conferma.setText("conferma")
        self.indietro.setText("← indietro")

        if(active_mod == True):
            self.Carica_items_maestre()

        self.centralWidget().setLayout(self.gridLayout)
        self.show()

    def inserimento_nuovo_maestra(self):
        nome = self.Edit_nome.text()
        cognome = self.Edit_cognome.text()
        password = self.Edit_Password.text()
        password_ver = self.Edit_Password_ver.text()
        amministratore = self.checkBox.checkState()
        if(password == password_ver):
            cndb.insert_admin(nome,cognome,password,amministratore)
        else:
            self.errore

    def Carica_items_maestre(self):
        global id_Maestra
        result1 = cndb.filter_id_to_maestre(id_Maestra)
        data = tuple(result1.fetchall())
        self.Edit_nome.setText(data[0][1])
        self.Edit_cognome.setText(data[0][2])
        self.checkBox.setCheckState(data[0][4])
        cndb.close_db()


    def modifica_maestra(self):
        global id_Maestra
        nome = self.Edit_nome.text()
        cognome = self.Edit_cognome.text()
        password = self.Edit_Password.text()
        password_ver = self.Edit_Password_ver.text()
        amministratore = self.checkBox.checkState()
        if(password == password_ver):
            cndb.edit_admin(nome,cognome,password,amministratore,id_Maestra)
        else:
            self.errore

#Pannello amministrativo
    def Pannello_amministrativo(self):
        global active_mod, Root
        active_mod = False
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.tableView = QtWidgets.QTableWidget()
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
        self.exit_Indietro = QtWidgets.QPushButton()
        self.exit_Indietro.setMinimumSize(QtCore.QSize(130, 30))
        self.exit_Indietro.setMaximumSize(QtCore.QSize(130, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/igs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_Indietro.setIcon(icon)
        self.exit_Indietro.setObjectName("exit_Indietro")
        self.horizontalLayout_2.addWidget(self.exit_Indietro)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Inserisci_maestra = QtWidgets.QPushButton()
        self.Inserisci_maestra.setMinimumSize(QtCore.QSize(110, 30))
        self.Inserisci_maestra.setMaximumSize(QtCore.QSize(110, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/maestra.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inserisci_maestra.setIcon(icon1)
        self.Inserisci_maestra.setObjectName("Inserisci_maestra")
        self.horizontalLayout.addWidget(self.Inserisci_maestra)
        self.Inserisci_bimbo = QtWidgets.QPushButton()
        self.Inserisci_bimbo.setMinimumSize(QtCore.QSize(110, 30))
        self.Inserisci_bimbo.setMaximumSize(QtCore.QSize(110, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/bimbo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inserisci_bimbo.setIcon(icon2)
        self.Inserisci_bimbo.setObjectName("Inserisci_bimbo")
        self.horizontalLayout.addWidget(self.Inserisci_bimbo)
        self.Inserisci_libro = QtWidgets.QPushButton()
        self.Inserisci_libro.setMinimumSize(QtCore.QSize(110, 30))
        self.Inserisci_libro.setMaximumSize(QtCore.QSize(110, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inserisci_libro.setIcon(icon3)
        self.Inserisci_libro.setObjectName("Inserisci_libro")
        self.horizontalLayout.addWidget(self.Inserisci_libro)
        self.Salva_modifice = QtWidgets.QPushButton()
        self.Salva_modifice.setMinimumSize(QtCore.QSize(110, 30))
        self.Salva_modifice.setMaximumSize(QtCore.QSize(110, 30))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/iconfinder_Compose_1891025.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Salva_modifice.setIcon(icon4)
        self.Salva_modifice.setObjectName("Salva_modifice")
        self.horizontalLayout.addWidget(self.Salva_modifice)
        self.Elimina = QtWidgets.QPushButton()
        self.Elimina.setMinimumSize(QtCore.QSize(110, 30))
        self.Elimina.setMaximumSize(QtCore.QSize(110, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/iconfinder_Close_1891023.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Elimina.setIcon(icon5)
        self.Elimina.setObjectName("Elimina")
        self.horizontalLayout.addWidget(self.Elimina)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel()
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox()
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
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.Parametro_ricerca = QtWidgets.QComboBox()
        self.Parametro_ricerca.setMinimumSize(QtCore.QSize(120, 25))
        self.Parametro_ricerca.setMaximumSize(QtCore.QSize(120, 25))
        self.Parametro_ricerca.setObjectName("Parametro_ricerca")
        self.horizontalLayout_3.addWidget(self.Parametro_ricerca)
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.Parametro_key = QtWidgets.QLineEdit()
        self.Parametro_key.setMinimumSize(QtCore.QSize(120, 25))
        self.Parametro_key.setMaximumSize(QtCore.QSize(120, 25))
        self.Parametro_key.setObjectName("Parametro_key")
        self.horizontalLayout_3.addWidget(self.Parametro_key)
        self.Cerca = QtWidgets.QPushButton()
        self.Cerca.setMinimumSize(QtCore.QSize(75, 25))
        self.Cerca.setMaximumSize(QtCore.QSize(75, 25))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/iconfinder_icon-ios7-search-strong_211817.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.Inserisci_bimbo.clicked.connect(self.inserimento_new_profilo_C)
        self.Inserisci_libro.clicked.connect(self.Inserimeto_libri)
        self.Inserisci_maestra.clicked.connect(self.inserimento_new_profilo_A)
        self.Salva_modifice.clicked.connect(self.modifica)
        self.Elimina.clicked.connect(self.elimina_per)
        self.exit_Indietro.clicked.connect(self.finestra1)
        self.Cerca.clicked.connect(self.cerca_per)

        self.Table_Select_SQL()
        self.centralWidget().setLayout(self.gridLayout)
        self.show()


    def Table_Select_SQL(self):
        global type_modifica
        sel_db = self.comboBox.currentText()
        if(sel_db == "Bambini"):
            self.Show_Table(cndb.show_client())
            self.Parametro_ricerca.clear()
            self.Parametro_ricerca.addItem("tutto")
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
            self.Parametro_ricerca.addItem("tutto")
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
            self.Parametro_ricerca.addItem("tutto")
            self.Parametro_ricerca.addItem("titolo")
            self.Parametro_ricerca.addItem("autore")
            self.Parametro_ricerca.addItem("disponibilità")
            colum_text = ["","","","","",""]
            self.tableView.setHorizontalHeaderLabels(colum_text)
            colum_text = ["ID","TITOLO","AUTORE","GENERE","COVER","DISPONILE"]
            self.tableView.setHorizontalHeaderLabels(colum_text)
            type_modifica = 2
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
        global type_modifica, active_mod, id_bimbo, id_Maestra, id_libro
        if(self.tableView.currentItem()== None):
            return "errore"
        id_linea = self.tableView.currentItem().row()
        id_Finale = self.tableView.item(id_linea,0).text()
        print(id_Finale)
        active_mod = True
        if(type_modifica == 0):
            id_bimbo = id_Finale
            self.inserimento_new_profilo_C()
        elif(type_modifica == 1):
            id_Maestra = id_Finale
            self.inserimento_new_profilo_A()
        elif(type_modifica == 2):
            id_libro = id_Finale
            self.Inserimeto_libri()
        else:
            print("ERRORE")
    
    def cerca_per(self):
        global type_modifica
        selc = self.Parametro_key.text()
        if(selc != ""):
            if(type_modifica == 0):
                if(self.Parametro_ricerca.currentText()=="nome"):
                    self.Show_Table(cndb.filter_name_to_Client(selc))
                elif(self.Parametro_ricerca.currentText()=="cognome"):
                    self.Show_Table(cndb.filter_cognome_to_Client(selc))
                elif(self.Parametro_ricerca.currentText()=="classe"):
                    self.Show_Table(cndb.filter_classe_to_Client(selc))
                elif(self.Parametro_ricerca.currentText()=="tutto"):
                    self.Show_Table(cndb.show_client())
                colum_text = ["","","","","",""]
                self.tableView.setHorizontalHeaderLabels(colum_text)
                colum_text = ["ID","COGNOME","NOME","CLASSE","ANNI","FOTO"]
                self.tableView.setHorizontalHeaderLabels(colum_text)
            if(type_modifica == 1):
                if(self.Parametro_ricerca.currentText()=="nome"):
                    self.Show_Table(cndb.filter_name_to_maestre(selc))
                elif(self.Parametro_ricerca.currentText()=="cognome"):
                    self.Show_Table(cndb.filter_cognome_to_maestre(selc))
                elif(self.Parametro_ricerca.currentText()=="tutto"):
                    self.Show_Table(cndb.show_admin())
                colum_text = ["","","","","",""]
                self.tableView.setHorizontalHeaderLabels(colum_text)
                colum_text = ["ID","COGNOME","NOME","AMMINISTRETORE",]
                self.tableView.setHorizontalHeaderLabels(colum_text)
            if(type_modifica == 2):
                if(self.Parametro_ricerca.currentText()=="titolo"):
                    self.Show_Table(cndb.filter_book(selc))
                elif(self.Parametro_ricerca.currentText()=="autore"):
                    self.Show_Table(cndb.filter_to_autore_book(selc))
                elif(self.Parametro_ricerca.currentText()=="disponibilità"):
                    self.Show_Table(cndb.show_book_Disponibili())
                elif(self.Parametro_ricerca.currentText()=="tutto"):
                    self.Show_Table(cndb.show_book())
                colum_text = ["","","","","",""]
                self.tableView.setHorizontalHeaderLabels(colum_text)
                colum_text = ["ID","TITOLO","AUTORE","GENERE","COVER","DISPONILE"]
                self.tableView.setHorizontalHeaderLabels(colum_text)
    
    def elimina_per(self):
        global type_modifica, admin, Root
        if(admin == True):
            if(self.tableView.currentItem()== None):
                return "errore"
            id_linea = self.tableView.currentItem().row()
            id_Finale = self.tableView.item(id_linea,0).text()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("AVVISO")
            msgBox.setWindowIcon(QtGui.QIcon("Icons/iconfinder_ic_info_48px_3669162.png"))
            msgBox.setText("Sei seicuro di Voler Eliminare?")
            msgBox.setInformativeText("")
            msgBox.setIcon(QtWidgets.QMessageBox.Question)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No )
            msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
            reply = msgBox.exec_()
            if reply == QtWidgets.QMessageBox.Yes:
                if(type_modifica == 0):
                    cndb.delete_id_client(id_Finale)
                    self.Show_Table(cndb.show_client())
                elif(type_modifica == 1):
                    cndb.delete_id_admin(id_Finale)
                    self.Show_Table(cndb.show_admin())
                elif(type_modifica == 2):
                    cndb.delete_id_book(id_Finale)
                    self.Show_Table(cndb.show_book())
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("AVVISO")
            msgBox.setWindowIcon(QtGui.QIcon("Icons/iconfinder_ic_info_48px_3669162.png"))
            msgBox.setText("Non hai il permesso di effetura questa operazione")
            msgBox.setInformativeText("")
            msgBox.setIcon(QtWidgets.QMessageBox.warning)
        
#richiamo della classe MainWindow, apertura della finestra, e stile
app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")
a_window = MainWindow()
sys.exit(app.exec_())
