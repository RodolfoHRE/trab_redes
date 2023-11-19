#Leitura dos dados do Broker MQTTS
import paho.mqtt.client as mqtt
import time

#Envio das flags de irrigação e semeadora
def data_sender(irrigacao, semeadura):
# Configuração do cliente MQTT
     client = mqtt.Client()

     def on_connect(client, userdata, flags, rc):
          print("Conectado com código de resultado: " + str(rc))
          # Subscrever a um tópico ao se conectar
          client.subscribe("GrupoZ_irrigação")
          #publicação
          client.publish(irrigacao)
          # Subscrever a um tópico ao se conectar
          client.subscribe("GrupoZ_semadura")
          #publicação
          client.publish(semeadura)

     client.on_connect = on_connect

     # Informações de conexão ao broker
     broker_address = "broker.hivemq.com"
     port = 1883
     username = "dadosClimaticosGrupoZ"
     password = ""

     # Conectar ao broker
     client.username_pw_set(username, password)
     client.connect(broker_address, port, 60)

     client.disconnect()

     # Função para salvar os dados em um arquivo CSV
def salvar_para_csv(dados):
    with open('dadosClimaticosGrupoZ.csv', 'a', newline='\n') as arquivo_csv:
        arquivo_csv.write(dados + '\n')
    print("Dados salvos no arquivo CSV com sucesso!")

dados_list = []
def data_treatment(dados):
    salvar_para_csv(dados)
    dados_list = dados.split(';')

    temperatura = dados_list[1]
    umidade = dados_list[2]

    if (20 < temperatura < 30) and (50 < umidade < 70): # temperatura em faixa de 20 a 30 graus e umidade do ar em faixa de 50 a 70% → irrigação = 1
        irrigacao = "1"
    else:
        irrigacao = "0"
    if (15 < temperatura < 30) and (60 < umidade < 70): # temperatura em faixa de 15 a 30 graus e umidade do ar em faixa de 60 a 70% → semeadora = 1
        semeadura = "1"
    else:
        semeadura = "0"

    data_sender(irrigacao, semeadura)

    
def data_reader():
    while input() != 'q':
        # Lista para armazenar os dados recebidos
        dados_coletados = ""

        # Função chamada quando a conexão com o broker é estabelecida
        def on_connect(client, userdata, flags, rc):
            print("Conectado com código de resultado: " + str(rc))
            # Subscrever a um tópico ao se conectar
            client.subscribe("GrupoZ_time_temp_umi_press_alt")

        # Função chamada quando uma nova mensagem é recebida do broker
        def on_message(client, userdata, msg):
            print("Mensagem recebida no tópico {}: {}".format(msg.topic, msg.payload.decode()))

            # Adicionar os dados à lista
            dados_coletados = msg.payload.decode()
            data_treatment(dados_coletados)

        # Configuração do cliente MQTT
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        # Informações de conexão ao broker
        broker_address = "broker.hivemq.com"
        port = 1883
        username = "dadosClimaticosGrupoZ"
        password = ""

        # Conectar ao broker
        client.username_pw_set(username, password)
        client.connect(broker_address, port, 60)


        # Manter o loop de execução para continuar recebendo mensagens
        client.loop_forever()
        time.sleep(1)

        #Encerra a conexão com o broker
    client.disconnect()

