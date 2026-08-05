import streamlit as st


st.set_page_config(
    page_title="AI Student Predictor",
    page_icon="🎓",
    layout="centered"
)


# ---------------- STYLE ----------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background:#f8fafc;
}


.title{

background:linear-gradient(90deg,#2563eb,#7c3aed);

padding:25px;

border-radius:15px;

color:white;

text-align:center;

font-size:36px;

font-weight:bold;

}


.sub{

text-align:center;

color:#475569;

font-size:18px;

}


div.stButton > button{

width:100%;

height:45px;

border-radius:10px;

font-size:18px;

font-weight:bold;

}


</style>
""",
unsafe_allow_html=True)



# ---------------- HEADER ----------------


st.markdown(
"""
<div class="title">

🎓 AI Student Performance Predictor

</div>
""",
unsafe_allow_html=True
)


st.markdown(
"""
<div class="sub">

Machine Learning Based Student Success Analysis System

</div>
""",
unsafe_allow_html=True
)


st.write("")

st.divider()

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=100
    )

    st.title("🎓 AI Predictor")

    st.write(
        """
        ### Project Details
        
        **Project:**
        AI Student Performance Predictor
        
        **Technology:**
        - Python
        - Machine Learning
        - Streamlit
        
        **Algorithm Used:**
        Random Forest
        
        **Dataset:**
        Student Academic Dataset
        
        **Purpose:**
        Predict student performance and
        provide improvement suggestions.
        """
    )

    st.divider()

    st.info(
        "🤖 AI Based Academic Analysis System"
    )

# ---------------- INPUT ----------------


st.subheader("👤 Student Information")



name = st.text_input(
    "Student Name"
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


    previous = st.number_input(
        "📝 Previous Marks",
        min_value=0,
        max_value=100,
        value=0
    )


    attendance = st.number_input(
        "📅 Attendance %",
        min_value=0,
        max_value=100,
        value=0
    )



with col2:


    sleep = st.number_input(
        "😴 Sleep Hours",
        min_value=0.0,
        max_value=12.0,
        value=0.0,
        step=0.5
    )


    mobile = st.number_input(
        "📱 Mobile Usage Hours",
        min_value=0.0,
        max_value=12.0,
        value=0.0,
        step=0.5
    )



st.write("")


# ---------------- BUTTON ----------------


if st.button(
    "🚀 Analyze Student Performance"
):


    if (
        name=="" or
        study==0 or
        previous==0 or
        attendance==0 or
        sleep==0 or
        mobile==0
    ):


        st.error(
            "⚠️ Please fill all student details"
        )


    else:


        st.session_state.student={

            "name":name,

            "study":study,

            "previous":previous,

            "attendance":attendance,

            "sleep":sleep,

            "mobile":mobile
        }



        st.success(
            "Analysis completed! Opening dashboard..."
        )


        st.switch_page(
            "pages/result.py"
        )