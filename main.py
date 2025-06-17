import streamlit as st

from helpers.utils import load_joblib_file



st.set_page_config(layout = "wide")

model = load_joblib_file("models/grade_prediction_model.pkl")
scaler = load_joblib_file("models/preprocessor_student_grade.pkl")

st.title("Previsão de Notas de Alunos")

col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

# Elementos da Página
with col1:
    st.subheader("Perfil do Aluno")
    st.radio(label="Gênero", options=["Masculino", "Feminino"])
    st.slider(label="Idade", min_value = 15, max_value = 22)

with col2:
    st.subheader("Situação da Mãe")
    st.pills(label="Educação da Mãe", options=["Sem Educação Formal", "Educação Primária", 
                                               "Ensino Fundamental", "Ensino Médio", "Ensino Superior"], key="Medu")
    st.selectbox(label="Ocupação da Mãe", options=["Professora", "Serviços Públicos", 
                                               "Fica em Casa", "Serviços de Saúde", "Outro"], key="Mjob")

with col3:
    st.subheader("Situação do Pai")
    st.pills(label="Educação do Pai", options=["Sem Educação Formal", "Educação Primária", 
                                               "Ensino Fundamental", "Ensino Médio", "Ensino Superior"], key="Fedu")
    st.selectbox(label="Ocupação do Pai", options=["Professora", "Serviços Públicos", 
                                               "Fica em Casa", "Serviços de Saúde", "Outro"], key="Fjob")
    
with col4:
    st.write(" ")
    st.write(" ")
    st.subheader("Estudos e Histórico")
    st.radio(label="Faz classes extras?", options=["Sim", "Não"])
    st.slider(label="Quantos anos foram repetidos?", min_value = 0, max_value = 3)
    st.selectbox(label="Tempo de Estudo (Semanal)", options=["Menos de 2 horas", "02 - 05 horas", "5 - 10 horas", "Mais de 10 horas"])

with col5:
    st.write(" ")
    st.write(" ")
    st.subheader("Perfil e Extraescolar")
    st.radio(label="Interesse em educação superior?", options=["Sim", "Não"], key="higher")
    st.radio(label="Possui acesso à internet em casa?", options=["Sim", "Não"], key="internet")
    st.selectbox(label="Quão frequentemente sai com amigos?", options=["Muito Pouco", "Pouco", "Moderado", "Alto", "Muito Alto"])

st.write(" ")
st.write(" ")
st.button("Prever")