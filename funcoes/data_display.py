#Display dos gráficos

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def cria_grafico(df, str2):
    str1 = "Timestamp"
    print(str2)
    plt.scatter(df[str1], df[str2])

    plt.xlabel(str1)
    plt.ylabel(str2)

    plt.title("Gráfico: tempo X "+ str2)

    plt.show()

