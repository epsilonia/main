import sys
from pysilonia import *
st.set_page_config(layout="centered")


def mylearnings_page():
	dp = DataPort()
	do = DisplayObject()
	mlo = MyLearnings()

	mylearnings_file = mlo.get_mylearnings_file()
	if not os.path.exists(mylearnings_file):
		mlo.initialize_mylearnings()

	do.display_title('My learnings')

	mylearnings = mlo.load_mylearnings()
	mylearnings_concepts_names = mylearnings['concepts']
	mylearnings_concepts = dp.load_concepts(mylearnings_concepts_names)

	mylearnings_courses_names = mylearnings['courses']
	# st.write(mylearnings_courses_names)
	mylearnings_courses = dp.load_courses(mylearnings_courses_names)


	with st.sidebar:

		# st.write("\n")
		styles={ "container": {"padding": "0!important", "background-color": "#f0f2f6"},
	             "nav-link": {"font-size": "14px", "color":"rgba(49, 51, 63, 0.6)", "text-align": "left", "margin":"0px"},
     	         "nav-link-selected": {"background-color": "#E3E7EE", "color":"#000000", "font-weight": "bold"}
     	        } 

		# selected = option_menu("", ['My concepts','	🎓 My courses','Create customized course'], 
		# 						key='mylearnings',
	    #     					icons=['puzzle-fill','book-fill','plus-circle-fill'], 
	    #     					menu_icon=' ',#"mortarboard-fill",
	    #     					styles=styles) #, default_index=0

		selected = option_menu("", ['🗨️ My concepts','📘 My courses','📝 Create customized course'], 
								key='mylearnings',
	        					icons=['  ','  ','  '], 
	        					menu_icon=' ',#"mortarboard-fill",
	        					styles=styles) #, default_index=0


	st.subheader(selected)

	if selected=='🗨️ My concepts':
		if len(mylearnings_concepts)==0:
			st.error('No concepts to display here. If you add concepts to MyLearnings. They will appear here.')
		else:
			do.display_list_of_concepts(mylearnings_concepts)

	if selected=='📘 My courses':
		if len(mylearnings_courses)==0:
			st.error('No courses to display here. If you add courses to MyLearnings. They will appear here.')
		else:
			do.display_list_of_courses(mylearnings_courses)

	if selected=='📝 Create customized course':
		course_title = st.text_input(key='course_title',label='Course name')
		selected_concepts = st.multiselect(key='select_concepts',
									   	   label='Add concepts from MyLearnings',
									   	   help='Select at least two concepts from MyLearnings. If MyLearnings is empty, you need to add concepts to it.',
									   	   options=[c.name for c in mylearnings_concepts])
		course_description = st.text_input(key='course_description',label='Course description')
		create = st.button("Create course")
		if create:
			mlo.create_course(course_title, selected_concepts, course_description)

# if __name__=='__main__':
add_logo()
mylearnings_page()
