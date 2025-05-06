import streamlit as st

# --- Page configuration ---
st.set_page_config(
    page_title="Home | Powercast",
    page_icon="⚡",
    layout="centered",
)

# --- Main Page ---

st.title("⚡ Powercast")

st.markdown(
    """
    Welcome to **Powercast** — your interactive dashboard for analyzing and forecasting electricity generation across various energy sources!
    This website provides insights on monthly electricity production across different energy sources from the USA using Lagrange interpolation.
    """
)

st.markdown("---")

st.success("**Select a method from the sidebar to get started.**")

st.markdown("---")

st.subheader("🖥️ Tools and Technologies")

st.markdown(
    """
    Powecast uses a :blue-background[[Kaggle Dataset](https://www.kaggle.com/datasets/sriharshaeedala/electricity-generated-in-us-by-sector)] to gather 
    information about electricity production per sector. The dataset offers insights on energy production, especially the breakdown of
    production from various fuel sources.

    The project uses the following tools and technologies:
    - [Python](https://www.python.org/): Used as the main programming language.
    - [Numpy](https://numpy.org/): Used for its mathematical and scientific computing library.
    - [Streamlit](https://streamlit.io/): Used for frontend due to its ease of use.
    - [Pandas](https://pandas.pydata.org/): Used for database functionality.
    - [Plotly](https://plotly.com/): Used for interactive graphs and plots.
    """
)

# --- Sidebar ---

with st.sidebar:
    st.header("Group Members")
    st.markdown(
        """
        - Shanize Dimaala
        - Wyell Garay
        - Denver Mulingbayan
        - Shanley Velasco
        """
    )

    st.markdown("---")

    st.header("GitHub Repository")
    st.link_button("Powercast", "https://github.com/wyllg/powercast")

    st.markdown("---")