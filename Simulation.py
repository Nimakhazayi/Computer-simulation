import numpy as np
import matplotlib.pyplot as plt

# Set the parameters
mean = 5 #1,2,3,4 for other examples
variance = 1
std_dev = np.sqrt(variance)
num_samples = 1000

# Generate random numbers from a normal distribution
random_numbers = np.random.normal(mean, std_dev, num_samples)

# Plot the histogram
plt.figure()
plt.hist(random_numbers, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title("Histogram of 1000 Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()