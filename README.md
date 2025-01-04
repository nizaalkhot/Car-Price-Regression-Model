# Car-Price-Regression-Model

## Overview
This project focuses on analyzing car specifications and predicting car prices using regression techniques. The dataset includes detailed information about various car models, their performance metrics, engine specifications, and pricing.

### Features
<ul>
<li>**Car Company Names**: The manufacturer or brand of the car.</li>
<li>**Car Models**: The specific name or series of the car.</li>
<li>**Engine Types**: Information on engine specifications.</li>
<li>**CC/Battery Capacity**: Engine displacement in cubic centimeters or battery capacity for electric cars.</li>
<li>**Horsepower (HP)**: The power output of the car's engine or motor.</li>
<li>**Top Speed**: The maximum speed the car can achieve.</li>
<li>**0-100 km/h Performance**: The time it takes for the car to accelerate from 0 to 100 km/h.</li>
<li>**Price (in USD)**: The car's price listed in United States dollars.</li>
<li>**Fuel Type**: Specifies whether the car uses petrol, diesel, electricity, or hybrid fuel systems.</li>
<li>**Seating Capacity**: The number of passengers the car can accommodate.</li>
<li>**Torque**: The rotational force the engine generates.</li>
</ul>

---

## Workflow
The project is divided into three primary steps:

1. **Dataset Loading**  
   The dataset is loaded and saved into the current working directory using the file:  
   [loading_dataset.py](loading_dataset.py)

2. **Data Cleaning and Preprocessing**  
   Performed operations such as renaming columns, handling missing values, standardizing data, and cleaning the dataset in:  
   [Data Cleaning.ipynb](Data Cleaning.ipynb)

3. **Analysis and Visualization**  
   Conducted exploratory data analysis and visualized trends, patterns, and correlations between features using:  
   [Data Analysis and Visualization.ipynb](Data Analysis and Visualization.ipynb)

---

## Analysis and Insights
Key takeaways from the analysis:
1. **Price Drivers**: Horsepower, Top Speed, and Battery Capacity are major contributors to car prices.
2. **Performance vs Price**: Cars with higher performance metrics (e.g., 0-100 km/h acceleration) have significantly higher prices.
3. **Fuel Type Trends**: Petrol remains dominant, but hybrid and electric vehicles are gaining ground.
4. **Brand Analysis**: Luxury brands such as Ferrari and Lamborghini dominate the high-performance and high-price categories.

---

## Installation and Usage
1. Clone the repository:  
   ```bash
   git clone https://github.com/nizaalkhot/Car-Price-Regression-Model.git
