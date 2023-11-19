import paho.mqtt.client as mqtt
import time

def data_sender(irrigacao, semeadura):
    client = mqtt.Client()

    def on_connect(client, userdata, flags, rc):
        print("Conectado com código de resultado: " + str(rc))
        client.subscribe("GrupoZ_irrigacao")
        client.publish("GrupoZ_irrigacao", irrigacao)
        client.subscribe("GrupoZ_semeadura")
        client.publish("GrupoZ_semeadura", semeadura)

    client.on_connect = on_connect

    broker_address = "broker.hivemq.com"
    port = 1883
    username = "dadosClimaticosGrupoZ"
    password = ""
    
    client.username_pw_set(username, password)
    client.connect(broker_address, port, 60)

    client.disconnect()

def salvar_para_csv(dados):
    with open('dadosClimaticosGrupoZ.csv', 'a', newline='\n') as arquivo_csv:
        arquivo_csv.write(dados + '\n')
    print("Dados salvos no arquivo CSV com sucesso!")

def data_treatment(dados):
    salvar_para_csv(dados)
    dados_list = dados.split(';')

    temperatura = float(dados_list[1])
    umidade = float(dados_list[2])

    irrigacao = "1" if (20 < temperatura < 30) and (50 < umidade < 70) else "0"
    semeadura = "1" if (15 < temperatura < 30) and (60 < umidade < 70) else "0"

    data_sender(irrigacao, semeadura)

def data_reader():
    client = mqtt.Client()
    
    broker_address = "broker.hivemq.com"
    port = 1883
    username = "dadosClimaticosGrupoZ"
    password = ""

    def on_connect(client, userdata, flags, rc):
        print("Conectado com código de resultado: " + str(rc))
        client.subscribe("GrupoZ_time_temp_umi_press_alt")

    def on_message(client, userdata, msg):
        print("Mensagem recebida no tópico {}: {}".format(msg.topic, msg.payload.decode()))
        data_treatment(msg.payload.decode())

    client.on_connect = on_connect
    client.on_message = on_message

    client.username_pw_set(username, password)
    client.connect(broker_address, port, 60)

    try:
        client.loop_forever()
    except:
        client.disconnect()


