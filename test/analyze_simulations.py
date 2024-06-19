import matplotlib.pyplot as plt
import pandas as pd

# Read the simulation results
results_file = 'simulation_results.txt'
data = pd.read_csv(results_file)

# Filter out rows with errors
data = data[data['DistanceToLight'] != 'ERROR']
data['DistanceToLight'] = data['DistanceToLight'].astype(float)

# Calculate statistics
mean_distance = data['DistanceToLight'].mean()
median_distance = data['DistanceToLight'].median()
std_distance = data['DistanceToLight'].std()
min_distance = data['DistanceToLight'].min()
max_distance = data['DistanceToLight'].max()

# Define a threshold for success
success_threshold = 1.0  # Example threshold value
success_rate = (data['DistanceToLight'] <= success_threshold).mean() * 100

print(f"Mean Distance: {mean_distance:.2f}")
print(f"Median Distance: {median_distance:.2f}")
print(f"Standard Deviation: {std_distance:.2f}")
print(f"Minimum Distance: {min_distance:.2f}")
print(f"Maximum Distance: {max_distance:.2f}")
print(f"Success Rate: {success_rate:.2f}%")

# Plot the distances
plt.figure(figsize=(10, 6))
plt.plot(data['Simulation'], data['DistanceToLight'], marker='o', linestyle='-', color='b', label='Distance')
plt.title('Distance to Light Over Simulations')
plt.xlabel('Simulation')
plt.ylabel('Distance to Light')
plt.grid(True)
plt.axhline(mean_distance, color='r', linestyle='--', label=f'Mean: {mean_distance:.2f}')
plt.axhline(median_distance, color='g', linestyle='--', label=f'Median: {median_distance:.2f}')
plt.axhline(success_threshold, color='y', linestyle='--', label=f'Success Threshold: {success_threshold:.2f}')
plt.legend()
plt.tight_layout()

# Save the plot
plt.savefig('distance_plot.png')

# Show the plot
plt.show()

# Histogram of distances
plt.figure(figsize=(10, 6))
plt.hist(data['DistanceToLight'], bins=20, color='c', edgecolor='k', alpha=0.7)
plt.title('Histogram of Distances to Light')
plt.xlabel('Distance to Light')
plt.ylabel('Frequency')
plt.axvline(mean_distance, color='r', linestyle='--', label=f'Mean: {mean_distance:.2f}')
plt.axvline(median_distance, color='g', linestyle='--', label=f'Median: {median_distance:.2f}')
plt.legend()
plt.tight_layout()

# Save the histogram
plt.savefig('distance_histogram.png')

# Show the histogram
plt.show()
