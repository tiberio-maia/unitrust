import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st
from urllib.request import urlopen
import json

# Load county GeoJSON data from URL
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Create a GeoDataFrame from the GeoJSON data
gdf = gpd.GeoDataFrame.from_features(counties["features"])

# Load median income data (replace with your own dataset)
# Assume a dictionary with FIPS codes as keys and median income as values
median_income_data = {
    "01001": 54321,
    "01003": 65432,
    # ... (other FIPS codes and median income values)
}

# Add median income data to the GeoDataFrame
gdf["median_income"] = gdf["id"].map(median_income_data)

# Streamlit web app
st.title("US County Median Income Map")

# Show the map using matplotlib and streamlit integration
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
gdf.boundary.plot(ax=ax, linewidth=0.8)
gdf.plot(column="median_income", cmap="YlGnBu", linewidth=0.8, ax=ax, edgecolor="0.8", legend=True)
plt.title("US County Median Income Map")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Display the plot using Streamlit
st.pyplot(fig)

# Optional: Display the median income data as a DataFrame
st.write("Median Income Data:")
st.dataframe(gdf[["id", "median_income"]])
