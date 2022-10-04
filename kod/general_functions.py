# functions that can be used throughout the classes
import pandas as pd
import time 
import datetime

# other 
def combine_dictionaries(dict_1: dict, dict_2: dict) -> dict:
    '''combines the content of the two dictionaries into a new one'''
    dict_3 = {**dict_1, **dict_2}
    for key, value in dict_3.items():
        if key in dict_1 and key in dict_2:
                dict_3[key] = [value , dict_1[key]]
    return dict_3


# open csv
def append_clean(filename: str, change_dirr = True) -> str:
    '''makes sure that the output ends in clean.csv
        if change_dirr == True we expect to be able to
        backtrack one folder and open the folder clean'''
    if change_dirr:
        if len(filename) <= 9 or filename[:9] != "..\\clean\\":
            filename = "..\\clean\\" + filename
    if len(filename) <= 4 or filename[-4:] != '.csv':
        return filename + ' clean.csv'
    else:
        return filename[:-4] + ' clean.csv'

def read_csv_as_df(filename: str) -> pd.core.frame.DataFrame:
    '''returns the csv as a df object'''
    try:
        return pd.read_csv(filename)
    except:
        return pd.read_csv(filename + '.csv')

def save_data_to_csv(filename: str, keys: list, values: list) -> None:
    # makes sure path is good
    if len(filename) <= 4 or filename[-4:] != '.csv':
        filename += '.csv'
    dic = dict()
    for i, key in enumerate(keys):
        dic[key] = values[i]
    df = pd.DataFrame(dic)
    df.to_csv(filename, index=False) 
    return

# time 
def readable_to_sec(t: str) -> int:
    '''returns the readable time in seconds'''
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(t.split(':'))))  

def sec_to_readable(t: float) -> str:
    '''returns the seconds as readable time'''
    return str(datetime.timedelta(seconds = t//1))

