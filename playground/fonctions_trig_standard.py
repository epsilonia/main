
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import datetime

st.set_page_config(layout="wide")

pi = 3.1415926535
def get_figure(M,A,P,T):
        
    visible = True
    
    # Create figure
    fig = go.Figure(layout_yaxis_range=[-2.5,8.5],
                    layout_xaxis_range=[-2,4])

    
    # The curve
    x = np.linspace(-2, 4, 500)

    fig.add_trace(
        go.Scatter(
            x=x,
            y=3+5*np.cos(2*pi/2*(x-.5)),
            mode='lines',
            showlegend=False,
            line=dict(color='red')
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x,
            y=M+A*np.cos(2*pi/P*(x-T)),
            showlegend=False,
            mode='lines',
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[-2,4],
            y=[0,0],
            showlegend=False,
            mode='lines',
            line=dict(color="black")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[0,0],
            y=[-2,8],
            showlegend=False,
            mode='lines',
            line=dict(color="black")
        )
    )
    if (A==5) & (M==3) & (T==.5) & (P==2):
        title = "Bravo!"
        title_color = 'rgba(0,125,0,255)'
    else:
        title = ""
        title_color = 'rgba(0,125,0,255)'


    fig.update_layout(
        title = title,   
        title_font_color=title_color,
        title_font=dict(size=40),
        xaxis=dict(dtick=1, showgrid=True),
        yaxis=dict(dtick=1, showgrid=True)
                )


    return fig


try:
    stats = pd.read_csv('./appstat.csv')
except:
    stats = pd.DataFrame(columns = ['time'])

now = datetime.datetime.now()
st.write(now)
stats.loc[len(stats),'time']=now
stats.to_csv('./appstat.csv',index=False)


st.markdown("<h1 style='text-align: center;'>Forme standard d'une fonction trigonométrique</h1>", unsafe_allow_html=True)
st.markdown("""---""")
st.markdown("<h3 style='text-align: left;'>Instructions</h3>", unsafe_allow_html=True)
st.markdown(r'''La forme standard d'une fonction trigonométrique est $f(t)=M+A\sin \left(\dfrac{2\pi}{P}(t-T)\right)$''')
st.markdown(r'''Les courbes ci-dessous représentent des fonctions trigonométriques sous la forme standard.
Vous pouvez contrôler les paramètres $M$, $A$, $P$ et $T$ de la courbe bleue. L'objectif est d'ajuster ces paramètres pour obtenir la courbe en rouge, sans faire de calcul.''', unsafe_allow_html=True)
st.markdown("""---""")
col1, col2,col3,col4 = st.columns([6,1,6,1])
with col1:
    M = st.slider("M", min_value=0.0, max_value=6., value=.5, step=.1, disabled=False, label_visibility="visible")
    A = st.slider("A", min_value=0.0, max_value=10.0, value=2.0, step=0.1, disabled=False, label_visibility="visible")
    P = st.slider("P", min_value=0.0, max_value=5.0, value=.5, step=0.1, disabled=False, label_visibility="visible")
    T = st.slider("T", min_value=0.0, max_value=1.0, value=.1, step=0.05, disabled=False, label_visibility="visible")
with col3:
    fig = get_figure(M,A,P,T)
    st.plotly_chart(fig, use_container_width=False, on_change=get_figure)





