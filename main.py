import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.colored_header import colored_header
from streamlit_lottie import st_lottie
import json




# Configuração da página principal
st.set_page_config(page_title="CardioPredictor", page_icon="❤️")



st.markdown(
    f"""
    <style>
    {open("static/styles.css").read()}
    </style>
    """,
    unsafe_allow_html=True
)

# animações
with open("animaçoes\pagina_inicial3.json") as source:
    animacao_1 = json.load(source)


def main():
    # Configuração do menu lateral
    with st.sidebar:


        #exibir animação
        st_lottie(animacao_1, height=100, width=270)

        # marcador azul
        colored_header(
        label="",
        description="",
        color_name="light-blue-70"
        )
        selection = option_menu(
            menu_title="Navegação",
            options=["Home", "Sobre o Projeto", "Previsão","Visão dos dados"],
            icons=["house", "info-circle", "bar-chart"],
            default_index=0
        )

    # Lógica para carregar a página selecionada
    if selection == "Home":
        import pages.nav.Home as home
        home.main()
    elif selection == "Sobre o Projeto":
        import pages.nav.about as sobre
        sobre.main()

    elif selection == "Visão dos dados":
        import pages.nav.data_views as date

        date.main()       
    elif selection == "Previsão":
        import pages.nav.predict as previsao
        previsao.main()

     

if __name__ == "__main__":
    main()
