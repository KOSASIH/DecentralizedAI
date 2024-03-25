import unittest
import os
import sys
sys.path.append(os.path.abspath('../..'))
from modules.data_processing import DataProcessing
from tools.data_visualization import DataVisualization

class IntegrationTests(unittest.TestCase):
    def test_integration(self):
        data_processing = DataProcessing()
        data_processing.load_data('data.csv')
        processed_data = data_processing.process_data()

        data_visualization = DataVisualization()
        data_visualization.visualize_data(processed_data)

        # Add assertions to check the correctness of the visualization

if __name__ == '__main__':
    unittest.main()
