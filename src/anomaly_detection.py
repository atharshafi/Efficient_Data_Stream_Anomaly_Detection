from collections import deque
import numpy as np

class AnomalyDetector:
    def __init__(self, window_size=10, threshold=1.5):
        """
        Initializes the AnomalyDetector with a sliding window and a threshold.

        Parameters:
        - window_size (int): The size of the sliding window for calculating statistics.
        - threshold (float): The Z-score threshold for determining anomalies.
        """
        self.window = deque(maxlen=window_size)  # Initialize a deque for the sliding window
        self.threshold = threshold  # Set the Z-score threshold

    def detect_anomaly_zscore(self, data_point):
        """
        Detects if a given data point is an anomaly based on the Z-score method.

        Parameters:
        - data_point (float): The new data point to evaluate.

        Returns:
        - bool: True if the data point is an anomaly, False otherwise.
        """
        # Validate input
        if not isinstance(data_point, (int, float)):
            raise ValueError("Data point must be a numeric value.")

        # If the window is not full yet, append the data point and return False (no anomaly)
        if len(self.window) < self.window.maxlen:
            self.window.append(data_point)
            return False  # Not enough data to determine anomaly

        # Calculate mean and standard deviation of the current window
        mean = np.mean(self.window)
        std_dev = np.std(self.window)

        # If std_dev is 0, avoid division by zero
        if std_dev == 0:
            return False  # All values are the same, no anomaly

        # Calculate Z-score
        z_score = (data_point - mean) / std_dev

        # Append the new data point to the window
        self.window.append(data_point)

        # Return True if the Z-score exceeds the threshold
        return abs(z_score) > self.threshold