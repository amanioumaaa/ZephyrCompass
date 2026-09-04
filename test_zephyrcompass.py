# test_zephyrcompass.py
"""
Tests for ZephyrCompass module.
"""

import unittest
from zephyrcompass import ZephyrCompass

class TestZephyrCompass(unittest.TestCase):
    """Test cases for ZephyrCompass class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZephyrCompass()
        self.assertIsInstance(instance, ZephyrCompass)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZephyrCompass()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
