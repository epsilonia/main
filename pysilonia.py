import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_agraph import agraph, Node, Edge, Config
import xml.etree.ElementTree as ET 
import pickle
import importlib
import os
import sys
import webbrowser
import random


# page parameters
subheader_color = 'blue'
concept_name_color = 'blue'
tabs_color ='red'

class Concept:

	# Defined by the user
	def __init__(self):
		self.name = None
		self.title = None
		self.description = None
		self.courses = None
		self.short_definition = None
		self.video_description = None
		self.video_duration = None
		self.keywords = None
		self.prerequisites = None
		self.further_concepts = None
		self.similar_concepts = None
		self.has_quiz = False
		self.has_exercises = False
		self.has_coding = False
		self.has_interactive_interface = False


	def automatic_fill(self):
		self.do = DisplayObject()
		self.dp = DataPort()
		self.mlo = MyLearnings()
		self.url = f"https://{self.name.replace('_','-')}.streamlit.app/"
		self.image =  self.dp.images_folder+f"{self.name}.png"
		self.video = {
						'title':'',
						'url': self.dp.videos_folder+f"{self.name}.mp4",
						'description': self.video_description,
						'duration' : self.video_duration
					 }
		if self.has_exercises:
			self.exercises_path = os.path.join(self.dp.concepts_folder,self.name,'exercises.xml')
		if self.has_quiz:
			self.quiz_path = os.path.join(self.dp.concepts_folder,self.name,'quiz.xml')
		if self.has_coding:
			self.coding_path = os.path.join(self.dp.concepts_folder,self.name,'coding.xml') 
		if self.has_interactive_interface:
			self.interactive_interface_path = os.path.join(self.dp.concepts_folder,self.name,'interactive_interface') 

	def display_concept_preview(self):
		with st.container():
			col1, col2 = st.columns([1,2])
			with col1:
				insert_space(height=3)
				src = self.image
				alt = self.name
				href = self.url
				html = f'<a href="{href}"><img src="{src}" alt="{alt}" width="220" ></a>' #height="170"
				st.write(html, unsafe_allow_html = True )
			with col2:
				st.markdown("<h4 style='color:#003F7A'>"+self.title+"</h4>", unsafe_allow_html=True)
				st.write(self.description)
				col21, col22 = st.columns([1,5])
				with col21:
					st.button(key=self.name+'_view'+str(random.randint(0,10)),label='View', args=(self.url,), on_click = DataPort.open_url)
				with col22:
					mylearnings = self.mlo.load_mylearnings()
					if self.name not in mylearnings['concepts']:
						st.button(key=self.name+'_add',label='Add to MyLearnings', args=(self.name,'concept'), on_click=self.mlo.add_to_mylearnings)
					else:
						st.button(key=self.name+'_remove',label='Remove from MyLearnings', args=(self.name,'concept'), on_click=self.mlo.remove_from_my_learnings)

	def display_prerequisites(self, expanded=False):
		if self.prerequisites:
			st.subheader(f":{subheader_color}[Prerequisites]")
			list_concepts = self.dp.load_concepts(self.prerequisites)
			label = 'Things you need to know first'
			self.do.display_list_of_concepts_in_expander(list_concepts, label, expanded)

	def display_courses(self, expanded=False):
		st.subheader(f":{subheader_color}[Related courses]")
		list_courses = self.dp.load_courses(self.courses)
		label = 'This concept can be part of the following courses'
		self.do.display_list_of_courses_in_expander(list_courses, label, expanded = expanded)

	def display_short_definition(self, expanded=False):
		st.subheader(f":{subheader_color}[Short definition]")
		with st.expander('The concept in a few words', expanded=expanded):
			st.write(self.short_definition)

	def display_video(self, expanded=False):
		st.subheader(f":{subheader_color}[Video]")
		video_url = self.video['url']
		description = self.video['description']
		with st.expander(f"Duration : {self.video['duration']}",expanded=expanded):
			st.write(description)
			st.video(video_url)

	def	display_interactive_interface(self, expanded=False):
		if self.has_interactive_interface:
			sys.path.insert(0, self.interactive_interface_folder)
			from interactive_interface import interactive_interface
			st.subheader(f":{subheader_color}[Interactive interface]")
			with st.expander('An interactive interface',expanded=expanded):
				interactive_interface()

	def display_quiz_xml(self, expanded=True):
		if self.has_quiz:
			quiz = self.dp.load_xml(self.quiz_path)
			n = len(quiz)
			st.subheader(f":{subheader_color}[Quiz]")
			expander_label = f'{n} questions' if n>1 else f'{n} question'
			with st.expander(expander_label,expanded=expanded):	
				tabs = (st.tabs([f"**:{tabs_color}[Question {i+1}]**" for i in range(n)]))
				for i in range(n):
					with tabs[i]:
						question = quiz[i]
						self.do.display_question_xml(question,i)
					
	def display_coding(self,expanded=True):
		if self.has_coding:
			coding = self.dp.load_xml(self.coding_path) 
			st.subheader(f":{subheader_color}[Coding exercice]")
			with st.expander('Learn math by coding',expanded=expanded):
				n = len(coding)
				for i in range(n):
					question = coding[i]
					statement = question.find('statement').text
					solution = question.find('solution').text
					st.info(statement)
					show_code = st.checkbox(key=i,label='**Show solution**')
					if show_code:
						st.code(solution,language="python")
		# except: pass


	def display_exercises(self, expanded=False):
		if self.has_exercises:
			exercises = self.dp.load_xml(self.exercises_path)

			videos_from_xml = exercices.find('videos')
			videos = []
			for v in videos:
				title = (v.attrib)['title']
				url = (v.attrib)['url']
				description = (v.attrib)['description']
				duration = (v.attrib)['duration']
				videos = video.append(new_video(title=title, url=url, description=description, duration=duration))

			links_from_xml = exercices.find('links')
			links = []
			for l in links:
				title = (l.attrib)['label']
				url = (l.attrib)['url']
				links = links.append(new_link_to_exercise(label=label, url=url))

			st.subheader(f":{subheader_color}[Exercises]")
			with st.expander('Exercises we selected for you',expanded=expanded):
				tab_video, tab_links = st.tabs([f':{tabs_color}[Videos]',f':{tabs_color}[Links]'])
				with tab_video:
					display_list_of_videos(self.exercises['videos'])
				with tab_links:
					display_list_of_exercice_links(self.exercises['links'])

	def	display_further_concepts(self,expanded=False):
		st.subheader(f":{subheader_color}[To go further]")
		label = 'Your possible next steps'
		list_concepts = self.further_concepts	
		display_list_of_concepts_in_expander(list_concepts, label, expanded=expanded)

	def display_similar_concepts(self,expanded=False):
		st.subheader(f":{subheader_color}[Similar concepts]")
		label = 'Concepts at the same level'
		list_concepts = self.similar_concepts	
		display_list_of_concepts_in_expander(list_concepts, label, expanded=expanded)
		
	def save_concept(self):
		concept_file = os.path.join(self.dp.concepts_folder, self.name, 'concept_object')
		with open(concept_file, 'wb') as outp:
			pickle.dump(self, outp, pickle.HIGHEST_PROTOCOL)


	def display_concept_page(self):
		self.do.display_title(self.title)
		self.display_short_definition()
		self.display_prerequisites()
		self.display_courses()
		self.display_video(expanded=True)
		self.display_interactive_interface(expanded=True)
		self.display_quiz_xml()
		self.display_coding()
		self.display_exercises()
		# display_further_concepts(concept)
		# display_similar_concepts(concept)

	def display_concept_in_course(self):
		self.do.display_title(self.title)
		self.display_short_definition()
		self.display_prerequisites()
		self.display_video(expanded=True)
		self.display_interactive_interface(expanded=True)
		self.display_quiz_xml()
		self.display_exercises()
		# self.display_further_concepts()
		# self.display_similar_concepts()

