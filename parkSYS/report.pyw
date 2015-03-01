#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Author:      Elder Sanitá Trevisan
#
# Copyright(©) 2015 Elder Sanitá Trevisan
# Licence:     GPL
#-------------------------------------------------------------------------------
import sqlite3
import csv
from tabulate import tabulate
from PySide.QtWebKit import *
from PySide import QtCore, QtGui

class Ui_Relatorio(object):
    def setupUi(self, Relatorio):
        Relatorio.setObjectName("Relatorio")
        Relatorio.resize(1020, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/favicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Relatorio.setWindowIcon(icon)
        self.scrollArea = QtGui.QScrollArea(Relatorio)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 1001, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 999, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1001, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vbox = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setObjectName("vbox")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Relatorio)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(710, 10, 300, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_exportar = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_exportar.setFont(font)
        self.bt_exportar.setObjectName("bt_exportar")
        self.horizontalLayout_2.addWidget(self.bt_exportar)
        self.bt_imprimir = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_imprimir.setFont(font)
        self.bt_imprimir.setObjectName("bt_imprimir")
        self.horizontalLayout_2.addWidget(self.bt_imprimir)
        spacerItem = QtGui.QSpacerItem(55, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bt_sair = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_sair.sizePolicy().hasHeightForWidth())
        self.bt_sair.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_sair.setFont(font)
        self.bt_sair.setObjectName("bt_sair")
        self.horizontalLayout_2.addWidget(self.bt_sair)
        self.horizontalLayoutWidget = QtGui.QWidget(Relatorio)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_dt_inicio = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_dt_inicio.setFont(font)
        self.lb_dt_inicio.setObjectName("lb_dt_inicio")
        self.horizontalLayout.addWidget(self.lb_dt_inicio)
        self.dt_inicio = QtGui.QDateEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dt_inicio.setFont(font)
        self.dt_inicio.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dt_inicio.setCalendarPopup(True)
        self.dt_inicio.setObjectName("dt_inicio")
        self.horizontalLayout.addWidget(self.dt_inicio)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dt_termino = QtGui.QDateEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dt_termino.setFont(font)
        self.dt_termino.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 12, 31), QtCore.QTime(0, 0, 0)))
        self.dt_termino.setDate(QtCore.QDate(2015, 12, 31))
        self.dt_termino.setCalendarPopup(True)
        self.dt_termino.setObjectName("dt_termino")
        self.horizontalLayout.addWidget(self.dt_termino)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bt_gerar = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_gerar.setFont(font)
        self.bt_gerar.setObjectName("bt_gerar")
        self.horizontalLayout.addWidget(self.bt_gerar)

        self.retranslateUi(Relatorio)
        QtCore.QObject.connect(self.bt_sair, QtCore.SIGNAL("clicked()"), Relatorio.close)
        QtCore.QMetaObject.connectSlotsByName(Relatorio)
        
