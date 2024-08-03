import requests
import time
import streamlit as st

def SendQuestion():
    try:
        requestData = {"Texto": txt}
        reponseData = requests.post("https://h6rsuwtrwb2v4bo42mynffjijm0utqnv.lambda-url.eu-west-1.on.aws/", json=requestData).json()
        st.success("Obirgado, enviamos sua solicitação para o departamento **" + reponseData["Classes"][0]["Name"] + "**, em breve retornaremos o seu contato.")
    except Exception as error:
        st.write(str(error))   

st.set_page_config(page_title="SAC - QuantumFinance")

st.title("Bem-vindo à Quantum Finance")
st.subheader("Como podemos te ajudar?")
st.write("Digite abaixo, sua reclamação ou infomações que deja realizar para que possamos direcioná-lo ao departamento correto!")


txt = st.text_area(
    "Entre com suas solicitações:",
    "", placeholder="Digíte aqui suas solicitações"
)

if st.button("Enviar", "primary"):
    if (txt == ""):
        st.error('Por favor digite suas solicitações', icon="🚨")
    else:
        with st.spinner('Por favor, aguarde... Estamos analisando sua solicitação.'):
            SendQuestion()
