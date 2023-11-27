# BIBLIOTECAS
import random
import datetime
import math

# VARIÁVEIS
t = int(datetime.datetime.now().timestamp())

# EXECUÇÃO
with open("dadosTesteFicticio50Minutos1Segundo.csv", "w", newline="\n") as arquivo_csv:
    # Cabeçalho
    arquivo_csv.write("Timestamp;Temperatura;Umidade;Pressao;Altitude")
    # Dados
    passo = 1  # Passo de 1 segundo
    for i in range(0, 50 * 60//passo): # 50 minutos, 60 segundos por minuto
        t += passo  # Passa o tempo
        pressao = random.uniform(940, 970)  # Pressão em hPa
        # Escreve no arquivo
        arquivo_csv.write(
            f"\n{t};{'{:.3f}'.format(random.uniform(20, 30))};{'{:.3f}'.format(random.randint(40, 60))};{'{:.3f}'.format(pressao)};{'{:.3f}'.format((1 - math.pow((pressao / 1013.25), 0.190284))*44307.69396)}")