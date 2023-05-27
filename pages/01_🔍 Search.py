from pysilonia import *
st.set_page_config(layout="centered")

def search_page():

    dp = DataPort()
    do = DisplayObject()

    # if __name__ == '__main__':

    col1, col2, col3 = st.columns([1,6,1])

    with col2:
        st.image("HighResolution.png")
    
    keyword = st.text_input('What do you wanna learn today?','')


    keyword = 'real numbers'
    if keyword != '':
        concept_names = [c for c in os.listdir(dp.concepts_folder) if c!='_template']
        list_of_concepts = dp.load_concepts(concept_names)
        research_result_concepts = [c for c in list_of_concepts if keyword in c.keywords ]
        len_results_concepts = len(research_result_concepts)

        course_names = [c for c in os.listdir(dp.courses_folder) if c!='_template']
        list_of_concepts = dp.load_courses(course_names)        
        research_result_courses = [c for c in list_of_concepts if c.keywords is not None if keyword in c.keywords ]
        len_results_courses = len(research_result_courses)

        len_results = len_results_courses+len_results_concepts
        s_concept = '' if len_results_concepts<=1 else 's'
        s_course = '' if len_results_courses<=1 else 's'
        found_string = f'{len_results} results found: {len_results_concepts} concept{s_concept} & {len_results_courses} course{s_course}' 
        st.subheader(found_string)
        st.write('---')
        st.subheader(f'Concepts:' )
        do.display_list_of_concepts(research_result_concepts)
        st.write('---')
        st.subheader(f'Courses:' )
        do.display_list_of_courses(research_result_courses)

if __name__=='__main__':
    search_page()
