import streamlit as st
import webbrowser
import pickle
import os
from pysilonia import * 


# words = 'real sequences'
# keywords = ['real sequences', 'real_numbers_basic_concepts_2','density','limit_real_sequence']
# print(any( [w in keywords for w in words.split(' ')]))
# print(words in keywords)

# def open_url(url):
# 	webbrowser.open_new_tab(url)

# st.button(key='view',label='View', args=('https://epsilonia.com',), on_click=open_url)

# users_path = "C:\\Users\\WALID\\OneDrive\\Desktop\\Private\\Epsilonia\\python\\github\\main\\users"

# mlo = MyLearnings()
# mylearnings = mlo.load_mylearnings()
# mylearnings = {'concepts':['density', 'limit_real_sequence', 'geometric_sequence', 'real_numbers_basic_concepts_2', 'real_numbers_basic_concepts_1'],
#  			   'courses':['real_numbers']}
# print(mylearnings['concepts'])
# new_list = mylearnings['concepts']+['new concept']
# mylearnings['concepts'] = list(set(new_list))
# print(mylearnings['concepts'])

# list(set()) # Adding concept and removing duplicate values
# mlo.save_mylearnings(mylearnings)
# mylearnings = mlo.load_mylearnings()
# print(mylearnings['concepts'])

# Test 
# initialize_mylearnings()
# mylearnings = load_mylearnings()
# mylearnings.append('density')
# save_mylearnings(mylearnings)
# mylearnings = load_mylearnings()
# mylearnings.append('density')
# print(mylearnings)
# remove_from_my_learnings('limit_real_sequence')
# mylearnings = load_mylearnings()
# print(mylearnings)

# filename = 'best_course_ever.mycourse'
# if filename.endswith('.mycourse'):
# 	print("It ends with .mycourse")

# concept_url = 'https://epsilonia.com/files/concepts/density'

# with open(concept_file, 'rb') as inp:
# 	concept = pickle.load(inp)


# import urllib.request
# with urllib.request.urlopen(concept_file) as inp:
#     concept = pickle.load(inp)

# print(concept.title)

import requests

concept_file = 'https://epsilonia.com/files/concepts/geometric_sequence.pkl'
downloaded_filename = 'geometric_sequence.pkl'

def download_file(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Ensure we got a successful response

    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

# Example usage:
download_file(concept_file, downloaded_filename)

# concept_file = os.path.join(self.concepts_folder, concept_name, 'concept_object')
# with open(concept_file, 'rb') as inp:
# 	concept = pickle.load(inp)
# return concept

with open(downloaded_filename, 'rb') as inp:
	concept = pickle.load(inp)

# dp = DataPort()

# concept = dp.load_concepts(['geometric_sequence'])
print(concept.title)


