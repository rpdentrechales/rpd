import streamlit as st

# --- PAGE SETUP ---
configurar_vendedoras_page = st.Page(
    "views/configurar_vendedoras.py",
    title="Configurar Vendedoras",
    icon=":material/thumb_up:",
    default=True,
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Pages": [configurar_vendedoras_page]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
