import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


from model import predict
from report import create_report



st.set_page_config(
    page_title="AI Performance Dashboard",
    page_icon="📊",
    layout="centered"
)



# ================= SESSION CHECK =================


if "student" not in st.session_state:
    st.session_state.student = {
        "name": "Test User",
        "study": 4,
        "previous": 75,
        "practice": 3,
        "sleep": 7,
        "mobile": 2,
        "education": "B.Tech",
        "board": "JNTU",
        "cgpa": 8.5
    }



student = st.session_state.student



# ================= MODEL INPUT =================


input_data = np.array([

    [

        student["study"],

        student["previous"],

        student["practice"],

        student["sleep"],

        student["mobile"]

    ]

])



score, accuracy = predict(input_data)



# ================= PERFORMANCE =================


if score >= 80:

    performance = "Excellent 🌟"
    risk = "Low Risk 🟢"


elif score >= 60:

    performance = "Good 👍"
    risk = "Medium Risk 🟡"


else:

    performance = "Needs Improvement ⚠️"
    risk = "High Risk 🔴"




# ================= HEADER STYLE =================


st.markdown(
"""
<style>

.header{

background:linear-gradient(90deg,#2563eb,#7c3aed);

padding:30px;

border-radius:20px;

color:white;

text-align:center;

font-size:38px;

font-weight:800;

}

</style>
""",
unsafe_allow_html=True
)




st.markdown(
"""
<div class="header">

📊 AI Student Performance Dashboard

</div>
""",
unsafe_allow_html=True
)



st.write("")



st.success(
f"Welcome {student['name']} 👋"
)




# ================= EDUCATION DETAILS =================


st.subheader(
"🎓 Education Details"
)



col1,col2,col3 = st.columns(3)



with col1:

    st.metric(
        "Education",
        student["education"]
    )



with col2:

    st.metric(
        "Board / University",
        student["board"]
    )



with col3:

    st.metric(
        "Academic Score",
        f"{student['previous']:.2f}%"
    )



if student["education"]=="B.Tech":

    st.info(
        f"🎯 CGPA : {student['cgpa']}"
    )



st.divider()




# ================= RESULT =================


st.subheader(
"🏆 AI Prediction Result"
)



c1,c2,c3,c4 = st.columns(4)



with c1:

    st.metric(
        "🎯 Predicted Score",
        f"{score:.1f}%"
    )



with c2:

    st.metric(
        "Performance",
        performance
    )



with c3:

    st.metric(
        "🤖 Model Accuracy",
        f"{accuracy*100:.1f}%"
    )



with c4:

    st.metric(
        "Risk",
        risk
    )



st.divider()




# ================= GAUGE =================


st.subheader(
"📈 AI Score Analysis"
)



fig = go.Figure(

    go.Indicator(

        mode="gauge+number",

        value=score,

        title={
            "text":"Predicted Performance"
        },

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









# ================= STRENGTHS =================


st.subheader(
"💪 Student Strengths"
)



strengths=[]



if student["previous"] >= 75:

    strengths.append(
        "Strong academic foundation"
    )



if student["practice"] >= 3:

    strengths.append(
        "Good practice habit"
    )



if student["study"] >= 4:

    strengths.append(
        "Good study routine"
    )



if student["sleep"] >= 6:

    strengths.append(
        "Healthy sleep schedule"
    )



if len(strengths)==0:

    strengths.append(
        "Need improvement in learning habits"
    )



for item in strengths:

    st.success(
        "✅ " + item
    )




# ================= AI SUGGESTIONS =================


st.subheader(
"🤖 Personalized AI Suggestions"
)



suggestions=[]



if student["study"] < 4:

    suggestions.append(
        "Increase daily study hours"
    )



if student["practice"] < 3:

    suggestions.append(
        "Increase practice and revision time"
    )



if student["mobile"] > 4:

    suggestions.append(
        "Reduce mobile usage during study"
    )



if student["sleep"] < 6:

    suggestions.append(
        "Maintain proper sleep schedule"
    )



if len(suggestions)==0:

    suggestions.append(
        "Excellent learning habits! Keep maintaining consistency 🔥"
    )



for item in suggestions:

    st.info(item)




# ================= ML EXPLANATION =================


st.divider()


st.subheader(
"🧠 Machine Learning Explanation"
)



st.write(
"""
This system uses **Random Forest Regression** algorithm.

The model analyzes:

✔ Previous Academic Score

✔ Study Hours

✔ Practice Hours

✔ Sleep Pattern

✔ Mobile Usage


Based on student learning behaviour,
AI predicts future performance.
"""
)




# ================= PDF REPORT =================


# ================= PDF REPORT =================

st.divider()
st.subheader("📄 Download Student Report")

if "pdf_ready" not in st.session_state:
    st.session_state.pdf_ready = False
    st.session_state.pdf_file = None
    st.session_state.pdf_name = None   # ✅ add this

if st.button("📄 Generate AI Report"):

    file = create_report(
        student["name"],
        student["education"],
        student["board"],
        student["previous"],
        student["cgpa"],
        score,
        performance,
        suggestions
    )

    with open(file, "rb") as f:
        st.session_state.pdf_file = f.read()

    st.session_state.pdf_name = file   # ✅ dynamic file name
    st.session_state.pdf_ready = True

    st.success("✅ Report Generated Successfully")


# 👇 Always visible after generate
if st.session_state.pdf_ready:

    st.download_button(
        label="⬇ Download AI Report PDF",
        data=st.session_state.pdf_file,
        file_name=st.session_state.pdf_name,  # ✅ IMPORTANT FIX
        mime="application/pdf"
    )