class Course:

	def __init__(self):
		self.name = None
		self.title = None
		self.description = None
		self.concepts = None
		self.prerequisites = None
		self.graph = None
		self.keywords = None
		self.image = 'https://epsilonia.com/images/concept_images/density.png'
		self.dp = DataPort()
		self.do = None
		self.mlo = None

	def display_introduction(self):
		col1, col2 = st.columns([1,2])
		# with col1:
		self.do.display_title(self.title)
		# st.title(course.title)
		st.subheader("About this course")
		st.write(self.description)
		st.subheader("The learning journey graph")
		st.write("Move the nodes to make the graph clearer for you")
		nodes, edges, config = self.graph
		agraph(nodes=nodes, edges=edges, config=config)

	def get_menu_titles(self):
		list_concepts = self.dp.load_concepts(self.concepts)
		menu_titles = [con.title for con in list_concepts]
		return menu_titles

	def display_course_page(self):
		sidebar_menu_styles = { "container": {"padding": "0!important", "background-color": "#f0f2f6"}}
		menu_titles = self.get_menu_titles()
		with st.sidebar:
			selected = option_menu("Course content", ['Course introduction']+menu_titles, 
		        					icons=['house-door']+['caret-right-square']*len(self.concepts), 
		        					menu_icon="book",
		        					styles=sidebar_menu_styles) #, default_index=0

		if selected=='Course introduction':
			self.display_introduction()

		list_concepts = [self.dp.load_concept(concept_name) for concept_name in self.concepts ]
		list_concepts_titles = [c.title for c in list_concepts ]

		for i in range(len(list_concepts_titles)):
			if selected==list_concepts_titles[i]:
				concept = list_concepts[i]
				concept.display_concept_in_course()


	def display_course_preview(self):
		with st.container():
			col1, col2 = st.columns([1,2])
			with col1:
				src = self.image
				alt = self.name
				href = f"https://{self.name.replace('_','-')}.streamlit.app/"
				html = f'<a href="{href}"><img src="{src}" alt="{alt}" width="200" ></a>' #height="170"
				st.write(html, unsafe_allow_html = True )
			with col2:
				st.markdown("<h4 style='color:#003F7A'>"+self.title+"</h4>", unsafe_allow_html=True)
				st.write(self.description)
				col21, col22 = st.columns([1,5])
				with col21:
					st.button(key=self.name+'_view'+str(random.randint(0,10)),label='View', args=(self.name,), on_click=self.dp.open_course)
				with col22:
					mylearnings = self.mlo.load_mylearnings()
					if self.name not in mylearnings['courses']:
						st.button(key=self.name+'_add'+str(random.randint(0,10)),label='Add to MyLearnings', args=(self.name,'course'), on_click=self.mlo.add_to_mylearnings)
					else:
						st.button(key=self.name+'_remove'+str(random.randint(0,10)),label='Remove from MyLearnings', args=(self.name,'course'), on_click=self.mlo.remove_from_my_learnings)
				list_concepts = self.dp.load_concepts(self.concepts)
				st.write("**Included concepts:**")
				for c in list_concepts:
					st.write("* "+c.title)

	def save_course(self,mycourse=False):
		course_file = os.path.join(self.dp.courses_folder, self.name,'course_object')
		if mycourse:
			course_file = os.path.join(self.dp.users_path, 'courses',self.name)
		with open(course_file, 'wb') as outp:
			pickle.dump(self, outp, pickle.HIGHEST_PROTOCOL)

	# def load_course(self, course_name):
	# 	if (course_name != '') & (course_name is not None):
	# 		course_file = os.path.join(self.concepts_folder, course_name)
	# 		with open(course_file, 'rb') as inp:
	# 			course = pickle.load(inp)
	# 		return course



