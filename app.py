import streamlit as st
import pandas as pd

st.title("MSc Application Probability Tool")
st.write("Rank your MSc applications by estimated acceptance probability.")

# Input table
st.header("Enter Your Applications")
st.write("Fill in the details for each program you are applying to:")

# Create empty dataframe for applications
applications = pd.DataFrame(columns=["University", "Program", "Your Background Fit (1-5)", "Funding Availability (1-5)", "Deadline Proximity (1-5)"])

# User input loop
num_apps = st.number_input("How many programs are you evaluating?", min_value=1, step=1)

for i in range(int(num_apps)):
    st.subheader(f"Program {i+1}")
    uni = st.text_input(f"University {i+1}")
    prog = st.text_input(f"Program {i+1}")
    fit = st.slider("Your Background Fit (1-5)", 1, 5)
    fund = st.slider("Funding Availability (1-5)", 1, 5)
    deadline = st.slider("Deadline Proximity (1-5)", 1, 5)
    
    if st.button(f"Add Program {i+1}"):
        applications = applications.append({
            "University": uni,
            "Program": prog,
            "Your Background Fit (1-5)": fit,
            "Funding Availability (1-5)": fund,
            "Deadline Proximity (1-5)": deadline
        }, ignore_index=True)

# Calculate simple score
if not applications.empty:
    applications["Score"] = applications[["Your Background Fit (1-5)", "Funding Availability (1-5)", "Deadline Proximity (1-5)"]].mean(axis=1)
    applications_sorted = applications.sort_values(by="Score", ascending=False)
    
    st.header("Ranked Applications")
    st.table(applications_sorted)