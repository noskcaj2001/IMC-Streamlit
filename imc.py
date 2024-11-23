import streamlit as st

with st.sidebar:
    st.title("Calculadora de IMC 🧮")

    #st.header("IMC: Definição?")
    st.header(" IMC :blue[Definição] ")

    st.write("Índice de massa corporal")

    st.write("É um índice que relaciona o peso e altura de uma pessoa")

st.title("Calculadora")


peso = st.number_input(label="Digite o seu peso em kg", min_value=0.0)

altura = st.number_input(label="Digite a sua altura em metros", min_value=0.0)

#Se o usuario cliar no botao, ele inicia o if
if st.button("Calcular"):
    imc = peso/(altura ** 2)
    imc_ideal = 21.7
    imc_delta = imc - imc_ideal

    if  imc < 18.5:
        resultado = {
            "classe" : "Abaixo do peso",
            "delta" : imc_delta
        }

    elif 18.5 <= imc < 25:
        resultado = {
            "classe" : "Peso ideal",
            "delta" : imc_delta 
        }

    elif 25 <= imc <=30:
        resultado = {
            "classe" : "Acima do peso",
            "delta" : imc_delta
        }

    elif imc <=40:
        resultado = {
            "classe": "Obesidade",
            "delta" : imc_delta
        }

    else:
        resultado = {
            "classe": "Obesidade morbida",
            "delta": imc_delta
        }


st.code(f"O resultado é {resultado}")


col1, col2 = st.columns(2)

col1.metric("IMC Classificado", resultado["classe"], resultado["delta"], delta_color="off")
col2.metric("IMC Calculado", round(imc, 2), resultado["delta"], delta_color="off")

st.divider()
st.text("Fonte")

st.image("./img.png")