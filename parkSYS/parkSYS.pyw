#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Author:      Elder Sanitá Trevisan
#
# Copyright(©) 2015 Elder Sanitá Trevisan
# Licence:     GPL
#-------------------------------------------------------------------------------
import locale
locale.setlocale(locale.LC_ALL, 'portuguese_brazil')
import sys
import os
from datetime import datetime, time, timedelta
import time
import gera_banco
import banco
import ticket
import configparser
from printer_settings import Ui_printer_settings
from cobranca_clientes import Ui_cobranca_mensalistas
from cadMensalistas import Ui_CadMensalistas
from settings import Ui_settings
from reprint import Ui_rePrint
from report import Ui_Relatorio
from PySide import QtCore, QtGui

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.setWindowModality(QtCore.Qt.NonModal)
        main.resize(775, 625)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        main.setMinimumSize(QtCore.QSize(775, 625))
        main.setMaximumSize(QtCore.QSize(775, 625))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/favicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hora_display = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hora_display.setFont(font)
        self.hora_display.setNumDigits(8)
        self.hora_display.setObjectName("hora_display")
        self.horizontalLayout.addWidget(self.hora_display)
        self.data_display = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_display.setFont(font)
        self.data_display.setNumDigits(10)
        self.data_display.setObjectName("data_display")
        self.horizontalLayout.addWidget(self.data_display)
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 140, 751, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridEntrada = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridEntrada.setContentsMargins(0, 0, 0, 0)
        self.gridEntrada.setObjectName("gridEntrada")
        self.ins_modelo = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ins_modelo.setFont(font)
        self.ins_modelo.setText("")
        self.ins_modelo.setMaxLength(15)
        self.ins_modelo.setAlignment(QtCore.Qt.AlignCenter)
        self.ins_modelo.setObjectName("ins_modelo")
        self.gridEntrada.addWidget(self.ins_modelo, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridEntrada.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridEntrada.addWidget(self.label_2, 0, 1, 1, 1)
        self.ins_marca = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ins_marca.setFont(font)
        self.ins_marca.setText("")
        self.ins_marca.setMaxLength(15)
        self.ins_marca.setAlignment(QtCore.Qt.AlignCenter)
        self.ins_marca.setObjectName("ins_marca")
        self.gridEntrada.addWidget(self.ins_marca, 1, 1, 1, 1)
        self.tipos_veiculos = QtGui.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tipos_veiculos.setFont(font)
        self.tipos_veiculos.setObjectName("tipos_veiculos")
        self.gridEntrada.addWidget(self.tipos_veiculos, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridEntrada.addWidget(self.label_4, 0, 3, 1, 1)
        self.ins_placa = QtGui.QLineEdit(self.gridLayoutWidget)
        self.ins_placa.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ins_placa.setFont(font)
        self.ins_placa.setText("")
        self.ins_placa.setMaxLength(8)
        self.ins_placa.setAlignment(QtCore.Qt.AlignCenter)
        self.ins_placa.setObjectName("ins_placa")
        self.gridEntrada.addWidget(self.ins_placa, 1, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridEntrada.addWidget(self.label_5, 0, 0, 1, 1)
        self.btn_gerar = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_gerar.setFont(font)
        self.btn_gerar.setObjectName("btn_gerar")
        self.gridEntrada.addWidget(self.btn_gerar, 1, 4, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.entrada = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.entrada.setFont(font)
        self.entrada.setAlignment(QtCore.Qt.AlignCenter)
        self.entrada.setObjectName("entrada")
        self.verticalLayout.addWidget(self.entrada)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 271, 62, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.saida = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.saida.setFont(font)
        self.saida.setObjectName("saida")
        self.verticalLayout_2.addWidget(self.saida)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 311, 91, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.busca_nv = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.busca_nv.setFont(font)
        self.busca_nv.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.busca_nv.setText("")
        self.busca_nv.setMaxLength(6)
        self.busca_nv.setAlignment(QtCore.Qt.AlignCenter)
        self.busca_nv.setObjectName("busca_nv")
        self.verticalLayout_3.addWidget(self.busca_nv)
        self.btn_busca_nv = QtGui.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_busca_nv.setFont(font)
        self.btn_busca_nv.setObjectName("btn_busca_nv")
        self.verticalLayout_3.addWidget(self.btn_busca_nv)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 401, 751, 104))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_tempo_permanencia = QtGui.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_tempo_permanencia.sizePolicy().hasHeightForWidth())
        self.lbl_tempo_permanencia.setSizePolicy(sizePolicy)
        self.lbl_tempo_permanencia.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_tempo_permanencia.setFont(font)
        self.lbl_tempo_permanencia.setFrameShape(QtGui.QFrame.Panel)
        self.lbl_tempo_permanencia.setText("")
        self.lbl_tempo_permanencia.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tempo_permanencia.setObjectName("lbl_tempo_permanencia")
        self.gridLayout.addWidget(self.lbl_tempo_permanencia, 1, 8, 1, 1)
        self.lbl_valor = QtGui.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_valor.sizePolicy().hasHeightForWidth())
        self.lbl_valor.setSizePolicy(sizePolicy)
        self.lbl_valor.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_valor.setFont(font)
        self.lbl_valor.setFrameShape(QtGui.QFrame.Panel)
        self.lbl_valor.setText("")
        self.lbl_valor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_valor.setObjectName("lbl_valor")
        self.gridLayout.addWidget(self.lbl_valor, 1, 9, 1, 1)
        self.l_valor = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_valor.setFont(font)
        self.l_valor.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_valor.setAlignment(QtCore.Qt.AlignCenter)
        self.l_valor.setObjectName("l_valor")
        self.gridLayout.addWidget(self.l_valor, 0, 9, 1, 1)
        self.l_hEntrada = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_hEntrada.setFont(font)
        self.l_hEntrada.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_hEntrada.setAlignment(QtCore.Qt.AlignCenter)
        self.l_hEntrada.setObjectName("l_hEntrada")
        self.gridLayout.addWidget(self.l_hEntrada, 0, 6, 1, 1)
        self.l_permancencia = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_permancencia.setFont(font)
        self.l_permancencia.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_permancencia.setAlignment(QtCore.Qt.AlignCenter)
        self.l_permancencia.setObjectName("l_permancencia")
        self.gridLayout.addWidget(self.l_permancencia, 0, 8, 1, 1)
        self.l_hSaida = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_hSaida.setFont(font)
        self.l_hSaida.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_hSaida.setAlignment(QtCore.Qt.AlignCenter)
        self.l_hSaida.setObjectName("l_hSaida")
        self.gridLayout.addWidget(self.l_hSaida, 0, 7, 1, 1)
        self.lbl_hora_saida = QtGui.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_hora_saida.sizePolicy().hasHeightForWidth())
        self.lbl_hora_saida.setSizePolicy(sizePolicy)
        self.lbl_hora_saida.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_hora_saida.setFont(font)
        self.lbl_hora_saida.setFrameShape(QtGui.QFrame.Panel)
        self.lbl_hora_saida.setText("")
        self.lbl_hora_saida.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_hora_saida.setObjectName("lbl_hora_saida")
        self.gridLayout.addWidget(self.lbl_hora_saida, 1, 7, 1, 1)
        self.lbl_hora_entrada = QtGui.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_hora_entrada.sizePolicy().hasHeightForWidth())
        self.lbl_hora_entrada.setSizePolicy(sizePolicy)
        self.lbl_hora_entrada.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_hora_entrada.setFont(font)
        self.lbl_hora_entrada.setFrameShape(QtGui.QFrame.Panel)
        self.lbl_hora_entrada.setText("")
        self.lbl_hora_entrada.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_hora_entrada.setObjectName("lbl_hora_entrada")
        self.gridLayout.addWidget(self.lbl_hora_entrada, 1, 6, 1, 1)
        self.btn_encerrar_nv = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.btn_encerrar_nv.setMaximumSize(QtCore.QSize(130, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_encerrar_nv.setFont(font)
        self.btn_encerrar_nv.setObjectName("btn_encerrar_nv")
        self.gridLayout.addWidget(self.btn_encerrar_nv, 3, 9, 1, 1)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 549, 751, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.msg = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.msg.setFont(font)
        self.msg.setFrameShape(QtGui.QFrame.Panel)
        self.msg.setText("")
        self.msg.setObjectName("msg")
        self.horizontalLayout_2.addWidget(self.msg)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_quit = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_quit.sizePolicy().hasHeightForWidth())
        self.btn_quit.setSizePolicy(sizePolicy)
        self.btn_quit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.btn_quit.setObjectName("btn_quit")
        self.horizontalLayout_2.addWidget(self.btn_quit)
        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(110, 310, 651, 71))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.l_marca = QtGui.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_marca.setFont(font)
        self.l_marca.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_marca.setAlignment(QtCore.Qt.AlignCenter)
        self.l_marca.setObjectName("l_marca")
        self.gridLayout_2.addWidget(self.l_marca, 0, 0, 1, 1)
        self.lbl_marca = QtGui.QLabel(self.gridLayoutWidget_3)
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
        self.gridLayout_2.addWidget(self.lbl_marca, 1, 0, 1, 1)
        self.l_modelo = QtGui.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_modelo.setFont(font)
        self.l_modelo.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_modelo.setAlignment(QtCore.Qt.AlignCenter)
        self.l_modelo.setObjectName("l_modelo")
        self.gridLayout_2.addWidget(self.l_modelo, 0, 1, 1, 1)
        self.lbl_modelo = QtGui.QLabel(self.gridLayoutWidget_3)
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
        self.gridLayout_2.addWidget(self.lbl_modelo, 1, 1, 1, 1)
        self.l_placa = QtGui.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_placa.setFont(font)
        self.l_placa.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_placa.setAlignment(QtCore.Qt.AlignCenter)
        self.l_placa.setObjectName("l_placa")
        self.gridLayout_2.addWidget(self.l_placa, 0, 2, 1, 1)
        self.lbl_placa = QtGui.QLabel(self.gridLayoutWidget_3)
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
        self.gridLayout_2.addWidget(self.lbl_placa, 1, 2, 1, 1)
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Arquivo = QtGui.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName("menu_Arquivo")
        self.menuConfig = QtGui.QMenu(self.menubar)
        self.menuConfig.setObjectName("menuConfig")
        self.menuAjuda = QtGui.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        self.menuMensalistas = QtGui.QMenu(self.menubar)
        self.menuMensalistas.setObjectName("menuMensalistas")
        main.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)
        self.actionFechar = QtGui.QAction(main)
        self.actionFechar.setObjectName("actionFechar")
        self.sobre = QtGui.QAction(main)
        self.sobre.setObjectName("sobre")
        self.actionVers_o = QtGui.QAction(main)
        self.actionVers_o.setObjectName("actionVers_o")
        self.actionContato = QtGui.QAction(main)
        self.actionContato.setObjectName("actionContato")
        self.actionImpressao = QtGui.QAction(main)
        self.actionImpressao.setObjectName("actionImpressao")
        self.actionGeral = QtGui.QAction(main)
        self.actionGeral.setObjectName("actionGeral")
        self.actionSistema = QtGui.QAction(main)
        self.actionSistema.setObjectName("actionSistema")
        self.actionRe_imprimir_NV = QtGui.QAction(main)
        self.actionRe_imprimir_NV.setObjectName("actionRe_imprimir_NV")
        self.actionRelat_rio_Gerencial = QtGui.QAction(main)
        self.actionRelat_rio_Gerencial.setObjectName("actionRelat_rio_Gerencial")
        self.tutorial = QtGui.QAction(main)
        self.tutorial.setObjectName("tutorial")
        self.actionCadastro = QtGui.QAction(main)
        self.actionCadastro.setObjectName("actionCadastro")
        self.actionCobranca = QtGui.QAction(main)
        self.actionCobranca.setObjectName("actionCobranca")
        self.menu_Arquivo.addAction(self.actionRe_imprimir_NV)
        self.menu_Arquivo.addAction(self.actionRelat_rio_Gerencial)
        self.menu_Arquivo.addSeparator()
        self.menu_Arquivo.addAction(self.actionFechar)
        self.menuConfig.addAction(self.actionGeral)
        self.menuConfig.addSeparator()
        self.menuConfig.addAction(self.actionImpressao)
        self.menuAjuda.addAction(self.tutorial)
        self.menuAjuda.addSeparator()
        self.menuAjuda.addAction(self.sobre)
        self.menuMensalistas.addAction(self.actionCadastro)
        self.menuMensalistas.addAction(self.actionCobranca)
        self.menubar.addAction(self.menu_Arquivo.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuMensalistas.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(main)
        QtCore.QObject.connect(self.actionFechar, QtCore.SIGNAL("triggered()"), main.close)
        QtCore.QObject.connect(self.btn_quit, QtCore.SIGNAL("clicked()"), main.close)
        QtCore.QMetaObject.connectSlotsByName(main)
        main.setTabOrder(self.tipos_veiculos, self.ins_marca)
        main.setTabOrder(self.ins_marca, self.ins_modelo)
        main.setTabOrder(self.ins_modelo, self.ins_placa)
        main.setTabOrder(self.ins_placa, self.btn_gerar)
        main.setTabOrder(self.btn_gerar, self.busca_nv)
        main.setTabOrder(self.busca_nv, self.btn_busca_nv)
        main.setTabOrder(self.btn_busca_nv, self.btn_quit)

#INÍCIO DA LÓGICA DO SISTEMA ###################################################
        
        #####INÍCIO DOS EVENTOS#####
        #EVENTO PARA ABRIR O TUTORIAL
        QtCore.QObject.connect(self.tutorial, QtCore.SIGNAL("triggered()"),self.abre_tutorial)
        #
        QtCore.QObject.connect(self.actionImpressao, QtCore.SIGNAL("triggered()"),self.printer_settings)
        #EVENTO PARA ABRIR A TELA DE COBRANÇA DE MENSALISTAS
        QtCore.QObject.connect(self.actionCobranca, QtCore.SIGNAL("triggered()"), self.cobranca_mensalistas)
        #EVENTO PARA ABRIR A TELA DE CADASTRO DE MENSALISTAS
        QtCore.QObject.connect(self.actionCadastro, QtCore.SIGNAL("triggered()"), self.cad_mensalistas)
        #EVENTO PARA ABRIR A TELA DE RELATÓRIO GERENCIAL
        QtCore.QObject.connect(self.actionRelat_rio_Gerencial, QtCore.SIGNAL("triggered()"), self.relatGerencial)
        #EVENTO PARA ABRIR A TELA DE INFORMAÇÕES
        QtCore.QObject.connect(self.sobre, QtCore.SIGNAL("triggered()"), self.info)
        #EVENTO PARA ABRIR A TELA DE REIMPRESSÃO
        QtCore.QObject.connect(self.actionRe_imprimir_NV, QtCore.SIGNAL("triggered()"), self.reimprimir)
        #EVENTO PARA ABRIR A TELA DE CONFIGURAÇÕES
        QtCore.QObject.connect(self.actionGeral, QtCore.SIGNAL("triggered()"), self.settings)
        #EVENTO PARA INSERIR DADOS NO BANCO
        QtCore.QObject.connect(self.btn_gerar,QtCore.SIGNAL("clicked()"),self.insereDb)
        #EVENTO PARA BUSCAR DADOS NO BANCO
        QtCore.QObject.connect(self.btn_busca_nv,QtCore.SIGNAL("clicked()"),self.buscaDb)
        #EVENTO PARA ENCERRAR A NV
        QtCore.QObject.connect(self.btn_encerrar_nv,QtCore.SIGNAL("clicked()"),self.encerraNv)
        #
        #####FIM DOS EVENTOS######
        
        completerMarca = QtGui.QCompleter(['GM - CHEVROLET','FIAT','FORD','VOLKSWAGEN',\
                                    'TOYOTA','HONDA','SUZUKI','YAMAHA','CHRYSLER','LAND ROVER',\
                                    'JAC MOTORS','RENAULT','KIA','VOLVO', 'AUDI','CITR\326EN',\
									'PEUGEOT'])
                                    
        self.ins_marca.setCompleter(completerMarca)
        self.ins_marca.textChanged.connect(self.upperCaseMarca)
        self.ins_modelo.textChanged.connect(self.upperCaseModelo)
        self.ins_placa.setInputMask(">AAA-0000")
        self.ins_placa.returnPressed.connect(self.insereDb)
        
        self.busca_nv.returnPressed.connect(self.buscaDb)
        
        #EXIBIÇÃO DE DATA E HORA NA TELA
        self.hora_display.display(time.strftime("%H:%M:%S"))
        self.data_display.display(time.strftime("%d-%m-%Y"))

        self.timer = QtCore.QTimer(main)
        self.timer.timeout.connect(self.time)
        self.timer.start(1000)

        self.horaAdicional = 0
        self.horaCarro = 0
        self.horaMoto = 0
        self.horaOutros = 0
        
        self.tipos = ("","CARRO","MOTO","OUTROS")
        self.listaTipos()
        
        #PROCESSO PARA VERIFICAR SE O BANCO EXISTE, SE NÃO EXISTIR DEVERÁ SER CRIADO
        if os.path.exists("db/database.db"):
            pass
        else:
            msgBox = QtGui.QMessageBox(main)
            ok = msgBox.addButton("Ok", QtGui.QMessageBox.AcceptRole)
            msgBox.setText("<b>ATENÇÃO: O BANCO DE DADOS NÃO FOI CRIADO!<br>"\
                "PARA UTILIZAR O SISTEMA DEVE-SE PRIMEIRO CRIAR O BANCO.</b>")
            msgBox.exec_()
            if msgBox.clickedButton() == ok:
                gera_banco
                sys.exit()
                
    def abre_tutorial(self):
        os.startfile("parkSYS - Tutorial.pdf")
        
    def printer_settings(self):
        printer_settings = QtGui.QDialog()
        ui = Ui_printer_settings()
        ui.setupUi(printer_settings)
        printer_settings.exec_()
        
    def cobranca_mensalistas(self):
        cobranca_mensalistas = QtGui.QDialog()
        ui = Ui_cobranca_mensalistas()
        ui.setupUi(cobranca_mensalistas)
        cobranca_mensalistas.exec_()
        
    #ABRE A TELA DE CADASTRO DE MENSALISTAS    
    def cad_mensalistas(self):
        CadMensalistas = QtGui.QDialog()
        ui = Ui_CadMensalistas()
        ui.setupUi(CadMensalistas)
        CadMensalistas.exec_()
    
    #ABRE A TELA DE RELATÓRIO GERENCIAL
    def relatGerencial(self):
        Relatorio = QtGui.QDialog()
        ui = Ui_Relatorio()
        ui.setupUi(Relatorio)
        Relatorio.exec_()
    
    #MÉTODO PARA SETAR OS VALORES DE CADA TIPO DE VEÍCULO
    def valores(self):
        self.config = configparser.SafeConfigParser()
        self.config.read('config/config.ini')
        self.horaAdicional = int(self.config.get('sistema','valor_hora_ad'))
        self.horaCarro = int(self.config.get('sistema','valor_hora_c'))
        self.horaMoto = int(self.config.get('sistema','valor_hora_m'))
        self.horaOutros = int(self.config.get('sistema','valor_hora_o'))
    
    #ABRE A TELA DE CONFIGURAÇÕES DO SISTEMA E DA EMPRESA
    def settings(self):
        settings = QtGui.QDialog()
        ui = Ui_settings()
        ui.setupUi(settings)
        settings.exec_()
    
    #ABRE A TELA DE REIMPRESSÃO DA NV
    def reimprimir(self):
        rePrint = QtGui.QDialog()
        ui = Ui_rePrint()
        ui.setupUi(rePrint)
        rePrint.exec_()
        
    #MÉTODOS PARA DEFINIR COMO MAIÚSCULO AUTOMATICAMENTE O CAMPO DE MARCA
    def upperCaseMarca(self):
        textMarca = self.ins_marca.text().upper()
        return self.ins_marca.setText(textMarca)
    
    #MÉTODOS PARA DEFINIR COMO MAIÚSCULO AUTOMATICAMENTE O CAMPO DE MODELO
    def upperCaseModelo(self):
        textModelo = self.ins_modelo.text().upper()
        return self.ins_modelo.setText(textModelo)
    
    #ABRE A TELA DE INFORMAÇÕES DO SISTEMA
    def info(self):
        versao = QtGui.QMessageBox()
        versao.information(main, "parkSYS - Informações",\
                        "<center><b>parkSYS<br>Sistema de Gerenciamento "\
                        "de Estacionamentos</b>\n"\
                        "<br>Versão: 1.0<br><br>"\
                        "Desenvolvimento: Elder S. Trevisan<br><br>"\
                        "Contato: <a href='mailto:trevisan.elder@gmail.com?"\
                        "Subject=Contato%20-%20parkSYS' target='_top'>"\
                            "trevisan.elder@gmail.com</a></center>",\
                            QtGui.QMessageBox.Ok)
        
    #MÉTODO PARA INSERIR OS TIPOS DE VEÍCULOS NO LISTBOX###############################
    def listaTipos(self):
        k = 0
        for i in self.tipos:
            self.tipos_veiculos.addItem("")
            self.tipos_veiculos.setItemText(k, QtGui.QApplication.translate("main", i, None, QtGui.QApplication.UnicodeUTF8))
            k += 1

    #MOSTRAR A HORA NA TELA
    def time(self):
        self.hora_display.display(time.strftime("%H:%M:%S"))

    #INSERE DADOS NO BANCO
    def insereDb(self):
        tipo = self.tipos_veiculos.currentIndex()
        marca = self.ins_marca.text()
        modelo = self.ins_modelo.text()
        placa = self.ins_placa.text()
        data = datetime.now()
        hora_entrada = datetime.now()
        msg, nv = banco.insertDb(tipo, marca, modelo, placa, data, hora_entrada)
        self.msg.setText(msg)
        self.impressao(nv, marca, modelo, placa, data, hora_entrada)
        self.tipos_veiculos.setFocus()

    #ABRE A JANELA DE DIÁLOGO DA IMPRESSÃO DO TICKET
    def impressao(self,nv,marca,modelo,placa,data,hora_entrada):
        self.config = configparser.SafeConfigParser()
        self.config.read('config/config.ini')
        impressora = self.config.get('impressao','impressora')
        left = int(self.config.get('impressao','m_esquerda'))
        top = int(self.config.get('impressao','m_topo'))
        right = int(self.config.get('impressao','m_direita'))
        bottom = int(self.config.get('impressao','m_fundo'))
        larg_papel = int(self.config.get('impressao','larg_papel'))
        hEntrada = datetime.strptime(str(hora_entrada), "%Y-%m-%d %H:%M:%S.%f")
        doc = ticket.ticket(nv,marca,modelo,placa,hEntrada.strftime("%d-%m-%Y"),hEntrada.strftime("%H:%M:%S"))
        msgBox = QtGui.QMessageBox(main)
        sim = msgBox.addButton("Sim", QtGui.QMessageBox.YesRole)
        nao = msgBox.addButton("Não", QtGui.QMessageBox.NoRole)
        msgBox.setText("<b>Deseja imprimir a NV?</b>")
        msgBox.exec_()
        
        if msgBox.clickedButton() == sim:
            printer = QtGui.QPrinter()
            printer.setPrinterName(impressora)
            printer.setCreator("parkSYS")
            printer.setResolution(600)  #dpi
            printer.setPageMargins(left, top, right, bottom, printer.Millimeter)  #left, top, right, bottom, unit
            sizePage = QtCore.QSizeF(larg_papel, 768)    #w,h
            printer.setPaperSize(sizePage, printer.Millimeter)  #ou Point, Inch, DevicePixel...
            printer.setFullPage(True)
            text = QtGui.QTextDocument(doc)
            printer.setDocName("parkSYS_"+str(nv))
            text.print_(printer)
        else:
            pass
        self.limpaCamposIns()
        
    #LIMPA OS CAMPOS DE INSERÇÃO DE DADOS
    def limpaCamposIns(self):
        self.ins_marca.clear()
        self.ins_modelo.clear()
        self.ins_placa.clear()
        self.msg.clear()
        self.tipos_veiculos.clear()
        self.listaTipos()

    #BUSCA DADOS NO BANCO
    def buscaDb(self):        
        self.valores()  #EXECUTA O MÉTODO VALORES PARA BUSCAR INFORMAÇÕES DE CONFIGURAÇÃO
        agora = datetime.now()  #ATRIBUTO COM A DATA ATUAL
        nv = int(self.busca_nv.text())  #CAPTURA O NUMERO DE NV INFORMADO NA TELA
        tolerancia = int(self.config.get('sistema','tolerancia'))
        permanencia = None
            
        if nv > 0:
            #BUSCAR AS INFORMAÇÕES DA NV NO BANCO
            try:
                tipo, marca, modelo, placa, data, hora_entrada, hora_saida, encerrado = banco.searchDb(nv)
                #CONVERTER EM DATETIME A VARIÁVEL hora_entrada
                hora_entrada = datetime.strptime(hora_entrada, "%Y-%m-%d %H:%M:%S.%f")
                #EXIBIR AS INFORMAÇÕES NA NV NA TELA
                self.lbl_marca.setText(marca)
                self.lbl_modelo.setText(modelo)
                self.lbl_placa.setText(placa)
                self.lbl_hora_entrada.setText(hora_entrada.strftime("%H:%M:%S"))
                #VERIFICA SE A NV ESTÁ ENCERRADA
                if (encerrado == "Não"):
                    self.msg.setText("<b>NV Aberta</b>")
                    self.lbl_hora_saida.setText(agora.strftime("%H:%M:%S"))
                    #CONDIÇÃO PRA SABER SE ESTÁ NA TOLERÂNCIA
                    if (agora-hora_entrada) > timedelta(days=0, hours=0, minutes=tolerancia, seconds=0):
                        #SE ESTIVER ACIMA DA TOLERÂNCIA, CHAMA O MÉTODO PAGAMENTO E
                        #ENVIA PARAMETROS DO TIPO DE VEÍCULO E A HORA DE ENTRADA DO VEÍCULO
                        self.calcula_hora(tipo, hora_entrada)
                    else:
                        #SE ESTIVER DENTRO DA TOLERÂNCIA, EXIBE A MENSAGEM NA TELA
                        permanencia = str(agora - hora_entrada)
                        self.lbl_tempo_permanencia.setText(permanencia)
                        self.msg.setText("<b>NV Dentro da tolerância</b>")
                        self.lbl_valor.clear()
                else:
                    self.msg.setText("<b>NV Encerrada</b>")
                    hSaida = datetime.strptime(hora_saida, "%H:%M:%S")
                    self.lbl_hora_saida.setText(hSaida.strftime("%H:%M:%S"))
                    self.lbl_tempo_permanencia.clear()
                    self.lbl_valor.clear()
            except:
                self.limpaCamposEnc()
                self.msg.setText("<b>NV Não existe.</b>")

    #ENCERRA A NV
    def encerraNv(self):
        nv = self.busca_nv.text()
        valor = self.lbl_valor.text()
        permanencia = self.lbl_tempo_permanencia.text()
        msg = banco.closesDb(nv, valor, permanencia)
        self.msg.setText(msg)        
        msgBox = QtGui.QMessageBox(main)
        ok = msgBox.addButton("Ok", QtGui.QMessageBox.AcceptRole)
        msgBox.setText("<b>NV encerrada com sucesso!</b>")
        msgBox.exec_()
        if msgBox.clickedButton() == ok:
            self.limpaCamposEnc()

    #MÉTODO PARA LIMPAR OS CAMPOS DE ENCERRAMENTO NA NV
    def limpaCamposEnc(self):
        self.lbl_marca.clear()
        self.lbl_modelo.clear()
        self.lbl_placa.clear()
        self.lbl_hora_entrada.clear()
        self.lbl_hora_saida.clear()
        self.lbl_tempo_permanencia.clear()
        self.lbl_valor.clear()
        self.msg.clear()
    
    #MÉTODO PARA CALCULAR O TEMPO DE PERMANENCIA E EXIBIR NA TELA
    def calcula_hora(self, tipo, hora_entrada):
        config = configparser.SafeConfigParser()
        config.read('config/config.ini')
        forma_pagamento = config.get('sistema','metodo')
        inicio_pernoite = config.get('sistema','hora_ini_pernoite')
        termino_pernoite = config.get('sistema','hora_term_pernoite')
        valor_pernoite = int(config.get('sistema','valor_pernoite'))
        hoje = datetime.now()   #DATA E HORA ATUAL)
        #CONVERTE A HORA DE INICIO DE PERNOITE EM DATETIME
        inicio_pernoite = datetime.strptime(inicio_pernoite, "%H:%M")
        #JUNTA A DATA ATUAL COM A HORA DE INICIO DA PERNOITE
        inicio_pernoite = datetime.combine(hora_entrada.date(),inicio_pernoite.time())        
        #CONVERTE A HORA DE INICIO DE PERNOITE EM DATETIME
        termino_pernoite = datetime.strptime(termino_pernoite, "%H:%M")
        #JUNTA A DATA ATUAL COM A HORA DE TERMINO DA PERNOITE
        termino_pernoite = datetime.combine(hora_entrada.date(),termino_pernoite.time())
        hCarro = self.horaCarro     #VALOR DA HORA PARA CARROS
        hMoto = self.horaMoto   #VALOR DA HORA PARA MOTOS
        hOutros = self.horaOutros   #VALOR DA HORA PARA OUTROS VEÍCULOS
        hAdicional = self.horaAdicional   #VALOR DA HORA ADICIONAL
        tipo= str(tipo)
        tipos = {"1":hCarro,"2":hMoto,"3":hOutros}
        valor_veic = [valor for chave,valor in tipos.items() if chave == tipo]
        valor_veic = valor_veic[0]
        entrada = hora_entrada + timedelta(hours=1) #ACRESCENTA 1 HORA NA HORA DE ENTRADA
        calculo = 0
        permanencia = hoje - hora_entrada
        self.lbl_tempo_permanencia.setText(str(permanencia))
        if forma_pagamento == "Inteiro":
            if hoje < inicio_pernoite:
                horas_cobrar = int((hoje - hora_entrada).total_seconds() // 3600)
                calculo = valor_veic + (horas_cobrar * hAdicional)
                self.lbl_valor.setText(str(calculo))
            else:
                dias_cobrar_pernoite = (hoje - hora_entrada).days
                total_horas_pernoite = int((dias_cobrar_pernoite * (inicio_pernoite - termino_pernoite)).total_seconds() // 3600)
                horas_cobrar = int(((hoje - hora_entrada).total_seconds() // 3600) + 1)
                calculo = ((horas_cobrar - total_horas_pernoite) * hAdicional) + (valor_pernoite * dias_cobrar_pernoite) + valor_veic
                self.lbl_valor.setText(str(calculo))            
        elif forma_pagamento == "Fracionado":
            if hoje < inicio_pernoite:
                horas_cobrar = (permanencia.total_seconds() // 60) / 60
                calculo = valor_veic + (horas_cobrar * hAdicional)
                self.lbl_valor.setText(str("%.2f"%(calculo)))
            else:
                dias_cobrar_pernoite = (hoje - hora_entrada).days
                total_horas_pernoite = int((dias_cobrar_pernoite * (inicio_pernoite - termino_pernoite)).total_seconds() // 3600)
                horas_cobrar = (permanencia.total_seconds() // 60) / 60
                calculo = ((horas_cobrar - total_horas_pernoite) * hAdicional) + (valor_pernoite * dias_cobrar_pernoite) + valor_veic
                self.lbl_valor.setText(str("%.2f"%(calculo)))
        else:
            self.msg.setText("ATENÇÃO: MÉTODO DE COBRANÇA NÃO ESTÁ CONFIGURADO!")

#FIM DA LÓGICA DO SISTEMA ######################################################

    def retranslateUi(self, main):
        main.setWindowTitle(QtGui.QApplication.translate("main", "parkSYS", None, QtGui.QApplication.UnicodeUTF8))
        self.ins_modelo.setToolTip(QtGui.QApplication.translate("main", "<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt;\">INSIRA O MODELO DO VEÍCULO</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("main", "MODELO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("main", "MARCA", None, QtGui.QApplication.UnicodeUTF8))
        self.ins_marca.setToolTip(QtGui.QApplication.translate("main", "<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt;\">INSIRA A MARCA DO VEÍCULO</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tipos_veiculos.setToolTip(QtGui.QApplication.translate("main", "<html><head/><body><p align=\"justify\">ESCOLHA O TIPO DE VEÍCULO</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("main", "PLACA", None, QtGui.QApplication.UnicodeUTF8))
        self.ins_placa.setToolTip(QtGui.QApplication.translate("main", "<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt;\">INSIRA A PLACA DO VEÍCULO</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("main", "TIPO", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_gerar.setToolTip(QtGui.QApplication.translate("main", "<html><head/><body><p align=\"justify\">PRESSIONE PARA GERAR A NV</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_gerar.setText(QtGui.QApplication.translate("main", "GERAR NV", None, QtGui.QApplication.UnicodeUTF8))
        self.entrada.setText(QtGui.QApplication.translate("main", "ENTRADA", None, QtGui.QApplication.UnicodeUTF8))
        self.saida.setText(QtGui.QApplication.translate("main", "SAÍDA", None, QtGui.QApplication.UnicodeUTF8))
        self.busca_nv.setToolTip(QtGui.QApplication.translate("main", "<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt;\">INFORME A NV PARA FAZER A BUSCA</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_busca_nv.setToolTip(QtGui.QApplication.translate("main", "<html><head/><body><p><span style=\" font-size:10pt;\">PRESSIONE PARA EFETUAR A BUSCA</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_busca_nv.setText(QtGui.QApplication.translate("main", "BUSCAR", None, QtGui.QApplication.UnicodeUTF8))
        self.l_valor.setText(QtGui.QApplication.translate("main", "VALOR R$", None, QtGui.QApplication.UnicodeUTF8))
        self.l_hEntrada.setText(QtGui.QApplication.translate("main", "<html><head/><body><p>HORA ENTRADA</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.l_permancencia.setText(QtGui.QApplication.translate("main", "<html><head/><body><p>TEMPO PERMANÊNCIA</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.l_hSaida.setText(QtGui.QApplication.translate("main", "<html><head/><body><p>HORA SAÍDA</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_encerrar_nv.setToolTip(QtGui.QApplication.translate("main", "<html><head/><body><p>PRESSIONE PARA ENCERRAR A NV</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_encerrar_nv.setText(QtGui.QApplication.translate("main", "ENCERRAR NV", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_quit.setToolTip(QtGui.QApplication.translate("main", "<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt;\">SAIR DO SISTEMA</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_quit.setText(QtGui.QApplication.translate("main", "SAIR", None, QtGui.QApplication.UnicodeUTF8))
        self.l_marca.setText(QtGui.QApplication.translate("main", "MARCA", None, QtGui.QApplication.UnicodeUTF8))
        self.l_modelo.setText(QtGui.QApplication.translate("main", "MODELO", None, QtGui.QApplication.UnicodeUTF8))
        self.l_placa.setText(QtGui.QApplication.translate("main", "PLACA", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Arquivo.setTitle(QtGui.QApplication.translate("main", "&Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConfig.setTitle(QtGui.QApplication.translate("main", "Configurações", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAjuda.setTitle(QtGui.QApplication.translate("main", "Ajuda", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMensalistas.setTitle(QtGui.QApplication.translate("main", "Mensalistas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFechar.setText(QtGui.QApplication.translate("main", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.sobre.setText(QtGui.QApplication.translate("main", "Sobre", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVers_o.setText(QtGui.QApplication.translate("main", "Versão", None, QtGui.QApplication.UnicodeUTF8))
        self.actionContato.setText(QtGui.QApplication.translate("main", "Contato", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImpressao.setText(QtGui.QApplication.translate("main", "Impressão", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGeral.setText(QtGui.QApplication.translate("main", "Geral", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSistema.setText(QtGui.QApplication.translate("main", "Sistema", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRe_imprimir_NV.setText(QtGui.QApplication.translate("main", "Reimprimir NV", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRelat_rio_Gerencial.setText(QtGui.QApplication.translate("main", "Relatório Gerencial", None, QtGui.QApplication.UnicodeUTF8))
        self.tutorial.setText(QtGui.QApplication.translate("main", "Tutorial", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCadastro.setText(QtGui.QApplication.translate("main", "Cadastro", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCobranca.setText(QtGui.QApplication.translate("main", "Cobrança", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    main = QtGui.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())

