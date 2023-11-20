from funcoes import data_reader
import pandas as pd
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt


def main():
    with open('dadosClimaticosGrupoZ.csv', 'w', newline='\n') as arquivo_csv:
        arquivo_csv.write("Timestamp;Temperatura;Umidade;Pressao;Altitude\n")

    print("Aperte Ctrl+C para interromper a leitura do broker e plotar os gráficos!")
    try:
        data_reader.data_reader()
    except:
        print("Conexão com o broker encerrada!")

    df = pd.read_csv('dadosClimaticosGrupoZ.csv', sep=';')
    print(df.head())
    figure, axis = plt.subplots(1,3, figsize=(15,6))
    
    axis[0].plot(df["Timestamp"], df["Temperatura"])
    axis[0].set_title("Tempo X Temperatura (°C)")
    axis[1].plot(df["Timestamp"], df["Umidade"])
    axis[1].set_title("Tempo X Umidade (%)")
    axis[2].plot(df["Timestamp"], df["Pressao"])
    axis[2].set_title("Tempo X Pressao (hPa)")
  # Obtém o gerenciador de figura atual
    fig_manager = plt.get_current_fig_manager()
    fig_manager.window.wm_geometry("+0+0")
    fig_manager.resize(1800,800)
    plt.show()

if __name__ == '__main__':
    main()