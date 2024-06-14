import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# Data
x = np.array(['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', 
              '2017', '2018', '2019', '2020'])
y = np.array([12.4, 29.97, 48.17, 82.62, 165.81, 308.96, 452.93, 580.40, 
              702.06, 812.67, 894.77, 914.02])

# Custom color map
colors = cm.viridis(np.linspace(0, 1, len(x)))

# Plot
fig, ax = plt.subplots(figsize=(14, 8))

# Bar graph with a custom color gradient and smaller bar width
bars = ax.bar(x, y, color=colors, edgecolor='black', linewidth=0.6, width=0.4)

# Add value labels on each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),  # 5 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')

# Add dots on each bar and line connecting them with a matching color
line_color = 'darkorange'
ax.plot(x, y, 'o-', color=line_color, markersize=8, label='Value Each Year')

# Create a gradient patch for the legend
gradient_patch = Patch(facecolor='black', edgecolor='black', label='Yearly Distribution')

# Improved legend with custom markers
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Value Each Year', markerfacecolor=line_color, markersize=10),
    Patch(facecolor=colors[0], edgecolor='black', label='Start of the year gradient'),
    Patch(facecolor=colors[-1], edgecolor='black', label='End of the year gradient')
]
ax.legend(handles=legend_elements, loc='upper left', frameon=True, framealpha=0.9, facecolor='white', edgecolor='black')

# Add finer gridlines
ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

# Add minor ticks for a finer grid
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', linewidth=0.5, color='grey', alpha=0.5)

# Remove top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Labels and title
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Value', fontsize=14, fontweight='bold')
ax.set_title('Yearly Distribution with Values Marked', fontsize=16, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
