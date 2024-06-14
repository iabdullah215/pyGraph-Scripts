import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm  # Missing import for cm
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# Data
attack_types = ['Espionage', 'Sabotage', 'DoS', 'Data Destruction', 'Financial Theft']
attack_values = [876, 669, 585, 398, 352]

# Custom color map
colors = cm.viridis(np.linspace(0, 1, len(attack_types)))

# Plot
fig, ax = plt.subplots(figsize=(14, 8))

# Bar graph with custom color gradient and smaller bar width
bars = ax.bar(attack_types, attack_values, color=colors, edgecolor='black', linewidth=0.6, width=0.4)

# Add value labels on each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),  # 5 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')

# Add dots on each bar and line connecting them with a matching color
line_color = 'darkorange'
ax.plot(attack_types, attack_values, 'o-', color=line_color, markersize=8, label='Value Each Attack')

# Custom legend
legend_elements = [Patch(facecolor=color, edgecolor='black', label=attack) for color, attack in zip(colors, attack_types)]
line_legend = Line2D([0], [0], marker='o', color='w', label='Value Each Attack', markerfacecolor=line_color, markersize=10)
ax.legend(handles=[line_legend] + legend_elements, loc='upper right', frameon=True, framealpha=0.9, facecolor='white', edgecolor='black')

# Add finer gridlines
ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

# Add minor ticks for a finer grid
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey', alpha=0.5)

# Remove top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Labels and title
ax.set_xlabel('Attack Type', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Attacks', fontsize=14, fontweight='bold')
ax.set_title('Top 5 Types of Attacks', fontsize=16, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
