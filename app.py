import streamlit as st


st.set_page_config(
    page_title="AI Student Predictor",
    page_icon="🎓",
    layout="centered"
)



# ================= STYLE =================


st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background:#f8fafc;
}


.main-title{

background:linear-gradient(90deg,#2563eb,#7c3aed);

padding:30px;

border-radius:20px;

color:white;

text-align:center;

font-size:40px;

font-weight:800;

}


.subtitle{

text-align:center;

color:#475569;

font-size:20px;

margin-top:10px;

}


div.stButton > button{

width:100%;

height:50px;

border-radius:12px;

font-size:18px;

font-weight:bold;

}

</style>
""",
unsafe_allow_html=True)




# ================= HEADER =================


st.markdown(
"""
<div class="main-title">

🎓 AI Student Performance Predictor

</div>
""",
unsafe_allow_html=True
)



st.markdown(
"""
<div class="subtitle">

Machine Learning Based Student Success Analysis System

</div>
""",
unsafe_allow_html=True
)



st.write("")

st.divider()



# ================= SIDEBAR =================


with st.sidebar:


    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=100
    )


    st.title("🎓 AI Predictor")


    st.markdown(
"""
### 📌 Project Details


**Objective**

Predict student academic performance
using Artificial Intelligence.


**Supported Students**

✅ 10th Standard

✅ Intermediate

✅ B.Tech


**Algorithm**

🌲 Random Forest Regression


**Input Factors**

📚 Study Hours

📝 Academic Score

✍️ Practice Hours

😴 Sleep

📱 Mobile Usage


**Technology**

🐍 Python

🤖 Machine Learning

🎨 Streamlit

"""
)


    st.divider()


    st.markdown(
"""
### 🤖 AI Workflow


1️⃣ Collect Student Details


2️⃣ Analyze Learning Behaviour


3️⃣ Apply ML Model


4️⃣ Generate Performance Report


"""
)


    st.info(
        "AI Based Academic Analysis System"
    )




# ================= STUDENT DETAILS =================


st.subheader(
    "👤 Student Information"
)



name = st.text_input(
    "Enter Student Name"
)



education = st.selectbox(
    "🎓 Select Education Level",

    [
        "10th Standard",
        "Intermediate",
        "B.Tech"
    ]
)



# ================= BOARD =================


if education == "10th Standard":


    board = st.selectbox(

        "🏫 Select Board",

        [
            "CBSE",
            "ICSE",
            "State Board",
            "Other"
        ]

    )


elif education == "Intermediate":


    board = st.selectbox(

        "🏫 Select Board",

        [
            "State Board",
            "CBSE",
            "Other"
        ]

    )


else:


    board = st.selectbox(

        "🏛️ Select University",

        [
            "JNTU",
            "Autonomous University",
            "Other University"
        ]

    )




# ================= ACADEMIC DETAILS =================


st.subheader(
    "📚 Academic Details"
)



cgpa = None



if education == "B.Tech":


    cgpa = st.number_input(

        "🎯 Enter CGPA",

        min_value=0.0,

        max_value=10.0,

        value=0.0,

        step=0.1

    )


    previous = cgpa * 9.5



    if cgpa > 0:

        st.success(

            f"Converted Percentage: {previous:.2f}%"

        )



else:


    col1,col2 = st.columns(2)



    with col1:


        obtained = st.number_input(

            "📝 Obtained Marks",

            min_value=0,

            value=0

        )



    with col2:


        maximum = st.number_input(

            "📊 Maximum Marks",

            min_value=1,

            value=100

        )



    previous = 0



    if obtained > 0:


        previous = (

            obtained / maximum

        ) * 100



        st.success(

            f"Calculated Percentage: {previous:.2f}%"

        )




# ================= LEARNING HABITS =================


st.subheader(
    "📊 Learning Habits"
)



col1,col2 = st.columns(2)



with col1:


    study = st.number_input(

        "📚 Study Hours / Day",

        min_value=0.0,

        max_value=15.0,

        value=0.0,

        step=0.5

    )



    practice = st.number_input(

        "✍️ Practice Hours / Day",

        min_value=0.0,

        max_value=15.0,

        value=0.0,

        step=0.5

    )




with col2:


    sleep = st.number_input(

        "😴 Sleep Hours / Day",

        min_value=0.0,

        max_value=12.0,

        value=0.0,

        step=0.5

    )



    mobile = st.number_input(

        "📱 Mobile Usage Hours / Day",

        min_value=0.0,

        max_value=12.0,

        value=0.0,

        step=0.5

    )




st.write("")



# ================= BUTTON =================



if st.button(

    "🚀 Generate AI Performance Report"

):


    if (

        name.strip()=="" or

        previous==0 or

        study==0 or

        practice==0 or

        sleep==0 or

        mobile==0

    ):


        st.error(

            "⚠️ Please fill all details"

        )



    else:



        st.session_state.student = {


            "name": name,


            "education": education,


            "board": board,


            "previous": previous,


            "cgpa": cgpa,


            "study": study,


            "practice": practice,


            "sleep": sleep,


            "mobile": mobile


        }




        st.success(

            "✅ Analysis Completed! Opening Dashboard..."

        )



        st.switch_page("pages/result.py")