import pandas as pd
import plotly.express as px

df = pd.read_csv("cleaned_crime_data.csv")

# Bar chart: Crime count by state
fig = px.bar(
    df,
    x="State",
    y="Crime_Count",
    color="Crime_Type",
    title="State-wise Crime Distribution"
)

fig.show()

fig = px.choropleth(
    df,
    locations="State",
    locationmode="geojson-id",
    color="Crime_Count",
    hover_name="State",
    animation_frame="Year",
    title="Crime Heatmap of India"
)

fig.show()
