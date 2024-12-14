import pandas as pd
import numpy as np

aqi = pd.read_csv("AQI_Data.csv")
print(aqi)

# Displaying the first 5 rows
print("The first 5 rows")
print(aqi.head(5))

# Displaying last 6 rows

print("The last 6 rows are : ")
print(aqi.tail(6))

# The summary statistics 

print("The summary of the data set is : ")
print(aqi.describe())

# in the csv file of aqi we have same city written at different indexes with different aqi values ,we have to write python code using numpy to calculate average aqi,N02 level,co2 level of cities . 

# using Numpy to compute mean aqi of various cities based on AQI level 
print("\n")

# Get unique cities
unique_cities = np.unique(aqi['City'])

# Initialize arrays to store average values
average_aqi = np.zeros(len(unique_cities))
average_PMtwo = np.zeros(len(unique_cities))
average_PMten = np.zeros(len(unique_cities))

# Calculate average values for each city
for i, city in enumerate(unique_cities):
    city_data = aqi[aqi['City'] == city]
    average_aqi[i] = np.mean(city_data['AQI'])
    average_PMtwo[i] = np.mean(city_data['PM2.5'])
    average_PMten[i] = np.mean(city_data['PM10'])

# Print the average values
print("The average AQI level, PM2.5, PM10 for different cities are listed below :");
for i, city in enumerate(unique_cities):
    print(f'City: {city}, Average AQI: {average_aqi[i]}, Average PM2.5 : {average_PMtwo[i]}, Average PM10 : {average_PMten[i]}')
# Print the average values


# CALCULATING AVERAGE AQI USING DICTIONARY TO CALCULATE CITIES WITH HIGHEST AND LOWEST AVERAGE AQI LEVEL
def calculate_average_aqi(aqi):
    average_aqi = {}
    for city in np.unique(aqi['City']):
        city_aqi_values = aqi[aqi['City'] == city]['AQI']
        average_aqi[city] = np.mean(city_aqi_values)
    return average_aqi

# CALLING THE FUNCTION
print("\n")
average = calculate_average_aqi(aqi)

# EXTRACTING THE HIGHEST AQI AND LOWEST AQI CITY 
print("\n")
highest = max(average, key=average.get)
lowest = min(average, key=average.get)

# PRINTING THE DESIRED OUTPUT
print("City with highest average AQI: ", highest)
print("\n")
print("City with lowest average AQI:", lowest)