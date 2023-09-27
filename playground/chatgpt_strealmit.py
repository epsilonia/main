import streamlit as st
import plotly.graph_objs as go

# Define the sequence function that converges to a finite limit L
def sequence(n):
    return 1/n

# Define the function that checks whether the value of N is good or not
def is_good_value_of_n(L, epsilon, N):
    for n in range(1,N):
        if abs(sequence(n) - L) <= epsilon:
            return False
    return True

# Define the function that returns the index N0 starting from which the terms of the sequence are inside the strip
def get_n0(L, epsilon):
    n = 1
    while True:
        if abs(sequence(n) - L) <= epsilon:
            return n
        n += 1

# Set the title of the Streamlit application
st.title("Convergence of Sequence")

# Create sliders for selecting the values of epsilon and N
epsilon = st.slider("Select the value of epsilon:", min_value=0.001, max_value=1.0, value=0.1, step=0.001)
N = st.slider("Select the value of N:", min_value=1, max_value=1000, value=50, step=1)

# Compute the limit of the sequence and the index N0 starting from which the terms of the sequence are inside the strip
L = sequence(1000)
n0 = get_n0(L, epsilon)

# Check whether the value of N is good or not and set the title of the graph accordingly
if is_good_value_of_n(L, epsilon, N):
    title = "This is a good value of N"
    title_color = "green"
else:
    title = "This is NOT a good value of N"
    title_color = "red"

# Create the data for the graph
x = []
y = []
colors = []

for n in range(1, N+1):
    x.append(n)
    y.append(sequence(n))
    if n0 < n <= N and abs(sequence(n) - L) <= epsilon:
        colors.append("red")
    else:
        colors.append("blue")

# Create the trace for the sequence
sequence_trace = go.Scatter(x=x, y=y, mode="markers", marker=dict(color=colors, size=5))

# Create the trace for the strip
strip_trace = go.Scatter(x=[1, N], y=[L - epsilon, L - epsilon], mode="lines", line=dict(color="black", width=1, dash="dash"), name="Strip")

# Create the layout for the graph
layout = go.Layout(title=dict(text=title, font=dict(color=title_color)),
                   xaxis=dict(title="n"),
                   yaxis=dict(title="x_n"))

# Create the figure for the graph
fig = go.Figure(data=[sequence_trace, strip_trace], layout=layout)

# Add the vertical line for N0 to the figure
if n0 <= N:
    fig.add_shape(type="line", x0=n0, x1=n0, y0=0, y1=1, line=dict(color="green", width=1, dash="dash"), name="N0")

# Display the plot using Streamlit
st.plotly_chart(fig)
