from pysilonia import *
st.set_page_config(layout="wide")

add_logo()
st.write('<iframe src="https://epsilonia.com/wp/home1" title="description" height="4500" width="100%" ></iframe>',unsafe_allow_html=True)


# def go_to_top():
#     js = '''
#     <script>
#         var body = window.parent.document.querySelector(".main");
#         console.log(body);
#         body.scrollTop = 0;
#     </script>
#     '''
    # st.components.v1.html(js)

# if __name__ == '__main__':
    
# styles={ "container": {"padding": "0!important", "background-color": "#f4f4f4"}}    
# menu = option_menu("", ['Home','Search','Catalogue','MyLearnings'], 
#                         key='main_menu',
#                         icons=['house-door','search','book','mortarboard'], 
#                         menu_icon="",
#                         orientation="horizontal",
#                         styles=styles) #, default_index=0

# if menu=='Home':
#     go_to_top()
#     st.write('<iframe src="https://epsilonia.com" title="description" height="1000" width="100%" ></iframe>',unsafe_allow_html=True)
# if menu=='Search':
#     go_to_top()
#     search_page()
# if menu=='MyLearnings':
#     go_to_top()
#     mylearnings_page()