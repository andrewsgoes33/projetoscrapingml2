import streamlit as st
import pandas as pd
import sqlite3

#Conectar ao banco de dados SQLite
conn = sqlite3.connect('../data/mercadolivre.db')

#Carregar os dados da tabela 'mercadolivre_items' em um DataFrame pandas
df = pd.read_sql_query('SELECT * FROM mercadolivre_items', conn)

#Fechar a conecão com o banco de dados
conn.close()

#Título da Aplicação
st.title('Pesquisa de Mercado - Notebooks no Mercado Livre')

#Melhorar o Layout com colunas para KPI's
st.subheader('KPIS principais do sistema')
col1, col2, col3 = st.columns(3)

#KPI 1: Número total de itens
total_itens = df.shape[0]
col1.metric(label='Número Total de Itens', value=total_itens)

#KPI 2: Número de Marcas únicas
unique_brands = df['brand'].nunique()
col2.metric(label='Número de marcas únicas', value=unique_brands)

# KPI 3: Preço médio novo (em reais)
average_new_price = df['new_price'].mean()
col3.metric(label='Preço Médio Novo (R$)', value=f'{average_new_price:.2f}')

#Quais marcas são mais encontradas até a página 10
col1, col2 = st.columns([4,2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

#Qual o preço médio por marca?
st.subheader('Preço médio por marca')
col1, col2 = st.columns([4,2])
df_non_zero_prices = df[df['new_price'] > 0]
average_price_by_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

#Qual satisfação por marca?
st.subheader('Satisfação por marca')
col1, col2 = st.columns([4,2])
df_non_zero_reviews = df[df['reviews_rating'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)