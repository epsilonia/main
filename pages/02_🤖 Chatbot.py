from pysilonia import *
from hugchat import hugchat
from hugchat.login import Login
st.set_page_config(layout="wide")

email = 'walid.benromdhane@gmail.com'
passwd = 'Qawe456(x)'
sign = Login(email, passwd)
cookies = sign.login()
sign.saveCookies()
chatbot = hugchat.ChatBot(cookies=cookies.get_dict()) 

def chatbot_page():

    dp = DataPort()
    do = DisplayObject()
    do.display_title('Chatbot')

    col1, col2, col3 = st.columns([1,6,1])

    with col2:

        question = st.text_input(label='Any question? EpsiBot is here to help',value='')
        if question != '':
            answer = chatbot.chat(question)
            st.write(answer)

# if __name__=='__main__':
add_logo()
chatbot_page()
