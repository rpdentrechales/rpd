import streamlit as st
import pandas as pd
import datetime
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="RPD - Configurar Vendedoras", page_icon="💎",layout="wide")

carregar_pag_vendedora = False

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
  dados_vendedora = df.loc[df["id_vendedora"] == id_vendedora]
  ids_encontrados = len(dados_vendedora)
 
  if 'dados_vendedora' not in st.session_state and ids_encontrados == 1:
      st.session_state['dados_vendedora'] = dados_vendedora

elif 'dados_vendedora' in st.session_state:
  dados_vendedora = st.session_state['dados_vendedora']
  carregar_pag_vendedora = True

if carregar_pag_vendedora:

  nome_vendedora = dados_vendedora["nome"].values[0]
  email_vendedora = dados_vendedora["email"].values[0]
  loja_vendedora = dados_vendedora["loja"].values[0]

  st.header(f"Olá, {nome_vendedora}")
  st.write(f"Sua loja é a {loja_vendedora}")
  st.write(f"Seu email é {email_vendedora}")

else:
  st.write("Essa página não existe")
