# Importing necessary libraries
import streamlit as st

# Defining main session state
if "salary" not in st.session_state:
    st.session_state["salary"] = 0

# Page's main structure
st.set_page_config(page_title="Criador de Orçamentos", layout="centered", page_icon="💵")
st.markdown("# 💵 Criador de Orçamentos")
st.divider()
st.caption("Cria uma sugestão de orçamento baseada em seu salário.")

# Program

def budget_calculate():
    if st.session_state["calculate"]:
        calculus = st.session_state["salary"]
        st.info(body= " A divisão ideal do seu salário deveria ser: \n 1. {:.2f} para impostos; \n 2. {:.2f} para reserva de emergência; \n 3. {:.2f} para investimentos; \n 4. {:.2f} para despesas gerais.".format((calculus * 10)/100, (calculus * 15.00)/100 , (calculus * 15.00)/100, (calculus * 60)/100), icon="ℹ️")  
        st.write("Lembre-se que as porcentagens podem variar de acordo com a sua realidade, entretanto, caso suas despesas gerais ou impostos fiquem abaixo do valor estipulado, é interessante que você destine esse valor à sua reserva de emergência e investimentos.")

salary = st.number_input(label="INSIRA O SEU SALÀRIO", key="salary")
submit = st.button(label="CALCULAR", key="calculate", on_click=budget_calculate)