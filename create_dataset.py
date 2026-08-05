import pandas as pd
import numpy as np



# Random seed

np.random.seed(42)



# Number of students

students = 5000



# ================= FEATURES =================


study_hours = np.round(
    np.random.uniform(0,12,students),
    1
)



previous_marks = np.round(
    np.random.uniform(35,100,students),
    1
)



practice_hours = np.round(
    np.random.uniform(0,8,students),
    1
)



sleep_hours = np.round(
    np.random.uniform(4,10,students),
    1
)



mobile_usage = np.round(
    np.random.uniform(0,10,students),
    1
)




# ================= SCORE LOGIC =================


final_score = (

    (previous_marks * 0.35)

    +

    (study_hours * 4)

    +

    (practice_hours * 5)

    +

    (sleep_hours * 2)

    -

    (mobile_usage * 3)

)



# Add small real-world variation

noise = np.random.normal(
    0,
    5,
    students
)


final_score = final_score + noise



# Limit between 0-100

final_score = np.clip(
    final_score,
    0,
    100
)



final_score = np.round(
    final_score,
    2
)




# ================= DATAFRAME =================


data = pd.DataFrame({


    "study_hours":study_hours,


    "previous_marks":previous_marks,


    "practice_hours":practice_hours,


    "sleep_hours":sleep_hours,


    "mobile_usage":mobile_usage,


    "final_score":final_score


})




# Save CSV


data.to_csv(

    "student_data.csv",

    index=False

)



print(
    "✅ 5000 Student Dataset Created Successfully"
)


print(
    data.head()
)