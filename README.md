# Efficient Data Stream Anomaly Detection

## Project Overview

This project implements a Python script capable of detecting anomalies in a continuous data stream. The data stream simulates real-time sequences of floating-point numbers, which could represent various metrics such as financial transactions or system metrics. The focus is on identifying unusual patterns, such as exceptionally high values or deviations from the norm.

## Objectives

- **Algorithm Selection**: Implemented a suitable algorithm for anomaly detection that adapts to concept drift and seasonal variations.
- **Data Stream Simulation**: Designed a function to emulate a data stream, incorporating regular patterns, seasonal elements, and random noise.
- **Anomaly Detection**: Developed a real-time mechanism to accurately flag anomalies as the data is streamed.
- **Optimization**: Ensured the algorithm is optimized for both speed and efficiency.
- **Visualization**: Created a straightforward real-time visualization tool to display both the data stream and any detected anomalies.

## Algorithm Used

### Z-score Method

The anomaly detection algorithm implemented in this project is the **Z-score method**. 

#### How It Works:
1. **Mean and Standard Deviation Calculation**: The algorithm calculates the mean and standard deviation of the values in a sliding window of recent data points.
2. **Z-score Calculation**: For each new data point, the Z-score is computed using the formula:
   Z = ( X - μ ) / σ
   where:
   - (Z) Z-score
   - (X) is the new data point.
   - (μ) is the mean of the data points in the sliding window.
   - (σ) is the standard deviation of the data points in the sliding window.
3. **Anomaly Detection**: If the absolute value of the Z-score exceeds a predefined threshold, the data point is flagged as an anomaly.

#### Effectiveness:
- **Sensitivity to Outliers**: The Z-score method is effective for detecting outliers in normally distributed data.
- **Real-time Detection**: The algorithm can be applied in real-time as new data points arrive.
- **Adaptability**: By using a sliding window, the algorithm adapts to changes in the data distribution over time.

#### Limitations:
- **Assumption of Normality**: The Z-score method assumes that the data follows a normal distribution.
- **Sensitivity to Window Size**: The choice of window size can impact detection performance.

## Requirements

- Python 3.x
- Minimal use of external libraries. The following libraries are used:
  - `numpy`
  - `matplotlib`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/atharshafi/efficient_data_stream_anomaly_detection.git
   cd efficient_data_stream_anomaly_detection
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script to start the anomaly detection system:
   ```bash
   python -m src.main
   ```

2. The program will simulate a data stream and visualize the data points along with any detected anomalies in real-time.

## Testing

To ensure the functionality of the code, unit tests are included in the `test` directory. You can run the tests using the following command:
   ```bash 
   python -m unittest discover -s test
   ```
