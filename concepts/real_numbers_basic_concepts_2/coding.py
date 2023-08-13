import streamlit as st
import xml.etree.ElementTree as ET 

def load_xml(xml_path):
	tree = ET.parse(xml_path) 
	root = tree.getroot() 
	return root

coding = load_xml('coding.xml') 
n = len(coding)
for i in range(n):
	question = coding[i]
	statement = question.find('statement').text
	solution = question.find('solution').text
	st.info(statement)
	show_code = st.checkbox(key=i,label='**Show solution**')
	if show_code:
		st.code(solution,language="python")