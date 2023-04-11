
import streamlit as st
import plotly.graph_objects as go
import numpy as np

def get_figure(a0):
        
    visible = True
    Nmax = 29
    x = np.arange(-1,8,.005)
    f = lambda x: np.sqrt(x+1)
    
    a = np.array([a0, a0  , f(a0), f(a0)   , f(f(a0))])
    b = np.array([0, f(a0), f(a0), f(f(a0)), f(f(a0))])
    
    for i in range(Nmax):
        a = np.append(a, [f(a[-3]),f(a[-2]),f(a[-1])])
        b = np.append(b, [f(b[-3]),f(b[-2]),f(b[-1])])           
    
    # Create figure
    fig = go.Figure()

    # The curve
    fig.add_trace(
        go.Scatter
        (
            x=x, 
            y=f(x), 
            mode='lines',
#             line_color='rgba(94,192,231,255)',
            visible=visible, 
            showlegend=False
        )
    )

    # The line y=x
    fig.add_trace(
        go.Scatter
        (
            x=x, 
            y=x, 
            mode='lines',
#             line_color='rgba(94,192,231,255)',
            visible=visible, 
            showlegend=False
        )
    )

    
    # The step curve
    fig.add_trace(
        go.Scatter
        (
            visible=visible,
            mode = 'lines',
            line = {'dash':'dot'},
            x=a,
            y=b,
            showlegend=False
        )
    )
        
    # Text "a0"
    fig.add_trace(
        go.Scatter
        (
             x=[a0],
             y=[-0.15],
             mode='text',
             text="<b>a0</b>",
             textfont = dict(size=18, color='rgba(255,0,0,255)'),
             showlegend=False,        
             visible=visible
        )
    )
    
#     fig.update_yaxes(
#                 scaleanchor="x",
#                 scaleratio=1,
#       )
    
    
    title = "The sequence converges to the fixed point of the function"
    title_color = 'rgba(94,192,231,255)'
    
    fig.update_layout(title = title,   title_font_color=title_color)
    fig.update_xaxes(range=[-2, 4.5],zeroline=True, zerolinewidth=1, zerolinecolor='black')
    fig.update_yaxes(range=[-0.2, 3],zeroline=True, zerolinewidth=1, zerolinecolor='black')


    return fig


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.markdown("<h1 style='text-align: center;'>Example of a recursive sequence</h1>", unsafe_allow_html=True)
st.markdown("""---""")
st.markdown("<h3 style='text-align: left;'>Instructions</h3>", unsafe_allow_html=True)
st.markdown("(1) Use the first slider to change the value of the first term a0", unsafe_allow_html=True)
st.latex("a_0 \geq -1 \quad ; \quad a_{n+1}=\sqrt{1+a_n}")
st.markdown("A good value of N is one such that all terms with indices greater than N are inside the strip of center 2 and radius ε", unsafe_allow_html=True)
st.markdown("""---""")
a0 = st.slider("a0", min_value=-1.0, max_value=4.0, value=-0.5, step=.001, disabled=False, label_visibility="visible")
fig = get_figure(a0)
st.plotly_chart(fig, use_container_width=False)





