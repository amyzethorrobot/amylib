import os.path
from datetime import datetime

def pwd_str(file_variable: str) -> str:
    return os.path.dirname(file_variable)

def time_tuple() -> tuple[int, ...]:

    '''
    Returns current system time in 
    year/month/day/hour/minute/second format in tuple
    '''
    
    current_date = datetime.now()
    
    return (current_date.year,
            current_date.month, 
            current_date.day, 
            current_date.hour, 
            current_date.minute,
            current_date.second)

def time_ymd_str(separator: str = '',
                 us: bool = True,
                 year: bool = False) -> str:

    current_date = datetime.now()

    if not year: 
        if us:
            return current_date.strftime('%m' 
                                         + separator 
                                         + '%d')
        else:
            return current_date.strftime('%d' 
                                         + separator 
                                         + '%m')
    else:
        if us:
            return current_date.strftime('%m' 
                                         + separator 
                                         + '%d'
                                         + separator
                                         + '%Y')
        else:
            return current_date.strftime('%d' 
                                         + separator 
                                         + '%m'
                                         + separator
                                         + '%Y')

    
def time_hms_str(separator: str = '',
                 seconds: bool = False) -> str:

    current_date = datetime.now()

    if not seconds:
        return current_date.strftime('%H'
                                     + separator
                                     + '%M')
    else:
        return current_date.strftime('%H'
                                     + separator
                                     + '%M'
                                     + separator
                                     + '%S')