# ÍNICIO DA LÓGICA ###############################################################################
        #EVENTO PARA IMPRIMIR O RELATÓRIO
        QtCore.QObject.connect(self.bt_imprimir, QtCore.SIGNAL("clicked()"), self.impressao)
        #EVENTO PARA GERAR O RELATÓRIO E EXIBIR NA TELA
        QtCore.QObject.connect(self.bt_gerar, QtCore.SIGNAL("clicked()"), self.exibeRelatorio)
        #EVENTO PARA EXPORTAR O RELATÓRIO
        QtCore.QObject.connect(self.bt_exportar, QtCore.SIGNAL("clicked()"), self.exportar)
        
        self.html = ''
        self.view = QWebView()
        
    #MÉTODO PARA IMPRESSÃO DOS RELATÓRIOS    
    def impressao(self):
        html = self.html
        rows, tnvs, encNao, encSim = self.geraRelatorio()
        #file = open('relatorio.html','w')
        html = """
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <meta charset="UTF-8">
                    <title>Relatório parkSYS</title>
                    </head>
                    <body>
                    <table border="1" width="100%" align="center">
                    <caption><h1>Relat&oacute;rio parkSYS</h1></caption>
                    <tr align="center"><th>NV</th> <th>Marca</th> <th>Modelo</th> <th>Placa</th> <th>Hora Entrada</th> <th>Hora Sa&iacute;da</th> <th>Tempo Perman&ecirc;ncia</th> <th>Valor (R$)</th> <th>Encerrada?</th><tr>
                    """
        
        cont = 0
        for i in rows:
            cont += 1
            if cont%2 == 0:
                html += '<tr align="center"><td>%s</td> <td>%s</td>  <td>%s</td><td>%s</td> <td>%s</td>  <td>%s</td><td>%s</td> <td>%s</td>  <td>%s</td> </tr>'%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
            else:
                html += '<tr align="center" bgcolor="#D3D3D3" ><td>%s</td> <td>%s</td>  <td>%s</td><td>%s</td> <td>%s</td>  <td>%s</td><td>%s</td> <td>%s</td>  <td>%s</td> </tr>'%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
        
        html += """
                    <tr><td colspan="9"><tr>
                    <tr align="center" bgcolor="yellow"><td colspan="2">Total de NV's: %s</td> <td colspan="2">NV's Encerradas: %s</td> <td colspan="2">NV's Abertas: %s</td> <td colspan="3">Valor total das NV's Encerradas (R$): %s</td></tr>
                    </table>
                    </body>
                    </html>
                    """%(tnvs[0],tnvs[1],encNao[0],encSim[0])
                    
        
        printer = QtGui.QPrinter()
        printer.setOrientation(QtGui.QPrinter.Landscape)
        printer.setDocName("Relatório")
        printer.setResolution(300)  #dpi
        printer.setPageMargins(0, 2, 2, 1, printer.Millimeter)  #left, top, right, bottom, unit
        printer.setFullPage(True)
        sizePage = QtCore.QSizeF(210, 297)    #w,h
        printDialog = QtGui.QPrintDialog(printer, None)
        file = ""
        if printDialog.exec_() == QtGui.QDialog.Accepted:
            self.view.setHtml(html)
            self.view.print_(printer)
    
    #MÉTODO PARA EXPORTAR RELATÓRIOS    
    def exportar(self):
        rows, tnvs, encNao, encSim = self.geraRelatorio()
        header = [("NV","Marca","Modelo","Placa","Hora Entrada","Hora Saída","Tempo Permanência","Valor (R$)","Encerrada?")]
        dInicio = self.dt_inicio.date().toString('yyyy-MM-dd')
        dTermino = self.dt_termino.date().toString('yyyy-MM-dd')        
        filtros = "Arquivo CSV (*.csv);;Texto (*.txt)"
        dialog = QtGui.QFileDialog(None, 'Salvar Como', '',filtros)
        dialog.setAcceptMode(QtGui.QFileDialog.AcceptSave)
        
        if dialog.exec_():
            conn = sqlite3.connect("db/database.db")
            cursor = conn.cursor()
            cursor.execute("""SELECT id, marca, modelo, placa, time(hora_entrada), hora_saida, permanencia, valor, encerrado
                            FROM veiculos WHERE (data >='%s') AND (data <='%s') """%(dInicio, dTermino))
            rows = cursor.fetchall()
            selectedFilter = dialog.selectedFilter()
            currentDir = dialog.selectedFiles()
            
            if selectedFilter == "Arquivo CSV (*.csv)":
                footerList = (["Total de NVs: %s"%(tnvs[0])],["NV's Encerradas: %s"%(encSim[0])],["NV's Abertas: %s"%(encNao[0])],["Valor total das NV's Encerradas (R$): %s"%(tnvs[1])])
                with open(currentDir[0],'wt') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';')                    
                    for i in header:
                        writer.writerow(i)
                    for j in rows:
                        writer.writerow(j)
                    for k in footerList:
                        writer.writerow(k)
                    csvfile.close()
            else:
                f = open(currentDir[0],'wt')
                header = ["NV","Marca","Modelo","Placa","Hora Entrada","Hora Saída","Tempo Permanência","Valor (R$)","Encerrada?"]
                footer = "\n\n\nTotal de NVs: %s\nNV's Encerradas: %s\nNV's Abertas: %s\nValor total das NV's Encerradas (R$): %s"%(tnvs[0],encSim[0],encNao[0],tnvs[1])
                table = []
                for i in rows:
                    table.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]])
                file = tabulate(table, header, tablefmt="grid")
                file += footer
                f.write(file)
                f.close()
            conn.close()
            
    def exibeRelatorio(self):
        html = self.html
        rows, tnvs, encNao, encSim = self.geraRelatorio()
        #file = open('relatorio.html','w')
        html = """
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <meta charset="UTF-8">
                    <title>Relatório parkSYS</title>
                    </head>
                    <body>
                    <table border="1" width="100%" align="center">
                    <caption><h1>Relat&oacute;rio parkSYS</h1></caption>
                    <tr align="center"><th>NV</th> <th>Marca</th> <th>Modelo</th> <th>Placa</th> <th>Hora Entrada</th> <th>Hora Sa&iacute;da</th> <th>Tempo Perman&ecirc;ncia</th> <th>Valor (R$)</th> <th>Encerrada?</th><tr>
                    """
        
        cont = 0
        for i in rows:
            cont += 1
            if cont%2 == 0:
                html += '<tr align="center"><td>%s</td> <td>%s</td>  <td>%s</td><td>%s</td> <td>%s</td>  <td>%s</td><td>%s</td> <td>%s</td>  <td>%s</td> </tr>'%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
            else:
                html += '<tr align="center" bgcolor="#D3D3D3" ><td>%s</td> <td>%s</td>  <td>%s</td><td>%s</td> <td>%s</td>  <td>%s</td><td>%s</td> <td>%s</td>  <td>%s</td> </tr>'%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
        
        html += """
                    <tr><td colspan="9"><tr>
                    <tr align="center" bgcolor="yellow"><td colspan="2">Total de NV's: %s</td> <td colspan="2">NV's Encerradas: %s</td> <td colspan="2">NV's Abertas: %s</td> <td colspan="3">Valor total das NV's Encerradas (R$): %s</td></tr>
                    </table>
                    </body>
                    </html>
                    """%(tnvs[0],encSim[0],encNao[0],tnvs[1])
        #file.close()
        self.view.setHtml(html)
        self.vbox.addWidget(self.view)
            
    #MÉTODO PARA GERAR RELATÓRIOS    
    def geraRelatorio(self):
        html = self.html
        dInicio = self.dt_inicio.date().toString('yyyy-MM-dd')
        dTermino = self.dt_termino.date().toString('yyyy-MM-dd')
        #self.cleanTable()
        conn = sqlite3.connect("db/database.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT id, marca, modelo, placa, time(hora_entrada), hora_saida, permanencia, valor, encerrado
        FROM veiculos WHERE (data >='%s') AND (data <='%s') """%(dInicio, dTermino))
        rows = cursor.fetchall()
        
        cursor.execute("""SELECT COUNT(id), TOTAL(valor) FROM veiculos WHERE (data >='%s') AND (data <='%s')"""%(dInicio, dTermino))
        tnvs = cursor.fetchone()
        
        cursor.execute("""SELECT COUNT(encerrado) FROM veiculos WHERE encerrado LIKE 'Não' AND (data >='%s') AND (data <='%s')"""%(dInicio, dTermino))
        encNao = cursor.fetchone()
        
        cursor.execute("""SELECT COUNT(encerrado) FROM veiculos WHERE encerrado LIKE 'Sim' AND (data >='%s') AND (data <='%s')"""%(dInicio, dTermino))
        encSim = cursor.fetchone()

        conn.close()
        return rows, tnvs, encNao, encSim
        
# FIM DA LÓGICA ###############################################################################

    def retranslateUi(self, Relatorio):
        Relatorio.setWindowTitle(QtGui.QApplication.translate("Relatorio", "parkSYS - Relatório Gerencial", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_exportar.setText(QtGui.QApplication.translate("Relatorio", "Exportar...", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_imprimir.setText(QtGui.QApplication.translate("Relatorio", "Imprimir", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_sair.setText(QtGui.QApplication.translate("Relatorio", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_dt_inicio.setText(QtGui.QApplication.translate("Relatorio", "Data Início", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Relatorio", "Data Término", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_gerar.setText(QtGui.QApplication.translate("Relatorio", "Gerar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Relatorio = QtGui.QDialog()
    ui = Ui_Relatorio()
    ui.setupUi(Relatorio)
    Relatorio.show()
    sys.exit(app.exec_())

