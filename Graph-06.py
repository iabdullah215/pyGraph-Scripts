import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
years = np.array(['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', 
                  '2017', '2018', '2019', '2020'])
values = np.array([12.4, 29.97, 48.17, 82.62, 165.81, 308.96, 452.93, 580.40, 
                   702.06, 812.67, 894.77, 914.02])

# Create a DataFrame
data = pd.DataFrame({'Year': years, 'Value': values})

# Set a light style
sns.set(style='whitegrid')

# Create the plot
plt.figure(figsize=(14, 7))
sns.lineplot(x='Year', y='Value', data=data, marker='o', color='#007acc', linewidth=2, label='Values', markersize=8)

# Add a trend line
sns.regplot(x=np.arange(len(data)), y='Value', data=data, scatter=False, color='#ff6f61', label='Trend Line', ci=None)

# Customize the plot
plt.title('Yearly Distribution with Values and Trend Line', fontsize=20, fontweight='bold')
plt.xlabel('Year', fontsize=16, fontweight='bold')
plt.ylabel('Value', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14, loc='upper left')

# Add annotations for key points
for i in range(len(data)):
    plt.text(x=i, y=values[i] + 20, s=f"{values[i]:.2f}", fontsize=10, ha='center', color='black')

# Simplified grid lines
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.grid(which='minor', linestyle=':', linewidth=0.3, alpha=0.5)  # Less prominent minor grid

# Save the figure
plt.tight_layout()
plt.savefig('yearly_distribution_with_trend_line_clean_background.png', dpi=300)

# Show the plot
plt.show()
