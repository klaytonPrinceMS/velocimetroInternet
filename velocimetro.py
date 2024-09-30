import os
import speedtest
import time
from tqdm import tqdm

def medir_velocidade():
    st = speedtest.Speedtest()
    #time.sleep(0.5)
    inicio = time.time()
    for _ in tqdm(range(5)):
        time.sleep((0.1))
    print('Aguarde...estamos concluindo o processo')
    for _ in tqdm(range(1)):
        st.download()
        st.upload()
    resultados = st.results.dict()
    fim = time.time()
    duracao = fim-inicio
    return resultados, duracao

def menu():
    os.system('cls')
    resultados, duracao = medir_velocidade()
    print(f'''
    ==========================================================================================
    ===                  DTI - Prefeitura de Monte Santo de Minas                          ===
    ==========================================================================================

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

    escolha = str(input("Digite S para refazer o teste:  ")).upper()
    if escolha == "S":
        menu()
    else:
        os.system('exit')

if __name__ == "__main__":
    menu()