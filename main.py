import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt
 
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import (

    classification_report,

    precision_score,

    recall_score,

    f1_score

)

from sklearn.calibration import calibration_curve

import xgboost as xgb
 
# Load penguins dataset

penguins = sns.load_dataset("penguins")
 
# Drop rows with missing values

penguins = penguins.dropna()
 
# Encode categorical variables using a loop

label_cols = ['species', 'island', 'sex']

for col in label_cols:

    penguins[col] = LabelEncoder().fit_transform(penguins[col])
 
# Features and target

X = penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'island', 'sex']]

y = penguins['species']
 
# Split data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# Define and train model

model = xgb.XGBClassifier(random_state=42)
 
# ✅ Saketh's part: Fit the model

model.fit(X_train, y_train)

print("\n✅ Model fitting complete (by Saketh)")
 
# Predict labels and probabilities

y_pred = model.predict(X_test)

y_proba = model.predict_proba(X_test)
 
# Print classification report

print("\nClassification Report:")

print(classification_report(y_test, y_pred))
 
# Print Macro Precision, Recall, F1

precision = precision_score(y_test, y_pred, average='macro')

recall = recall_score(y_test, y_pred, average='macro')

f1 = f1_score(y_test, y_pred, average='macro')
 
print(f"\nMacro Precision: {precision:.2f}")

print(f"Macro Recall: {recall:.2f}")

print(f"Macro F1-score: {f1:.2f}")
 
# Plot calibration curve for class 0

prob_pos_class0 = y_proba[:, 0]

fraction_of_positives, mean_predicted_value = calibration_curve((y_test == 0), prob_pos_class0, n_bins=10)
 
plt.figure(figsize=(6, 6))

plt.plot(mean_predicted_value, fraction_of_positives, "s-", label="Class 0")

plt.plot([0, 1], [0, 1], "--", label="Perfectly calibrated")

plt.xlabel("Mean predicted probability")

plt.ylabel("Fraction of positives")

plt.title("Calibration curve (Class 0)")

plt.legend()

plt.grid()

plt.show()

 