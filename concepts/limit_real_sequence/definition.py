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
	concept.title = "Limit of a real sequence"
	concept.description = "Definition of the limit of a real sequence"
	concept.short_definition = r'A real sequence is said to be convergent, or has a finite limit $\ell\;$ if it gets arbitrarily close to $\ell\;$'
	concept.keywords = ['real numbers', 'definition', 'basic properties','archimedean property','absolute value','intervals']
	concept.courses = ['real_numbers']
	# concept.prerequisites = ['upper_bound_supremum_greatest_element']
	# concept.further_concepts = ['subsequences']

	concept.video_description = 'Limit of a real number'
	concept.video_duration = '8 min'

	concept.name = os.path.basename(os.path.dirname(__file__))

	# concept.has_coding = True
	concept.has_exercices = True
	concept.has_interactive_interface = True
	concept.has_quiz = True

	concept.automatic_fill()

	return concept

if __name__ == '__main__':
	concept = define_concept()
	concept.save_concept()
