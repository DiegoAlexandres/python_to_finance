#%%
import pandas as pd
import yfinance as yf

#%%
def analisar_acao(ticker: str, retornos: list = [0.06, 0.08, 0.10]):
    acao = yf.Ticker(ticker)
    
    # Dividendos dos últimos 5 anos
    historico = acao.history(period='5y')
    dividendos = historico['Dividends']
    dividendos = dividendos[dividendos > 0]
    media_anual = dividendos.sum() / 5
    
    # Preço atual
    preco_atual = acao.fast_info["last_price"]
    
    print(f"\n📊 Análise: {ticker}")
    print(f"Dividendo médio anual (5 anos): R$ {media_anual:.2f}")
    print(f"Preço atual: R$ {preco_atual:.2f}\n")
    
    for r in retornos:
        teto = media_anual / r
        status = "🟢 BARATO" if preco_atual < teto else "🔴 CARO"
        print(f"Preço teto ({int(r*100)}%): R$ {teto:.2f} → {status}")

analisar_acao("TAEE11.SA")