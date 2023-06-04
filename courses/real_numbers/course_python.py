# import streamlit as st
import sys
main_path = "C:\\Users\\WALID\\OneDrive\\Desktop\\Private\\Epsilonia\\python\\github\\main"
sys.path.insert(0, main_path)
from pysilonia import *

concept_titles = ['Real numbers basic concepts (1/2)', 'Real numbers basic concepts (2/2)', 'Density of a subset of R']
course_concept_names = ['real_numbers_basic_concepts_1','real_numbers_basic_concepts_2','density']

def get_graph():
	nodes = []
	edges = []
	n = len(concept_titles)
	for i in range(n):
		nodes.append(Node(id=concept_titles[i], label=concept_titles[i],shape="circular"))

	edges.append( Edge( source=concept_titles[0], label="comes before", target=concept_titles[1]))
	edges.append( Edge( source=concept_titles[1], label="comes before", target=concept_titles[2]))

	config = Config(width=750,
	                height=300,
	                directed=True, 
	                physics=False, 
	                hierarchical=False,
	                )
	return nodes, edges, config


course = Course()

course.name = "real_numbers"
course.title = "Real Numbers"
course.url = f'{course.name}.streamlit.app'
course.image = 'https://epsilonia.com/images/concept_images/density.png'
course.description = r"This course is about real numbers. It defines the set $\mathbb{R}$ of real numbers and gives their fundamental properties"
course.concepts = course_concept_names
course.prerequisites = course_concept_names
course.keywords = ['real numbers','real analysis']
course.graph = get_graph()

# course.display_preview()
# course.display_sidebar_menu()

if __name__=='__main__':
	course.save_course()