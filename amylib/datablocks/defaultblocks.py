import numpy as np
from ..datablocks.datablock import DataBlock

class UniversalData(DataBlock):

    def __init__(self, 
                 raw_data: np.ndarray, 
                 feature_dict: dict, 
                 series: bool = True):
        
        super().__init__(feature_dict = feature_dict,
                         block_type = 'Universal',
                         block_name = 'Un')

        data_shape = np.shape(raw_data)
        shape_len = len(data_shape)
        
        if shape_len == 1:
            self.__series = 1
            self.__length = data_shape[0]
            self.__sample_shape = 1
            self.__data = np.array([raw_data])
            
        elif shape_len > 1 and series == True:
            self.__series = data_shape[0]
            self.__length = data_shape[1]
            self.__sample_shape = 1 if data_shape[2:] == () else data_shape[2:]
            self.__data = raw_data

        elif shape_len > 1 and series == False:
            self.__series = 1
            self.__length = data_shape[0]
            self.__sample_shape = 1 if data_shape[1:] == () else data_shape[1:]
            self.__data = np.array([raw_data])
        else:
            raise ValueError('Invalid data shape {0}'.format(data_shape))
        
class Curve2d(DataBlock):

    def __init__(self, 
                 raw_data: np.ndarray, 
                 feature_dict: dict):
        
        super().__init__(feature_dict = feature_dict,
                         block_type = 'Curve 2d',
                         block_name = 'C2d')

        data_shape = np.shape(raw_data)
        shape_len = len(data_shape)

        if shape_len == 1:
            self.series = 1
            self.length = data_shape[0]
            self.data = np.array([raw_data])

        elif shape_len == 2:
            self.series = data_shape[0]
            self.length = data_shape[1]
            self.data = raw_data

        else:
            raise ValueError('Invalid data shape {0}, expected (2, N)'.format(data_shape))

        self.length = data_shape[1]
        self.sample_shape = 1

    @classmethod
    def loadnp(cls, data_path: str, feature_dict: dict):
        return Curve2d(np.load(data_path), feature_dict)
    
class LossCurve(DataBlock):

    def __init__(self, 
                 raw_data: np.ndarray, 
                 lr: float):
        
        super().__init__(feature_dict = {'lr': lr},
                         block_type = 'Loss Curve',
                         block_name = 'LC')

        data_shape = np.shape(raw_data)
        shape_len = len(data_shape)

        if shape_len == 1:
            self.series = 1
            self.length = data_shape[0]
            self.data = np.array([raw_data])

        elif shape_len == 2:
            self.series = data_shape[0]
            self.length = data_shape[1]
            self.data = raw_data

        else:
            raise ValueError('Invalid data shape {0}, expected (2, N)'.format(data_shape))

        self.length = data_shape[1]
        self.sample_shape = 1

    @classmethod
    def loadnp(cls, data_path: str, lr: float):
        return LossCurve(np.load(data_path), lr)
    
    def treshold_points(self, 
                        value_th: float) -> np.ndarray:
        
        '''
        Returns indices (time in iterations) 
        of first encountering of loss value <= value_th
        for each loss curve in an array

        args:

        value_th: float - treshold value

        returns:

        points: np.ndarray - array of indices
        
        '''
        
        points = np.zeros(self.series)
        
        for i, s in enumerate(self.data):
            
            th_indices = np.argwhere(np.where(s <= value_th, 
                                              1, 0))
            
            if th_indices.shape[0] == 0:
                idx = self.length - 1 
            else:
                idx = th_indices[0]
            points[i] = idx
        
        return points