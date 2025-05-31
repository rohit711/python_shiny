🌍 Python Shiny Gapminder Dashboard

This is an interactive data visualization dashboard built using Python Shiny and Plotly, based on the famous Gapminder dataset. The dashboard allows users to explore the relationship between GDP per capita, life expectancy, and population across different countries and over time.

📊 Features

Year Slider: Select a year to filter the dataset and update all charts.
Country Selector: Dynamically select multiple countries for comparison.
Scatter Plot: Visualizes GDP per capita vs. life expectancy for the selected year.
Time Series: Shows life expectancy over time for the selected countries.
Population Trend: Line chart of population growth over time.
GDP Trend: GDP per capita evolution across years for selected countries.
🚀 Getting Started

Prerequisites
Install the required Python packages:

pip install shiny plotly
Run the App
Save the code to a Python file, e.g., app.py, and run:

shiny run --reload app.py
Then, open your browser and go to the address shown in the terminal (usually http://localhost:8000).

📁 Data Source

This app uses the built-in gapminder dataset from Plotly:

GDP per capita (gdpPercap)
Life Expectancy (lifeExp)
Population (pop)
Country and Continent
Year (1952–2007 in 5-year intervals)
