#%%
import pandas as pd
import yfinance as yf

#%%
# Extraindo o histórico de preços e dividendos dos últimos 5 anos
bbas3 = yf.Ticker('TAEE11.SA')
historico = bbas3.history(period='5y')

#%%
historico.tail()

#%%
# Isolando a coluna de dividendos do histórico
dividendos_filtrados = historico['Dividends']

#%%
# Removendo os dias sem pagamento de dividendos (valor zero)
dividendos_filtrados = dividendos_filtrados[dividendos_filtrados > 0]

#%%
dividendos_filtrados.tail()

#%%
# Criando o DataFrame com apenas os pagamentos de dividendos dos últimos 5 anos
dados = pd.DataFrame(dividendos_filtrados).reset_index()
dados

#%%
# Somando o total distribuído em dividendos no período
soma_dividendos = dados['Dividends'].sum()
soma_dividendos

#%%
# Calculando o dividendo médio anual (total dividido por 5 anos)
pagamento_medio = soma_dividendos / 5
pagamento_medio

#%%
# Função de preço teto pelo método Décio Bazin
# Fórmula: dividendo médio anual / retorno esperado
def preco_teto(pagamento_medio, retorno_esperado):
    return pagamento_medio / retorno_esperado

#%%
# Calculando o preço teto com retorno esperado de 10% ao ano
preco_teto(pagamento_medio, 0.10)

#%%
# Preço teto calculado e preço atual da ação
preco_teto_da_acao = 35.03
preco_atual = 31.15

#%%
# Upside (negativo) ou downside (positivo) em relação ao preço teto
percentual = (preco_atual / preco_teto_da_acao - 1) * 100
print(f'{percentual:.2f}%')

#%%
if percentual > 0:
    print(f'Ação está {percentual:.2f}% ACIMA do preço teto — CARA')
else:
    print(f'Ação está {abs(percentual):.2f}% ABAIXO do preço teto — BARATA')
