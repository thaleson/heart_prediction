import json
import streamlit as st
from streamlit_lottie import st_lottie

def main():
    # Título principal
    st.title("Bem-vindo ao CardioPredictor! ❤️")

    # Subtítulo
    st.subheader("Olá! Eu sou Thaleson Silva 👋")

    # Adicionando uma seção com animações
    col1, col2 = st.columns(2)

    # Carregar animações
    with open("animaçoes/pagina_inicial1.json") as source:
        animacao_1 = json.load(source)
    with open("animaçoes/pagina_inicial2.json") as source:
        animacao_2 = json.load(source)

    # Conteúdo da coluna 1
    with col1:
        st_lottie(animacao_1, height=350, width=400)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<h5 style='text-align: justify;'>CardioPredictor é um  projeto visa fornecer previsões precisas sobre o risco de doenças cardíacas, ajudando a promover a saúde e o bem-estar. Acompanhe o progresso do projeto e explore as funcionalidades que oferecemos para uma análise detalhada e útil.</h5>", unsafe_allow_html=True)

    # Conteúdo da coluna 2
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<h5 style='text-align: justify;'> Aqui, você terá a oportunidade de acompanhar todas as etapas envolvidas no desenvolvimento deste projeto, desde a concepção até a criação de um modelo de previsão personalizado, adaptado especificamente às características únicas de cada paciente.</h5>", unsafe_allow_html=True)
        st_lottie(animacao_2, height=400, width=440)

    # Adicionando um aviso
    st.markdown(
        """
            <div style='background-color: #f8d7da; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #721c24;'>Aviso:</h4>
                <p style='color: #721c24;'>Este é um projeto de demonstração. A acurácia do modelo é de <strong>72.34%</strong> e pode não ser adequada para uso em ambientes clínicos.</p>
            </div>
            """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
