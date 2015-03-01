#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Author:      Elder Sanitá Trevisan
#
# Copyright(©) 2015 Elder Sanitá Trevisan
# Licence:     GPL
#-------------------------------------------------------------------------------
import configparser
from PySide import QtCore, QtGui

class Ui_printer_settings(object):
    def setupUi(self, printer_settings):
        printer_settings.setObjectName("printer_settings")
        printer_settings.resize(611, 248)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/favicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        printer_settings.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtGui.QWidget(printer_settings)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 591, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_imp_disponiveis = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_imp_disponiveis.sizePolicy().hasHeightForWidth())
        self.lb_imp_disponiveis.setSizePolicy(sizePolicy)
        self.lb_imp_disponiveis.setObjectName("lb_imp_disponiveis")
        self.horizontalLayout.addWidget(self.lb_imp_disponiveis)
        self.cb_imp_disponiveis = QtGui.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_imp_disponiveis.sizePolicy().hasHeightForWidth())
        self.cb_imp_disponiveis.setSizePolicy(sizePolicy)
        self.cb_imp_disponiveis.setMaximumSize(QtCore.QSize(16777215, 150))
        self.cb_imp_disponiveis.setObjectName("cb_imp_disponiveis")
        self.horizontalLayout.addWidget(self.cb_imp_disponiveis)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.impressora_padrao = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.impressora_padrao.sizePolicy().hasHeightForWidth())
        self.impressora_padrao.setSizePolicy(sizePolicy)
        self.impressora_padrao.setText("")
        self.impressora_padrao.setObjectName("impressora_padrao")
        self.horizontalLayout.addWidget(self.impressora_padrao)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(printer_settings)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 191, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_larg_papel = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.lb_larg_papel.setObjectName("lb_larg_papel")
        self.horizontalLayout_2.addWidget(self.lb_larg_papel)
        self.ins_larg_papel = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.ins_larg_papel.setObjectName("ins_larg_papel")
        self.horizontalLayout_2.addWidget(self.ins_larg_papel)
        self.gridLayoutWidget = QtGui.QWidget(printer_settings)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(300, 120, 301, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.sb_fundo = QtGui.QSpinBox(self.gridLayoutWidget)
        self.sb_fundo.setObjectName("sb_fundo")
        self.gridLayout.addWidget(self.sb_fundo, 1, 4, 1, 1)
        self.sb_direita = QtGui.QSpinBox(self.gridLayoutWidget)
        self.sb_direita.setObjectName("sb_direita")
        self.gridLayout.addWidget(self.sb_direita, 1, 3, 1, 1)
        self.lb_margens = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_margens.setObjectName("lb_margens")
        self.gridLayout.addWidget(self.lb_margens, 1, 0, 1, 1)
        self.sb_topo = QtGui.QSpinBox(self.gridLayoutWidget)
        self.sb_topo.setObjectName("sb_topo")
        self.gridLayout.addWidget(self.sb_topo, 1, 2, 1, 1)
        self.sb_esq = QtGui.QSpinBox(self.gridLayoutWidget)
        self.sb_esq.setObjectName("sb_esq")
        self.gridLayout.addWidget(self.sb_esq, 1, 1, 1, 1)
        self.lb_esq = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_esq.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_esq.setObjectName("lb_esq")
        self.gridLayout.addWidget(self.lb_esq, 0, 1, 1, 1)
        self.lb_topo = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_topo.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_topo.setObjectName("lb_topo")
        self.gridLayout.addWidget(self.lb_topo, 0, 2, 1, 1)
        self.lb_dir = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_dir.setObjectName("lb_dir")
        self.gridLayout.addWidget(self.lb_dir, 0, 3, 1, 1)
        self.lb_fundo = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_fundo.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_fundo.setObjectName("lb_fundo")
        self.gridLayout.addWidget(self.lb_fundo, 0, 4, 1, 1)
        self.lb_config_impressora = QtGui.QLabel(printer_settings)
        self.lb_config_impressora.setGeometry(QtCore.QRect(10, 10, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.lb_config_impressora.setFont(font)
        self.lb_config_impressora.setObjectName("lb_config_impressora")
        self.horizontalLayoutWidget_3 = QtGui.QWidget(printer_settings)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(310, 210, 291, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_salvar = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.bt_salvar.setObjectName("bt_salvar")
        self.horizontalLayout_3.addWidget(self.bt_salvar)
        self.bt_padrao = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.bt_padrao.setObjectName("bt_padrao")
        self.horizontalLayout_3.addWidget(self.bt_padrao)
        spacerItem1 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.bt_sair = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.bt_sair.setObjectName("bt_sair")
        self.horizontalLayout_3.addWidget(self.bt_sair)

        self.retranslateUi(printer_settings)
        QtCore.QObject.connect(self.bt_sair, QtCore.SIGNAL("clicked()"), printer_settings.close)
        QtCore.QMetaObject.connectSlotsByName(printer_settings)
        printer_settings.setTabOrder(self.cb_imp_disponiveis, self.ins_larg_papel)
        printer_settings.setTabOrder(self.ins_larg_papel, self.sb_esq)
        printer_settings.setTabOrder(self.sb_esq, self.sb_topo)
        printer_settings.setTabOrder(self.sb_topo, self.sb_direita)
        printer_settings.setTabOrder(self.sb_direita, self.sb_fundo)
        printer_settings.setTabOrder(self.sb_fundo, self.bt_salvar)
        printer_settings.setTabOrder(self.bt_salvar, self.bt_padrao)
        printer_settings.setTabOrder(self.bt_padrao, self.bt_sair)
        
#INÍCIO DA LÓGICA DO SISTEMA###################################################
        #EVENTO PARA RESTAURAR OS PADRÕES DE CONFIGURAÇÃO DE IMPRESSÃO
        QtCore.QObject.connect(self.bt_padrao, QtCore.SIGNAL("clicked()"), self.restaura_padrao)
        #EVENTO PARA ENVIAR O NOME DA IMPRESSORA SELECIONADA NO COMBOBOX PARA O MÉTODO INDICADO
        QtCore.QObject.connect(self.cb_imp_disponiveis, QtCore.SIGNAL("currentIndexChanged(QString)"), self.imp_padrao)
        #EVENTO PARA SALVAR AS CONFIGURAÇÕES DA IMPRESSORA
        QtCore.QObject.connect(self.bt_salvar, QtCore.SIGNAL("clicked()"), self.salva_config)
        
        self.config = configparser.SafeConfigParser()
        self.config.read('config/config.ini')
        
        #CARREGAR TODAS AS IMPRESSORAS DISPONÍVEIS E EXIBIR NO COMBOBOX DE IMPRESSORAS
        printers = QtGui.QPrinterInfo.availablePrinters()
        self.cb_imp_disponiveis.addItem("")
        k = 0
        for i in printers:
            i = QtGui.QPrinterInfo.printerName(i)
            k += 1
            self.cb_imp_disponiveis.addItem("")
            self.cb_imp_disponiveis.setItemText(k, QtGui.QApplication.translate("printer_settings", i, None, QtGui.QApplication.UnicodeUTF8))
        
        self.lerConfig()
        
    def restaura_padrao(self):
        self.impressora_padrao.setText('')
        self.ins_larg_papel.setText('150')
        self.sb_esq.setValue(1)
        self.sb_topo.setValue(1)
        self.sb_direita.setValue(1)
        self.sb_fundo.setValue(1)
        self.salva_config()
        
    def imp_padrao(self, arg):
        self.impressora_padrao.setText(arg)
    
    def lerConfig(self):
        self.impressora_padrao.setText(self.config.get('impressao','impressora'))
        self.ins_larg_papel.setText(self.config.get('impressao','larg_papel'))
        self.sb_esq.setValue(int(self.config.get('impressao','m_esquerda')))
        self.sb_topo.setValue(int(self.config.get('impressao','m_topo')))
        self.sb_direita.setValue(int(self.config.get('impressao','m_direita')))
        self.sb_fundo.setValue(int(self.config.get('impressao','m_fundo')))
    
    def salva_config(self):
        impressora = self.impressora_padrao.text()
        larg_papel = self.ins_larg_papel.text()
        marg_esq = str(self.sb_esq.value())
        marg_topo = str(self.sb_topo.value())
        marg_dir = str(self.sb_direita.value())
        marg_fundo = str(self.sb_fundo.value())
        
        self.config.set('impressao','impressora',impressora)
        self.config.set('impressao','larg_papel',larg_papel)
        self.config.set('impressao','m_esquerda',marg_esq)
        self.config.set('impressao','m_topo',marg_topo)
        self.config.set('impressao','m_direita',marg_dir)
        self.config.set('impressao','m_fundo',marg_fundo)
        
        with open('config/config.ini', 'w') as configfile:
            self.config.write(configfile)
        self.inf()
        
    def inf(self):
        versao = QtGui.QMessageBox()
        versao.information(None, "parkSYS",\
                        "<center>Informações gravadas com sucesso!!!</center>\n",\
                            QtGui.QMessageBox.Ok)
        
#FIM DA LÓGICA DO SISTEMA######################################################

    def retranslateUi(self, printer_settings):
        printer_settings.setWindowTitle(QtGui.QApplication.translate("printer_settings", "parkSYS - Configurações da Impressora", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_imp_disponiveis.setText(QtGui.QApplication.translate("printer_settings", "Impressoras disponíveis:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_larg_papel.setText(QtGui.QApplication.translate("printer_settings", "Largura do papel (mm):", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_margens.setText(QtGui.QApplication.translate("printer_settings", "Margens (mm):", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_esq.setText(QtGui.QApplication.translate("printer_settings", "Esquerda", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_topo.setText(QtGui.QApplication.translate("printer_settings", "Topo", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_dir.setText(QtGui.QApplication.translate("printer_settings", "Direita", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_fundo.setText(QtGui.QApplication.translate("printer_settings", "Fundo", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_config_impressora.setText(QtGui.QApplication.translate("printer_settings", "Configurações da Impressora", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_salvar.setText(QtGui.QApplication.translate("printer_settings", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_padrao.setText(QtGui.QApplication.translate("printer_settings", "Padrão", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_sair.setText(QtGui.QApplication.translate("printer_settings", "Sair", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    printer_settings = QtGui.QDialog()
    ui = Ui_printer_settings()
    ui.setupUi(printer_settings)
    printer_settings.show()
    sys.exit(app.exec_())

