import numpy as np

class Color:

    '''
    Base Color class
    '''

    @staticmethod
    def clamp(channel_values: np.ndarray, 
              max_val: int, 
              min_val: int = 0) -> np.ndarray:

        channel_clamped_max = np.where(channel_values <= max_val,
                 channel_values,
                 max_val)

        channel_clamped = np.where(channel_clamped_max >= min_val,
                 channel_clamped_max,
                 min_val)
        
        return channel_clamped

    def __init__(self, 
                 channel_values: np.ndarray, 
                 max_depth: np.ndarray):

        '''
        args:

        channel_values: np.ndarray - array of channel values for each color channel
        max_depth: np.ndarray - maximum value for each channel
        '''
        
        self.__channel_values = Color.clamp(channel_values, max_depth)
        self.__max_depth = max_depth
        self.__channels_number = len(self.__channel_values)

    ## getters

    @property
    def channel_values(self):
        return self.__channel_values

    @property
    def max_depth(self): 
        return self.__max_depth

    @property
    def channels_number(self): 
        return self.__channels_number
    
    @property
    def rgb(self):
        raise NotImplementedError
    
    @property
    def rgb_channel_values(self):
        raise NotImplementedError

    @classmethod
    def functional(cls, 
                         color_function: callable, 
                         color1: 'Color', 
                         color2: 'Color') -> 'Color':
        ...
