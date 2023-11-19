from funcoes import data_reader, data_display
import pandas as pd

def main():
    with open('dadosClimaticosGrupoZ.csv', 'w', newline='\n') as arquivo_csv:
        arquivo_csv.write("Timestamp, Temperatura, Umidade, Pressao, Altitude\n")
    data_reader.data_reader()

    df = pd.read_csv('dadosClimaticosGrupoZ.csv')
    print(df.head())
    data_display.cria_grafico(df,"Temperatura")
    data_display.cria_grafico(df,"Umidade")
    data_display.cria_grafico(df,"Pressao")
   
if __name__ == main:
    main()