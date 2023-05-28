import sys, os

up = os.path.dirname
main_path = up(up(up(__file__)))
sys.path.insert(0, main_path)

from pysilonia import *

if __name__== '__main__':
    course_name =  os.path.basename(up(__file__))
    dp = DataPort()
    course = dp.load_course(course_name)
    course.display_course_page()