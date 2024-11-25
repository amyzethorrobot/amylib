import unittest
from amylib.datablocks import * 

class dataBlockTC(unittest.TestCase):

    def setUp(self):

        self.datablock = DataBlock({'f': 0.1})

        return super().setUp()
    
    def test_next_empty(self):

        with self.assertRaises(RuntimeError):
            next_val = self.datablock.next()

    def test_current_empty(self):
        
        with self.assertRaises(RuntimeError):
            curr_val = self.datablock.current()

    def test_next_overflow(self):

        total_series = 5

        dummy_data = np.array([np.ones(10) * i 
                               for i in range(0, total_series)])
        
        dummyblock = DataBlock({'f': 0.1})
        dummyblock.data = dummy_data
        dummyblock.series = total_series

        for i in range(0, total_series * 3):

            next_val = dummyblock.next()[0]
            self.assertEqual(next_val, 
                             i % total_series)
    
    def tearDown(self):
        return super().tearDown()