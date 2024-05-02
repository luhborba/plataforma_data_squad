import base64

import streamlit as st

from paginas.cursos import cursos
from paginas.home import pagina_inicial


def main():
    logo = "assets/logo.jpeg"
    st.set_page_config(
        page_title="Plataforma - DataSquad",
        page_icon=logo,
        layout="wide",
    )

    st.image(logo)
    st.title("Plataforma - DataSquad")
    st.divider()
    st.sidebar.header("DataSquad")
    st.sidebar.subheader("Páginas")
    pagina = st.sidebar.selectbox(
        "Selecione uma página",
        [
            "Página Inicial",
            "Cursos",
            "Roadmap de Estudos",
            "Repositórios",
            "Projetos",
            "Contato",
        ],
    )

    if pagina == "Página Inicial":
        pagina_inicial()
    elif pagina == "Cursos":
        cursos()
    elif pagina == "Roadmap de Estudos":
        st.write("Em desenvolvimento...")
    elif pagina == "Repositórios":
        st.write("Em desenvolvimento...")
    elif pagina == "Projetos":
        st.write("Em desenvolvimento...")
    elif pagina == "Contato":
        st.write("Em desenvolvimento...")


if __name__ == "__main__":
    main()
