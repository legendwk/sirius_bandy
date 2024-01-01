import time as t
import random as r 
import string
import matplotlib.pyplot as plt
import general_functions as gf
import numpy as np
import pandas as pd
import os
from compile_stats import CompileStats





'''

os.chdir(r'C:\Users\viking.nilsson\Desktop')
# Replace this with the path to your directory
directory_path = 'clean'

# Loop through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        print(filename)
        file_path = os.path.join(directory_path, filename)
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        teams = {team for team in df['team'].tolist() if team != '0'}
        opp = teams.difference({'iks'}).pop()

        # Applying the conditions
        df.loc[(df['team'] == 'iks') & (df['event'] == 'utkast'), 'player'] = 13
        df.loc[(df['team'] == opp) & ((df['event'] == 'skott') | (df['event'] == 'mål') | (df['event'] == 'skottyp')), 'player'] = 13

        # Save the modified DataFrame back to the same CSV file
        df.to_csv(file_path, index=False)




if __name__ != '__main__':




# Load the CSV file
df = pd.read_csv(r"C:\Users\viking.nilsson\Desktop\20231201 Vänersborg - IKS halvlek 1.csv")

# Combine the specified columns into a single 'event' column
df['event'] = df[['Event', 'Subevent', 'Zon', 'Lag', 'Spelare']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)

# Create the new DataFrame with 'event' and 'time' columns
new_df = df[['Tid', 'event']].rename(columns={'Tid': 'time'})

# Save the new DataFrame to a new CSV file
new_df.to_csv(r"C:\Users\viking.nilsson\Desktop\20231201 Vänersborg - IKS halvlek 1 raw.csv", index=False)




    # mapparna
    season2223 = 'data\\compile\\säsong 2223'
    regular_season2223 = 'data\\compile\\grundserie 2223'
    all_games = 'data\\compile\\alla'
    cup2223 = 'data\\compile\\cupen 2223'
    all_45_min = 'data\\compile\\45 min'
    outdoors = 'data\\compile\\utomhus'
    indoors = 'data\\compile\\inomhus'
    bad_ice = 'data\\compile\\dålig is'
    playoff2122 = 'data\\compile\\slutspel 2122'
    playoff2223 = 'data\\compile\\slutspel 2223'
    custom = 'data\\compile\\custom'
    inne2223 = 'data\\compile\\inne 2223'
    ute2223 = 'data\\compile\\ute 2223'

    # dataobjekt
    cs = CompileStats(custom)


    header = ['halvlek', 'mål iks', 'mål motståndare', 'xg sirius', 'xg motståndare']#, 
    # 'xg-skillnad', 'bra försvar (xg mot - mål mot)', 'otur frammåt (xg för - mål för)', 
    # 'resultatsskillnad (xg - resultat)']
    values = [list() for i in range(len(header))]

    cs = CompileStats(regular_season2223)

    for game in cs.games:
        half_list = game.out.split('\\')
        half = ' '.join(half_list[2:].pop().split()[1:-1])
        values[0].append(half)
        goals_sirius = sum(game.prints['score']['sirius'].values())
        values[1].append(goals_sirius)
        goals_opp = sum(game.prints['score'][game.opposite_team('sirius')].values())
        values[2].append(goals_opp)
        # goal_diff = goals_sirius - goals_opp
        # values[3].append(goal_diff)
        xg_sirius = round(game.prints['expected goals']['sirius'], 3)
        values[3].append(xg_sirius)
        xg_opp = round(game.prints['expected goals'][game.opposite_team('sirius')], 3)
        values[4].append(xg_opp)
        # xg_diff = xg_sirius - xg_opp
        # values[6].append(xg_diff)
        # defense = xg_opp - goals_opp 
        # values[7].append(defense)
        # efficiency = xg_sirius - goals_sirius
        # values[8].append(efficiency)
        # diff_result = xg_diff - goal_diff 
        # values[9].append(diff_result)



    gf.save_data_to_csv('säsong', header, values)

    print(os.getcwd())
    


    # mål
    goals_sir = np.array(cs.all_stats['goals']['sirius'])
    goals_opp = np.array(cs.all_stats['goals']['opponent'])
    goals_diff = goals_sir - goals_opp


    # dueller och närkamper
    duels_sir = np.array(cs.all_stats['duels']['sirius'])
    duels_opp = np.array(cs.all_stats['duels']['opponent'])
    duels_diff = duels_sir - duels_opp


    print(np.corrcoef(goals_diff, duels_diff))

    scrimmages_sir = np.array(cs.all_stats['scrimmages']['sirius'])
    scrimmages_opp = np.array(cs.all_stats['scrimmages']['opponent'])

    interceptions_sir = np.array(cs.all_stats['interceptions']['sirius'])
    interceptions_opp = np.array(cs.all_stats['interceptions']['opponent'])

    sog_sir = np.array(cs.all_stats['shots on goal']['sirius'])
    sog_opp = np.array(cs.all_stats['shots on goal']['opponent'])

    shots_sir = np.array(cs.all_stats['shot attempts']['sirius'])
    shots_opp = np.array(cs.all_stats['shot attempts']['opponent'])


    
  
    for grabb in cs.all_stats:
        print(grabb)
        print(cs.all_stats[grabb])



    cs_bad_ice = CompileStats(bad_ice)
    cs_custom = CompileStats(custom)
    print(f"dålig is = {cs_bad_ice.stats_summary['long passes']}")
    print(f"utomhus = {cs_custom.stats_summary['long passes']}")


    # dueller
    cs = CompileStats(season2223)
    sir_g, opp_g = cs.all_stats['goals']['sirius'], cs.all_stats['goals']['opponent']
    sir_d, opp_d = cs.all_stats['duels']['sirius'], cs.all_stats['duels']['opponent']

    goal_diff = [sir_g[i] - opp_g[i] for i in range(len(sir_g))]
    duel_diff = [sir_d[i] - opp_d[i] for i in range(len(sir_d))]

    sir_res, op_res = [0,0,0], [0,0,0] # V,O,F
    for i, duels in enumerate(duel_diff):
        if duels > 0:
            if goal_diff[i] > 0:
                sir_res[0] += 1
            if goal_diff == 0:
                sir_res[1] += 1
            else:
                sir_res[2] += 1
        elif duels < 0:
            if goal_diff[i] < 0:
                op_res[0] += 1
            if goal_diff == 0:
                op_res[1] += 1
            else:
                op_res[2] += 1
    
    print(sir_res)
    print(op_res)


    
    teams = {'a','b'}
    strings = 'zxc'
    d = {team: dict() for team in teams}
    li = [(r.choice(list(teams)), r.choice(strings), r.randint(1,10)) for i in range(10)]

    for grabb in li:
        if grabb[1] in d[grabb[0]]:
            d[grabb[0]][grabb[1]] += grabb[2]
        else:
            d[grabb[0]][grabb[1]] = grabb[2]
    print(li)
    print(d)



    os.chdir(r'data\2023\clean')
    df = pd.read_csv('20221209 IK Sirius - Bollnäs GIF halvlek 2 clean.csv')
    goals_df = df.loc[df['event'] == 'mål']

    subevents = goals_df["subevent"].unique()
    teams = {'a','b'}
    d = {team: {subevent: 0 for subevent in subevents} for team in teams}
    print(d)        



    values = {'sirius':[122, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 73, 0, 0, 86, 0, 0, 0, 0, 69, 0, 0, 0, 0, 67, 0, 0, 0, 0, 0, 0, 0, 0, 165, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'frillesås':[0, 0, 0, 0, 0, 148, 0, 0, 181, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 77, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 66, 0, 0, 65, 0, 0, 0]}

    mtv = values['sirius']
    otv = values['frillesås']
    x = np.array([i for i in range(len(mtv))])
    #x = [i for i in]
    xlables = [str(i) if i%3 == 0 else '' for i in range(len(mtv))]

    width = 0.25
    print(f'{len(mtv)}, {len(x)}')
    print(f'{len(otv)}, {len(x)}')

    fig, ax = plt.subplots()
    ax.bar(x - width/2, mtv, width = width, label='sirius')
    ax.bar(x + width/2, otv, width = width, label='frillesås')
    ax.set_xlabel('matchminut')
    ax.set_ylabel('sekunder')
    ax.legend()
    plt.show()



    # string matching
    alpha = string.ascii_lowercase

    N = 100000
    length = 20
    words = [''.join(r.choice(alpha) for i in range(length)) for n in range(N + 1)]
    
    print('string matching with ==')
    t0 = t.time()
    for i in range(N):
        words[i] == words[i]
    t_equals_same = t.time() - t0
    t0 = t.time()
    for i in range(N):
        words[i] == words[i+1]
    t_equals_different = t.time() - t0
    t0 = t.time()
    for i in range(N):
        words[i] == words[i] + 'a'
    t_equals_worst = t.time() - t0
    
    
    print('string matching with set')
    t0 = t.time()
    for i in range(N):
        words[i] in {words[i]}
    t_set_same = t.time() - t0
    t0 = t.time()
    for i in range(N):
        words[i] in {words[i+1]}
    t_set_different = t.time() - t0
    t0 = t.time()
    for i in range(N):
        words[i] in {words[i] + 'a'}
    t_set_worst = t.time() - t0
    

    print(f'word length: {length}')
    print(f'total time with == {t_equals_same + t_equals_different + t_equals_worst} \nwhere same: {t_equals_same} and different: {t_equals_different}, worst case non-equal: {t_equals_worst}')
    print(f'total time with set {t_set_same + t_set_different + t_set_worst} \nwhere same: {t_set_same} and different: {t_set_different}, worst case non-equal: {t_set_worst}')
    
    word length: 20
    total time with == 0.14231657981872559
    where same: 0.04626917839050293 and different: 0.044864654541015625, worst case non-equal: 0.05118274688720703
    total time with set 0.19072270393371582
    where same: 0.06296539306640625 and different: 0.05798149108886719, worst case non-equal: 0.06977581977844238
    
    
    
    
    # plotting

    l = [2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    labels = [str(i) for i in range(len(l))]

    plt.bar(labels, l)
    plt.ylabel('antal 40-spel')
    plt.yticks([i for i in range(max(l) + 1)])
    plt.xlabel('matchminut')
    plt.title(f'Spridningen av de totalt {sum(l)} "40-spelen"')
    plt.margins(x=0.02)

    plt.show()
    '''