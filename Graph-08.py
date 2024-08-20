import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
funding_amount = np.array([73, 39, 287, 116, 417, 365])  # in millions
deal_count = np.array([6, 10, 13, 23, 26, 37])

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Bar plot (Funding amount)
bars1 = ax1.bar(years - 0.2, funding_amount, color='#29b6f6', width=0.4, label='Funding Amount ($M)')
ax1.set_xlabel('Year', fontsize=14, fontweight='bold')
ax1.set_ylabel('Funding Amount ($M)', fontsize=14, fontweight='bold', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_ylim(0, 500)

# Add labels to the bars for funding amount with dollar sign
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 5, f'${yval}M', ha='center', va='bottom', fontsize=12, color='#29b6f6')

# Create a twin y-axis for the deal count
ax2 = ax1.twinx()
bars2 = ax2.bar(years + 0.2, deal_count, color='#ab47bc', width=0.4, label='Deal Count', alpha=0.7)
ax2.set_ylabel('Deal Count', fontsize=14, fontweight='bold', color='black')
ax2.tick_params(axis='y', labelcolor='black')
ax2.set_ylim(0, 40)

# Annotate deal counts
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval}', ha='center', va='bottom', fontsize=12, color='#ab47bc')

# Add trend line for funding amount on the primary y-axis
coefficients = np.polyfit(years, funding_amount, 1)  # Linear fit
poly = np.poly1d(coefficients)

# Define x range for the trend line (full range of years)
x_range = np.linspace(years.min(), years.max(), 100)
trendline = poly(x_range)

# Plot the trend line with the same scale as funding_amount
ax1.plot(x_range, trendline, color='red', linestyle='-', linewidth=2, label='Trend Line')

# Add title
plt.title('Quantum Computing Deals Are On The Rise\nDisclosed Deals & Equity Funding ($M), 2015 - 2020', fontsize=16, fontweight='bold')

# Combine legends from both axes
handles, labels = [], []
for ax in [ax1, ax2]:
    for handle, label in zip(*ax.get_legend_handles_labels()):
        handles.append(handle)
        labels.append(label)

# Place the combined legend on the left side
ax1.legend(handles, labels, loc='upper left')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()
