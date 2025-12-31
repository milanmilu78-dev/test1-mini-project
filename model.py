import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("learning_style_data.csv")

X = data.drop("Label", axis=1)
y = data["Label"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Prediction function
def predict_style(inputs):
    return model.predict([inputs])[0]
