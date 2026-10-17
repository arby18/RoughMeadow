# test_roughmeadow.py
"""
Tests for RoughMeadow module.
"""

import unittest
from roughmeadow import RoughMeadow

class TestRoughMeadow(unittest.TestCase):
    """Test cases for RoughMeadow class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughMeadow()
        self.assertIsInstance(instance, RoughMeadow)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughMeadow()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
