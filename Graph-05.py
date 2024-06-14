import matplotlib.pyplot as plt

# Data for the pyramid chart
labels = ['< 20', '20 - 29', '30 - 39', '40 - 49', '50 - 59', '60 <']
sizes = [18174, 62410, 88138, 84052, 65924, 101068]  # Example sizes for the entities
colors = ['#add8e6', '#ffb6c1', '#98fb98', '#f0e68c', '#dda0dd', '#ffdab9']  # Light colors

# Function to create pyramid chart
def pyramid_chart(labels, sizes, colors):
    fig, ax = plt.subplots()

    # Create bars for each entity with different colors
    for i, (label, size, color) in enumerate(zip(labels, sizes, colors)):
        ax.barh(i, size, color=color, edgecolor='black')

    # Set the y-axis labels
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontweight='bold')

    # Invert the y-axis to have the largest bar at the bottom
    ax.invert_yaxis()

    # Add labels to each bar
    for i, size in enumerate(sizes):
        ax.text(size + 1, i, str(size), va='center', fontweight='bold')

    # Set labels and title
    ax.set_xlabel('No. of Complaints', fontweight='bold')
    ax.set_title('Complaints by different age groups', fontweight='bold')

    # Remove the top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add grid
    ax.grid(True)

    plt.show()

# Call the function to create the pyramid chart
pyramid_chart(labels, sizes, colors)
