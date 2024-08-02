import streamlit as st


def main():
   

 st.markdown(
        '''
         <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

        <div class="description">
            <h1>Sobre o Projeto <span role="img" aria-label="heart">❤️</span></h1>
            <p>
                Este projeto tem como objetivo a previsão de risco de doença cardíaca utilizando modelos de aprendizado de máquina. O modelo foi treinado com o dataset <a href="https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset" target="_blank">Heart Disease Dataset</a>.
            </p>
            <h2>Algoritmo Utilizado <span role="img" aria-label="brain">🧠</span></h2>
            <p>
                Utilizamos um modelo de classificação baseado em <strong>Regressão Logística</strong>. O modelo foi treinado para identificar padrões e prever a probabilidade de uma pessoa ter doença cardíaca com base em várias características.
            </p>
            <h2>Acurácia do Modelo <span role="img" aria-label="bar chart">📊</span></h2>
            <p>
                O modelo atual alcançou uma acurácia de <strong>72.34%</strong>. Estamos continuamente aprimorando o modelo para melhorar essa métrica e fornecer previsões mais precisas.
            </p>
            <h2>Tecnologias Utilizadas <span role="img" aria-label="technologies">🔧</span></h2>
            <ul>
                <li><i class="tech-icons fab fa-python"></i><strong>Python</strong>: Linguagem de programação principal para o desenvolvimento do projeto.</li>
                <li><i class="tech-icons fab fa-python"></i><strong>Streamlit</strong>: Framework utilizado para criar a interface interativa da aplicação.</li>
                <li><i class="tech-icons fab fa-python"></i><strong>Scikit-learn</strong>: Biblioteca para machine learning, utilizada para treinamento e avaliação do modelo.</li>
                <li><i class="tech-icons fas fa-cogs"></i><strong>NumPy</strong>: Biblioteca para manipulação eficiente de arrays e operações matemáticas.</li>
                <li><i class="tech-icons fas fa-database"></i><strong>Pandas</strong>: Biblioteca para análise e manipulação de dados.</li>
                <li><i class="tech-icons fas fa-chart-line"></i><strong>Matplotlib</strong> e <strong>Seaborn</strong>: Bibliotecas para visualização de dados, usadas para gerar gráficos informativos.</li>
            </ul>
        </div>
        <div class="footer">
            <p>Desenvolvido por <strong>Thaleson Silva</strong>. Para mais informações, visite meu <a href="https://www.linkedin.com/in/thaleson-silva-9298a0296/" class="linkedin-button"><i class="fab fa-linkedin"></i> LinkedIn</a>.</p>
        </div>            
     
        ''',
        unsafe_allow_html=True
    )



