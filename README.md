# **Redes de Computadores 1 – Projeto Prático Interdisciplinar**

## Engenharia da Computação – Instituto Federal de Educação, Ciência e Tecnologia de São Paulo, Campus Piracicaba

### Alunos

- [Alexandre Medici Ceregato](mailto:)
- [André Lisboa Augusto](mailto:andre.lisboa@aluno.ifsp.edu.br)
- [Marcos Henrique Maimoni Campanella](mailto:marcos.campanella@aluno.ifsp.edu.br)
- [Rodolfo Henrique Raymundo Engelmann](mailto:rodolfo.engelmann@aluno.ifsp.edu.br)
- [Victor Probio Lopes](mailto:victor.probio@aluno.ifsp.edu.br)

## Introdução

Projeto desenvolvido em conjunto com a matéria de Microcontroladores, ministrada pelo Prof. Pablo Rodrigo de Souza.
O tema deste projeto interdisciplinar foca na coleta e análise de dados climáticos em tempo real, elaborando uma aplicação IoT na qual os aspectos de hardware e software serão desenvolvidos, respectivamente, nas disciplinas de Microcontroladores e Redes de Computadores 1.
</br>
Os dados do tema são coletados no ambiente de cultivo da agricultura de precisão, afim de serem processados adequadamente em prol da tomada de ações que visem melhorar a eficiência geral do plantio.
</br>
Em maiores detalhes, o objetivo do programa desenvolvido é coletar os dados referentes à temperatura, umidade e pressão de um certo local onde se encontra uma placa microcontroladora ESP32 (cujo trabalho é ler os dados e enviá-los para um _broker_ MQTT). Com base nos dados coletados, o programa decide se uma semeadora e/ou uma irrigadora devem ser acionados no local de medição, e envia essas respostas para o _broker_, que são então lidas pelo ESP32, que por sua vez efetua as ações necessárias.
</br>
Além disso, o programa também salva as variáveis climaticas lidas do ESP32 em um arquivo CSV (um segundo por linha). Esse arquivo pode então ser carregado no software novamente para gerar gráficos referentes às medições em um determinado período.

## Materiais e métodos

O presente trabalho foi desenvolvido usando a linguagem de programação Python, funcionando em um _notebook_ Jupyter, programado especificamente para funcionar no serviço de hospedagem de _notebooks_ Google Colaboratory - já que utiliza-se de algumas de suas funcionalidades específicas (como menus e a integração com o Google Drive para hospedagem de arquivos).
</br>
Para o correto funcionamento do software, foi empregado o uso das bibliotecas `paho-mqtt`, `time`, `datetime`, `pandas`, `matplotlib`, `shutil`, `google` e `os`.

## Instruções de uso

Para executar o programa, é necessário executar suas células (partes individuais de código em um _notebook_ Jupyter). Cada Célula possui instruções específicas que podem ser lidas em uma célula textual acima do código. Para executar uma célula, basta mover o _mouse_ para cima desta e clicar sobre o botão de execução, em seu canto superior esquerdo.
