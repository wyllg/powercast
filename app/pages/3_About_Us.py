import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="About Us | Powercast",
    page_icon="👩‍🎓",
    layout="centered",
)

# --- Main Content ---
st.title("⚡ About Us")
st.subheader("Meet the Powercast Team")

st.markdown("---")

st.markdown(
    """
    **Powercast** is a project for forecasting electricity generation trends 
    using mathematical interpolation.

    Our goal is to provide an intuitiveand interactive platform to help visualize 
    and predict energy production across different sources.

    ---
    ### Group Members:
    - **Shanize Marie Dimaala**
    - **Wyell Garay**
    - **Denver Marc Mulingbayan**
    - **Shanley Ingrid Velasco**

    ---
    ### Contact Us:
    - GitHub: [Powercast GitHub](https://github.com/wyllg/powercast)
    - Email: garaywyell@gmail.com
    """
)

st.markdown("---")

st.success("Thank you for using Powercast! ⚡")

