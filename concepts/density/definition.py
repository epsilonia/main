import plotly.graph_objects as go
import numpy as np
import importlib
import os
import sys
import inspect

main_path = "C:\\Users\\WALID\\OneDrive\\Desktop\\Private\\Epsilonia\\python\\github\\main"
sys.path.insert(0, main_path)

from pysilonia import *

def define_concept():
	concept = Concept()
	concept.title = "Density of a subset of ℝ"
	concept.description = "This is an introduction to the course and the second part of the video on the definition of real numbers"
	concept.short_definition = r'Some fundamental properties of real numbers and the set $\mathbb{R}$: the archimedean property, the absolute value and the intervals.'
	concept.keywords = ['real numbers', 'definition', 'basic properties','archimedean property','absolute value','intervals']
	concept.prerequisites = ['real_numbers_basic_concepts_1']
	concept.further_concepts = ['upper_bound_supremum_greatest_element']
	concept.courses = ['real_numbers']
	concept.video_description = 'This is an introduction to the course and the second part of the video on the definition of real numbers'
	concept.video_duration = '13 min'

	concept.url = "https://epsilonia.com"
	concept.name = os.path.basename(os.path.dirname(__file__))

	concept.has_coding = True
	concept.has_exercices = False
	concept.has_interactive_interface = False
	concept.has_quiz = False

	concept.automatic_fill()

	return concept

if __name__ == '__main__':
	concept = define_concept()
	concept.save_concept()
	print(f'["{concept.name}"', 'has been saved successfully!]')
