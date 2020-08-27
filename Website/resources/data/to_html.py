import pandas as pd

data = pd.read_csv("weather_df.csv")
data = data[["City", "Latitude", "Longitude", "Max_Temp", "Humidity", "Cloudiness", "Description", "Wind_Speed", "Country", "Date"]]
data.to_html("weather_data.html")