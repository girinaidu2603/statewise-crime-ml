from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("cleaned_crime_data.csv")

@app.route("/")
def home():
    states = df['State'].unique()
    return render_template("index.html", states=states)

@app.route("/dashboard")
def dashboard():
    data = df.to_dict(orient='records')
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
