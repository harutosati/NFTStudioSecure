# test_nftstudiosecure.py
"""
Tests for NFTStudioSecure module.
"""

import unittest
from nftstudiosecure import NFTStudioSecure

class TestNFTStudioSecure(unittest.TestCase):
    """Test cases for NFTStudioSecure class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTStudioSecure()
        self.assertIsInstance(instance, NFTStudioSecure)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTStudioSecure()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
