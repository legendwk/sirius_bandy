from pptx.dml.color import ColorFormat, RGBColor

# colors according to: [main, second, third]
# main should be the one best suited for text color (black or white)
colors = {
    'iks': [RGBColor(0, 0, 0), RGBColor(20, 92, 172), RGBColor(250, 226, 12)],
'villa' : [RGBColor(255, 254, 254), RGBColor(44,45,132), RGBColor(226, 33, 33)],
'aik': [RGBColor(143, 124, 79), RGBColor(7, 41, 74), RGBColor(253, 221, 5)], 
'bol': [RGBColor(243, 135, 85), RGBColor(14, 59, 82), RGBColor(255, 255, 255)],
'bro': [RGBColor(255, 213, 32), RGBColor(0, 116, 190), RGBColor(0, 0, 0)],
'eds': [RGBColor(228, 179, 78), RGBColor(3, 56, 99), RGBColor(255, 255, 255)],
'fri': [RGBColor(254, 222, 1), RGBColor(0, 134, 76), RGBColor(0, 0, 0)],
'gri': [RGBColor(0, 0, 0), RGBColor(254, 221, 1), RGBColor(255, 255, 255)],
'ham': [RGBColor(255, 255, 255,), RGBColor(1, 169, 87), RGBColor(254, 223, 25)],
'mot': [RGBColor(255, 255, 255), RGBColor(0, 74, 146), RGBColor(255, 255, 255)], 
'saik': [RGBColor(255, 255, 255), RGBColor(0, 0, 0), RGBColor(255, 255, 255)],
'vän': [RGBColor(255, 255, 255), RGBColor(0, 90, 155), RGBColor(255, 255, 255)],
'vet': [RGBColor(0, 0, 0), RGBColor(255, 243, 0), RGBColor(0, 0, 0)],
'vsk': [RGBColor(255, 255, 255), RGBColor(1, 130, 72), RGBColor(255, 255, 255)],
'opponent': [RGBColor(255, 255, 255), RGBColor(255, 255, 255), RGBColor(255, 255, 255)],
'rät' : [RGBColor(255, 255, 255), RGBColor(31, 80, 166), RGBColor(255, 255, 255)]

}

# logo images wihout relative link 
logos = {
    'aik': 'aik logo.png', 'bol': 'bollnas logo.png', 'bro': 'broberg logo.png',
    'eds': 'edsbyn logo.png', 'fri': 'frillesas logo.png', 'gri': 'gripen logo.png',
    'ham': 'hammarby logo.png', 'mot': 'motala logo.png', 'saik': 'saik logo.png', 
    'iks': 'sirius logo.png', 'vän': 'vanersborg logo.png', 'vet': 'vetlanda logo.png',
    'villa': 'villa logo.png', 'vsk': 'vsk logo.png', 'opponent': 'bandyförbundet logo.png',
    'rät': 'rattvik logo.png'
}

nicknames = {
    'aik' : {'full': 'AIK Bandy', 'short': 'AIK', 'abbreviation': 'AIK'}, 
    'bol' : {'full': 'Bollnäs GIF', 'short': 'Bollnäs', 'abbreviation': 'BGIF'},
    'bro': {'full': 'Broberg/ Söderhamn Bandy IF', 'short': 'Broberg', 'abbreviation': 'BRO'},
    'eds': {'full': 'Edsbyns IF', 'short': 'Edsbyn', 'abbreviation': 'EIF'},
    'fri': {'full': 'Frillesås Bandy', 'short': 'Frillesås', 'abbreviation': 'FBK'},
    'gri': {'full': 'Gripen Trollhättan BK', 'short': 'Gripen', 'abbreviation': 'GBK'},
    'ham': {'full': 'Hammarby IF Bandy', 'short': 'Hammarby', 'abbreviation': 'HIF'},
    'mot': {'full': 'IFK Motala', 'short': 'Motala', 'abbreviation': 'MOT'},
    'vän': {'full': 'IFK Vänersborg', 'short': 'Vänersborg', 'abbreviation': 'VÄN'},
    'iks': {'full': 'IK Sirius', 'short': 'Sirius', 'abbreviation': 'IKS'},
    'saik' : {'full': 'Sandvikens AIK Bandy', 'short': 'Sandviken', 'abbreviation': 'SAIK'},
    'vet' : {'full': 'Vetlanda BK', 'short': 'Vetlanda',  'abbreviation': 'VBK'},
    'villa': {'full': 'Villa Lidköping BK', 'short': 'Villa Lidköping', 'abbreviation': 'VLBK'},
    'vsk': {'full' : 'Västerås SK Bandy', 'short': 'Västerås', 'abbreviation': 'VSK'},
    'opponent' : {'full' : 'Motståndare', 'short': 'Mostståndare', 'abbreviation': 'ANNAN'},
    'rät': {'full': 'IFK Rättvik', 'short': 'Rättvik', 'abbreviation': 'IFKR'}
}

