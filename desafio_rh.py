import pandas as pd

data = {
    'Nome': [
        'Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo',
        'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana',
        'Kleber', 'Larissa', 'Marcos', 'Natália', 'Otávio',
        'Patrícia', 'Rafael', 'Sabrina', 'Tiago', 'Vanessa',
        'William', 'Yasmin', 'André', 'Bianca', 'Caio',
        'Débora', 'Felipe', 'Giovana', 'Henrique', 'Isabela'
    ],
    'Salario': [
        3500, 8000, 4500, 10000, 7000,
        5200, 6800, 3900, 7200, 6100,
        4800, 5500, 8200, 4300, 9100,
        4700, 7600, 5400, 6200, 5800,
        11000, 4600, 7300, 5100, 8900,
        4200, 6700, 4900, 9500, 6000
    ],
    'Idade': [
        22, 35, 28, 41, 31,
        26, 33, 24, 37, 29,
        45, 27, 39, 23, 42,
        30, 34, 25, 38, 32,
        47, 21, 36, 28, 40,
        24, 35, 26, 43, 31
    ]
}

df = pd.DataFrame(data)

# Mostrar funcionarios que recebem mais de 5000
print("Pessoas com salário maior que R$5000:")
print(df[df['Salario']>5000])

# Criar coluna Bônus com 10% salário
df['Bonus'] = df['Salario'] * 0.1
print("\n DataFrame com a nova coluna de Bônus:")
print(df)

# Salário médio da empresa
mediaSalario = df['Salario'].mean()
print("\nMédia do salário da empresa:")
print(mediaSalario)

# 3 maiores salários
print(df.nlargest(3, 'Salario'))

# Salvar o df em um arquivo CSV
df.to_csv('bonus_funcionarios.csv', index=False) # Vai na pasta dos códigos, abre no terminal, e executa o programa 
# lá para gravar através do comando: python usando_pandas.py