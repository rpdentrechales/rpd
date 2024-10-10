import streamlit as st

# --- PAGE SETUP ---
vendedoras_page = st.Page(
    "views/inserir_vendas.py",
    title="Configurar Vendedoras",
    icon=":material/thumb_up:",
    default=True,
)

configurar_vendedoras_page = st.Page(
    "views/configurar_vendedoras.py",
    title="Configurar Vendedoras",
    icon=":material/thumb_up:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    { 
        "Vendedoras":[vendedoras_page],
        "Configurar": [configurar_vendedoras_page]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
