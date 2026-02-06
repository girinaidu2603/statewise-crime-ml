import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("cleaned_crime_data.csv")

# Encode categorical data
le_state = LabelEncoder()
le_crime = LabelEncoder()

df['State'] = le_state.fit_transform(df['State'])
df['Crime_Type'] = le_crime.fit_transform(df['Crime_Type'])

X = df[['State', 'Year', 'Crime_Type']]
y = df['Crime_Count']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model Accuracy:", model.score(X_test, y_test))

prediction = model.predict([[5, 2025, 2]])
print("Predicted Crime Count:", int(prediction[0]))
