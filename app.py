import pandas as pd
import streamlit as st

# Set up file paths for historical and today's data
history_file = "History.xlsx"
today_file = 'Today.xlsx'

# Streamlit UI title
st.title('Data Comparison: History vs Today')

# Input for the lower and upper limits
lower_limit = st.number_input('Enter the lower limit for CLOSE_history:', min_value=0, max_value=1000, value=10)
upper_limit = st.number_input('Enter the upper limit for CLOSE_today:', min_value=0, max_value=1000, value=100)

# Attempt to read the data, handle file-related errors
try:
    # Read historical data from Excel
    data = pd.read_excel(history_file)
    df = pd.DataFrame(data)

    # Read today's data from the second sheet
    df_today = pd.read_excel(today_file, sheet_name='Sheet1')

    # Merge the historical and today's data on 'Name'
    merged_df = pd.merge(df, df_today, on='Name', suffixes=('_history', '_today'))

    # Filter the data based on user input for the limits
    filtered_df = merged_df[(merged_df['CLOSE_history'] <= lower_limit) & (merged_df['CLOSE_today'] >= upper_limit)]

    # Display the filtered dataframe without styling first
    st.header(f'Filtered Data (CLOSE_history <= {lower_limit} and CLOSE_today >= {upper_limit})')
    st.dataframe(filtered_df)  # Display the filtered data as-is

    # Apply styling to the filtered data and display using st.write()
    st.header('Styled Filtered Data')
    st.write(filtered_df.style.background_gradient(cmap='Greens').format(precision=2).to_html(), unsafe_allow_html=True)

except FileNotFoundError as e:
    st.write("File not found. Please check the file path:", e)
except Exception as e:
    st.write("An error occurred while processing the data:", e)

# End of the report
st.write("End of Report")
