import sys
import unittest

# Add the target branch's code path to sys.path, change after ./code ...
sys.path.insert(0, './code/Code/Sprint2/Loading_Module')

# Import functions from the code in the Data-Loading-Module branch
from data_loading_module import load_gtfs_data


class TestDataLoadingModule(unittest.TestCase):
    
    def test_load_gtfs_data_valid(self):
        """
        Test loading a valid GTFS data file to check that the data is parsed correctly.
        """
        result = load_gtfs_data('tests/test_data/gtfs_data.zip')
        
        # Check that the GTFS data was loaded correctly and verify the data structure
        self.assertIsInstance(result, dict)
        self.assertIn('routes', result)
        self.assertIn('trips', result)
        self.assertIn('stop_times', result)
        self.assertIn('stops', result)
        
    def test_load_gtfs_data_invalid(self):
        """
        Test loading an invalid GTFS data file to check that errors are handled correctly.
        """
        with self.assertRaises(Exception):
            load_gtfs_data('tests/test_data/invalid_gtfs.zip')


if __name__ == '__main__':
    unittest.main()
