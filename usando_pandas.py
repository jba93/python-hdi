import pandas as pd

# Criando um dataframe com o pandas
data = {
    'Nome': ['Caio', 'Katherine', 'Lucas', 'Juliana', 'Pedro'],
    'Salario': [2000, 3000, 4000, 5000, 6000], # Pode usar com ou sem aspas
    'Idade': [15, 20, 25, 30, 35] # Pode usar com ou sem aspas
}

df = pd.DataFrame(data)

# Exibindo o dataframe
print("DataFrame criado:")
print(df)

# Exibindo colunas
print("\n Coluna Nome:")
print(df['Nome'])

# Filtrando linhas (exemplo: idade maior que 30)
print("\n Pessoas com idade maior que 30 anos:")
print(df[df['Idade']>30])

# Adicionar mais uma coluna
df['Imposto'] = df['Salario'] * 0.1
print("\n DataFrame com a nova coluna de imposto:")
print(df)

# Calculando a média do salário
mediaSalario = df['Salario'].mean()
print("\nMédia do salário:")
print(mediaSalario)

# Selecionar múltiplas colunas
print('\nSelecionando duas colunas:')
print(df[['Salario', 'Idade']])

# Informações gerais do DataFrame
print('\nDados comuns do DataFrame:')
print('\n- Info')
print(df.info())

print('\n- Describe')
print(df.describe())

print('\n- Shape')
print(df.shape)

print('\n- Columns')
print(df.columns)

# Ordenação dos dados:
print('\nDados ordenados por salário:')
print(df.sort_values('Salario', ascending=False))

# Filtrando com múltiplas condições
print('\nIdade maior que 30 anos e salário maior que 5000:')
print(df[(df['Idade']>30) & (df['Salario']>5000)])

# Contagem de valores
print('\nQuantos dados temos na tabela:')
print(df['Nome'].value_counts())

# Agrupamento [MUITO IMPORTANTE]
df['Departamento'] = ['Pricing', 'Pricing', 'Atuarial', 'Atuarial', 'Dados']
print(
    df.groupby('Departamento')['Salario'].mean()
)

# Remover colunas
print('\nRemover a coluna de imposto:')
df.drop('Imposto', axis=1, inplace=True)
print(df)

# Remover duplicadas
print("\nRemover itens duplicados:")
df.drop_duplicates(inplace=True)
print(df)

# Usar funções lambda
print('\n Usando funções:')
df['Salario Anual'] = df['Salario'].apply(
    lambda x: x * 12
)
print(df)

# Criar categorias usando lambda:
print('\n Faixa Salarial:')
df['Faixa'] = df['Salario'].apply(
    lambda x: 'Alta' if x >= 5000 else 'Baixa'
)
print(df)

# Juntar dataframes (JOIN)
departamentos = pd.DataFrame({
    'Nome':['Leonardo', 'João', 'Amanda', 'Thomas', 'Lorena', 'Caio', 'Katherine', 'Lucas', 'Juliana', 'Pedro'],
    'Estado': ['SP', 'MG', 'CE', 'RJ', 'AM', 'SP', 'MG', 'CE', 'RJ', 'AM']
})

resultado = pd.merge(df, departamentos, on='Nome')
print('\n Merge df com departamentos:')
print(resultado)

# Top N registros
print('\n Os 3 maiores salários:')
print(df.nlargest(3, 'Salario'))

# Exibir apenas 2 itens da tabela:
print('\n Apenas 2 itens iniciais da tabela:')
print(df.head(2))

# Exibir 2 últimos itens da tabela:
print('\n Apenas 2 itens finais da tabela:')
print(df.tail(2))

# Amostra aleatória
print('\n Amostra aleatória:')
print(df.sample()) # Pode colocar a qtd de itens da amostra dentro do parêntese

# Índices
print('\n Índices:')
print(df.index)

# Tipos de dados
print('\n Tipos de dados:')
print(df.dtypes)

# Quantidade de registro total
print('\n Quantidade de registros total:')
print(len(df))

# Salvar o df em um arquivo CSV
df.to_csv('meus_salarios.csv', index=False) # Vai na pasta dos códigos, abre no terminal, e executa o programa 
# lá para gravar através do comando: python usando_pandas.py