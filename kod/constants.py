from pptx.dml.color import ColorFormat, RGBColor

# colors according to: [main, second, third]
# main should be the one best suited for text color (black or white)
colors = {
    'sirius': [RGBColor(0, 0, 0), RGBColor(20, 92, 172), RGBColor(250, 226, 12)],
'villa' : [RGBColor(255, 254, 254), RGBColor(44,45,132), RGBColor(226, 33, 33)],
'aik': [RGBColor(143, 124, 79), RGBColor(7, 41, 74), RGBColor(253, 221, 5)], 
'bollnäs': [RGBColor(243, 135, 85), RGBColor(14, 59, 82), RGBColor(255, 255, 255)],
'broberg': [RGBColor(255, 213, 32), RGBColor(0, 116, 190), RGBColor(0, 0, 0)],
'edsbyn': [RGBColor(228, 179, 78), RGBColor(3, 56, 99), RGBColor(255, 255, 255)],
'frillesås': [RGBColor(254, 222, 1), RGBColor(0, 134, 76), RGBColor(0, 0, 0)],
'gripen': [RGBColor(0, 0, 0), RGBColor(254, 221, 1), RGBColor(255, 255, 255)],
'hammarby': [RGBColor(255, 255, 255,), RGBColor(1, 169, 87), RGBColor(254, 223, 25)],
'motala': [RGBColor(255, 255, 255), RGBColor(0, 74, 146), RGBColor(255, 255, 255)], 
'saik': [RGBColor(255, 255, 255), RGBColor(0, 0, 0), RGBColor(255, 255, 255)],
'vänersborg': [RGBColor(255, 255, 255), RGBColor(0, 90, 155), RGBColor(255, 255, 255)],
'vetlanda': [RGBColor(0, 0, 0), RGBColor(255, 243, 0), RGBColor(0, 0, 0)],
'vsk': [RGBColor(255, 255, 255), RGBColor(1, 130, 72), RGBColor(255, 255, 255)]
}

# logo images wihout relative link 
logos = {
    'aik': 'aik logo.png', 'bollnäs': 'bollnas logo.png', 'broberg': 'broberg logo.png',
    'edsbyn': 'edsbyn logo.png', 'frillesås': 'frillesas logo.png', 'gripen': 'gripen logo.png',
    'hammarby': 'hammarby logo.png', 'motala': 'motala logo.png', 'saik': 'saik logo.png', 
    'sirius': 'sirius logo.png', 'vänersborg': 'vanersborg logo.png', 'vetlanda': 'vetlanda logo.png',
    'villa': 'villa logo.png', 'vsk': 'vsk logo.png'
}

nicknames = {
    'aik' : {'full': 'AIK Bandy', 'short': 'AIK', 'abbreviation': 'AIK'}, 
    'bollnäs' : {'full': 'Bollnäs GIF', 'short': 'Bollnäs', 'abbreviation': 'BGIF'},
    'broberg': {'full': 'Broberg/ Söderhamn Bandy IF', 'short': 'Broberg', 'abbreviation': 'BRO'},
    'edsbyn': {'full': 'Edsbyns IF', 'short': 'Edsbyn', 'abbreviation': 'EIF'},
    'frillesås': {'full': 'Frillesås Bandy', 'short': 'Frillesås', 'abbreviation': 'FBK'},
    'gripen': {'full': 'Gripen Trollhättan BK', 'short': 'Gripen', 'abbreviation': 'GBK'},
    'hammarby': {'full': 'Hammarby IF Bandy', 'short': 'Hammarby', 'abbreviation': 'HIF'},
    'motala': {'full': 'IFK Motala', 'short': 'Motala', 'abbreviation': 'MOT'},
    'vänersborg': {'full': 'IFK Vänersborg', 'short': 'Vänersborg', 'abbreviation': 'VÄN'},
    'sirius': {'full': 'IK Sirius', 'short': 'Sirius', 'abbreviation': 'IKS'},
    'saik' : {'full': 'Sandvikens AIK Bandy', 'short': 'Sandviken', 'abbreviation': 'SAIK'},
    'vetlanda' : {'full': 'Vetlanda BK', 'short': 'Vetlanda',  'abbreviation': 'VBK'},
    'villa': {'full': 'Villa Lidköping BK', 'short': 'Villa Lidköping', 'abbreviation': 'VLBK'},
    'vsk': {'full' : 'Västerås SK Bandy', 'short': 'Västerås', 'abbreviation': 'VSK'}
}

# five colors from dark to light in Sirius blue 
color_scale = [RGBColor(0,55,100), RGBColor(0,74,152), 
                RGBColor(0,85,184), RGBColor(0,154,222), RGBColor(94,179,228)]

readable_numbers = {1: 'en', 2: 'två', 3: 'tre', 4: 'fyra', 5: 'fem', 6: 'sex', 7: 'sju', 8: 'åtta', 9: 'nio', 10: 'tio', 11: 'elva', 12: 'tolv'}