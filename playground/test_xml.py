import xml.etree.ElementTree as ET 
from pysilonia import *
import os

concept_name = 'limit_real_sequence'
quiz_path = os.path.join(concepts_folder,concept_name,'quiz.xml') 
# Pass the path of the xml document 
tree = ET.parse(quiz_path) 
quiz = tree.getroot() 

# for question in quiz:
# 	print((question.attrib)['statement'])
# 	for option in question:
# 		text = (option.attrib)['text']
# 		iscorrect = (option.attrib)['iscorrect']
# 		comment = (option.attrib)['comment']
# 		print(f"* {text}")
# 		print(f"  {iscorrect}: {comment}")


concept_name = 'real_numbers_basic_concepts_2'
coding_path = os.path.join(concepts_folder,concept_name,'exercises.xml') 
# Pass the path of the xml document 
tree = ET.parse(coding_path) 
exercices = tree.getroot() 

videos = exercices.find('videos')
links = exercices.find('link')
for v in videos:
	print((v.attrib)['title'])
	print((v.attrib)['url'])
	print((v.attrib)['description'])
	print((v.attrib)['duration'])
# for ex in exercices:
# 	print(ex)
	# print(ex.find('video').text)
	# print((question.attrib)['statement'])
	# print((question.attrib)['solution'])
# print(exercices.find('videos'))