import unittest
from amylib.colors import * 

class rgbColorTC(unittest.TestCase):

    def setUp(self):

        self.red = rgbColor([300, 0, 0])
        self.green = rgbColor([0, 255, 0])
        self.blue = rgbColor([-200, 0, 250])
        self.sum = lambda x, y: x + y
        self.mul = lambda x, y: x * y
        return super().setUp()

    def test_color_overflow(self):

        with self.assertRaises(OverflowError):
            col_str = rgbColor.to_string([255, 345, 0])

    def test_to_string_wrong(self):

        input_list = [
            '#ffff',
            '#fffff',
            '#',
            'ffff',
            'fffff'
        ]

        for inp in input_list:

            with self.assertRaises(ValueError):
                print('Example {0}'.format(inp))
                black = rgbColor.from_string(inp)

    def test_functional_sum(self):

        c3 = rgbColor.functional(self.sum, self.red, self.green)
        self.assertEqual(c3.rgb, '#ffff00')

    def test_fromrgb_string(self):

        colors_list = ['#ffffff',
                       '#ff0000',
                       '#00ff00',
                       '#0000ff',
                       '#4569ff',
                       '#990087',
                       '#cdcd01']
        
        for c in colors_list:

            color = rgbColor.from_string(c)
            self.assertEqual(color.rgb, c)

    def tearDown(self):
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()