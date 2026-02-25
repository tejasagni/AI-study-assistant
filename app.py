import streamlit as st
import pandas as pd
import plotly.express as px

from analysis import analyze_data
from insights import generate_insight
from report import create_report

st.title("AI Study Assistant Dashboard")

file = st.file_uploader("Upload Student CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    subject_avg, topper, weakest, df = analyze_data(df)

    st.subheader("Data Preview")
    st.dataframe(df)

    st.subheader("Subject Averages")
    fig = px.bar(subject_avg, title="Average Marks per Subject")
    st.plotly_chart(fig)

    st.success(f"Topper: {topper}")
    st.warning(f"Weakest Subject: {weakest}")

    st.subheader("Student Feedback")

    student = st.selectbox("Select Student", df['Name'])

    row = df[df['Name']==student].iloc[0]
    insight = generate_insight(row)

    st.write(insight)

    if st.button("Generate PDF Report"):
        file_name = create_report(student, insight)
        with open(file_name, "rb") as f:
            st.download_button("Download Report", f, file_name)