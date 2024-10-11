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

st.title("Testes - Link das vendedoras")

df = load_df("base_vendedoras")

nome_das_vendedoras = df["nome_crm"].unique()

vendedora_selecionada = st.selectbox("Selecione uma Vendedora", nome_das_vendedoras)

id_vendedora = df.loc[df["nome_crm"] == vendedora_selecionada, "id_vendedora"].values[0]

st.markdown(f'[Abrir site da vendedora](https://rpd-procorpo.streamlit.app/inserir_vendas?id={id_vendedora})')
