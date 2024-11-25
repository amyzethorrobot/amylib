import unittest
from amylib.colors import * 
from amylib.utils import pwd_str

class rgbPaletteTC(unittest.TestCase):

    def setUp(self):

        self.current_dir = os.path.join(pwd_str(__file__),
                                   'test_palettes')

        return super().setUp()
    
    def test_load(self):

        filepath = os.path.join(self.current_dir,
                                'testpal0.json')

        palette = rgbPalette.load(filepath)
        
        with open(filepath, 'r') as file:
                color_json_dict = json.load(file)
        
        for k in color_json_dict.keys():
            self.assertEqual(palette.get_rgb_color(k), color_json_dict[k])

        return
    
    def test_iterate(self):

        filepath = os.path.join(self.current_dir,
                                'testpal0.json')
        colors_list = ['#ff0000', '#00ff00', '#0000ff']
        color_len = len(colors_list)

        for j in range(0, 100):

            palette = rgbPalette.load(filepath)

            for i in range(0, 10):
                self.assertEqual(palette.next(), colors_list[i%color_len])

        return

    def tearDown(self):
        return super().tearDown()