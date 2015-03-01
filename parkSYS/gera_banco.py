#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Author:      Elder Sanitá Trevisan
#
# Copyright(©) 2015 Elder Sanitá Trevisan
# Licence:     GPL
#-------------------------------------------------------------------------------
import banco
import hashlib
import os.path

def aut():
    if os.path.exists("db/database.db"):
        print("Já existe um banco de dados!")
    else:
        u = str(input("Informe o login: "))
        u_hashed = "91f5167c34c400758115c2a6826ec2e3"	#administrador
        u = hashlib.md5(u.encode())
        
        if u.hexdigest() == u_hashed:
            print("Usuário correto!\n")
            p = str(input("Agora informe a senha: "))
            p_hashed = "bd977d0538409cb5e7171cbbac684362"	#parkSYS
            p = hashlib.md5(p.encode())
            if p.hexdigest() == p_hashed:
                print("Dados de login corretos!\nO processo para criar o banco "\
                    "será executado agora!")
                banco.criaDb()
                print("Banco de dados criado com sucesso!")
            else:
                print("Senha incorreta!")
        else:
            print("Usuário não cadastrado!")
    input("Pressione ENTER para finalizar")
