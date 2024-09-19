import unittest
from collections import deque
from src.anomaly_detection import AnomalyDetector

class TestAnomalyDetection(unittest.TestCase):
    def setUp(self):
        # Initialize a sliding window with some normal values
        self.detector = AnomalyDetector(window_size=5, threshold=2)  # Adjusted threshold
        self.detector.window.extend([10, 12, 11, 13, 14])  # Fill the window

    def test_normal_case(self):
        # Test with a normal data point
        self.assertFalse(self.detector.detect_anomaly_zscore(12))  # Should not be an anomaly

    def test_anomaly_case(self):
        # Test with an anomalous data point
        self.assertTrue(self.detector.detect_anomaly_zscore(25))  # Should be an anomaly

    def test_edge_case(self):
        # Test with a value that is on the edge of being an anomaly
        self.assertFalse(self.detector.detect_anomaly_zscore(14))  # Should not be an anomaly
        self.assertFalse(self.detector.detect_anomaly_zscore(15))  # Should not be an anomaly

if __name__ == '__main__':
    unittest.main()