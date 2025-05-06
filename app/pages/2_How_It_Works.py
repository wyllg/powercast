import streamlit as st

# --- Page configuration ---
st.set_page_config(
    page_title="How It Works | Powercast",
    page_icon="🧐",
    layout="centered",
)

# --- Title ---
st.title("⚡ How Lagrange Interpolation Works")

# --- Introduction ---
st.write("""
The Lagrange Interpolation Formula identifies a polynomial known as the Lagrange Polynomial, 
which takes on certain values at any point. It is an nth-degree polynomial expression for the function f(x). 
The interpolation approach is used to identify new data points within a finite collection of known data points.

This technique is useful for predicting missing or intermediate values, 
especially in datasets like electricity production over months!
""")

# Mathematical formula
st.header("Formula Overview")

st.latex(r'''
P(x) = \sum_{i=0}^{n-1} y_i \prod_{\substack{0 \leq j \leq n-1 \\ j \neq i}} \frac{x - x_j}{x_i - x_j}
''')

st.markdown("""
- $P(x)$ is the interpolated value at $x$.
- $y_i$ is the known value at point $x_i$.
""", unsafe_allow_html=True)


# Expanded form
st.header("🔬 Expanded View")

st.latex(r'''
P(x) = y_0 \frac{(x-x_1)\cdots(x-x_n)}{(x_0-x_1)\cdots(x_0-x_n)}
+ y_1 \frac{(x-x_0)\cdots(x-x_n)}{(x_1-x_0)\cdots(x_1-x_n)}
+ \cdots
+ y_n \frac{(x-x_0)\cdots(x-x_{n-1})}{(x_n-x_0)\cdots(x_n-x_{n-1})}
''')

# --- Process ---
st.header("Step-by-Step Process")

st.markdown("""
1. **Select known data points**: $(x_0, y_0), (x_1, y_1), \\dots, (x_n, y_n)$.
2. **Construct Lagrange basis polynomials** 
3. **Multiply each $y_i$** by its corresponding basis polynomial.
4. **Sum** all the terms to get the final interpolated polynomial $P(x)$.
5. **Evaluate** $P(x)$ at the desired point!
""", unsafe_allow_html=True)

