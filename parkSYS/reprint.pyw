﻿#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Author:      Elder Sanitá Trevisan
#
# Copyright(©) 2015 Elder Sanitá Trevisan
# Licence:     GPL
#-------------------------------------------------------------------------------
from datetime import datetime, time, timedelta
import banco
import ticket
from PySide import QtCore, QtGui, QtXml, QtXmlPatterns

class Ui_rePrint(object):
    def setupUi(self, rePrint):
        rePrint.setObjectName("rePrint")
        rePrint.resize(600, 285)
        rePrint.setMinimumSize(QtCore.QSize(600, 285))
        rePrint.setMaximumSize(QtCore.QSize(600, 285))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/favicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        rePrint.setWindowIcon(icon)
        self.gridLayoutWidget = QtGui.QWidget(rePrint)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 100, 581, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_placa = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_placa.sizePolicy().hasHeightForWidth())
        self.lbl_placa.setSizePolicy(sizePolicy)
        self.lbl_placa.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_placa.setFont(font)
        self.lbl_placa.setFrameShape(QtGui.QFrame.Panel)
        self.lbl_placa.setText("")
        self.lbl_placa.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_placa.setObjectName("lbl_placa")
        self.gridLayout.addWidget(self.lbl_placa, 1, 4, 1, 1)
        self.lbl_modelo = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_modelo.sizePolicy().hasHeightForWidth())
        self.lbl_modelo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_modelo.setFont(font)
        self.lbl_modelo.setFrameShape(QtGui.QFrame.Panel)
        self.lbl_modelo.setText("")
        self.lbl_modelo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_modelo.setObjectName("lbl_modelo")
        self.gridLayout.addWidget(self.lbl_modelo, 1, 3, 1, 1)
        self.l_modelo = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_modelo.setFont(font)
        self.l_modelo.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_modelo.setAlignment(QtCore.Qt.AlignCenter)
        self.l_modelo.setObjectName("l_modelo")
        self.gridLayout.addWidget(self.l_modelo, 0, 3, 1, 1)
        self.l_placa = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_placa.setFont(font)
        self.l_placa.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_placa.setAlignment(QtCore.Qt.AlignCenter)
        self.l_placa.setObjectName("l_placa")
        self.gridLayout.addWidget(self.l_placa, 0, 4, 1, 1)
        self.l_marca = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_marca.setFont(font)
        self.l_marca.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_marca.setAlignment(QtCore.Qt.AlignCenter)
        self.l_marca.setObjectName("l_marca")
        self.gridLayout.addWidget(self.l_marca, 0, 0, 1, 1)
        self.lbl_marca = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_marca.sizePolicy().hasHeightForWidth())
        self.lbl_marca.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_marca.setFont(font)
        self.lbl_marca.setFrameShape(QtGui.QFrame.Panel)
        self.lbl_marca.setText("")
        self.lbl_marca.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_marca.setObjectName("lbl_marca")
        self.gridLayout.addWidget(self.lbl_marca, 1, 0, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(rePrint)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_buscaNv = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_buscaNv.sizePolicy().hasHeightForWidth())
        self.lb_buscaNv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lb_buscaNv.setFont(font)
        self.lb_buscaNv.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_buscaNv.setObjectName("lb_buscaNv")
        self.verticalLayout.addWidget(self.lb_buscaNv)
        self.horizontalLayoutWidget = QtGui.QWidget(rePrint)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 160, 33))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.busca_nv = QtGui.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.busca_nv.setFont(font)
        self.busca_nv.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.busca_nv.setText("")
        self.busca_nv.setMaxLength(6)
        self.busca_nv.setAlignment(QtCore.Qt.AlignCenter)
        self.busca_nv.setObjectName("busca_nv")
        self.horizontalLayout.addWidget(self.busca_nv)
        self.bt_busca_nv = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_busca_nv.setFont(font)
        self.bt_busca_nv.setObjectName("bt_busca_nv")
        self.horizontalLayout.addWidget(self.bt_busca_nv)
        self.verticalLayoutWidget_2 = QtGui.QWidget(rePrint)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(470, 190, 121, 88))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bt_imprimir = QtGui.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_imprimir.setFont(font)
        self.bt_imprimir.setObjectName("bt_imprimir")
        self.verticalLayout_2.addWidget(self.bt_imprimir)
        spacerItem = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.bt_quit = QtGui.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_quit.setFont(font)
        self.bt_quit.setObjectName("bt_quit")
        self.verticalLayout_2.addWidget(self.bt_quit)

        self.retranslateUi(rePrint)
        QtCore.QObject.connect(self.bt_quit, QtCore.SIGNAL("clicked()"), rePrint.close)
        QtCore.QMetaObject.connectSlotsByName(rePrint)
        
