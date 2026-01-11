

# PROGRAMMING-FOR-DATA-ANALYTICS


# PROJECT - Wind Power Analysis in Ireland

The aim of this project is to analyze historical wind data from Met Éireann to evaluate the potential for wind energy generation at a specific location in Ireland. Using long-term observations of wind speed, gusts, and wind direction, we calculate the theoretical wind power that could be harnessed by a modern wind turbine and investigate trends in wind energy over time.

## The objectives of this analysis include:

Data Cleaning and Preparation: Extracting relevant wind data from historical CSV files, converting units from knots to meters per second, and ensuring that all records are in a usable datetime format.

Theoretical Wind Power Calculation: Computing the power output of a wind turbine based on rotor size, air density, and measured wind speeds using the standard wind power formula.

Time Series Analysis: Resampling the data to daily, monthly, and yearly averages to visualize temporal trends in wind power potential.

Trend Projection: Using linear regression to estimate how wind power might change over the next decade, providing insight into long-term energy planning.

Visualization: Plotting the daily, monthly, and yearly trends along with future projections to support data-driven decision-making for wind energy deployment.

This project provides a practical demonstration of how historical meteorological data can be leveraged to assess renewable energy potential and supports strategic planning for sustainable energy infrastructure.

All working, figures and references are in the project notebook

## Summary of Finding :

The plots indicate that a medium-sized commercial wind turbine in Ireland (50 m tower, 48 m rotor, 800 kW rated power) could be viable at this location. Based on industry references, such a turbine typically produces around 30% of its theoretical maximum over the year, yielding approximately 2.1 million kWh annually. The historical data show that average wind power reaches near the turbine’s maximum output only for a portion of the year, supporting the feasibility of a wind farm here. However, the plots also suggest a slight decline in power over the years, highlighting the need for trend analysis to forecast wind power potential over the next decade.

Based on the historical data, the estimated trend indicates an annual decrease of approximately 0.65 kW per year. Despite this decline, the wind farm would remain viable over the next 10 years, meeting the required power needs. However, if the trend continues, there may be potential challenges in maintaining sufficient output beyond the 10-year period.



** all windfarm and turbine stats and information was found from below references: 

Reference :Teagasc https://teagasc.ie/rural-economy/rural-development/diversification/wind-energy/ accessed 11 of January 2026.
Reference: pbs north Carolina, https://www.pbsnc.org/blogs/science/how-much-wind-does-a-wind-turbine-need/ accessed 11th of January 2026.

