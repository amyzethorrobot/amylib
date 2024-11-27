import json

class Config:

    '''
    Class for managing json configs
    '''

    def __init__(self, config_path):

        try:
            with open(config_path, 'r') as file:
                self.__properties = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError('Config file at  \"{0}\"  doesnt exist'.
                                    format(config_path))

    @property
    def properties(self):
        return self.__properties

    def get_value(self, key):
        return self.__properties[key]
    
    def is_in(self, prop):
        return prop in self.__properties

    def set_value(self, key, new_value):
        
        if key not in self.__properties:
            raise KeyError('Property {} doesnt exist!'.format(key))

        self.__properties[key] = new_value
