"""
Funções de carga e descrição dos dados
"""

import requests
import pandas as pd
import os

def download_data():
    if(os.path.exists("data/01_raw/dataset_kobe_dev.parquet")):
        print("Usando dados já salvos...")
        df_dev = pd.read_parquet("data/01_raw/dataset_kobe_dev.parquet")
        df_prod = pd.read_parquet("data/01_raw/dataset_kobe_prod.parquet")
    else:
        print("Baixando dados do repositório...")
        resp_dev = requests.get("https://github.com/tciodaro/eng_ml/raw/refs/heads/main/data/dataset_kobe_dev.parquet")
        with open("file_dev.parquet", "wb") as file_dev:
            file_dev.write(resp_dev.content)
        resp_prod = requests.get("https://github.com/tciodaro/eng_ml/raw/refs/heads/main/data/dataset_kobe_prod.parquet")
        with open("file_prod.parquet", "wb") as file_prod:
            file_prod.write(resp_prod.content)
        df_dev = pd.read_parquet("file_dev.parquet")
        df_prod = pd.read_parquet("file_prod.parquet")

    return df_dev, df_prod

def descricao_dados(base):
    # criar um dataframe de nomes das colunas
    base_var_df = pd.DataFrame(base.columns.tolist(), columns=["Nome das variáveis"])
    
    # inserir no dataframe os tipos das colunas
    base_var_df["Tipo"] = base.dtypes.tolist()
    
    # inserir no dataframe a quantidade de missing values
    base_var_df["Nr. de missing values"] = base.isnull().sum().tolist()
    
    # inserir no dataframe a quantidade de observacoes
    base_var_df["Nr. de observações"] = base.count().tolist()

    return base_var_df