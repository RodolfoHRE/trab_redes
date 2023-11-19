#Leitura dos dados do Broker MQTTS
import paho.mqtt.client as mqtt
import csv

import time


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

