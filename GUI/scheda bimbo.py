# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\scheda bimbo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profile(object):
    def setupUi(self, profile):
        profile.setObjectName("profile")
        profile.resize(832, 654)
        profile.setStyleSheet("background-color:grey;")
        self.centralwidget = QtWidgets.QWidget(profile)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Img_avatar = QtWidgets.QLabel(self.centralwidget)
        self.Img_avatar.setMinimumSize(QtCore.QSize(250, 250))
        self.Img_avatar.setMaximumSize(QtCore.QSize(500, 250))
        self.Img_avatar.setStyleSheet("background-color:white;")
        self.Img_avatar.setText("")
        self.Img_avatar.setObjectName("Img_avatar")
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
        self.indietro_2 = QtWidgets.QPushButton(self.centralwidget)
        self.indietro_2.setObjectName("indietro_2")
        self.indietro_2.clicked.connect(self.finestra1)
        self.horizontalLayout_5.addWidget(self.indietro_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setMinimumSize(QtCore.QSize(530, 30))
        self.label_nome.setObjectName("label_nome")
        self.verticalLayout_2.addWidget(self.label_nome)
        self.label_cognome = QtWidgets.QLabel(self.centralwidget)
        self.label_cognome.setMinimumSize(QtCore.QSize(530, 30))
        self.label_cognome.setObjectName("label_cognome")
        self.verticalLayout_2.addWidget(self.label_cognome)
        self.label_classe = QtWidgets.QLabel(self.centralwidget)
        self.label_classe.setMinimumSize(QtCore.QSize(530, 30))
        self.label_classe.setObjectName("label_classe")
        self.verticalLayout_2.addWidget(self.label_classe)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.scrollArea_libri_inpossesso = QtWidgets.QScrollArea(self.centralwidget)
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
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 30))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.scrollArea_Libri_Disponibili = QtWidgets.QScrollArea(self.centralwidget)
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
        profile.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(profile)

        profile.setWindowTitle("profilo utente")
        self.indietro_2.setText("← indietro")
        self.label_2.setText("Libri in Possesso")
        self.label_INT_0.setText("nome libro")
        self.label_6.setText("Libri Disponibili")
        self.label_DSP_0.setText("nome libro")

        self.Load_sheda_bimbo()

    def Load_sheda_bimbo(self):
        global Root, nome, cognome
        self.label_nome.setText("Nome: "+nome)
        self.label_cognome.setText("Cognome:"+cognome)
        result_1 = cndb.filter_Login_Client(nome,cognome)
        cndb.close_db()
        data = tuple(result.fetchall())
        self.label_classe.setText("Classe:"+data[3][0])
        self.Img_avatar.setPixmap(QtGui.QPixmap(Root+data[5][0]))
        result_2 = cndb.show_libri_inpossesso(data[0][0])
        cndb.close_db()
        data_2 = tuple(result_2.fetchall())
        for y in enumerate(result_2):
            result_3 = cndb.show_book_by_ID(data_2[y][2])
            data_3 = tuple(result_3.fetchall())
            self.horizontalLayout_INT_[y] = QtWidgets.QHBoxLayout()
            self.horizontalLayout_INT_[y].setObjectName("horizontalLayout_INT_"+y)
            self.Cover_INT_[y] = QtWidgets.QLabel(self.scrollAreaWidgetContents_INT)
            self.Cover_INT_[y].setMinimumSize(QtCore.QSize(160, 0))
            self.Cover_INT_[y].setMaximumSize(QtCore.QSize(160, 95))
            self.Cover_INT_[y].setStyleSheet("background-color:white;")
            self.Cover_INT_[y].setText("")
            self.Cover_INT_[y].setObjectName("Cover_INT_0")
            self.Cover_INT_[y].setPixmap(QtGui.QPixmap(Root+data_3[1][0]))
            self.horizontalLayout_INT_[y].addWidget(self.Cover_INT_[y])
            self.label_INT_[y] = QtWidgets.QLabel(self.scrollAreaWidgetContents_INT)
            self.label_INT_[y].setMinimumSize(QtCore.QSize(170, 50))
            self.label_INT_[y].setMaximumSize(QtCore.QSize(16777215, 95))
            self.label_INT_[y].setObjectName("label_INT_"+y)
            self.label_INT_[y].setText(data_3[0][0])
            self.horizontalLayout_INT_[y].addWidget(self.label_INT_[y])
            self.verticalLayout_5.addLayout(self.horizontalLayout_INT_[y])
        result_4 = cndb.show_book_Disponibili()
        data_4 = tuple(result_4.fetchall())
        for x in enumerate(result_4):
            self.horizontalLayout_DSP_[x] = QtWidgets.QHBoxLayout()
            self.horizontalLayout_DSP_[x].setObjectName("horizontalLayout_DSP_"+x)
            self.Cover_DSP_[x] = QtWidgets.QLabel(self.scrollAreaWidgetContents_DSP)
            self.Cover_DSP_[x].setMinimumSize(QtCore.QSize(160, 0))
            self.Cover_DSP_[x].setMaximumSize(QtCore.QSize(160, 95))
            self.Cover_DSP_[x].setStyleSheet("background-color:white;")
            self.Cover_DSP_[x].setText("")
            self.Cover_DSP_[x].setObjectName("Cover_DSP_"+x)
            self.Cover_INT_[y].setPixmap(QtGui.QPixmap(Root+data_4[1][0]))
            self.horizontalLayout_DSP_[x].addWidget(self.Cover_DSP_[x])
            self.label_DSP_[x] = QtWidgets.QLabel(self.scrollAreaWidgetContents_DSP)
            self.label_DSP_[x].setMinimumSize(QtCore.QSize(170, 50))
            self.label_DSP_[x].setMaximumSize(QtCore.QSize(16777215, 95))
            self.label_DSP_[x].setObjectName("label_DSP_"+x)
            self.label_INT_[y].setText(data_4[0][0])
            self.horizontalLayout_DSP_[x].addWidget(self.label_DSP_[x])
            self.verticalLayout_6.addLayout(self.horizontalLayout_DSP_[x])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile = QtWidgets.QMainWindow()
    ui = Ui_profile()
    ui.setupUi(profile)
    profile.show()
    sys.exit(app.exec_())
