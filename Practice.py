import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Dataset
# -----------------------------
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 18000, 14000, 22000, 25000],
    "Profit": [2000, 2500, 3000, 1800, 4000, 5000],
    "Expenses": [8000, 9000, 10000, 8500, 12000, 13000],
    "Category": ["A", "B", "A", "C", "B", "C"]
}

df = pd.DataFrame(data)

# Title
st.title("Interactive Sales Dashboard")

# Sidebar Filters

st.sidebar.header("Filter Options")
selected_months = st.sidebar.multiselect(
    "Select Months",
    options=df["Month"].unique(),
    default=df["Month"].unique()
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    options=["All"] + list(df["Category"].unique())
)

sales_threshold = st.sidebar.slider(
    "Minimum Sales Value",
    min_value=int(df["Sales"].min()),
    max_value=int(df["Sales"].max()),
    value=int(df["Sales"].min())
)

# Filtering Data
filtered_df = df[df["Month"].isin(selected_months)]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

filtered_df = filtered_df[filtered_df["Sales"] >= sales_threshold]


# Show Data
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# 1. Line Chart (Sales Trend)

st.subheader("Sales Trend")
fig1, ax1 = plt.subplots()
ax1.plot(filtered_df["Month"], filtered_df["Sales"], marker="o", color="blue")
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")
ax1.set_title("Sales Trend Based on Filters")
st.pyplot(fig1)


# 2. Bar Chart (Profit)

st.subheader("Profit Analysis")
fig2, ax2 = plt.subplots()
ax2.bar(filtered_df["Month"], filtered_df["Profit"], color="orange")
ax2.set_xlabel("Month")
ax2.set_ylabel("Profit")
ax2.set_title("Profit Based on Filters")
st.pyplot(fig2)


# 3. Scatter Plot (Sales vs Expenses)

st.subheader("Sales vs Expenses")
fig3, ax3 = plt.subplots()
ax3.scatter(filtered_df["Sales"], filtered_df["Expenses"], color="green")
ax3.set_xlabel("Sales")
ax3.set_ylabel("Expenses")
ax3.set_title("Relationship Between Sales and Expenses")
st.pyplot(fig3)