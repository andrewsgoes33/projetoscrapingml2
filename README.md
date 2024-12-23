# projetoscrapingml2

Para rodar o web scraping

````bash
scrapy crawl mercadolivre -o ../data/data.jsonl
````

Para Rodar o PANDAS tem que fazer isso dentro da pasta SRC

````bash
python transformacao/main.py
````

Para rodar o Streamlit e visualizar o Dashboard na pasta SRC

````bash
streamlit run dashboard/app.py
````