# five colors from dark to light in Sirius blue 
color_scale = [RGBColor(0,55,100), RGBColor(0,74,152), 
                RGBColor(0,85,184), RGBColor(0,154,222), RGBColor(94,179,228)]

readable_numbers = {
    1: 'en', 2: 'två', 3: 'tre', 4: 'fyra', 5: 
    'fem', 6: 'sex', 7: 'sju', 8: 'åtta', 9: 'nio', 
    10: 'tio', 11: 'elva', 12: 'tolv'
    }

expected_goals = {
    'centralt': 0.2, 'friställande': 0.5384615384615384, 
    'inlägg': 0.21505376344086022, 'fast': 0.13069908814589665, 
    'retur': 0.29577464788732394, 'dribbling': 0.19642857142857142, 
    'utifrån': 0.05263157894736842, 'straff': 0.8
}



players = {
    '13' : {
        'name': 'Anton Andersson', 'position': 'målvakt', 'image' : 'anton.png'
    },
    '80' : {
        'name': 'Axel Götlin', 'position': 'målvakt', 'image' : 'axel.png'
    },
        '12' : {
        'name': 'Oscar Qvist', 'position': 'försvarare', 'image' : 'qvist.png'
    }, 
        '15' : {
        'name': 'Jerker Ortman', 'position': 'försvarare', 'image' : 'jerke.png'
    },
        '40' : {
        'name': 'Sune Gustafsson', 'position': 'försvarare', 'image' : 'sune.png'
    },
        '2' : {
        'name': 'Stefan Kröller', 'position': 'försvarare', 'image' : 'kröller.png'
    },
        '6' : {
        'name': 'David Thorén', 'position': 'ytterhalv', 'image' : 'davva.png'
    },
        '61' : {
        'name': 'Ted Haraldsson', 'position': 'ytterhalv', 'image' : 'harald.png'
    },
        '7' : {
        'name': 'Jimmy Jansson', 'position': 'mittfältare'
    },
        '17' : {
        'name': 'Nils Bergström', 'position': 'mittfältare', 'image' : 'nisse.png'
    },
        '39' : {
        'name': 'Arvid Tapper', 'position': 'mittfältare', 'image' : 'arvid.png'
    },
        '10' : {
        'name': 'Ted Bergström', 'position': 'anfallare', 'image' : 'tedb.png'
    },
        '11' : {
        'name': 'Albin Thomsen', 'position': 'anfallare', 'image' : 'albin.png'
    },
        '20' : {
        'name': 'Kalle Mårtensson', 'position': 'anfallare', 'image' : 'kalle.png'
    },
        '70' : {
        'name': 'Colin Dahlberg', 'position': 'anfallare', 'image' : 'colin.png'
    }, 
        '66' : {
        'name': 'Alexander Karlgren', 'position': 'mittfältare' 
    },
        '98' : {
        'name': 'Alexander Härndahl', 'position': 'anfallare'
    },
        '9' : {
        'name': 'Emil Eskhult', 'position': 'anfallare'
    },
        '88' : {
        'name' : 'Samuel Heeger', 'position': 'anfallare'
    }
}