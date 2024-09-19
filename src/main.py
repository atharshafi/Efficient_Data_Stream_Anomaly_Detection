from collections import deque
from src.data_stream import data_stream_simulation
from src.anomaly_detection import AnomalyDetector
from src.visualize import visualize_data

def main():
    """
    Main function to run the anomaly detection system.
    
    This function initializes parameters, simulates a data stream, detects anomalies,
    and visualizes the results. It runs for a specified number of data points and
    visualizes the data every 50 points.
    """
    # Initialize parameters
    window_size = 10  # Size of the sliding window for anomaly detection
    sliding_window = deque(maxlen=window_size)  # Deque to hold the most recent data points
    data_points = []  # List to store all data points
    anomalies = []  # List to store detected anomalies

    # Create an instance of the AnomalyDetector with a specified threshold
    detector = AnomalyDetector(window_size, threshold=1.5)

    # Simulate the data stream
    stream = data_stream_simulation()
    for _ in range(200):  # Run for 200 data points
        data_point = next(stream)  # Get the next data point from the stream
        sliding_window.append(data_point)  # Add the data point to the sliding window
        data_points.append(data_point)  # Store the data point

        # Check for anomalies using the Z-score method
        is_anomaly = detector.detect_anomaly_zscore(data_point)
        if is_anomaly:
            anomalies.append(data_point)  # Store the anomaly if detected
        else:
            anomalies.append(None)  # Append None if no anomaly is detected

        # Visualize data every 50 data points
        if len(data_points) % 50 == 0:
            visualize_data(data_points, anomalies)  # Visualize the current data and anomalies

    # Final visualization after the stream ends
    visualize_data(data_points, anomalies)  # Visualize all data points and detected anomalies

if __name__ == '__main__':
    main()  # Execute the main function when the script is run