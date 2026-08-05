import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score



# Load Dataset

data = pd.read_csv(
    "student_data.csv"
)



X = data[
[
"study_hours",
"previous_marks",
"attendance",
"sleep_hours",
"mobile_usage"
]
]


y = data["final_score"]



# Split Data

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# Model

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)



model.fit(
    X_train,
    y_train
)



# Accuracy

prediction = model.predict(
    X_test
)


accuracy = r2_score(
    y_test,
    prediction
)



def predict(input_data):

    score = model.predict(
        input_data
    )[0]

    return score, accuracy