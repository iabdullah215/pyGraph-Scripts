import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 
import matplotlib.colors as mcolors  # For color interpolation 

# Example data 
x = np.array(['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', 
              '2017', '2018', '2019', '2020']) 
y = np.array([12.4, 29.97, 48.17, 82.62, 165.81, 308.96, 452.93, 580.40, 702.06, 
              812.67, 894.77, 914.02]) 

# Check for negative or NaN values in data 
if np.any(np.isnan(y)) or np.any(y < 0): 
    raise ValueError("Data contains NaN or negative values, which is invalid for bar charts.") 

# Create a color gradient from light blue to dark blue with more contrast 
cmap = plt.get_cmap('Blues', len(x))  # A color map with consistent contrast 
colors = [cmap(i / (len(x) - 1)) for i in range(len(x))]  # Adjusted gradient 

# Increase the figure size for more space 
plt.figure(figsize=(10, 6))  # Set a wider and taller figure for better space 

# Create the bar chart with thinner bars 
bar_width = 0.5  # Reduced width for thinner bars 
plt.bar(x, y, color=colors, width=bar_width, zorder=3)  # Higher zorder keeps bars above grid 

# Remove the grid and set y-axis spines and values to invisible 
plt.grid(False)  # Disable the grid 
plt.gca().axes.yaxis.set_visible(False)  # Hide the y-axis values 
plt.gca().spines['left'].set_visible(False)  # Hide the left spine 
plt.gca().spines['top'].set_visible(False)  # Hide the top spine 
plt.gca().spines['right'].set_visible(False)  # Hide the right spine 

# Add values on top of the bars with a larger offset 
for i, value in enumerate(y): 
    plt.text(i, value + 25, f"{value:.2f}", ha='center', va='bottom', fontweight='bold')  # Adjust offset and add value on top 

# Adjust the x-axis labels for better visibility and bold them 
plt.xticks(np.arange(len(x)), x, rotation=0, fontweight='bold')  # Normal (horizontal) rotation with bold font 

# Adjust the margins to prevent label cut-off 
plt.subplots_adjust(bottom=0.2)  # Increase the bottom margin to allow space for labels 

# Set the title 
plt.title('Yearly Growth in Values') 

# Show the chart 
plt.show()
