import pandas as pd
import sqlite3
from datetime import datetime

#Carregar e definir o caminho do arquivo extraído
df = pd.read_json('../data/data.jsonl', lines=True)

# Setar o pandas para mostrar todas as colunas no terminal do git bash
pd.options.display.max_columns = None

#Adicionar Colunas no Pandas
df['_source'] = "https://lista.mercadolivre.com.br/notebooks"

#Adicionar Coluna de data da coleta
df['_date_extract'] = datetime.now()

#Transformando Colunas Nulas, adicionando um texto representativo.
df['brand'] = df['brand'].fillna('Sem Marca')

#Transformando Coluna Seller, remover o "Por" e o espaço, e deixando somente o nome da Empresa e removendo os null e colocando um nome genérico
df['seller'] = df['seller'].str.replace('Por', '').str.strip()
df['seller'] = df['seller'].fillna('Vendedor Desconhecido')

#Tranformando Colunas de Valores
df["old_price"] = df["old_price"].fillna(0).astype(float)
df["new_price"] = df["new_price"].fillna(0).astype(float)
df["reviews_rating"] = df["reviews_rating"].fillna(0).astype(float)

#Removendo Parênteses do reviews_total e setando tipo
df["reviews_total"] = df["reviews_total"].str.replace(r'[\(\)]','', regex=True)
df["reviews_total"] = df["reviews_total"].fillna(0).astype(int)

#Conectando ao banco de dados SQLite(ou criar um novo)
conn = sqlite3.connect('../data/mercadolivre.db')

#Salvar Dataframe no banco de dados SQLite
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

#Fechar conexão com o banco após salvar o Dataframe
conn.close()




