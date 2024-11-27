import numpy as np

class DataBlock:

    '''
    Base data block class 
    which implements basic functions to iterate through data 
    and store/process some hyperparameters of an experiment 
    '''

    DEFAULT_ITERATION_STEP = 1

    def __init__(self, 
                 feature_dict: dict,
                 block_type: str = 'default',
                 block_name: str = 'name'
                ):

        self.__feature_dict = feature_dict
        self.__active_index = 0
        self.__iteration_step = DEFAULT_ITERATION_STEP
        self.__type = block_type
        self.__name = block_name

        self.__series = None
        self.__length = None
        self.__sample_shape = None
        self.__data = None

    ## getters
    
    def feature(self, name: str):
        return self.__feature_dict[name]

    @property
    def iteration_step(self):
        return self.__iteration_step
    
    @property
    def feature_dict(self):
        return self.__feature_dict

    @property
    def length(self):
        return self.__length

    @property
    def series(self):
        return self.__series

    @property
    def sample_shape(self):
        return self.__sample_shape

    @property
    def type(self):
        return self.__type

    @property
    def data(self):
        return self.__data
    
    @property
    def active_index(self):
        return self.__active_index

    ## setters

    def set_feature(self, feature_name: str, feature_value):
        
        if feature_name not in self.__feature_dict:
            raise ValueError('Invalid feature name!')
        self.__feature_dict[feature_name] = feature_value

    @iteration_step.setter
    def iteration_step(self, step_value: int):
        self.__iteration_step = step_value

    @series.setter
    def series(self, new_series: int):
        self.__series = new_series

    @length.setter
    def length(self, new_len: int):
        self.__length = new_len

    @sample_shape.setter
    def sample_shape(self, new_sample: list[int] | int):
        self.__sample_shape = new_sample

    @data.setter
    def data(self, data_array: np.ndarray):
        self.__data = data_array

    ## other

    def reset_active_index(self):

        '''
        Resets current iteration index to 0
        '''
        
        self.__active_index = 0

    def add_feature(self, feature_name: str, feature_value):
        
        if feature_name in self.__feature_dict:
            raise ValueError('Feature already exists!')
        self.__feature_dict[feature_name] = feature_value

    ## iterations and plots

    def next(self, step: int | None = None):

        '''
        Method for iterating through data series. 
        Returns data at current index 
        and then increases index value by step

        args:

        step: int or None - iteration step.
        If None then default value is used
        '''

        if isinstance(self.__data, type(None)):
            raise RuntimeError('DataBlock is empty')

        if step == None: step = self.__iteration_step
        prev_index = self.__active_index
        self.__active_index = (self.__active_index + step)%self.__series
        return self.__data[prev_index]

    def current(self):

        ''' 
        Returns data at current index
        '''

        if isinstance(self.__data, type(None)):
            raise RuntimeError('DataBlock is empty')
            
        return self.__data[self.__active_index]
