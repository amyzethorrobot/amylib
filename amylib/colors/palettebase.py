import matplotlib.pyplot as plt
import numpy as np

class Palette:

    '''
    Base class for color palettes.
    Includes basic constructor from dict(),
    basic setters/getters,
    methods for iterating through colors for plots and stuff
    and preview method.
    '''

    ITERATION_START = 2

    def __init__(self, 
                 color_dict: dict):

        self.__color_list = list(color_dict.values())
        self.__color_dict = color_dict

        self.__length = len(self.__color_list)

        self.__iteration_indices = [i for i in range(Palette.ITERATION_START, self.__length)]
        self.__active_index = 0
        self.__iteration_step = 1

    def get_rgb_color(self, 
                      query: str | int):

        if isinstance(query, str):
            return self.__color_dict[query].rgb
        elif isinstance(query, int):
            return self.__color_list[query].rgb
        else:
            raise ValueError('Query type must be \'int\' or \'string\'')
        
    # GETTERS

    @property
    def active_index(self):
        return self.__active_index
        
    @property
    def length(self): 
        return self.__length

    @property
    def color_dict(self):
        return self.__color_dict

    @property
    def color_list(self):
        return self.__color_list

    @property
    def iteration_indices(self):
        return self.__iteration_indices

    @property
    def iteration_step(self):
        return self.__iteration_step
    
    # SETTERS

    @iteration_step.setter
    def iteration_step(self, new_step):
        self.__iteration_step = new_step

    def reset_active_index(self):
        self.__active_index = 0

    def set_iteration_indices(self, 
                              iteration_indices: list[int]):
        self.__iteration_indices = iteration_indices

    # ITERATIONS

    def next(self, 
             step: int | None = None, 
             as_channels: bool = False) -> np.ndarray | str:
        
        '''
        Method for iterating through colors in palette

        args:

        step: int or None - size of iteration step. 
        If set to None, uses default value of this palette instance
        as_channels: bool - format of returned value

        return:

        np.ndarray of channels values in as_channels == True, rgb-string otherwise
        '''

        if step == None: step = self.__iteration_step
        prev_index = self.__active_index
        self.__active_index = (self.__active_index + step)%len(self.__iteration_indices)

        if as_channels:
            return self.__color_list[self.__iteration_indices[prev_index]].channel_values
        else:
            return self.__color_list[self.__iteration_indices[prev_index]].rgb

    # PREVIEW

    def preview(self, 
                line_size: int = 10):

        '''
        Draws all colors in a palette as 2d grid in plt.figure

        args:

        line_size: int - number of colors in a row
        '''

        if self.__length%line_size == 0: 
            lines = self.__length//line_size 
        else:
            lines = self.__length//line_size + 1

        color_matrix = np.ones((lines, line_size, 3), dtype = np.int16)*255
        
        for i in range(self.__length):
            color_matrix[i//line_size][i%line_size] = \
                self.__color_list[i].rgb_channel_values

        f = plt.figure(figsize = (line_size * 1.1, lines * 1.1))
        a = f.subplots(1, 1)
        a.imshow(color_matrix)
        a.set_xticks([])
        a.set_yticks([])
        
        return
