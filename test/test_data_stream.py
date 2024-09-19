import unittest
from src.data_stream import data_stream_simulation

class TestDataStream(unittest.TestCase):
    def test_data_stream(self):
        # Test the data stream to ensure it yields values
        stream = data_stream_simulation()
        normal_count = 0
        anomaly_count = 0

        # Check the first 100 data points
        for _ in range(100):
            value = next(stream)
            if value < 20:  # Normal range
                normal_count += 1
            elif value >= 50:  # Anomalous range
                anomaly_count += 1

        # Assert that we have a mix of normal and anomalous values
        self.assertGreater(normal_count, 0, "No normal data points found.")
        self.assertGreater(anomaly_count, 0, "No anomalous data points found.")

if __name__ == '__main__':
    unittest.main()