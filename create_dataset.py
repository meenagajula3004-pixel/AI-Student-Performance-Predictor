import pandas as pd
import random


data=[]


for i in range(1000):

    study = round(random.uniform(1,10),1)

    previous = random.randint(35,100)

    attendance = random.randint(50,100)

    sleep = round(random.uniform(4,9),1)

    mobile = round(random.uniform(0,8),1)


    score = (
        study*5
        + previous*0.4
        + attendance*0.2
        + sleep*2
        - mobile*2
    )


    if score>100:
        score=100


    data.append([
        study,
        previous,
        attendance,
        sleep,
        mobile,
        round(score,2)
    ])



df=pd.DataFrame(
    data,
    columns=[
        "study_hours",
        "previous_marks",
        "attendance",
        "sleep_hours",
        "mobile_usage",
        "final_score"
    ]
)



df.to_csv(
    "student_data.csv",
    index=False
)


print("Dataset Created Successfully")