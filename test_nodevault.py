# test_nodevault.py
"""
Tests for NodeVault module.
"""

import unittest
from nodevault import NodeVault

class TestNodeVault(unittest.TestCase):
    """Test cases for NodeVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeVault()
        self.assertIsInstance(instance, NodeVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
