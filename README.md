# PROGRAMMING-FOR-DATA-ANALYTICS
# CONTAINS ASSIGNMENTS AND PROJECT 

# PROJECT
1. Cleans and normalizes historical wind data.

2. Converts wind speeds from knots → m/s.

3. Computes theoretical wind power for a turbine with a 50m rotor.

4. Resamples daily, monthly, and yearly averages.

5. Plots daily, monthly, and yearly trends.

6. Performs a simple linear trend analysis to see if wind power is increasing/decreasing over decades.

7. Provides summary statistics for wind speed and power.

"Specialized machines

Upwind turbines face into the wind, while downwind turbines face away. Some of the new generation of wind turbines can work at lower wind speeds, generally about five miles per hour. However these turbines are generally smaller, don’t generate as much energy, and are not designed to withstand higher wind ranges.

Most of what you would call large-scale wind turbines typically start turning in winds of seven to nine miles per hour. Their top speeds are around 50-55 mph, which is their upper safety limit. Large-scale wind turbines normally have a braking system that kicks in around 55 mph to prevent damage to the blades.

Ironically, many industrial-scale wind turbines require an electric 'kick-start' to begin turning. That’s what overcomes the inertia of getting the blades to start turning."


"Producing power

You might think that once the blades are turning, electricity is being generated.

But that’s not quite true, because the blades aren’t turning fast enough.

The blades are connected to a shaft that turns at between 30 to 60 rotations per minute. The shaft then connects to a gear box that increases the rotation speed from 1000 to 1800 rotations per minute, which is the speed required by most generators to produce electricity.

Of course, the amount of electricity a wind turbine generates depends on the size of the turbine, also known as the power rating, and how fast the wind is traveling at the turbine’s location. Wind turbines have a power rating usually ranging from 250 watts (enough to charge a battery) to 10 kilowatts (enough to power a house) to six megawatts (enough to power more than 1600 houses)."

Reference: pbs north Carolina, https://www.pbsnc.org/blogs/science/how-much-wind-does-a-wind-turbine-need/ accessed 11th of January 2026.


Typical income from wind turbines 

An 800kW turbine working at rated output would generate 7 million kWh per year if the wind blows continuously at the speed required to give the rated output.

Obviously, this will not always happen. The actual output would normally be in the order of 30% of the theoretical maximum. The wind allows the turbine to produce its rated output over 30% of the year, giving 2.1 million kWh for the 800kW machine per year.

Reference :Teagasc https://teagasc.ie/rural-economy/rural-development/diversification/wind-energy/ accessed 11 of January 2026.


# From above plots the figures would support the viability of a wind farm using the Requirement found : https://www.pbsnc.org/blogs/science/how-much-wind-does-a-wind-turbine-need/ and https://teagasc.ie/rural-economy/rural-development/diversification/wind-energy/

# "A medium-sized commercial scale turbine for a farm in Ireland may have a tower height of 50m and a rotor diameter of 48m, giving a tip height of 74m, and a rated power output of 800kW."

# "The actual output would normally be in the order of 30% of the theoretical maximum. The wind allows the turbine to produce its rated output over 30% of the year, giving 2.1 million kWh for the 800kW machine per year."

# with the above information and the plot above it shows that the average Power produced by the wind at this location over the year would be at max for the medium sized comercial turbine. with the power output being 800kw at max and that being the max output for only 30% of the year , the figures show that it would be viable .

# from this plot we can see the power values lowering over the years , so we will need to do some trend analysis to try and predict the next 10 years.

As seen above the the estimated trend from historic data predicts the annual decrease of -0.65 kw a year .
this wouls still be viable for the next 10 years as it would still make the required power needs , but may be issues after the 10 year mark if the estimations are correct.