#INÍCIO DA LÓGICA DO SISTEMA###################################################
        #EVENTO PARA FAZER A BUSCA DA NV NO BANCO DE DADOS
        QtCore.QObject.connect(self.bt_busca_nv, QtCore.SIGNAL("clicked()"), self.buscaNv)
        
        #EVENTO PARA FAZER A RE-IMPRESSÃO
        QtCore.QObject.connect(self.bt_imprimir, QtCore.SIGNAL("clicked()"), self.impressao)
        
        self.nv = 0
        
    def buscaNv(self):
        """MÉTODO PARA FAZER A BUSCA DA NV NO BANCO
        E EXIBIR NA TELA"""
        nv = self.busca_nv.text()
        marca, modelo, placa = banco.search(nv)
        self.lbl_marca.setText(marca)
        self.lbl_modelo.setText(modelo)
        self.lbl_placa.setText(placa)
        self.nv = nv
        
    def impressao(self):
        self.nv = int(self.nv)
        tipo, marca, modelo, placa, data, hora_entrada, hora_saida, encerrado = banco.searchDb(self.nv)
        hEntrada = datetime.strptime(str(hora_entrada), "%Y-%m-%d %H:%M:%S.%f")
        doc = ticket.ticket(self.nv,marca,modelo,placa,hEntrada.strftime("%d-%m-%Y"),hEntrada.strftime("%H:%M:%S"))
        printer = QtGui.QPrinter()
        printer.setCreator("parkSYS")
        printer.setResolution(600)  #dpi
        printer.setPageMargins(1, 1, 1, 1, printer.Millimeter)  #left, top, right, bottom, unit
        sizePage = QtCore.QSizeF(350, 500)    #w,h
        printer.setPaperSize(sizePage, printer.Millimeter)  #ou Point, Inch, DevicePixel...
        printer.setFullPage(True)
        text = QtGui.QTextDocument(doc)
        printer.setDocName("parkSYS_"+str(self.nv))
        text.print_(printer)
        
#FIM DA LÓGICA DO SISTEMA###################################################

    def retranslateUi(self, rePrint):
        rePrint.setWindowTitle(QtGui.QApplication.translate("rePrint", "parkSYS - Reimpressão", None, QtGui.QApplication.UnicodeUTF8))
        self.l_modelo.setText(QtGui.QApplication.translate("rePrint", "MODELO", None, QtGui.QApplication.UnicodeUTF8))
        self.l_placa.setText(QtGui.QApplication.translate("rePrint", "PLACA", None, QtGui.QApplication.UnicodeUTF8))
        self.l_marca.setText(QtGui.QApplication.translate("rePrint", "MARCA", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_buscaNv.setText(QtGui.QApplication.translate("rePrint", "Buscar NV", None, QtGui.QApplication.UnicodeUTF8))
        self.busca_nv.setToolTip(QtGui.QApplication.translate("rePrint", "<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt;\">INFORME A NV PARA FAZER A BUSCA</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_busca_nv.setToolTip(QtGui.QApplication.translate("rePrint", "<html><head/><body><p><span style=\" font-size:10pt;\">PRESSIONE PARA EFETUAR A BUSCA</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_busca_nv.setText(QtGui.QApplication.translate("rePrint", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_imprimir.setToolTip(QtGui.QApplication.translate("rePrint", "<html><head/><body><p><span style=\" font-size:10pt;\">PRESSIONE PARA EFETUAR A BUSCA</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_imprimir.setText(QtGui.QApplication.translate("rePrint", "Imprimir", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_quit.setToolTip(QtGui.QApplication.translate("rePrint", "<html><head/><body><p><span style=\" font-size:10pt;\">PRESSIONE PARA EFETUAR A BUSCA</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_quit.setText(QtGui.QApplication.translate("rePrint", "Sair", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    rePrint = QtGui.QDialog()
    ui = Ui_rePrint()
    ui.setupUi(rePrint)
    rePrint.show()
    sys.exit(app.exec_())
