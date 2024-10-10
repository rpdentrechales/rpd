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

st.title("RPD - Configurar Vendedoras")

df = load_df("base_vendedoras")

nome_das_vendedoras = df["NOME"].unique()

vendedora_selecionada = st.selectbox("Selecione a Vendedora", nome_das_vendedoras)

id_vendedora = df.loc[df["NOME"] == vendedora_selecionada, "ID"].values[0]

st.markdown(f'[ID da Vendedora: {id_vendedora}](https://rpd-procorpo.streamlit.app/?id={id_vendedora})')
