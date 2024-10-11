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

st.title("RPD - Link das vendedoras")

df = load_df("base_vendedoras")

nome_das_vendedoras = df["nome"].unique()

vendedora_selecionada = st.selectbox("Selecione a Vendedora", nome_das_vendedoras)

id_vendedora = df.loc[df["nome"] == vendedora_selecionada, "id_vendedora"].values[0]

st.markdown(f'[Abrir site da vendedora](https://rpd-procorpo.streamlit.app/?id={id_vendedora})')
