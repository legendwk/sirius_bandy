# functions that can be used throughout the classes
import pandas as pd
import time 
import datetime
import os
import constants

# other 
def combine_dictionaries(dict_1: dict, dict_2: dict) -> dict:
    '''combines the content of the two dictionaries into a new one
        expects dicts to be of format {team0: {key0: val0, key1: val1, ...}, ...}'''
    d = dict_1.copy()
    for key in dict_2:
        for subkey in dict_2[key]:
            if subkey in d[key]:
                d[key][subkey] += dict_2[key][subkey]
            else:
                d[key][subkey] = dict_2[key][subkey]
    return d

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
        return pd.read_csv(filename, engine='python')
    except:
        return pd.read_csv(filename + '.csv', engine='python')

def save_data_to_csv(filename: str, keys: list, values: list) -> None:
    # makes sure path is good
    if len(filename) <= 4 or filename[-4:] != '.csv':
        filename += '.csv'
    df = make_df(keys, values)
    df.to_csv(filename, index=False) 
    return

def make_df(keys: list, values: list) -> pd.core.frame.DataFrame:
    '''converts the two lists into a dataframe object'''
    dic = dict()
    for i, key in enumerate(keys):
        dic[key] = values[i]
    return pd.DataFrame(dic)

# time 
def readable_to_sec(t: str) -> int:
    '''returns the readable time in seconds
        returns False if unable to convert t'''
    try:
        return sum(int(x) * 60 ** i for i, x in enumerate(reversed(t.split(':'))))  
    except:
        return False

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

# maintenance
def clean_up() -> None:
    '''cleans the autogen image and game report powerpoint folders
        will raise an exception if unable to remove (most likely due to it being open)'''
    os.chdir('powerpointer\matchrapporter')
    for f in os.listdir(os.getcwd()):
        try:
            os.remove(f)
        except Exception as e:
            print(e)
    os.chdir('..\\säsongsrapporter')
    for f in os.listdir(os.getcwd()):
        try:
            os.remove(f)
        except Exception as e:
            print(e)
    os.chdir('..\\..\\bilder\\autogen')
    for f in os.listdir(os.getcwd()):
        try:
            os.remove(f)
        except Exception as e:
            print(e)
    os.chdir('..\\..')
    return

# get data from constats
def get_logo_image(team: str) -> str:
    '''returns the logo of team
        if team does not have one returns opponent logo'''
    try:
        return constants.logos[team]    
    except KeyError:
        return constants.logos['opponent']

def get_nickname(team: str, length: str) -> str:
    '''returns the nickname of type length for team
        if team does not have one returns oppponent nickname'''
    try:
        return constants.nicknames[team][length]
    except KeyError:
        return constants.nicknames['opponent'][length]
    
def get_player_info(player: str, info_type: str) -> str:
    '''returns the info_type for said player
        if player not in constants.players returns placeholder info
        will convert to string if need be'''
    if type(player) == int:
        player = str(player)
    try:
        return constants.players[player][info_type]
    except KeyError:
        return constants.players['placeholder'][info_type]
    
def get_colors(team: str, index: int) -> tuple:
    '''returns the color of team
        if team does not have one returns opponent color'''
    try:
        return constants.colors[team][index]
    except KeyError:
        return constants.colors['opponent'][index]
    
def readable_number(num: int) -> str:
    '''returns num as readable'''
    try:
        return constants.readable_numbers[num]
    except KeyError:
        return str(num)

# manually check csv files
def control_time(filename: str) -> None:
    '''runs through the csv and checks that the timesstamps are in ascending order'''
    df = read_csv_as_df(filename)

    for i, row in df.iterrows():
        if i != 0 and i != df.shape[0] - 1:
            if row['time'] > df.loc[i+1]['time']:
                print(f'fel på rad {i+2}')
    return