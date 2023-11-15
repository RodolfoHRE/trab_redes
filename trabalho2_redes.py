import paho.mqtt.client as mqtt
import csv

# Defina o número de dados a serem coletados
num_dados_a_coletar = 10

# Lista para armazenar os dados recebidos
dados_coletados = []

# Função chamada quando a conexão com o broker é estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado: " + str(rc))
    # Subscrever a um tópico ao se conectar
    client.subscribe("seu_topico")

# Função chamada quando uma nova mensagem é recebida do broker
def on_message(client, userdata, msg):
    print("Mensagem recebida no tópico {}: {}".format(msg.topic, msg.payload.decode()))

    # Adicionar os dados à lista
    dados_coletados.append(msg.payload.decode())

    # Se atingiu o número desejado de dados, desconectar e salvar no CSV
    if len(dados_coletados) >= num_dados_a_coletar:
        client.disconnect()
        salvar_para_csv(dados_coletados)

# Função para salvar os dados em um arquivo CSV
def salvar_para_csv(dados):
    with open('dados.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for dado in dados:
            escritor_csv.writerow([dado])
    print("Dados salvos no arquivo CSV com sucesso!")

# Configuração do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Informações de conexão ao broker
broker_address = "endereco_do_broker"
port = 1883
username = "seu_username"
password = "sua_senha"

# Conectar ao broker
client.username_pw_set(username, password)
client.connect(broker_address, port, 60)

# Manter o loop de execução para continuar recebendo mensagens
client.loop_forever()
