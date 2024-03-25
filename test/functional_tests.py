import unittest
from modules.ai_network import AI_Network
from tools.customization import customize_network

class FunctionalTests(unittest.TestCase):
    def test_customize_network(self):
        # Initialize AI_Network
        ai_network = AI_Network()

        # Customize AI_Network
        customization_settings = {
            "parameter1": "value1",
            "parameter2": "value2"
        }
        customized_network = customize_network(ai_network, customization_settings)

        # Check if the network is customized correctly
        self.assertEqual(customized_network.parameter1, "value1")
        self.assertEqual(customized_network.parameter2, "value2")

if __name__ == '__main__':
    unittest.main()
