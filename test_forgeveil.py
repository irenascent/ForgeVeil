# test_forgeveil.py
"""
Tests for ForgeVeil module.
"""

import unittest
from forgeveil import ForgeVeil

class TestForgeVeil(unittest.TestCase):
    """Test cases for ForgeVeil class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ForgeVeil()
        self.assertIsInstance(instance, ForgeVeil)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ForgeVeil()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
