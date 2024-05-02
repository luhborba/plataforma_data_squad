import streamlit as st


def cursos():
    curso = st.selectbox(
        "Selecione o Curso:",
        ["Aspirantes em Dados #2", "SuperLive"],
        index=None,
        placeholder="Escolha um Curso",
    )
    if curso == "Aspirantes em Dados #2":
        st.subheader("Aspirantes em Dados #2")
        st.write("Neste curso vamos abordar diversos temas do mundo de Dados!!!")
        st.markdown(
            "[Acesse o Drive com Arquivos das Aulas](https://drive.google.com/drive/folders/1KAxr5cIIj08ROeF4xp6-oaoiV1i97fuY)"
        )
        with st.expander("Aula 01"):
            st.video(
                "https://www.youtube.com/watch?v=LbMLomCXs-g&list=PLPAlZw8xZuOUK0Nq6AWxxZbzG2c_nEtDL&index=1"
            )
        with st.expander("Aula 02"):
            st.video(
                "https://www.youtube.com/watch?v=Wl0gKuTalgo&list=PLPAlZw8xZuOUK0Nq6AWxxZbzG2c_nEtDL&index=2"
            )
        with st.expander("Aula 03"):
            st.video(
                "https://www.youtube.com/watch?v=_2M825ktW1Q&list=PLPAlZw8xZuOUK0Nq6AWxxZbzG2c_nEtDL&index=3"
            )
        with st.expander("Aula 04"):
            st.video(
                "https://www.youtube.com/watch?v=qvFi95Q2AmE&list=PLPAlZw8xZuOUK0Nq6AWxxZbzG2c_nEtDL&index=4"
            )
        with st.expander("Aula 05"):
            st.video(
                "https://www.youtube.com/watch?v=L7RM_IFRtcg&list=PLPAlZw8xZuOUK0Nq6AWxxZbzG2c_nEtDL&index=5"
            )
        with st.expander("Aula 06"):
            st.video(
                "https://www.youtube.com/watch?v=6vzQOl7oqoQ&list=PLPAlZw8xZuOUK0Nq6AWxxZbzG2c_nEtDL&index=6"
            )
        with st.expander("Aula 07"):
            st.video(
                "https://www.youtube.com/watch?v=Q5MYQMamEGQ&list=PLPAlZw8xZuOUK0Nq6AWxxZbzG2c_nEtDL&index=7"
            )
        with st.expander("Aula 08"):
            st.video(
                "https://www.youtube.com/watch?v=a-zKBI-Oj8s&list=PLPAlZw8xZuOUK0Nq6AWxxZbzG2c_nEtDL&index=8"
            )
        with st.expander("Aula 09"):
            st.video(
                "https://www.youtube.com/watch?v=5M3pt0SGvh0&list=PLPAlZw8xZuOUK0Nq6AWxxZbzG2c_nEtDL&index=9"
            )
        with st.expander("Aula 10"):
            st.video(
                "https://www.youtube.com/watch?v=KtzWo-pe1es&list=PLPAlZw8xZuOUK0Nq6AWxxZbzG2c_nEtDL&index=10"
            )
        with st.expander("Aula 11"):
            st.video(
                "https://www.youtube.com/watch?v=I3JOtry3i8w&list=PLPAlZw8xZuOUK0Nq6AWxxZbzG2c_nEtDL&index=11"
            )
    elif curso == "SuperLive":
        st.subheader("SuperLive")
        st.video("https://www.youtube.com/watch?v=PNVqar-1mK8")
    else:
        st.write("Nenhum curso selecionado")
