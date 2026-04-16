import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Dynamic Visualization Dashboard")

#  Data
data = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Kiran"],
    "Math": [85, 92, 70, 88, 60],
    "Science": [78, 88, 65, 90, 55],
    "English": [90, 95, 72, 85, 65]
}

df = pd.DataFrame(data)

# Show Data
st.subheader("Dataset")
st.dataframe(df)

# Dropdown for Subject Selection
subject = st.selectbox("Select Subject", ["Math", "Science", "English"])

# Slider for Minimum Marks Filter
min_marks = st.slider("Select Minimum Marks", 0, 100, 50)

# Multiselect for Students
students = st.multiselect("Select Students", df["Name"], default=df["Name"])

# Filter Data
filtered_df = df[(df["Name"].isin(students)) & (df[subject] >= min_marks)]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Chart Type Selection
chart_type = st.selectbox("Select Chart Type", ["Bar", "Line"])

# Plot Chart
st.subheader("Visualization")

plt.figure()

if chart_type == "Bar":
    plt.bar(filtered_df["Name"], filtered_df[subject])
elif chart_type == "Line":
    plt.plot(filtered_df["Name"], filtered_df[subject], marker='o')

plt.xlabel("Students")
plt.ylabel(subject)
plt.title(f"{subject} Marks Visualization")

st.pyplot(plt)