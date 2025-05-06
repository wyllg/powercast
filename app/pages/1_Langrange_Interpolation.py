import sqlite3
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objs as go


# --- Page configuration ---
st.set_page_config(
    page_title="Lagrange Interpolation",
    page_icon="📈",
    layout="centered",
)

# --- Lagrange interpolation function ---
def lagrange_interpolation(x, y, x_values):

    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    x_values = np.asarray(x_values, dtype=np.float64)
    
    result = np.zeros_like(x_values)
    n = len(x)

    # Compute individual terms of above formula
    for i in range(n):
        term = np.ones_like(x_values)
        for j in range(n):
            if i != j:
                term *= (x_values - x[j]) / (x[i] - x[j])
        result += term * y[i]
    
    return result

# --- Main Page ---
st.title("⚡ Lagrange Interpolation")

st.markdown(
    """
    This page interpolates values of electricity generated based on a given dataset. Choose a year from the sidebar, and choose an energy sector
    from the dropdown below.
    """
)

st.markdown("---")

# --- Sidebar ---
st.sidebar.header("Choose a Year")
years = [str(year) for year in range(2023, 2009, -1)] # Years list
with st.sidebar: 
    selected_year = st.radio("Select a Year", years) # Year selection in sidebar
st.session_state['selected_year'] = selected_year # Save selected year to session_state

# --- Database and Query ---
conn = sqlite3.connect('data/database.db')  # Connect to database
query = "SELECT * FROM electricitydb WHERE Month LIKE ?"
df = pd.read_sql_query(query, conn, params=(f"{selected_year}%",))

# --- Show Data in Main Page ---
if not df.empty:

    # Mapping: Display Name -> Actual Database Column Name
    column_display_names = {
        "All Fuels": "All_Fuels",
        "Coal": "Coal",
        "Gas": "Gas",
        "Nuclear": "Nuclear",
        "Hydroelectric": "Hydroelectric",
        "Wind": "Wind",
    }

    # --- Dropdown Selection ---
    st.subheader(f"Select an Energy Source from {selected_year}")
    selected_display_name = st.selectbox("Energy Sources", list(column_display_names.keys()))

    # After selection, get the real database column name
    selected_column = column_display_names[selected_display_name]

    # Extract Month and electricity values for interpolation
    months = pd.to_datetime(df['Month'], format='%Y-%m').dt.month.values
    electricity = df[selected_column].values

    # Perform Lagrange interpolation
    x_values = np.linspace(min(months), max(months), 100)
    y_values = lagrange_interpolation(months, electricity, x_values)

    # Ploting the data and interpolation
    fig = go.Figure()

    # Original data
    fig.add_trace(go.Scatter(x=months, y=electricity, mode='markers', name='Original Data', marker=dict(color='blue')))

    # Interpolated curve
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name='Lagrange Interpolation', line=dict(color='orange')))

    # Update plot layout
    fig.update_layout(
        title=f"Lagrange Interpolation for {selected_year}",
        xaxis_title="Month",
        yaxis_title="Electricity Usage (MWh)",
        showlegend=True
    )

    # Display the plot
    st.plotly_chart(fig)

    st.markdown("---")

    # Input box for user to enter a value (allowing float inputs)
    st.subheader("Interpolate Specific x Values")
    user_input = st.number_input("Enter a month (1-12) to interpolate:", min_value=1.0, max_value=12.0, step=0.1, format="%.1f")

    # Get the interpolated value for the user input
    if user_input:
        interpolated_value = lagrange_interpolation(months, electricity, np.array([user_input]))
        clean_input = round(user_input, 1)
        clean_output = round(interpolated_value[0], 5)
        st.subheader(f"Result: :orange-background[{clean_output} thousand MWh] (megawatt-hours)")

    st.markdown("---")

    # --- Display Table ---
    st.subheader("Dataset Values")
    if 'index' in df.columns:
        df = df.drop(columns=['index'])
    st.dataframe(df)

    st.markdown("---")

else:
    st.warning(f"No data found for the year {selected_year}.")

conn.close()
