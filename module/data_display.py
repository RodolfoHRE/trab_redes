#Display dos gráficos

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('teste.csv')

def cria_grafico(str1, str2):

    print(df.head())

    plt.scatter(df[str1], df[str2])

    plt.xlabel(str1)
    plt.ylabel(str2)

    plt.title("Gráfico"+ str2 + "X tempo")

    plt.show()

    print(df.head())

cria_grafico('coluna_x','coluna_y')
