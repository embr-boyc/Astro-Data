# -*- coding: utf-8 -*-
"""Annual Earnings

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X0T2q-_MWDPUx1dILeDjUFbW63a4mxt0
"""

import numpy as np
import matplotlib.pyplot as plt

Income_arr = np.array ([30900, 36700, 39100, 43100, 60800, 75700]) # Extract column data for female income
Education_arr = np.array ([ # X-axis lables
"Less than high school completion",
"High school completion",
"Some college, no degree",
"Associate’s degree",
"Bachelor’s degree",
"Master’s or higher degree"])

plt.plot(Education_arr,Income_arr, "o-", color = "red") # Plotting data points
plt.legend(["Female"]) # Key
plt.xlabel("Education Level") # X-axis label
plt.ylabel("Income [$]") # Y-axis label
plt.xticks(Education_arr, rotation=45, ha="right") # Rotating them so they fit the graph better
plt.show()

Education_numeric = np.arange(len(Education_arr)) # Creating a numerical representation
f_linear = np.polyfit(Education_numeric,Income_arr,1) # Calculating linear fit
print("Slope = ", f_linear[0], " in dollar per level") # Slope of the line
print("Y-intercept = ", f_linear[1], " in dollar at level 0, i.e., Less than high school completion") # Y-intercept of the line

O = Income_arr
O_err = np.array([1910, 500, 2220, 2140, 1540, 2580]) # extract from the same figure with Confidence interval toggled on, and remove the first entry

linear = f_linear[0] * Education_numeric + f_linear[1] # Declaring linear function

Income_arr = np.array ([30900, 36700, 39100, 43100, 60800, 75700]) # Restating data points
Education_arr_numeric = np.arange(len(Income_arr)) # Creating a numerical representation

plt.errorbar(Education_arr_numeric, O, yerr=O_err, marker="o", linestyle = "None", color = "black", label = "Female Data") # Plotting data points
plt.plot(Education_arr_numeric,linear, color = "red", label = "Linear fit") # Graphing line of best fit
plt.legend()
plt.xlabel("Education Level") # X-axis label
plt.ylabel("Income [$]") # Y-axis label
plt.show()