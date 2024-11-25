from .misc import time_hms_str, time_ymd_str

def print_date_time(seconds: bool = False, 
                    year: bool = False,
                    indentation: int = 0):
    
    string_time = time_hms_str(seconds = seconds,
                               separator = ':')
    string_date = time_ymd_str(year = year, 
                              separator = '.')
    
    if indentation == 0:
        print('date: ' 
              + string_date, 
              end = ' ')
        print('time: ' 
              + string_time, 
              '\n')
    else:
        print('' * indentation
              + 'date: ' 
              + string_date, 
              end = ' ')
        print('time: ' 
              + string_time, 
              '\n')
