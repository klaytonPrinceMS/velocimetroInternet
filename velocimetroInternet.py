#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import TesteInternet
from TesteInternet import shell
import time


def medir_velocidade():
    inicio = time.time()
    st = TesteInternet.Speedtest()
    st.download()
    st.upload()
    resultados = st.results.dict()
    fim = time.time()
    duracao = fim-inicio
    os.system('cls')
    print(f'''
====================================================================
===      DTI - Pref. Monte Santo de Minas - Teste de Internet    ===    
====================================================================

Cliente Provedor            : {resultados['client']['isp']}
Velocidade de download      : {resultados['download'] / (1024 * 1024):.2f} megabits
Velocidade de upload        : {resultados['upload'] / (1024 * 1024):.2f} megabits

Servidor de teste - Cidade  : {resultados['server']['name']}
Servidor de teste - Provedor: {resultados['server']['sponsor']}
Servidro url                : {resultados['server']['host']}
Ping                        : {resultados['ping']} ms

Tempo total do teste        : {duracao:.1f} Segundos

versão                      : 1.0.20240930
by                          : PRINCE, K.B

    ''')
    escolhendo()
def medir_velocidadeShell():
    shell()
    escolhendo()





def menu():
    print(f'''
====================================================================
===      DTI - Pref. Monte Santo de Minas - Teste de Internet    ===    
====================================================================
''')
    escolhendo()
def escolhendo():
    print(f'''

1 - Teste Rapido
2 - Teste Completo

''')
    escolha = str(input("Qual teste vamos fazer:  ")).upper()
    if escolha == "1":
        os.system('cls')
        medir_velocidadeShell()
    if escolha == "2":
        os.system('cls')
        medir_velocidade()
    else:
        os.system('exit')




if __name__ == "__main__":
    try:
        menu()
    except Exception as erro:
        print(f'Erro ao acessar servidor {erro} ')