class DataPort:

	def __init__(self):
		# self.courses_folder = "C:\\Users\\WALID\\OneDrive\\Desktop\\Private\\Epsilonia\\courses\\"
		# self.concepts_folder = "C:\\Users\\WALID\\OneDrive\\Desktop\\Private\\Epsilonia\\concepts\\"
		main = os.path.dirname(os.path.abspath(__file__))
		self.courses_folder = ".\\courses\\"
		self.concepts_folder = ".\\concepts\\"
		self.images_folder = "https://epsilonia.com/images/concept_images/"
		self.videos_folder = "https://epsilonia.com/videos/"
		# self.concept_url = "https://appname.streamlit.app/"
		self.courses_folder = os.path.join(main,'courses')
		self.concepts_folder = os.path.join(main,'concepts')
		self.users_path = os.path.join(main,'users')

	def load_xml(self, xml_path):
		tree = ET.parse(xml_path) 
		root = tree.getroot() 
		return root

	def open_course(self, course_name):
		course_python = os.path.join(self.courses_folder,course_name,'course_page.py')
		os.system(f'streamlit run {course_python}')

	def open_url(self,url):
		webbrowser.open_new_tab(url)

	def load_concept(self, concept_name):
		if (concept_name != '') & (concept_name is not None):
			concept_file = os.path.join(self.concepts_folder, concept_name, 'concept_object')
			with open(concept_file, 'rb') as inp:
				concept = pickle.load(inp)
			concept.automatic_fill()
			return concept

	def load_concepts(self, concept_names):
		concepts = [self.load_concept(c) for c in concept_names if c!='']
		return concepts

	def get_coursefile(self,course_name):
		if course_name.endswith('.mycourse'):
			course_file = os.path.join(self.users_path, 'courses',course_name)
		else:
			course_file = os.path.join(self.courses_folder, course_name,'course_object')
		return course_file

	def load_course(self, course_name):
		if (course_name != '') & (course_name is not None):
			course_file = self.get_coursefile(course_name)
			with open(course_file, 'rb') as inp:
				course = pickle.load(inp)
			course.do = DisplayObject()
			course.dp = DataPort()
			course.mlo = MyLearnings()
			return course

	def load_courses(self, course_names):
		courses = [self.load_course(c) for c in course_names if c!='']
		return courses


