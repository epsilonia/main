from pysilonia import *
# import os



# if __name__== '__main__':

	# options = st.multiselect(
    # 	'What are your favorite colors',
    # 	['Real numbers basic concepts 1',
    # 	 'Real numbers basic concepts 2',
    # 	 'Density of a subset of R',
    # 	 'Another long name for a mathematical concept',
    # 	 'Can you add this one also',
    # 	 'Last concept name to be added'],
    # 	)
	# st.write('The course "" will contain the following concepts:', options)
	# st.button("Create course")

concept_name = 'geometric_sequence'
dp = DataPort()
concept = dp.load_concept(concept_name)
concept.display_concept_page()


# import streamlit as st
# import time

# placeholder = st.empty()

# # Replace the placeholder with some text:
# placeholder.text("Hello")
# time.sleep(3)


# # Replace the text with a chart:
# placeholder.line_chart({"data": [1, 5, 2, 6]})
# time.sleep(3)

# # Replace the chart with several elements:
# with placeholder.container():
#     st.write("This is one element")
#     time.sleep(3)
#     st.write("This is another")
#     time.sleep(3)

# # Clear all those elements:
# placeholder.empty()