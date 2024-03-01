# Import the necessary libraries
import numpy as np
from skmultiflow.drift_detection.adwin import ADWIN

# Simulate a data stream (you can replace this with your actual data)
data_stream = np.random.randint(2, size=2000)  # Simulating a normal distribution of 1's and 0's

# Introduce a concept drift (change in data distribution) from index 999 to 2000
for i in range(999, 2000):
    data_stream[i] = np.random.randint(4, high=8)

# Initialize ADWIN
adwin = ADWIN()

# Add stream elements to ADWIN and verify if drift occurred
for i in range(2000):
    adwin.add_element(data_stream[i])
    if adwin.detected_change():
        print(f"Change detected in data: {data_stream[i]} - at index: {i}")
