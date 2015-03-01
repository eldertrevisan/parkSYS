#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Author:      Elder Sanitá Trevisan
#
# Copyright(©) 2015 Elder Sanitá Trevisan
# Licence:     GPL
#-------------------------------------------------------------------------------
import locale
locale.setlocale(locale.LC_ALL, 'portuguese_brazil')
import datetime
import banco
import configparser
from PySide import QtCore, QtGui

class Ui_cobranca_mensalistas(object):
    def setupUi(self, cobranca_mensalistas):
        cobranca_mensalistas.setObjectName("cobranca_mensalistas")
        cobranca_mensalistas.resize(848, 422)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/favicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cobranca_mensalistas.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtGui.QWidget(cobranca_mensalistas)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 321, 24))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_buscar = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_buscar.sizePolicy().hasHeightForWidth())
        self.lb_buscar.setSizePolicy(sizePolicy)
        self.lb_buscar.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.lb_buscar.setFont(font)
        self.lb_buscar.setObjectName("lb_buscar")
        self.horizontalLayout.addWidget(self.lb_buscar)
        self.cb_buscar_cliente = QtGui.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_buscar_cliente.sizePolicy().hasHeightForWidth())
        self.cb_buscar_cliente.setSizePolicy(sizePolicy)
        self.cb_buscar_cliente.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_buscar_cliente.setFont(font)
        self.cb_buscar_cliente.setEditable(True)
        self.cb_buscar_cliente.setObjectName("cb_buscar_cliente")
        self.horizontalLayout.addWidget(self.cb_buscar_cliente)
        self.verticalLayoutWidget = QtGui.QWidget(cobranca_mensalistas)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 431, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabela_veiculos = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.tabela_veiculos.setObjectName("tabela_veiculos")
        self.tabela_veiculos.setColumnCount(4)
        self.tabela_veiculos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabela_veiculos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_veiculos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_veiculos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_veiculos.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tabela_veiculos)
        self.verticalLayoutWidget_2 = QtGui.QWidget(cobranca_mensalistas)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(510, 100, 331, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabela_pagamento = QtGui.QTableWidget(self.verticalLayoutWidget_2)
        self.tabela_pagamento.setObjectName("tabela_pagamento")
        self.tabela_pagamento.setColumnCount(3)
        self.tabela_pagamento.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabela_pagamento.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_pagamento.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_pagamento.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tabela_pagamento)
        self.lb_relacao_veic = QtGui.QLabel(cobranca_mensalistas)
        self.lb_relacao_veic.setGeometry(QtCore.QRect(10, 70, 250, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_relacao_veic.sizePolicy().hasHeightForWidth())
        self.lb_relacao_veic.setSizePolicy(sizePolicy)
        self.lb_relacao_veic.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.lb_relacao_veic.setFont(font)
        self.lb_relacao_veic.setObjectName("lb_relacao_veic")
        self.lb_pag = QtGui.QLabel(cobranca_mensalistas)
        self.lb_pag.setGeometry(QtCore.QRect(510, 60, 241, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_pag.sizePolicy().hasHeightForWidth())
        self.lb_pag.setSizePolicy(sizePolicy)
        self.lb_pag.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.lb_pag.setFont(font)
        self.lb_pag.setObjectName("lb_pag")
        self.horizontalLayoutWidget_3 = QtGui.QWidget(cobranca_mensalistas)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(640, 384, 204, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_salvar = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.bt_salvar.setFont(font)
        self.bt_salvar.setObjectName("bt_salvar")
        self.horizontalLayout_3.addWidget(self.bt_salvar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.bt_sair = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.bt_sair.setFont(font)
        self.bt_sair.setObjectName("bt_sair")
        self.horizontalLayout_3.addWidget(self.bt_sair)
        self.gridLayoutWidget = QtGui.QWidget(cobranca_mensalistas)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 350, 431, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_mes_vig = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.lb_mes_vig.setFont(font)
        self.lb_mes_vig.setObjectName("lb_mes_vig")
        self.gridLayout.addWidget(self.lb_mes_vig, 0, 0, 1, 1)
        self.mes_vigente = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.mes_vigente.setFont(font)
        self.mes_vigente.setText("")
        self.mes_vigente.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_vigente.setObjectName("mes_vigente")
        self.gridLayout.addWidget(self.mes_vigente, 0, 1, 1, 1)
        self.qtd_veiculos = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.qtd_veiculos.setFont(font)
        self.qtd_veiculos.setText("")
        self.qtd_veiculos.setAlignment(QtCore.Qt.AlignCenter)
        self.qtd_veiculos.setObjectName("qtd_veiculos")
        self.gridLayout.addWidget(self.qtd_veiculos, 0, 3, 1, 1)
        self.lb_qtd_veic = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_qtd_veic.setFont(font)
        self.lb_qtd_veic.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_qtd_veic.setObjectName("lb_qtd_veic")
        self.gridLayout.addWidget(self.lb_qtd_veic, 0, 2, 1, 1)
        self.lb_valor_pagar = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_valor_pagar.setFont(font)
        self.lb_valor_pagar.setObjectName("lb_valor_pagar")
        self.gridLayout.addWidget(self.lb_valor_pagar, 1, 0, 1, 1)
        self.valor_pagar = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.valor_pagar.setFont(font)
        self.valor_pagar.setText("")
        self.valor_pagar.setAlignment(QtCore.Qt.AlignCenter)
        self.valor_pagar.setObjectName("valor_pagar")
        self.gridLayout.addWidget(self.valor_pagar, 1, 1, 1, 1)
        self.bt_confirmar = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.bt_confirmar.setFont(font)
        self.bt_confirmar.setObjectName("bt_confirmar")
        self.gridLayout.addWidget(self.bt_confirmar, 1, 3, 1, 1)

        self.retranslateUi(cobranca_mensalistas)
        QtCore.QObject.connect(self.bt_sair, QtCore.SIGNAL("clicked()"), cobranca_mensalistas.close)
        QtCore.QMetaObject.connectSlotsByName(cobranca_mensalistas)
        cobranca_mensalistas.setTabOrder(self.cb_buscar_cliente, self.bt_confirmar)
        cobranca_mensalistas.setTabOrder(self.bt_confirmar, self.bt_salvar)
        cobranca_mensalistas.setTabOrder(self.bt_salvar, self.bt_sair)
        cobranca_mensalistas.setTabOrder(self.bt_sair, self.tabela_veiculos)
        cobranca_mensalistas.setTabOrder(self.tabela_veiculos, self.tabela_pagamento)

#INÍCIO DA LÓGICA DO SISTEMA###################################################
        #
        #EVENTO PARA SALVA AS INFORMAÇÕES DE PAGAMENTO NO BANCO DE DADOS
        QtCore.QObject.connect(self.bt_salvar, QtCore.SIGNAL("clicked()"), self.salva_pagamento)
        #EVENTO PARA CONFIRMAR O PAGAMENTO DO MÊS VIGENTE E EXIBIR NA TABELA CORRESPONDENTE NA TELA
        QtCore.QObject.connect(self.bt_confirmar, QtCore.SIGNAL("clicked()"), self.confirma_pagamento)
        #EVENTO PARA ENVIAR O TEXTO SELECIONADO DO COMBOBOX DE CLIENTE PARA O MÉTODO INDICADO
        QtCore.QObject.connect(self.cb_buscar_cliente, QtCore.SIGNAL("currentIndexChanged(QString)"), self.exibe_clientes)
        #
        
        #EXIBE O MÊS VIGENTE NA TELA
        self.mes_vig = datetime.date.today()
        self.mes_vig = self.mes_vig.strftime("%B")
        self.mes_vig = str(self.mes_vig).capitalize()
        self.mes_vigente.setText(self.mes_vig)
        #
        
        self.cod_cliente = 0    #SERÁ USADA PARA BUSCAR CLIENTE NO BD PELO CÓDIGO
        self.bt_confirmar.setEnabled(False)     #DESABILITA O BOTÃO 'CONFIRMAR'
        self.bt_salvar.setEnabled(False)        #DESABILITA O BOTÃO 'SALVAR'
        self.cliente_cod = {}       #SERÁ USADO PARA ARMAZENAR O NOME E CÓDIGO DO CLIENTE
        self.carrega_clientes_banco()       #CHAMA A FUNÇÃO INDICADA
        
    #MÉTODO PARA CARREGAR OS CLIENTES DO BANCO E EXIBIR NO COMBOBOX
    def carrega_clientes_banco(self):
        self.cliente_cod = {}
        clientes = banco.carrega_clientes()
        k = 0
        self.cb_buscar_cliente.addItem("")
        for i in clientes:
            self.cliente_cod[i[0]] = i[1]
            k += 1
            self.cb_buscar_cliente.addItem("")
            self.cb_buscar_cliente.setItemText(k, QtGui.QApplication.translate("CadMensalistas", i[0], None, QtGui.QApplication.UnicodeUTF8))
    
    #MÉTODO PARA EXIBIR OS DADOS DO CLIENTE NA TABELA CORRESPONDENTE NA TELA
    def exibe_clientes(self, arg):
        self.config = configparser.SafeConfigParser()
        self.config.read('config/config.ini')
        self.limpa_campos_veic()
        carros = 0
        motos = 0
        outros = 0
        valor_c = int(self.config.get('sistema','valor_mensal_c'))
        valor_m = int(self.config.get('sistema','valor_mensal_m'))
        valor_o = int(self.config.get('sistema','valor_mensal_o'))
        for cliente,codigo in self.cliente_cod.items():
            if cliente == arg:
                veiculos, pagamentos = banco.carrega_veic_pag(codigo)
                self.cod_cliente = codigo
                j = 0
                qtdRows = self.tabela_veiculos.rowCount()
                for k in veiculos:
                    self.tabela_veiculos.insertRow(self.tabela_veiculos.rowCount())
                    for items in k:
                        item = QtGui.QTableWidgetItem()
                        item.setText(str(items))
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.tabela_veiculos.setItem(qtdRows,j,item)
                        j += 1
                self.qtd_veiculos.setText(str(len(veiculos)))
                for i in veiculos:
                    if i[0] == "Carro":
                        carros += 1
                    elif i[0] == "Moto":
                        motos += 1
                    elif i[0] == "Outros":
                        outros += 1
                    else:
                        pass
                self.bt_confirmar.setEnabled(True)
                
                j = 0
                qtdRows = self.tabela_pagamento.rowCount()
                for k in pagamentos:
                    self.tabela_pagamento.insertRow(self.tabela_pagamento.rowCount())
                    for items in k:
                        item = QtGui.QTableWidgetItem()
                        item.setText(str(items))
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.tabela_pagamento.setItem(qtdRows,j,item)
                        j += 1
        
        #FÓRMULA PARA CALCULAR E EXIBIR NA TELA O VALOR A SER PAGO PELA QUANTIDADE DE VEÍCULOS
        calculo = (carros*valor_c) + (motos*valor_m) + (outros*valor_o)
        calculo = str(calculo)
        self.valor_pagar.setText("R$"+calculo)
        
    #MÉTODO PARA INSERIR NA TABELA DE PAGAMENTO AS INFORMAÇÕES DE PAGAMENTO PARA O MÊS VIGENTE
    def confirma_pagamento(self):
        hoje = datetime.datetime.now()
        hoje = hoje.strftime("%c")
        itens_tabela = (self.mes_vig, hoje, self.valor_pagar.text())
        j = 0
        qtdRows = self.tabela_pagamento.rowCount()
        self.tabela_pagamento.insertRow(self.tabela_pagamento.rowCount())
        for items in itens_tabela:
            item = QtGui.QTableWidgetItem()
            item.setText(str(items))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tabela_pagamento.setItem(qtdRows,j,item)
            j += 1
        self.bt_confirmar.setEnabled(False)
        self.bt_salvar.setEnabled(True)
        
    #MÉTODO PARA SALVAR NO BD AS INFORMAÇÕES DE PAGAMENTO
    def salva_pagamento(self):
        itens_salvar = []
        row = self.tabela_pagamento.rowCount()-1
        column = self.tabela_pagamento.columnCount()
        for c in range(column):
            itens_salvar.append(self.tabela_pagamento.item(row,c).text())
                
        banco.salva_pagamento(self.cod_cliente, itens_salvar)
        self.limpa_campos_veic()
        self.cb_buscar_cliente.setCurrentIndex(0)
    
    #LIMPA OS CAMPOS DAS TABELAS
    def limpa_campos_veic(self):
        self.bt_confirmar.setEnabled(False)
        self.bt_salvar.setEnabled(False)
        self.qtd_veiculos.setText("0")
        #REMOVE TODAS AS LINHAS DA TABELA DE VEÍCULOS
        lt = self.tabela_veiculos.rowCount()
        while lt >= 0:
            self.tabela_veiculos.removeRow(lt)
            lt -= 1
            
        lt = self.tabela_pagamento.rowCount()
        while lt >= 0:
            self.tabela_pagamento.removeRow(lt)
            lt -= 1            
        
#FIM DA LÓGICA DO SISTEMA######################################################

    def retranslateUi(self, cobranca_mensalistas):
        cobranca_mensalistas.setWindowTitle(QtGui.QApplication.translate("cobranca_mensalistas", "parkSYS - Cobrança de Mensalistas", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_buscar.setText(QtGui.QApplication.translate("cobranca_mensalistas", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabela_veiculos.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("cobranca_mensalistas", "TIPO", None, QtGui.QApplication.UnicodeUTF8))
        self.tabela_veiculos.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("cobranca_mensalistas", "MARCA", None, QtGui.QApplication.UnicodeUTF8))
        self.tabela_veiculos.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("cobranca_mensalistas", "MODELO", None, QtGui.QApplication.UnicodeUTF8))
        self.tabela_veiculos.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("cobranca_mensalistas", "PLACA", None, QtGui.QApplication.UnicodeUTF8))
        self.tabela_pagamento.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("cobranca_mensalistas", "MÊS REF.", None, QtGui.QApplication.UnicodeUTF8))
        self.tabela_pagamento.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("cobranca_mensalistas", "DATA DO PAG.", None, QtGui.QApplication.UnicodeUTF8))
        self.tabela_pagamento.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("cobranca_mensalistas", "VALOR", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_relacao_veic.setText(QtGui.QApplication.translate("cobranca_mensalistas", "Relação de veículos do cliente:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_pag.setText(QtGui.QApplication.translate("cobranca_mensalistas", "<html><head/><body><p>Pagamentos efetuados:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_salvar.setText(QtGui.QApplication.translate("cobranca_mensalistas", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_sair.setText(QtGui.QApplication.translate("cobranca_mensalistas", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_mes_vig.setText(QtGui.QApplication.translate("cobranca_mensalistas", "Mês vigente:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_qtd_veic.setText(QtGui.QApplication.translate("cobranca_mensalistas", "Qtd. Veículos:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_valor_pagar.setText(QtGui.QApplication.translate("cobranca_mensalistas", "Valor total à pagar:", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_confirmar.setText(QtGui.QApplication.translate("cobranca_mensalistas", "Confirmar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    cobranca_mensalistas = QtGui.QDialog()
    ui = Ui_cobranca_mensalistas()
    ui.setupUi(cobranca_mensalistas)
    cobranca_mensalistas.show()
    sys.exit(app.exec_())

