import json
import os
from . import Palette
from . import rgbColor
from ..utils.misc import pwd_str
from ..utils.configs import Config
import importlib.resources as impres
from . import rgb_palettes 
from .. import configdata

PALETTE_CONF_PATH = impres.files(configdata).joinpath('palette_conf.json')
PALETTES_PATH = impres.files(rgb_palettes)
palette_config = Config(PALETTE_CONF_PATH)

class rgbPalette(Palette):

    '''
    Palette with rgbColor colors class
    '''

    def __init__(self, 
                 color_dict: dict):

        super(rgbPalette, self).__init__(color_dict) 

    def save(self,
             filepath : str) -> None:

        '''
        Method for saving palette to a json file

        args:
        filepath: str - file name and path to save palette
        '''
    
        try:
            with open(filepath, 'w', encoding = 'utf-8') as file:
                json.dump(self.color_dict, 
                          file, 
                          ensure_ascii = False, 
                          indent = 2)
    
        except FileExistsError:
            print('Can`t save: palette already exist')

    @classmethod
    def load(cls,
             filepath : str) -> 'rgbPalette':

        '''
        Constructor/loader of rgbPalette from a json file

        args:

        filepath: str - file name and path of loaded palette
        '''
    
        try:
            with open(filepath, 'r') as file:
                color_json_dict = json.load(file)

                color_dict = {}

                for color_name in color_json_dict.keys():
                    color_dict[color_name] = rgbColor.from_string(color_json_dict[color_name])
                
                return rgbPalette(color_dict)
                
        except FileNotFoundError:
                raise FileNotFoundError('Config file at  \"{}\"  doesnt exist'.format(filepath))

    @classmethod
    def pick(cls,
             name: str) -> 'rgbPalette':

        '''
        Allows to load rgbPalette from existing presets
        saved at "rgb_palettes/%preset_name%.json" and 
        included in palette_conf.json file in "available schemes" 
        as "%preset_name%"

        args:

        name: str - name of a palette preset
        '''
        
        if name not in palette_config.get_value("available schemes"):
            raise ValueError("Palette with name \"{}\" doesnt exist".format(name))
        
        else:
            return cls.load(PALETTES_PATH.joinpath(name + '.json'))
