
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
    
    
    title = "The sequence converges to the fixed point of the function, which is the golden ratio phi"
    title_color = 'rgba(94,192,231,255)'
    
#    fig.update_layout(title = title,   title_font_color=title_color)
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
st.markdown("<h1 style='text-align: center;'>An astonishing property of the golden ratio</h1>", unsafe_allow_html=True)
st.markdown("""---""")
st.markdown("<h3 style='text-align: left;'>Introduction</h3>", unsafe_allow_html=True)

text = r'''
The golden ratio is the only positive number whose square is obtained just by adding 1. In math terms: 
$$ 
\qquad \qquad \phi > 0 \quad ; \quad \phi^{2} = 1+\phi \qquad \qquad (1)
$$
The astonishing property referred to in the title is the following:
$$
 \qquad \qquad \phi = \sqrt{1+\sqrt{1+\sqrt{1+\sqrt{1+\cdots}}}}  \qquad \qquad (2)
$$
Which can be understood intuitively as follows:  
$\bullet$ We take the square root of equation (1) above:
$$
\phi = \sqrt{1+\phi}
$$
$\bullet$ We replace $\; \phi \;$  on the right-hand side with $ \; \sqrt{1+\phi} \;$  (because they're equal), we obtain:
$$
\phi = \sqrt{1+\sqrt{1+\phi}}
$$
$\bullet$ We keep doing this over and over again and we obtain the above-mentioned property
'''
st.markdown(text)
st.markdown("""---""")
st.markdown("<h3 style='text-align: left;'>Why is that?</h3>", unsafe_allow_html=True)

text = r'''
The short answer is that $\; \phi \;$  is the limit of the sequence obtained by applying the function: 
$$
f(x)=\sqrt{1+x}
$$
several times starting from any number greater than -1.
In other words, if we define a sequence $(a_n)$ by: 
$$
\qquad \qquad a_0 \geq -1 \quad ; \quad a_{n} = \sqrt{1+a_{n-1}} \qquad \qquad (1)
$$
we will have:   
$\bullet \; a_1 = \sqrt{1+a_0}$  
$\bullet \; a_2 = \sqrt{1+a_1} = \sqrt{1+\sqrt{1+a_0}}$  
$\bullet \; a_3 = \sqrt{1+a_2} = \sqrt{1+\sqrt{1+\sqrt{1+a_0}}}$  
$\bullet \; a_4 = \sqrt{1+a_2} = \sqrt{1+\sqrt{1+\sqrt{1+\sqrt{1+a_0}}}}$  
$\quad \vdots$  
and 
$$
\underset{+\infty}{\lim} \; a_{n}= \sqrt{1+\sqrt{1+\sqrt{1+\sqrt{1+\cdots}}}}
$$
'''
st.markdown(text)

st.markdown("""---""")
st.markdown("<h3 style='text-align: left;'>Instructions</h3>", unsafe_allow_html=True)

text = r'''
Use the slider to change the value of $a_0$, the first term of the sequence. Observe that the sequence always 
converges to the fixed-point of the function. Prove that this fixed point is the golden ratio $\phi$.  
For a rigourous proof, you can use the fixed-point theorem.

'''
st.markdown(text)

a0 = st.slider("a0", min_value=-1.0, max_value=4.0, value=-0.5, step=.001, disabled=False, label_visibility="visible")
fig = get_figure(a0)
st.plotly_chart(fig, use_container_width=False)

