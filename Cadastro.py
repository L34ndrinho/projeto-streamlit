import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, dt_nasc, tipo):
    if nome and dt_nasc <= date.today():
        with open('Clientes.csv', 'a', encoding='utf-8') as file:
            file.write(f'{nome}, {dt_nasc}, {tipo}\n')
        st.session_state['sucesso'] = True
    else:
        st.session_state['sucesso'] = False

st.set_page_config(
    page_title='Cadastro de Clientes',
    page_icon='👌'
)


st.header('Projeto Cadastro de cliente com Streamlit')
st.divider()
st.title('Cadastro de Clientes')

nome = st.text_input('Digite o nome do cliente',
                     key = 'nome_cliente')

dt_nasc = st.date_input('Digite a data de nascimento', format='DD/MM/YYYY')

tipo = st.selectbox('Tipo de cliente',
                    ['Pessoa Física', 'Pessoa Jurídica', 'Outros'])


btn_cadastrar = st.button('Cadastrar', 
                          on_click=gravar_dados,
                          args=[nome, dt_nasc, tipo]
                          )

if btn_cadastrar:
    if st.session_state['sucesso']:
        st.success('Cliente cadastrado com sucesso',
                   icon='👌')
    else:
        st.error('Algo deu errado no seu cadastro',
                 icon='❌')
        
        


