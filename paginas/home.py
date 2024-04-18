import streamlit as st


def pagina_inicial():
    st.write("## Bem vindo a nossa plataforma!")
    with st.expander("**Sobre a Plataforma**"):
        st.markdown(
            """
            **Somos a DataSquad**,
            Somos uma empresa da área de Análise de Dados e Business Intelligence, mercado que vem em um crescimento constante no setor de tecnologia. Nosso pelotão de consultores é composto por profissionais que nós mesmos formamos, com rigor, garantindo o comprometimento e excelência nos nossos serviços.

            O braço educacional é um dos nossos pontos fortes, além de formar nosso time, também capacitamos profissionais que desejam adentrar num dos mercados que melhor remunera atualmente. A plataforma tem como objetivo centralizar os nossos projetos educacionais, para que nossos alunos e toda nossa comunidade possam acessar de forma efetiva e eficiente os conteúdos.
            """
        )
    with st.expander("**Lider do Projeto**"):
        st.subheader("Rodolfo Barbosa")
        st.markdown(
            """
    - Qlik Partner Abasador 2023
    - 50 Pessoas para Seguir Segundo a Gama Academy
    - Linkedin Creator
    - Bacharel em Sistemas de Informacao
    - MBA em Gestão Estratégica
    - Com mais de 7 mil alunos formados, tenho muita honra e compartilhar conhecimento e mudar a vida de muitas pessoas com dados.
    """
        )
        st.image("assets/rodolfo.png", width=200)
    with st.expander("**Redes Sociais**"):
        st.markdown("[LinkedIn](https://www.linkedin.com/in/generalrodolfao/)")
        st.markdown("[Youtube](https://www.youtube.com/@DataSquad)")
        st.markdown("[Site](https://dtsqd.com/)")
