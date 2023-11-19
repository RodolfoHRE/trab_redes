#Envio das flags de irrigação e semeadora
import paho.mqtt.client as mqtt
    

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
    