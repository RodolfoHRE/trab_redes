#Tratamento dos dados e tomada de decisões
from funcoes import data_sender
dados_coletados = []

def data_treatment(dados):
        salvar_para_csv(dados)
        dados_coletados = dados.split(';')

        temperatura = dados_coletados[1]
        umidade = dados_coletados[2]

        if (20 < temperatura < 30) and (50 < umidade < 70): # temperatura em faixa de 20 a 30 graus e umidade do ar em faixa de 50 a 70% → irrigação = 1
             irrigacao = "1"
        else:
             irrigacao = "0"
        if (15 < temperatura < 30) and (60 < umidade < 70): # temperatura em faixa de 15 a 30 graus e umidade do ar em faixa de 60 a 70% → semeadora = 1
             semeadura = "1"
        else:
             semeadura = "0"

        data_sender(irrigacao,semeadura)

# Função para salvar os dados em um arquivo CSV
def salvar_para_csv(dados):
    with open('dadosClimaticosGrupoZ.csv', 'a', newline='\n') as arquivo_csv:
        arquivo_csv.write(dados + '\n')
    print("Dados salvos no arquivo CSV com sucesso!")
