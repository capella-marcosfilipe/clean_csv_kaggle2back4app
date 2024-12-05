"""
Script para limpar e preparar um CSV baixado do Kaggle para importação no Back4App

Funcionalidades:
- Remove espaços em branco ao redor dos nomes das colunas;
- Remove aspas duplas dos dados;
- Seleciona apenas colunas relevantes para análise;
- Converte colunas específicas para tipos numéricos;
- Remove linhas com valores ausentes (nan);
- Salva o CSV limpo em um novo arquivo.

Dependências:
- pandas

author: github.com/capella-marcosfilipe
"""

import pandas as pd

def clean_csv(file_path, output_path):
    """Limpa e processa um arquivo CSV

    Args:
        file_path (str): caminho do csv original
        output_path (csv): caminho onde será salvo o csv limpo
    """
    
    # Leitura do arquivo csv
    df = pd.read_csv(
        file_path, 
        encoding='utf-8', 
        quotechar='"', 
        on_bad_lines='skip' # Ignora linhas problemáticas
    )
    
    # Removendo espaços em branco dos nomes das colunas
    df.columns = df.columns.str.strip()
    # Removendo aspas duplas
    df.replace({'"': ''}, regex=True, inplace=True)
    
    # Selecionando colunas de interesse da base de dados
    columns_to_keep = [
        'track_name', 'artist_name', 'released_year', 'streams', 'bpm', 
        'danceability', 'energy', 'acousticness'
    ]
    # Verificando que estão contidas na base
    if set(columns_to_keep).issubset(df.columns):
        df = df[columns_to_keep]
    else:
        print("Erro: nem todas as colunas a serem mantidas estão na base.")

    # Convertendo colunas para tipos numéricos
    if 'streams' in df.columns:
        df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
    if 'released_year' in df.columns:
        df['released_year'] = pd.to_numeric(df['released_year'], errors='coerce')
        
    # Removendo linhas com valores ausentes (nan)
    df.dropna(inplace=True)
    
    # Salvando o arquivo CSV limpo
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"CSV limpo salvo em: {output_path}")

input_file = 'C:\\Users\\marco\\Downloads\\archive (2)\\Spotify Most Streamed Songs.csv'
output_file = 'C:\\Users\\marco\\Downloads\\archive (2)\\Cleaned_Spotify Most Streamed Songs.csv'

clean_csv(input_file, output_file)
