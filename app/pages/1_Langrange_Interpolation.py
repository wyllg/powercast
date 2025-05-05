import sqlite3
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objs as go

# Lagrange interpolation function
def lagrange_interpolation(x, y, x_values):
    result = np.zeros_like(x_values)
    n = len(x)
    
    for i in range(n):
        term = np.ones_like(x_values)
        for j in range(n):
            if i != j:
                term *= (x_values - x[j]) / (x[i] - x[j])
        result += term * y[i]
    
    return result

# Streamlit app setup
st.set_page_config(page_title="Interpolation", page_icon="📈")
st.markdown("# Lagrange Interpolation")

# Sidebar
st.sidebar.header("Choose a Year")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

# Years list
years = [str(year) for year in range(2023, 2009, -1)]

# Year selection in sidebar
with st.sidebar:
    selected_year = st.radio("Select a Year", years)

# Save selected year to session_state
st.session_state['selected_year'] = selected_year

# Display selected year
st.subheader(f"Selected Year: {selected_year}")

# Connect to database
conn = sqlite3.connect('data/database.db')  # Make sure it's database.db

# --- Correct Query ---
query = "SELECT * FROM electricitydb WHERE Month LIKE ?"
df = pd.read_sql_query(query, conn, params=(f"{selected_year}%",))

# Show data
if not df.empty:
    
    # Extract Month and electricity values for interpolation
    months = pd.to_datetime(df['Month'], format='%Y-%m').dt.month.values
    electricity = df['all fuels (utility-scale) thousand megawatthours'].values  # Adjust this column name if needed

    # Perform Lagrange interpolation
    x_values = np.linspace(min(months), max(months), 100)
    y_values = lagrange_interpolation(months, electricity, x_values)

    # Plot the data and interpolation
    fig = go.Figure()

    # Original data
    fig.add_trace(go.Scatter(x=months, y=electricity, mode='markers', name='Original Data', marker=dict(color='blue')))

    # Interpolated curve
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name='Lagrange Interpolation', line=dict(color='red')))

    # Update plot layout
    fig.update_layout(
        title=f"Lagrange Interpolation for {selected_year}",
        xaxis_title="Month",
        yaxis_title="Electricity Usage",
        showlegend=True
    )

    # Display the plot
    st.plotly_chart(fig)

    st.dataframe(df)
else:
    st.warning(f"No data found for the year {selected_year}.")

conn.close()
