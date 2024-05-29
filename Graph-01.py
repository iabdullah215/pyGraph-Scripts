import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.interpolate import make_interp_spline # For smoothing
# Example data
x = np.array(['Private Sectors', 'Government', 'Government & Private Sectors',
'Military', 'Private Sectors & Government', 'Civil Society', 'Government & Civil 
Society'])
y = np.array([196, 170, 61, 29, 20, 112, 30])
# Use the Oranges colormap for a gradient effect
colors = cm.Oranges(y / y.max())
# Increase the figure size for more space
plt.figure(figsize=(10, 6)) # Wider and taller figure
# Create the bar chart with thinner bars
bar_width = 0.5 # Reduced width for thinner bars
plt.bar(x, y, color=colors, width=bar_width, zorder=3) # Bars with higher zorder
# Add a grid to the background with a lower zorder
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray',
alpha=0.7, zorder=1)
# Smooth the line using interpolation
x_numeric = np.arange(len(x))
x_smooth = np.linspace(x_numeric.min(), x_numeric.max(), 300) # More points for 
smooth line
spline = make_interp_spline(x_numeric, y) # Spline to smooth the line
y_smooth = spline(x_smooth)
# Plot the smoothed dotted line through the peaks with orange
plt.plot(x_smooth, y_smooth, color='darkorange', linestyle=':', linewidth=2,
zorder=4) # Dotted line for smooth peaks
plt.scatter(x_numeric, y, color='darkorange', zorder=4) # Scatter plot for the 
actual points
# Adjust the x-axis labels for better visibility
plt.xticks(x_numeric, x, rotation=45, ha='right', rotation_mode='anchor') # 
Rotate labels, align them to the right
# Adjust the margins to prevent label cut-off
plt.subplots_adjust(bottom=0.2) # Increase bottom margin to give space for 
labels
# Set the title
plt.title('Top Affected Sectors')
# Show the chart
plt.show()
