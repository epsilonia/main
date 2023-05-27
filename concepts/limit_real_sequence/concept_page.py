import sys

main_path = "C:\\Users\\WALID\\OneDrive\\Desktop\\Private\\Epsilonia\\python\\github\\main"
sys.path.insert(0, main_path)

from pysilonia import *

if __name__== '__main__':
    concept_name =  os.path.basename(os.path.dirname(__file__))
    dp = DataPort()
    concept = dp.load_concept(concept_name)
    concept.courses = ['real_numbers']
    concept.display_concept_page()