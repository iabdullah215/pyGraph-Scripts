import matplotlib.pyplot as plt
import numpy as np

# Data for the states and number of complaints
states = ['Ohio', 'New York', 'Florida', 'Texas', 'California']
complaints = [17864, 26948, 41061, 47305, 77271]

# Convert state index to a numeric array for plotting
state_indices = np.arange(len(states))

# Create figure and axis
fig, ax = plt.subplots()

# Bar chart for number of complaints (light gray with transparency)
ax.bar(state_indices, complaints, color='#d3d3d3', alpha=0.9, label='Yearly Distribution')

# Line chart for total complaints (blue color) touching the peaks of the bars
ax.plot(state_indices, complaints, color='#1f77b4', marker='o', linestyle='-', label='Total Complaints')

# Adding data labels for the complaints at the peaks
for i, txt in enumerate(complaints):
    ax.annotate(f'{txt}', (state_indices[i], complaints[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Setting title and labels
ax.set_title('Complaints Per State', fontsize=14, fontweight='bold')
ax.set_xlabel('States', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Complaints', fontsize=12, fontweight='bold')

# Customize x-axis to display state names
ax.set_xticks(state_indices)
ax.set_xticklabels(states)

# Adding legend and grid
ax.legend(loc='best', frameon=False)
ax.grid(True, linestyle='--', alpha=0.6)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()
