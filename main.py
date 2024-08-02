import streamlit as st
from streamlit_option_menu import option_menu





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

def main():
    # Configuração do menu lateral
    with st.sidebar:
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
