import random
import time

def data_stream_simulation():
    while True:
        # Simulate normal data points
        if random.random() < 0.9:
            yield random.uniform(10, 20)  # Normal data
        else:
            yield random.uniform(50, 100)  # Anomalous data
        time.sleep(0.1)  # Simulate real-time data arrival