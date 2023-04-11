
import streamlit as st
import plotly.graph_objects as go
import numpy as np

def get_figure(eps, N):
        
    visible = True
    Nmax = 29
    
    # Create figure
    fig = go.Figure(layout_yaxis_range=[-.2,3],
                    layout_xaxis_range=[-.2,25])

    # Band lower line
    fig.add_trace(
        go.Scatter
        (
            x=[0, Nmax], 
            y=[2-eps, 2-eps], 
            fill=None, 
            mode='lines',
            line_color='rgba(94,192,231,255)',
            visible=visible, 
            showlegend=False
        )
    )
    
    # Band upper line
    fig.add_trace(go.Scatter(
        x=[0, Nmax], 
            y=[2+eps, 2+eps],
            fill='tonexty', # fill area between trace0 and trace1
            mode='lines', 
            line_color='rgba(94,192,231,255)',
            visible=visible,
            showlegend=False        
        )
    )

    # Limit line
    fig.add_trace(
        go.Scatter
        (
            visible=visible,
            mode = 'lines',
            line = {'dash':'dash', 'color':'white', 'width':1},
            x=[0,Nmax],
            y=[2,2],
            hoverinfo = 'skip',
            showlegend=False
        )
    )
    
    # Vectical dashed line at x=N     
    fig.add_trace(
        go.Scatter
        (
            visible=visible,
            mode = 'lines',
            line = {'dash':'dot', 'color':'rgba(94,192,231,255)','width':1},
            x=[N,N],
            y=[0, 2*(1-np.exp(-N/5))],
            hoverinfo = 'skip',
            showlegend=False
        )
    )
    
    # Text "N"
    fig.add_trace(
        go.Scatter
        (
             x=[N],
             y=[-0.15],
             mode='text',
             text="<b>N</b>",
             textfont = dict(size=18, color='rgba(94,192,231,255)'),
             showlegend=False,        
             visible=visible)
    )


    # Text epsilon
    fig.add_trace(
        go.Scatter
        (
             x=[3,3],
             y=[2-eps/2,2+eps/2],
             mode='text',
             text=['ε','ε'],
             textfont = dict(size=18, color='rgba(94,192,231,255)'),
             showlegend=False,        
             visible=visible)
    )
    
    
    # Arrows 
    fig.add_trace(go.Scatter(x=[2,2],y=[2,2+eps],mode="lines+markers",line_color='rgba(94,192,231,255)',
            marker=dict(symbol="arrow",size=10,angleref="previous"),
            showlegend=False, visible=visible))
    fig.add_trace(go.Scatter(x=[2,2],y=[2+eps,2],mode="lines+markers",line_color='rgba(94,192,231,255)',
            marker=dict(symbol="arrow",size=10,angleref="previous"),
            showlegend=False, visible=visible))
    fig.add_trace(go.Scatter(x=[2,2],y=[2-eps,2],mode="lines+markers",line_color='rgba(94,192,231,255)',
            marker=dict(symbol="arrow",size=10,angleref="previous"),
            showlegend=False, visible=visible))
    fig.add_trace(go.Scatter(x=[2,2],y=[2,2-eps],mode="lines+markers",line_color='rgba(94,192,231,255)',
            marker=dict(symbol="arrow",size=10,angleref="previous"),
            showlegend=False, visible=visible))

    
    # The curve
    x = np.arange(0, Nmax, 1)

    fig.add_trace(
        go.Scatter(
            visible=True,
            mode='markers',
            marker= {'color':'rgba(110,170,70,255)','size':10},
            x=x,
            y=2*(1-np.exp(-x/5)),
            hoverinfo = 'skip',
            showlegend=False

        )
    )
    
    
    N0 = int(-5*np.log(eps/2))+1
    title = "This is a good value for N. All points after N are inside the strip"
    title_color ='rgba(110,170,70,255)'
    
    if N0>N:
        xred = np.arange(N, N0, 1)
        fig.add_trace(
            go.Scatter(
                visible=True,
                mode='markers',
#                 marker= {'color':'rgba(255,0,0,255)','size':10},
                x=xred,
                y=2*(1-np.exp(-xred/5)),
                hoverinfo = 'skip',
                showlegend=False

            )
        )
        
        title = "This is NOT a good value for N. Points in red are outside the strip."
#         title_color = 'rgba(255,0,0,255)'

    fig.update_layout(title = title,   title_font_color=title_color)
    
    return fig

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown("<h1 style='text-align: center;'>Finite limit of a real sequence</h1>", unsafe_allow_html=True)
st.markdown("""---""")
st.markdown("<h3 style='text-align: left;'>Instructions</h3>", unsafe_allow_html=True)
st.markdown("(1) Use the first slider to change the value of ε", unsafe_allow_html=True)
st.markdown("(2) For each chosen value of ε, adjust N with the second slider to obtain a good value", unsafe_allow_html=True)
st.markdown("A good value of N is one such that all terms with indices greater than N are inside the strip of center 2 and radius ε", unsafe_allow_html=True)
st.markdown("""---""")
eps = st.slider("epsilon", min_value=0.01, max_value=1., value=.5, step=.01, disabled=False, label_visibility="visible")
N = st.slider("N", min_value=1, max_value=30, value=5, step=1, disabled=False, label_visibility="visible")
fig = get_figure(eps,N)
st.plotly_chart(fig, use_container_width=False, on_change=get_figure)





