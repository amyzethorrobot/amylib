import json
import os
from . import Palette
from . import rgbColor
from ..utils.misc import pwd_str
from ..utils.configs import Config

palette_config = Config(os.path.join(pwd_str(__file__), 
                                     "palette_conf.json"))

class rgbPalette(Palette):

    def __init__(self, 
                 color_dict: dict):

        super(rgbPalette, self).__init__(color_dict) 

    def save(self,
             filepath : str):
    
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
             name) -> 'rgbPalette':
        
        if name not in palette_config.get_value("available schemes"):
            raise ValueError("Palette with name \"{}\" doesnt exist".format(name))
        
        else:
            return cls.load(os.path.join(pwd_str(__file__), 
                                         "rgb_palettes",
                                         name + ".json"))