class MyLearnings:

	def __init__(self):
		self.dp = DataPort()

	def get_mylearnings_file(self):
		return os.path.join(self.dp.users_path, 'mylearnings')

 
	def save_mylearnings(self, mylearnings):
		mylearnings_file = self.get_mylearnings_file()
		with open(mylearnings_file, 'wb') as outp:
			pickle.dump(mylearnings, outp, pickle.HIGHEST_PROTOCOL)

	def load_mylearnings(self):
		mylearnings_file = self.get_mylearnings_file()
		with open(mylearnings_file, 'rb') as inp:
			mylearnings = pickle.load(inp)
		return mylearnings

	def add_to_mylearnings(self, element_name, element_type): # element_type : {'course','concept'}
		element_type = element_type+'s'
		mylearnings = self.load_mylearnings()
		new_list = mylearnings[element_type]+[element_name] # Adding concept 
		mylearnings[element_type] = list(set(new_list)) # Removing duplicate values
		self.save_mylearnings(mylearnings)

	def remove_from_my_learnings(self, element_name, element_type): # element_type : {'course','concept'}
		# Modifying the list in myleaning
		element_type = element_type+'s'		
		mylearnings = self.load_mylearnings()
		new_list = mylearnings[element_type] 
		new_list.remove(element_name)
		mylearnings[element_type] = new_list
		self.save_mylearnings(mylearnings)
		# Removing the file physically, if the course was created by the user
		if element_name.endswith('.mycourse'):
			course_file = self.dp.get_coursefile(element_name)
			os.remove(course_file)

	def initialize_mylearnings(self):
		mylearnings = {'concepts':[],'courses':[]}
		self.save_mylearnings(mylearnings)

	def create_course(self, course_title, selected_concepts, course_description):
		if course_title=='':
			st.error('Course name cannot be empty')
		else:
			if len(selected_concepts)<2:
				st.error('The course must contain at least two concepts')
			else:
				course = Course()
				course.title = course_title
				course.url = ''
				course.name = course_title.lower().replace(' ','_')+'.mycourse'
				course.description = course_description
				course.concepts = selected_concepts
				course.dp = DataPort()
				course.mlo = MyLearnings()
				course.save_course(mycourse=True)
				self.add_to_mylearnings(course.name, 'course')

				st.success(f'The course "{course_title}" is now available in "MyCourses"')




