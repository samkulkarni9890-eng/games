import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("Age-Based Data Explorer")

# Sample Dataset
data = {
    "Age": [22, 25, 30, 35, 40, 28, 32, 45],
    "Salary": [25000, 30000, 40000, 50000, 60000, 35000, 45000, 65000],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT", "HR"]
}

df = pd.DataFrame(data)
print(df)

# Age Slider
age_range = st.slider("Select Age Range", int(df["Age"].min()), int(df["Age"].max()), (20, 50))

# Department Dropdown
dept = st.selectbox("Select Department", ["All"] + list(df["Department"].unique()))

# Filter Data (used only for visualization)
filtered_df = df[(df["Age"] >= age_range[0]) & (df["Age"] <= age_range[1])]

if dept != "All":
    filtered_df = filtered_df[filtered_df["Department"] == dept]

# Boxplot
st.subheader("Salary Distribution by Department")

plt.figure()
sns.boxplot(x="Department", y="Salary", data=filtered_df)
plt.title("Boxplot of Salary by Department")

st.pyplot(plt)