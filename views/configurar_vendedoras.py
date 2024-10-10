import streamlit as st
import pandas as pd
import datetime
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Configurar Vendedoras", page_icon="💎",layout="wide")

@st.cache_data
def load_df(worksheet):

  conn = st.connection("gsheets", type=GSheetsConnection)
  df = conn.read(worksheet=worksheet)

  return df

st.title("Configurar Vendedoras")

df = load_df("base_vendedoras")

st.dataframe(df)
