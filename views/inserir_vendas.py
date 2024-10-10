import streamlit as st
import pandas as pd
import datetime
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="RPD - Configurar Vendedoras", page_icon="💎",layout="wide")

@st.cache_data
def load_df(worksheet):

  conn = st.connection("gsheets", type=GSheetsConnection)
  df = conn.read(worksheet=worksheet)

  return df

url_parameters = st.query_params

st.title("RPD - Área das vendedoras")

if "id" in url_parameters:
  id_vendedora = st.query_params["id"]
  df = load_df("base_vendedoras")
  dados_vendedora = df.loc[df["ID"] == id_vendedora]

  nome_vendedora = dados_vendedora["NOME"].values[0]
  email_vendedora = dados_vendedora["EMAIL"].values[0]
  loja_vendedora = dados_vendedora["LOJA"].values[0]



  st.header(f"Olá, {nome_vendedora}")
  st.write(f"Sua loja é a {loja_vendedora}")
  st.write(f"Seu email é {email_vendedora}")
else:
  st.header("Você não está logado")
