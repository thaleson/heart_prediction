import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Função principal
def main():
    st.title("Visualização de Dados 📊")

    # Instruções para o usuário
    st.header("Instruções")
    st.write(
        """
        Para usar esta ferramenta, por favor, carregue um arquivo CSV que contenha os seguintes dados:
        
        - **age**: Idade (em dias)
        - **height**: Altura (em cm)
        - **weight**: Peso (em kg)
        - **ap_hi**: Pressão arterial sistólica
        - **ap_lo**: Pressão arterial diastólica
        - **cholesterol**: Nível de colesterol (1: normal, 2: acima do normal, 3: bem acima do normal)
        - **gluc**: Nível de glicose (1: normal, 2: acima do normal, 3: bem acima do normal)
        - **smoke**: Tabagismo (0: não, 1: sim)
        - **alco**: Consumo de álcool (0: não, 1: sim)
        - **active**: Atividade física (0: não, 1: sim)
        - **cardio**: Presença de doença cardíaca (0: não, 1: sim)
        
        O arquivo CSV deve ter um delimitador de ponto e vírgula (`;`).
        """
    )

    # Carregar o dataset diretamente na página
    st.header("Carregar Dados")
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file, delimiter=';')
        st.write("Dados carregados com sucesso!")

        # Mostrar o dataframe
        if st.checkbox("Mostrar Dados"):
            st.write(data.head())

        # Análise de dados
        st.header("Principais Análises e Gráficos")

        # Gráfico de distribuição de idades
        st.subheader("Distribuição das Idades")
        fig, ax = plt.subplots()
        sns.histplot(data['age'], bins=30, kde=True, ax=ax)
        ax.set_title('Distribuição de Idade')
        st.pyplot(fig)

        # Gráfico de pressão arterial
        st.subheader("Pressão Arterial")
        fig, ax = plt.subplots()
        sns.histplot(data['ap_hi'], bins=30, kde=True, color='blue', label='Sistólica', ax=ax)
        sns.histplot(data['ap_lo'], bins=30, kde=True, color='red', label='Diastólica', ax=ax)
        ax.set_title('Distribuição da Pressão Arterial')
        ax.legend()
        st.pyplot(fig)


        # Conclusão
        st.header("Conclusão")
        st.write(
            """
            Com os gráficos apresentados, é possível obter uma visão geral dos principais dados no seu dataset:
            
            - **Distribuição das Idades**: Ajuda a entender a faixa etária dos indivíduos.
            - **Pressão Arterial**: Mostra a distribuição das pressões sistólica e diastólica.
           
            Esses gráficos são úteis para identificar padrões e características predominantes nos dados. Utilize essas informações para análises mais aprofundadas ou para treinar modelos preditivos.
            """
        )

if __name__ == "__main__":
    main()
