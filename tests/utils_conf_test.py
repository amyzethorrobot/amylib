import unittest
import os.path
from amylib.utils.configs import *
from amylib.utils import pwd_str

class configsTC(unittest.TestCase):

    def setUp(self):

        current_dir = os.path.join(pwd_str(__file__),
                                   'test_conf_jsons')
        
        self.TEST_PATHS = []
        for i in range(3):
            self.TEST_PATHS.append(os.path.join(current_dir, 
                                        'config' + str(i) + '.json'))
        
        self.TEST_KEYS = ['key' + str(i) for i in range(5)]
        self.TEST_VALUES = ['val' + str(i) for i in range(5)]
        
    def test_nosuch_file(self):

        with self.assertRaises(FileNotFoundError):
            conf = Config(self.TEST_PATHS[0])

    def test_read_config(self):

        conf = Config(self.TEST_PATHS[1])

    def test_wrong_key(self):

        conf = Config(self.TEST_PATHS[1])

        with self.assertRaises(KeyError):
            conf.get_value('notkey')
    
    def test_true_kv(self):

        conf = Config(self.TEST_PATHS[1])

        for i in range(5):
            self.assertEqual(conf.get_value(self.TEST_KEYS[i]), 
                             self.TEST_VALUES[i])
            
    def test_false_kv(self):

        conf = Config(self.TEST_PATHS[2])

        for i in range(5):
            self.assertNotEqual(conf.get_value(self.TEST_KEYS[i]), 
                             self.TEST_VALUES[i])
            
    def tearDown(self):
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()

        