import streamlit as st 
from hugchat import hugchat
from hugchat.login import Login

email = 'walid.benromdhane@gmail.com'
passwd = 'Qawe456(x)'
sign = Login(email, passwd)
cookies = sign.login()
sign.saveCookies()

chatbot = hugchat.ChatBot(cookies=cookies.get_dict()) 

col1, col2, col3 = st.columns([1,6,1])

with col2:
	st.image("https://epsilonia.com/files/high_resolution.png")

question = st.text_input(label='Any question? EpsiBot is ready to answer',value='')
if question != '':
	answer = chatbot.chat(question)
	st.write(answer)