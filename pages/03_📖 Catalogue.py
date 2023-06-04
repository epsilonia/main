from pysilonia import *
st.set_page_config(layout="wide")


def update_i(delta):
    st.session_state.i = st.session_state.i+delta

def update_j(delta):
    st.session_state.j = st.session_state.j+delta


def catalogue_page():

    dp = DataPort()
    do = DisplayObject()

    do.display_title('Learning catalogue')


    st.subheader('Concepts')
    st.write("---")
    # st.write(dp.concepts_folder)


    with st.container():
        col1, col2, col3 = st.columns([1,20,1])
        with col1:
            insert_space()
            st.button(key='next_concept',label= ':arrow_backward:',args=(-1,),on_click=update_i)
        with col3:
            insert_space()
            st.button(key='previous_concept',label=':arrow_forward:',args=(1,),on_click=update_i)

        with col2:
            concept_names = [c for c in os.listdir(dp.concepts_folder) if c!='_template']
            n = len(concept_names)
            if 'i' not in st.session_state:
                st.session_state.i = 0
            i=st.session_state.i
            ncols = 3
            cols = st.columns(ncols)
            for ik in range(0,ncols):
                i0 = (i+ik)%n
                concepti0 = dp.load_concept(concept_names[i0])
                with cols[ik]:  
                    src = concepti0.image
                    alt = concepti0.name
                    href = concepti0.url
                    html = f'<a href="{href}"><img src="{src}" alt="{alt}" width="300" ></a>' #height="170"
                    st.write(html, unsafe_allow_html = True )
                    # st.image(concepti0.image)
                    st.write(f'<p style="text-align:center; font-weight:bold"> {concepti0.title} </p>',unsafe_allow_html=True)

    st.write("---")
    st.subheader('Courses')
    st.write("---")
    with st.container():
        col1, col2, col3 = st.columns([1,20,1])
        with col1:
            insert_space()
            st.button(key='next_course',label= ':arrow_backward:',args=(1,),on_click=update_j)
        with col3:
            insert_space()
            st.button(key='previous_course',label=':arrow_forward:',args=(-1,),on_click=update_j)

        with col2:
            courses_names = [c for c in os.listdir(dp.courses_folder) if c!='_template']
            n = len(courses_names)
            if 'j' not in st.session_state:
                st.session_state.j = 0
            j=st.session_state.j
            ncols = 3
            cols = st.columns(ncols)
            for ik in range(0,ncols):
                i0 = (i+ik)%n
                coursei0 = dp.load_course(courses_names[i0])
                with cols[ik]:  
                    src = coursei0.image
                    alt = coursei0.name
                    href = coursei0.url
                    html = f'<a href="{href}"><img src="{src}" alt="{alt}" width="300" ></a>' #height="170"
                    st.write(html, unsafe_allow_html = True )
                    # st.image(coursei0.image)
                    st.write(f'<p style="text-align:center; font-weight:bold"> {coursei0.title} </p>',unsafe_allow_html=True)

# if __name__=='__main__':
add_logo()
catalogue_page()
