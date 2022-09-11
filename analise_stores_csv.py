# Importa as bibliotecas pandas e numpy como pd e np

import pandas as pd
import numpy as np

# Usa o pandas para permitir a leitura do arquivo "Stores.csv"
tabela = pd.read_csv('Stores.csv')

# Usa a função "max" para calcular o valor máximo em cada coluna
max_produtos = (tabela['Produtos'].max())
max_clientes = (tabela['Clientes'].max())
max_vendas = (tabela['Vendas'].max())

# Usa a função "min" para calcular o valor mínimo em cada coluna
min_produtos = (tabela['Produtos'].min())
min_clientes = (tabela['Clientes'].min())
min_vendas = (tabela['Vendas'].min())

# Calcula o valor médio de cada coluna, somando todos os valores de cada coluna e dividindo pela quantidade de valores
med_produtos = (tabela['Produtos'].sum() / len(tabela['Produtos']))
med_clientes = (tabela['Clientes'].sum() / len(tabela['Clientes']))
med_vendas = (tabela['Vendas'].sum() / len(tabela['Vendas']))

# Usa o np.std para calcular o desvio padrão de cada coluna
desvio_produtos = (np.std(tabela['Produtos']))
desvio_clientes = (np.std(tabela['Clientes']))
desvio_vendas = (np.std(tabela['Vendas']))

# Mostra na tela os valores máximos, mínimos, médios de cada tabela, assim como o seu desvio padrão

print(f'Os valores máximos das colunas "Produtos", "Clientes" e "Vendas" são respectivamente {max_produtos}, {max_clientes} e {max_vendas}')

print(f'Os valores mínimos das colunas "Produtos", "Clientes" e "Vendas" são respectivamente {min_produtos}, {min_clientes} e {min_vendas}')

print(f'Os valores médios das colunas "Produtos", "Clientes" e "Vendas" são respectivamente {med_produtos}, {med_clientes} e {med_vendas}')

print(f'Os desvios padrão das colunas "Produtos", "Clientes" e "Vendas" são respectivamente {desvio_produtos}, {desvio_clientes} e {desvio_vendas}')