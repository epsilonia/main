import sys, os

main_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, main_path)

from pysilonia import *

if __name__== '__main__':
    concept_name =  os.path.basename(os.path.dirname(__file__))
    dp = DataPort()
    concept = dp.load_concept(concept_name)
    concept.display_concept_page()