class DisplayObject:

	def __init__(self):
		self.display = None

	def display_list_of_concepts(self, list_concepts):
		n = len(list_concepts)
		for i in range(n):
			concept = list_concepts[i]
			concept.display_concept_preview()
			if i<n-1:
				st.write("----")


	def display_list_of_courses(self, list_courses):
		n = len(list_courses)
		for i in range(n):
			course = list_courses[i]
			course.display_course_preview()
			if i<n-1:
				st.write("----")

	def display_list_of_videos(self, list_videos):
		n = len(list_videos)
		for i in range(n):
			with st.container():
				video_i = list_videos[i]
				col1, col2 = st.columns([1,1])
				with col2:
					video_url = video_i['url']
					st.video(video_url)
				with col1:
					st.markdown("<h4 style='color:#003F7A'>"+video_i['title']+"</h4>", unsafe_allow_html=True)
					st.write(video_i['description'])

	def display_list_of_exercice_links(self, list_links):
		n = len(list_links)
		for i in range(n):
			label = list_links[i]['label']
			url = list_links[i]['url']
			markdown = f":link: [{label}]({url})"
			st.markdown(markdown, unsafe_allow_html=True)

	def display_list_of_concepts_in_expander(self, list_concepts, label, expanded):
	        with st.expander(label=label,expanded=expanded):
	        	self.display_list_of_concepts(list_concepts)
			
	def display_list_of_courses_in_expander(self, list_courses, label, expanded):
	        with st.expander(label=label,expanded=expanded):
	        	self.display_list_of_courses(list_courses)
			
	def	display_title(self, title):
		st.markdown("<h1 style='text-align: center;'>"+title+"</h1>", unsafe_allow_html=True)

	def display_question_xml(self, question, qi):

		if f'checkbox{qi}' not in st.session_state:
			st.session_state[f'checkbox{qi}'] = (0,0,0)

		def change1():
			st.session_state[f'checkbox{qi}'] = (1,0,0)
		def change2():
			st.session_state[f'checkbox{qi}'] = (0,1,0)
		def change3():
			st.session_state[f'checkbox{qi}'] = (0,0,1)
			
		change = [change1, change2, change3]

		statement = (question.attrib)['statement']
		st.write(f"**{statement}**")
		answers = []
		n = len(question)
		for i in range(n):
			option = question[i]
			text = (option.attrib)['text']
			ans = st.checkbox(key=f"{qi}{i}" ,label=f"{text}", value = st.session_state[f'checkbox{qi}'][i], on_change = change[i])
			answers.append(ans)

		if sum(answers)==0:
			st.write('Select an answer')
		else:
			for i in range(n):
				if answers[i]:
					option = question[i]
					iscorrect = (option.attrib)['iscorrect']
					comment = (option.attrib)['comment']
					color = 'green' if iscorrect=='True' else 'red'
					comment = f":{color}[{comment}]"
					st.write(comment)
	

def new_video(title, url, description, duration):
	video = {'title':title, 'url':url, 'description':description, 'duration':duration}
	return video

def new_link_to_exercise(label, url):
	link = {'label':label, 'url':url}
	return link

def insert_space(height=70):
    html = f'<img src="https://epsilonia.com/images/icons/space.png" height="{height}" width="20" alt="">'
    st.write(html, unsafe_allow_html = True )


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://epsilonia.com/files/logo_white.svg);
                background-repeat: no-repeat;
                padding-top: 20px;
                background-position: 20px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )