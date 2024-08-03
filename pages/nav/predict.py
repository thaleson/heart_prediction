import streamlit as st
import numpy as np
import joblib
import time

def main():
    # Carregar o modelo e o scaler
    model = joblib.load('model/heart_disease_model.pkl')
    scaler = joblib.load('model/scaler.pkl')

    st.title("Previsão de Doença Cardíaca")

    st.write("Preencha os dados abaixo para fazer a previsão (os campos podem ser deixados em branco se não quiser preencher):")

    # Inputs para os dados
    age = st.number_input("Idade (anos)", min_value=0, max_value=120, value=0)
    gender = st.selectbox("Sexo", ["Selecione", "Masculino", "Feminino"], index=0)
    height = st.number_input("Altura (cm)", min_value=0, max_value=250, value=0)
    weight = st.number_input("Peso (kg)", min_value=0, max_value=200, value=0)
    ap_hi = st.number_input("Pressão Arterial Sistólica", min_value=0, max_value=250, value=0)
    ap_lo = st.number_input("Pressão Arterial Diastólica", min_value=0, max_value=150, value=0)
    cholesterol = st.selectbox("Colesterol", ["Selecione", "Normal", "Acima do Normal", "Muito Acima do Normal"], index=0)
    gluc = st.selectbox("Glicose", ["Selecione", "Normal", "Acima do Normal", "Muito Acima do Normal"], index=0)
    smoke = st.selectbox("Fumante", ["Selecione", "Não", "Sim"], index=0)
    alco = st.selectbox("Consumo de Álcool", ["Selecione", "Não", "Sim"], index=0)
    active = st.selectbox("Atividade Física", ["Selecione", "Não", "Sim"], index=0)

    # Converter entradas categóricas
    gender = 1 if gender == "Masculino" else (2 if gender == "Feminino" else 0)
    cholesterol = ["Normal", "Acima do Normal", "Muito Acima do Normal"].index(cholesterol) if cholesterol != "Selecione" else 0
    gluc = ["Normal", "Acima do Normal", "Muito Acima do Normal"].index(gluc) if gluc != "Selecione" else 0
    smoke = 1 if smoke == "Sim" else 0
    alco = 1 if alco == "Sim" else 0
    active = 1 if active == "Sim" else 0

    # Converter a idade de anos para dias
    age_days = age * 365

    # Criar um array com os dados de entrada, com 12 características
    input_data = np.array([
        age_days,  # idade em dias
        gender,
        height,
        weight,
        ap_hi,
        ap_lo,
        cholesterol,
        gluc,
        smoke,
        alco,
        active,
        0  # Adiciona uma característica adicional como placeholder
    ]).reshape(1, -1)

    # Verificar o número de características
    expected_features = 12  # Atualize isso se o número de características for diferente
    if input_data.shape[1] != expected_features:
        st.error(f"Erro: Esperado {expected_features} características, mas foram fornecidas {input_data.shape[1]}.")
        return

    # Verificar se todos os campos estão zerados
    if st.button("Prever"):
        if np.all(input_data == 0):
            st.warning("Insira os dados, por favor, para poder prever.")
        else:
            with st.spinner('Fazendo a previsão...'):
                time.sleep(2)  # Simula um tempo de carregamento
                
                # Escalar os dados
                input_data_scaled = scaler.transform(input_data)

                # Fazer a previsão
                prediction = model.predict_proba(input_data_scaled)[0][1]

                # Mostrar a previsão
                if prediction > 0.5:
                    st.markdown(
                        f"<h2 style='color:red;'>Sua chance de ter doença cardíaca é: {prediction * 100:.2f}% (Alta)</h2>",
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        "<div style='background-color: #f8d7da; padding: 10px; border-radius: 5px;'>"
                        "<p style='color: #721c24;'>A chance de você ter doença cardíaca é alta. Recomendamos que você procure um médico para uma avaliação mais detalhada.</p>"
                        "</div>", unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"<h2 style='color:green;'>Sua chance de ter doença cardíaca é: {prediction * 100:.2f}% (Baixa)</h2>",
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        "<div style='background-color: #d4edda; padding: 10px; border-radius: 5px;'>"
                        "<p style='color: #155724;'>A chance de você ter doença cardíaca é baixa. Continue mantendo um estilo de vida saudável.</p>"
                        "</div>", unsafe_allow_html=True
                    )

if __name__ == "__main__":
    main()