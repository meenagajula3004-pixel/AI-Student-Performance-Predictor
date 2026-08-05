import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error



# ================= LOAD DATASET =================


data = pd.read_csv(
    "student_data.csv"
)



# ================= INPUT FEATURES =================


X = data[

    [

        "study_hours",

        "previous_marks",

        "practice_hours",

        "sleep_hours",

        "mobile_usage"

    ]

]



# Target value

y = data[

    "final_score"

]




# ================= SPLIT DATA =================


X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)




# ================= RANDOM FOREST MODEL =================


model = RandomForestRegressor(

    n_estimators=300,

    max_depth=12,

    random_state=42

)



model.fit(

    X_train,

    y_train

)




# ================= MODEL TEST =================


prediction = model.predict(

    X_test

)



accuracy = r2_score(

    y_test,

    prediction

)



mae = mean_absolute_error(

    y_test,

    prediction

)




# ================= FEATURE IMPORTANCE =================


feature_importance = pd.DataFrame({

    "Feature":

    X.columns,


    "Importance":

    model.feature_importances_

})



feature_importance = feature_importance.sort_values(

    by="Importance",

    ascending=False

)




# ================= PREDICT FUNCTION =================


def predict(input_data):


    score = model.predict(

        input_data

    )[0]



    score = max(

        0,

        min(

            score,

            100

        )

    )


    return score, accuracy




# ================= MODEL INFO =================


def get_model_details():

    return {

        "algorithm":

        "Random Forest Regression",


        "dataset_size":

        len(data),


        "accuracy":

        accuracy,


        "mae":

        mae,


        "features":

        feature_importance

    }