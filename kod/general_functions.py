# functions that can be used throughout the classes
import pandas as pd
import time 
import datetime
import os

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
    df = make_df(keys, values)
    df.to_csv(filename, index=False) 
    return

def make_df(keys, values) -> pd.core.frame.DataFrame:
    '''converts the two lists into a dataframe object'''
    dic = dict()
    for i, key in enumerate(keys):
        dic[key] = values[i]
    return pd.DataFrame(dic)

# time 
def readable_to_sec(t: str) -> int:
    '''returns the readable time in seconds'''
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(t.split(':'))))  

def sec_to_readable(t: float) -> str:
    '''returns the seconds as readable time'''
    return str(datetime.timedelta(seconds = t//1))

# colors
def faded_rgb_color(rgb: tuple, a: float, background = (255, 255, 255)) -> tuple:
    '''returns the color code in rgb rgb faded with a % opacity 
     ontop of background, default white'''
    r, g, b = rgb
    br, bg, bb = background
    return (int((1-a)*br+a*r), int((1-a)*bg+a*g), int((1-a)*bb+a*b))

def hex_to_rgb(h: str) -> tuple:
    '''returns the hex of a color as a (r, g, b) tuple'''
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb255_to_rgb1(rgb: tuple) -> tuple:
    '''converts an RGB color from [0, 255] to [0, 1]'''
    return tuple([x/255 for x in rgb])

def rgb1_to_rgb255(rgb: tuple) -> tuple:
    '''converts an RGB color from [0, 1] to [0, 255]'''
    return tuple([x * 255 for x in rgb])

def clean_up() -> None:
    '''cleans the autogen image and game report powerpoint folders'''
    os.chdir('powerpointer\matchrapporter')
    for f in os.listdir(os.getcwd()):
        os.remove(f)
    os.chdir('..\\..\\bilder\\autogen')
    for f in os.listdir(os.getcwd()):
        os.remove(f)
    os.chdir('..\\..')
    return