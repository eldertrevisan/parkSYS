#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Author:      Elder Sanitá Trevisan
#
# Copyright(©) 2015 Elder Sanitá Trevisan
# Licence:     GPL
#-------------------------------------------------------------------------------
import configparser
config = configparser.SafeConfigParser()
config.read('config/config.ini')

rs = config.get('empresa','razao_social')
nf = config.get('empresa','nome_fantasia')
cnpj = config.get('empresa','cnpj')
ie = config.get('empresa','ie')
end = config.get('empresa','endereco')
end += ', '
end += config.get('empresa','num')
end += ' '
end += config.get('empresa','bairro')
end += ' '
end += config.get('empresa','cidade')
end += ' '
end += config.get('empresa','uf')
end += ' \nCEP: '
end += config.get('empresa','cep')
  
def ticket(nv,marca,modelo,placa,dEntrada,hEntrada):
    doc = """
    %s\n
    %s\n
    CNPJ: %s - I.E.: %s\n
    %s\n\n
    NV: %i\n\n
    Dados do veiculo:\n
    Marca: %s\n
    Modelo: %s\n
    Placa: %s\n\n
    Entrada:\n
    %s %s\n\n
    -*-Sem valor fiscal-*-
    """%(rs,nf,cnpj,ie,end,nv,marca,modelo,placa,dEntrada,hEntrada)
    return doc
