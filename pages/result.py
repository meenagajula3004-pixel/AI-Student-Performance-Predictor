import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from model import predict
from report import create_report


st.set_page_config(
    page_title="Performance Dashboard",
    page_icon="📊",
    layout="centered"
)


if "student" not in st.session_state:
    st.warning("Please enter student details first")
    st.stop()


student = st.session_state.student


input_data = np.array([[
    student["study"],
    student["previous"],
    student["attendance"],
    student["sleep"],
    student["mobile"]
]])


score, accuracy = predict(input_data)


if score >= 80:
    performance = "Excellent 🌟"

elif score >= 60:
    performance = "Good 👍"

else:
    performance = "Needs Improvement ⚠️"



st.markdown(
"""
<style>

.title{
background:linear-gradient(90deg,#2563eb,#7c3aed);
padding:20px;
border-radius:15px;
color:white;
text-align:center;
font-size:32px;
font-weight:bold;
}

</style>
""",
unsafe_allow_html=True
)



st.markdown(
"""
<div class="title">
📊 Student Performance Report
</div>
""",
unsafe_allow_html=True
)


st.write("")

st.success(
f"Welcome {student['name']} 👋"
)



# Main Cards

col1,col2,col3 = st.columns(3)


with col1:
    st.metric(
        "🎯 Score",
        f"{score:.1f}%"
    )


with col2:
    st.metric(
        "🏆 Level",
        performance
    )


with col3:
    st.metric(
        "🤖 Accuracy",
        f"{accuracy*100:.1f}%"
    )



st.divider()



# Gauge

st.subheader("Performance Level")


fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=score,
        gauge={
            "axis":{
                "range":[0,100]
            }
        }
    )
)


st.plotly_chart(
    fig,
    use_container_width=True
)



# Simple Analysis

st.subheader("📈 Student Analysis")


chart = pd.DataFrame({

    "Category":[
        "Study",
        "Attendance",
        "Sleep",
        "Mobile"
    ],

    "Value":[
        student["study"],
        student["attendance"],
        student["sleep"],
        student["mobile"]
    ]

})


st.bar_chart(
    chart.set_index("Category")
)



# Suggestions

st.subheader("🤖 AI Suggestions")


suggestions=[]


if student["study"] < 4:
    suggestions.append("Increase study hours")

if student["attendance"] < 75:
    suggestions.append("Improve attendance")

if student["mobile"] > 4:
    suggestions.append("Reduce mobile usage")

if student["sleep"] < 6:
    suggestions.append("Maintain proper sleep")


if len(suggestions)==0:
    suggestions.append(
        "Excellent routine! Keep maintaining consistency 🔥"
    )


for s in suggestions:
    st.info(s)



st.divider()



# PDF

if st.button("📄 Generate Report"):

    file=create_report(
        student["name"],
        score,
        performance,
        suggestions
    )


    with open(file,"rb") as f:

        st.download_button(
            "⬇ Download PDF",
            f,
            file_name="Student_Report.pdf"
        )