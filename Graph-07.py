import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.array(['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
              '2017', '2018', '2019', '2020'])
y = np.array([12.4, 29.97, 48.17, 82.62, 165.81, 308.96, 452.93, 580.40, 702.06,
              812.67, 894.77, 914.02])

# Convert years to numeric values for trendline plotting
x_numeric = np.arange(len(x))

# Check for negative or NaN values in data
if np.any(np.isnan(y)) or np.any(y < 0):
    raise ValueError("Data contains NaN or negative values, which is invalid for bar charts.")

# Calculate additional statistics
max_value = np.max(y)
min_value = np.min(y)
average_growth = np.mean(y)

# Define custom colors
bar_color = '#C5E3ED'
trendline_color = '#4783B3'
border_color = '#DCDCDC'

# Increase the figure size for more space
plt.figure(figsize=(12, 8))

# Create the bar chart
bar_width = 0.5
bars = plt.bar(x, y, color=bar_color, width=bar_width, zorder=3)

# Add values on top of the bars
for bar, value in zip(bars, y):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10, f"{value:.2f}",
             ha='center', va='bottom', fontsize=10, fontweight='normal')

# Create mountain-type trendline (zigzag)
plt.plot(x, y, color=trendline_color, linestyle='-', linewidth=2, marker='o', markersize=6, zorder=4)

# Set titles and labels
plt.title('Yearly Growth in Values', fontsize=14, fontweight='bold')
plt.ylabel('Values', fontsize=12, fontweight='bold')
plt.xticks(rotation=0, fontsize=11, fontweight='bold')
plt.yticks(fontsize=12)

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Customize border (spine) color
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_edgecolor(border_color)
    spine.set_linewidth(1.5)

plt.subplots_adjust(bottom=0.2)

# Create custom legend-like box with key statistics
legend_elements = [
    plt.Line2D([0], [0], marker='s', color='w', label=f'Max Value: {max_value:.2f}',
               markerfacecolor=bar_color, markersize=15),
    plt.Line2D([0], [0], marker='s', color='w', label=f'Average Growth: {average_growth:.2f}',
               markerfacecolor=bar_color, markersize=15),
    plt.Line2D([0], [0], marker='s', color='w', label=f'Min Value: {min_value:.2f}',
               markerfacecolor=bar_color, markersize=15),
    plt.Line2D([0], [0], color=trendline_color, linestyle='-', linewidth=2, marker='o', markersize=6, label='Trendline')
]

# Place the legend elements on the plot
plt.legend(handles=legend_elements, loc='upper left', fontsize=10, bbox_to_anchor=(0.05, 0.95))

# Save and show the figure
plt.savefig('yearly_growth_with_custom_colors_and_border.png', bbox_inches='tight')
plt.show()
