#Passo 1 - Criar o título ok
#Passo 2 - Cria o campo de mensagem ok
#Passo 3 - Printar as mensagens na tela ok
#Passo 4 - Armazenar as mensagens ok
#Passo 5 - Exibir todas as mensagens
#Passo 6 - Implementar a OpenAI

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="sk-proj-6jb7YAQw_NNGTMB5HdjY8BX")

st.write("## Cauã's AI")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_user = st.chat_input("Escreva aqui sua mensagem!")

if mensagem_user:
    st.chat_message("user").write(mensagem_user)
    mensagem = {"role": "user", "content": mensagem_user}
    st.session_state["lista_mensagens"].append(mensagem)

    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )

    resposta_ia = resposta_ia = resposta_modelo.choices[0].message.content

    print(resposta_modelo)

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
