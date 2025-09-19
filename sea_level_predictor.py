import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # ===============================
    # 1. Ler os dados do arquivo CSV
    # ===============================
    df = pd.read_csv("epa-sea-level.csv")

    # ===============================
    # 2. Criar gráfico de dispersão
    # ===============================
    plt.figure(figsize=(10, 6))  # tamanho do gráfico
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Dados observados")

    # ===============================
    # 3. Primeira linha de melhor ajuste (1880 até último dado)
    # ===============================
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Criar eixo x de 1880 até 2050
    years_extended = pd.Series(range(1880, 2051))
    # Fórmula da reta: y = slope*x + intercept
    plt.plot(years_extended, intercept + slope*years_extended, "r", label="Tendência (1880-2050)")

    # ===============================
    # 4. Segunda linha de melhor ajuste (2000 até último dado)
    # ===============================
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )

    # Criar eixo x de 2000 até 2050
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, intercept_recent + slope_recent*years_recent, "green", label="Tendência (2000-2050)")

    # ===============================
    # 5. Personalizar gráfico
    # ===============================
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # ===============================
    # 6. Salvar e retornar gráfico
    # ===============================
    plt.savefig("sea_level_plot.png")
    return plt.gca()
