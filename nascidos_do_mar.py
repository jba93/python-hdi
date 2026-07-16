import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Criamos primeiro o dataframe com os dados usando o Pandas
data = {
    'Idade':[22, 25, 27, 30, 35, 40, 45, 50],
    'Salario':[2200, 2500, 2700, 3000, 3500, 4000, 4500, 5000]
}

df = pd.DataFrame(data)

# Criar gráfico de dispersão com o SeaBorn, usando o dataframe
sns.scatterplot(data=df, x='Idade', y='Salario', color='green')

# Título e rótulos
plt.title('Relação entre idade e salário')
plt.xlabel('Idade')
plt.ylabel('Salario')

# Exibe o gráfico
plt.show()