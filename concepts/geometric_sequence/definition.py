import plotly.graph_objects as go
import numpy as np
import importlib
import os
import sys
import inspect

main_path = "C:\\Users\\WALID\\OneDrive\\Desktop\\Private\\Epsilonia\\python\\github\\main"
sys.path.insert(0, main_path)

from pysilonia import *

concepts_folder = "C:\\Users\\WALID\\OneDrive\\Desktop\\Private\\Epsilonia\\python\\github\\main\\concepts\\"
concepts_folder = "C:\\Users\\WALID\\OneDrive\\Desktop\\Private\\Epsilonia\\concepts\\"

def define_concept():
	concept = Concept()
	concept.title = "Geometric sequences"
	concept.description = "Geometric sequence"
	concept.short_definition = r'To obtain a geometric sequence, pick a number and multiply it by a constant value, then reapeat indefinitely.'
	concept.keywords = ['real numbers', 'geometric sequence', 'geometric sequences']
	concept.courses = ['real_numbers']
	# concept.prerequisites = ['upper_bound_supremum_greatest_element']
	# concept.further_concepts = ['subsequences']

	concept.video_description = 'Limit of a real number'
	concept.video_duration = '8 min'

	concept.url = "https://epsilonia.com"
	concept.name = os.path.basename(os.path.dirname(__file__))

	# concept.has_coding = True
	concept.has_exercices = True
	# concept.has_interactive_interface = True
	concept.has_quiz = True

	concept.automatic_fill()
	
	return concept

if __name__ == '__main__':
	concept = define_concept()
	# module = importlib.import_module('.\\epsilonia')
	concept.save_concept()
