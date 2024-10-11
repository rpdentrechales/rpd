import streamlit as st

# --- PAGE SETUP ---
vendedoras_page = st.Page(
    "views/inserir_vendas.py",
    title="Área da Vendedora",
    icon=":material/universal_currency:",
    default=True,
)

# teste_vendedoras_page = st.Page(
#     "views/teste_vendedoras.py",
#     title="Teste Vendedora",
#     icon=":material/manufacturing:"
# )

teste_url_vendedoras_page = st.Page(
    "views/configurar_vendedoras.py",
    title="Configurar Vendedoras",
    icon=":material/manufacturing:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Vendedoras":[vendedoras_page],
        "Testes": [teste_url_vendedoras_page]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
