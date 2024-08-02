# import streamlit as st

# def main():
#     # Título principal
#     st.title("Bem-vindo à Página Inicial!")

#     # Subtítulo
#     st.subheader("Olá! Eu sou Thaleson Silva")

#     # Texto principal
#     st.write(
#         "Bem-vindo à aplicação de previsão de doença cardíaca. Aqui você pode utilizar nosso modelo "
#         "de aprendizado de máquina para avaliar o risco de doenças cardíacas com base em dados fornecidos. "
#         "Sinta-se à vontade para explorar as diferentes seções da aplicação para obter mais informações e realizar previsões."
#     )

#     # Seção para informações de contato
#     st.markdown(
#     'Para mais informações, veja o meu perfil no <a href="https://www.linkedin.com/in/thaleson-silva-9298a0296/" class="linkedin-button"><i class="fab fa-linkedin"></i> LinkedIn</a>',
#     unsafe_allow_html=True
# )


#     # Adicionando um aviso
#     st.markdown(
#         """
#         <div style='background-color: #f8d7da; padding: 10px; border-radius: 5px;'>
#             <h4 style='color: #721c24;'>Aviso:</h4>
#             <p style='color: #721c24;'>Este é um projeto de demonstração. A acurácia do modelo é de 72.34% e pode não ser adequada para uso em ambientes clínicos.</p>
#         </div>
#         """, unsafe_allow_html=True
#     )


import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def main():

    # Título principal
    st.title("Bem-vindo ao CardioPredictor! ❤️")

    # Subtítulo
    st.subheader("Olá! Eu sou Thaleson Silva 👋")

    # Texto principal
    st.write(
        "Bem-vindo à aplicação de previsão de doença cardíaca. Aqui você pode utilizar nosso modelo "
        "de aprendizado de máquina para avaliar o risco de doenças cardíacas com base em dados fornecidos. "
        "Sinta-se à vontade para explorar as diferentes seções da aplicação para obter mais informações e realizar previsões."
    )
    

   
  
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
