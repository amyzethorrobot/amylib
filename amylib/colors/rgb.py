from ..colors.colorbase import Color
import numpy as np

class rgbColor(Color):

    RGB_MAX_DEPTH = 255

    def __init__(self, 
                 channel_values: list[int] | np.ndarray):

        if len(channel_values) != 3:
            raise ValueError('rgb color must be 3-channel, not {0}-channel'.format(len(channel_values)))
        super().__init__(channel_values, np.ones(3, dtype = np.int16) 
                         * rgbColor.RGB_MAX_DEPTH)
        self.__color_string = rgbColor.to_string(self.channel_values)
        
    @property
    def rgb(self):
        return self.__color_string
    
    @property
    def rgb_channel_values(self):
        return self.channel_values

    @classmethod
    def from_string(cls, color_string: str) -> 'rgbColor':

        if not isinstance(color_string, str):
            raise TypeError('color_string must be a <class \'str\'>, not {0}'
                            .format(type(color_string)))

        if color_string[0] == '#':
            color_string = color_string[1:]
        else:
            pass
        
        str_len = len(color_string)
        if str_len < 6:
            raise ValueError('color_string {0} is missing some digits'.format(color_string))
            
        channel_values = np.zeros(3, dtype = np.int16)
        
        for i in range(3):
            channel_values[i] = int(color_string[i*2:i*2 + 2], 16)

        return rgbColor(channel_values)
    
    @classmethod
    def to_string(cls, 
                  channel_values: np.ndarray | list[int]) -> str:
        
        output_string = '#'

        if isinstance(channel_values, list):
            channel_values = np.array(channel_values)

        if any(channel_values > rgbColor.RGB_MAX_DEPTH):
            raise OverflowError('One of the channels value is greater than maximum')

        for ch in channel_values:
            ch_hex = hex(ch)[2:]
            if len(ch_hex)==2:
                output_string += str(ch_hex)
            else:
                output_string += '0' + str(ch_hex)
        return output_string

    @classmethod
    def functional(cls, 
                         color_function: callable, 
                         color1: 'rgbColor', 
                         color2: 'rgbColor') -> 'rgbColor':

        '''
        Applies color_function() (such as sum, mul, etc) to 2 input colors.
        color_function() must be a function of __channels_number positional arguments
        '''

        color3_channel_values = Color.clamp(color_function(color1.channel_values, 
                                               color2.channel_values),
                                            255)

        return rgbColor(color3_channel_values)