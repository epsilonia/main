import streamlit as st
from streamlit_modal import Modal
from pysilonia import *


import streamlit.components.v1 as components

def create_course():
    if course_name=='':
        st.error('Course name cannot be empty')
    else:
        if len(selected_concepts)<2:
            st.error('The course must contain at least two concepts')
        else:
            st.success(f'The course "{course_name}" is now available in "MyCourses"')

mylearnings = load_mylearnings()
mylearnings_concepts = load_concepts(mylearnings)

selected = "Create course"
modal = Modal("Create course",key='modal')
open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():

        course_name = st.text_input(key='course_name',label='Course name')
        selected_concepts = st.multiselect(key='select_concepts',
                                           label='Add concepts to the course',
                                           help='Select at least two concepts',
                                           options=mylearnings)
        create = st.button("Create course")
        if create:
            create_course()


