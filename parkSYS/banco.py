#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Author:      Elder Sanitá Trevisan
#
# Copyright(©) 2015 Elder Sanitá Trevisan
# Licence:     GPL
#-------------------------------------------------------------------------------
import sqlite3
from datetime import datetime

nvG = 0
msg = ("Dados inseridos com sucesso!", "NV encerrada com sucesso!", "Esta NV já foi encerrada!")

def criaDb():
    """FUNÇÃO PARA CRIAR O BANCO DE DADOS"""
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS veiculos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 tipo INTEGER NOT NULL,
                 marca TEXT,
                 modelo TEXT,
                 placa TEXT NOT NULL,
                 data NUMERIC,
                 hora_entrada NUMERIC,
                 hora_saida NUMERIC,
                 permanencia NUMERIC,
                 valor FLOAT,
                 encerrado TEXT
                 );
                 """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS mensalistas
                (id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                nome_razao TEXT NOT NULL,
                fantasia TEXT,
                telefone1 INTEGER NOT NULL,
                telfone2 INTEGER,
                celular INTEGER,
                email1 TEXT NOT NULL,
                email2 TEXT,
                endereco TEXT NOT NULL,
                bairro TEXT NOT NULL,
                cidade TEXT MOT NULL,
                uf TEXT NOT NULL,
                rg_ie INTEGER NOT NULL,
                cpf_cnpj INTEGER NOT NULL,
                info TEXT
                );
                """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS veiculos_mensalistas
                (id_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,
                cod_cliente INTEGER NOT NULL,
                tipo TEXT NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                placa TEXT NOT NULL,
                cor TEXT,
                chassi TEXT NOT NULL,
                FOREIGN KEY(cod_cliente) REFERENCES mensalistas(id_cliente)
                );
                """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS pagamento_mensalistas
                (id_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
                cod_cliente INTEGER NOT NULL,
                mes_ref NUMERIC,
                data_pag NUMERIC NOT NULL,
                valor TEXT NOT NULL,
                FOREIGN KEY(cod_cliente) REFERENCES mensalistas(id_cliente)
                );
                """)
    conn.close()

#-------------------v-FUNÇÕES PARA VEÍCULOS AVULSOS-v-------------------------#
def insertDb(tipo, marca, modelo, placa, data, hora_entrada):
    """FUNÇÃO PARA INSERIR DADOS NO BANCO"""
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO veiculos
                        VALUES(?,?,?,?,?,?,?,?,?,?,?)""",(None, tipo, marca,\
                        modelo, placa, data, hora_entrada, 0, 0, 0, "Não"));
    nvG = cursor.lastrowid
    cursor.close()
    conn.commit()
    conn.close()
    return  msg[0], nvG

def searchDb(nv):
    """FUNÇÃO PARA FAZER BUSCA NO BANCO"""
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT tipo, marca, modelo, placa, data, hora_entrada,
    hora_saida, encerrado FROM veiculos WHERE id=?""",(nv,))
    row = cursor.fetchone()
    return row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
    conn.close()

def closesDb(nv, valor, permanencia):
    """FUNÇÃO PARA ENCERRAR A NV"""
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    mensg = ""
    cursor.execute("""SELECT encerrado FROM veiculos WHERE id=?""",(nv,))
    row = cursor.fetchone()
    if row[0] == "Não":
        cursor.execute("""UPDATE veiculos SET hora_saida=strftime('%H:%M:%S',
        'now','localtime'),encerrado=?,valor=?, permanencia=? WHERE id=?""",\
        ("Sim", valor, permanencia, nv))
        mensg = msg[1]
    elif row[0] == "Sim":
        mensg = msg[2]
    conn.commit()
    conn.close()
    return mensg

def search(nv):
    """FUNÇÃO PARA FAZER BUSCA NO BANCO PARA EXIBIR NA TELA DE RE-IMPRESSÃO"""
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT marca, modelo, placa FROM veiculos WHERE id=?""",(nv,))
    row = cursor.fetchone()
    conn.close()
    return row[0], row[1], row[2]


#------------------------v-FUNÇÕES PARA MENSALISTAS-v-------------------------#
def insere_mensalista(cliente, veiculos):
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO mensalistas
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(cliente));
    id_v = cursor.lastrowid
    for i in veiculos:
        cursor.execute("""INSERT INTO veiculos_mensalistas
                        VALUES(?,?,?,?,?,?,?,?)""",(None, id_v, i[0],i[1],i[2],\
                        i[3],i[4],i[5]));
    cursor.close()
    conn.commit()
    conn.close()
    
def carrega_clientes():
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT nome_razao, id_cliente FROM mensalistas""")
    row = cursor.fetchall()
    conn.close()
    return row
    
def carrega_clientes_completo(arg):
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM mensalistas WHERE id_cliente=?""",(arg,));
    rowC = cursor.fetchall()
    cursor.execute("""SELECT * FROM veiculos_mensalistas WHERE cod_cliente=?""",(arg,));
    rowV = cursor.fetchall()
    conn.close()
    return rowC, rowV
    
def atualiza_dados_cliente(cliente, veiculos):
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute("""UPDATE mensalistas SET tipo=?, nome_razao=?, fantasia=?,
                    telefone1=?, telfone2=?, celular=?, email1=?, email2=?,
                    endereco=?, bairro=?, cidade=?, uf=?, rg_ie=?, cpf_cnpj=?,
                    info=?
                    WHERE id_cliente=?""",(cliente[1], cliente[2], cliente[3],\
                    cliente[4], cliente[5], cliente[6], cliente[7], cliente[8],\
                    cliente[9], cliente[10], cliente[11], cliente[12], cliente[13],\
                    cliente[14], cliente[15],cliente[0]));
    
    cursor.execute("""SELECT id_veiculo FROM veiculos_mensalistas
                    WHERE cod_cliente=?""",(cliente[0],));
    l_v = cursor.fetchall()
    lis_veiculos = []
    for i in l_v:
        for j in i:
            lis_veiculos.append(j)
    
    for i in lis_veiculos:
        cursor.execute("""DELETE FROM veiculos_mensalistas WHERE id_veiculo='%i'
                        """%(i));
                 
    for i in veiculos:
        cursor.execute("""INSERT INTO veiculos_mensalistas
                        VALUES(?,?,?,?,?,?,?,?)""",(None, cliente[0],i[0],i[1],i[2],\
                        i[3],i[4],i[5]));
    
    conn.commit()
    conn.close()
    
def carrega_veic_pag(cod):
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT tipo, marca, modelo, placa 
                   FROM veiculos_mensalistas WHERE cod_cliente='%i'"""%(cod));
    veiculos = cursor.fetchall()
    cursor.execute("""SELECT mes_ref, data_pag, valor
                FROM pagamento_mensalistas WHERE cod_cliente='%i'"""%(cod));
    pagamento = cursor.fetchall()
    conn.close()
    return veiculos, pagamento
    
def salva_pagamento(cod, val):
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO pagamento_mensalistas 
                    VALUES(?,?,?,?,?)""",(None, cod, val[0],val[1],val[2]));
    conn.commit()
    conn.close()

def relatorio():
    conn = sqlite3.connect("db/database.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM mensalistas""")
    row = cursor.fetchall()
    for i in row:
        print("Mensalistas: ",i)

    cursor.execute("""SELECT * FROM veiculos_mensalistas""")
    row = cursor.fetchall()
    for j in row:
        print("Veiculos mensalistas: ",j)

    conn.close()

#relatorio()
