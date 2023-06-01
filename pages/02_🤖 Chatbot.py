from pysilonia import *
st.set_page_config(layout="wide")


def chatbot_page():

    dp = DataPort()
    do = DisplayObject()
    do.display_title('Chatbot')
    st.text_input('Have any math question? Epsibot is here to help!')


# if __name__=='__main__':
add_logo()
chatbot_page()
