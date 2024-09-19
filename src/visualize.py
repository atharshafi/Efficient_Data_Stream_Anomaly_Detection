import matplotlib.pyplot as plt

def visualize_data(data_points, anomalies):
    """
    Visualizes the data stream and highlights detected anomalies.

    Parameters:
    - data_points (list): A list of data points to plot.
    - anomalies (list): A list of anomalies corresponding to the data points.
                        Anomalies should be represented as their values, while
                        non-anomalous points should be None.

    This function creates a line plot for the data points and overlays a scatter plot
    for the detected anomalies, allowing for easy visual identification of outliers.
    """
    plt.figure(figsize=(10, 5))  # Set the figure size for the plot
    plt.plot(data_points, label='Data Points', color='blue')  # Plot the data points as a line
    
    # Plot anomalies
    anomaly_indices = [i for i, x in enumerate(anomalies) if x is not None]  # Get indices of anomalies
    anomaly_values = [anomalies[i] for i in anomaly_indices]  # Get values of anomalies
    plt.scatter(anomaly_indices, anomaly_values, color='red', label='Anomalies', zorder=5)  # Scatter plot for anomalies

    # Set plot title and labels
    plt.title('Data Stream and Anomalies')
    plt.xlabel('Time')  # X-axis label
    plt.ylabel('Value')  # Y-axis label
    plt.legend()  # Show legend
    plt.show()  # Display the plot