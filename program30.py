# NUMPY CODES

import numpy as np
import matplotlib.pyplot as plt

# Input data for the COVID-19 cases as a numpy array
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1
    [1600, 2100, 1900, 1300, 950],  # Day 2
    [1700, 2200, 2000, 1400, 1000],  # Day 3
    [1650, 2150, 1950, 1350, 980],  # Day 4
    [1750, 2250, 2050, 1450, 1020],  # Day 5
    [1800, 2300, 2100, 1500, 1050],  # Day 6
    [1900, 2400, 2200, 1600, 1100]   # Day 7
])

# Task 1: Basic Statistics
# Calculate total cases for each country over 7 days
total_cases_per_country = covid_data.sum(axis=0)

# Determine the country with the highest total cases
highest_total_cases_country = np.argmax(total_cases_per_country)

# Task 2: Daily Analysis
# Calculate the average number of cases reported per day across all countries
average_daily_cases = covid_data.mean(axis=1)

# Identify the day with the highest total cases across all countries
highest_daily_total_cases = np.argmax(covid_data.sum(axis=1))

# Task 3: Trends
# Calculate percentage increase or decrease from Day 1 to Day 7 for each country
percentage_change = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100

# Country with the highest percentage increase
highest_percentage_increase_country = np.argmax(percentage_change)

# Task 4: Data Transformation
# Normalize the data (scale between 0 and 1) for each country
normalized_data = (covid_data - covid_data.min(axis=0)) / (covid_data.max(axis=0) - covid_data.min(axis=0))

# Task 5: Visualization
# Prepare data for visualization
days = np.arange(1, 8)  # Days 1 to 7
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']

# Line chart showing daily cases for each country
plt.figure(figsize=(10, 6))
for i in range(covid_data.shape[1]):
    plt.plot(days, covid_data[:, i], marker='o', label=countries[i])

# Highlight the day with the highest total cases
highest_day = highest_daily_total_cases + 1
highest_day_total = covid_data.sum(axis=1)[highest_daily_total_cases]

plt.axvline(x=highest_day, color='red', linestyle='--', label='Highest Total Cases Day')
plt.scatter([highest_day], [highest_day_total], color='red', zorder=5, label='Highest Day Total')

# Add labels, legend, and title
plt.title('Daily COVID-19 Cases for Each Country')
plt.xlabel('Days')
plt.ylabel('Number of Cases')
plt.xticks(days)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Show the plot
plt.show()

# Print the results
print("Task 1: Basic Statistics")
print("Total cases per country:", total_cases_per_country)
print("Country with highest total cases:", countries[highest_total_cases_country])

print("\nTask 2: Daily Analysis")
print("Average daily cases across all countries:", average_daily_cases)
print("Day with highest total cases:", highest_day)

print("\nTask 3: Trends")
print("Percentage change (Day 1 to Day 7) per country:", percentage_change)
print("Country with highest percentage increase:", countries[highest_percentage_increase_country])

print("\nTask 4: Normalized Data")
print("Normalized dataset:\n", normalized_data)
