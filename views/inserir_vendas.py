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

if "id" in url_parameters:

  id_vendedora = st.query_params["id"]
  df = load_df("base_vendedoras")
  dados_vendedora = df.loc[df["id_vendedora"] == id_vendedora]
  ids_encontrados = len(dados_vendedora)
 
  if 'dados_vendedora' not in st.session_state and ids_encontrados == 1:
      st.session_state['dados_vendedora'] = dados_vendedora

if 'dados_vendedora' in st.session_state:
  dados_vendedora = st.session_state['dados_vendedora']
  carregar_pag_vendedora = True

if carregar_pag_vendedora:

  nome_vendedora = dados_vendedora["nome"].values[0]
  email_vendedora = dados_vendedora["email"].values[0]
  loja_vendedora = dados_vendedora["loja"].values[0]
  id_vendedora = dados_vendedora["id_vendedora"].values[0]

  st.markdown("# RPD - Área das vendedoras")
  st.write(f"Olá, {nome_vendedora}. Tenha um bom dia!")

  coluna_1, coluna_2 = st.columns(2)

  with coluna_1:

    with st.form("inserir_vendas",enter_to_submit=False):

      st.write("Inserir Vendas")
      id_cliente = st.number_input("Id do Cliente", value=None, placeholder="Insira o Id do Cliente")

      submitted = st.form_submit_button("Inserir Venda")
    if submitted:
      st.write("Id cliente", id_cliente)
      st.baloons()
  
else:
  st.markdown("# Essa página não existe")
