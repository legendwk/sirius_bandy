import time as t
import random as r 
import string
import matplotlib.pyplot as plt
import general_functions as gf
import numpy as np


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






if __name__ == '__main__':





    '''
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

    


    # sustained attacks
    teams = {'sirius', 'frillesås'}
    other = {'sirius': 'frillesås', 'frillesås': 'sirius'}
    pl = [('sirius', '0:00:00'), ('frillesås', '0:02:02'), ('sirius', '0:02:23'), (None, '0:03:20'), ('sirius', '0:03:50'), ('frillesås', '0:04:13'), ('sirius', '0:04:24'), (None, '0:04:46'), ('sirius', '0:05:08'), ('frillesås', '0:05:15'), ('sirius', '0:06:16'), ('frillesås', '0:06:23'), ('sirius', '0:07:50'), ('frillesås', '0:08:14'), ('sirius', '0:09:42'), ('frillesås', '0:09:47'), (None, '0:11:04'), ('frillesås', '0:11:40'), ('sirius', '0:11:56'), ('frillesås', '0:12:34'), ('sirius', '0:12:41'), ('frillesås', '0:13:16'), ('sirius', '0:13:27'), (None, '0:13:40'), ('frillesås', '0:14:15'), ('sirius', '0:14:50'), ('frillesås', '0:16:16'), ('sirius', '0:17:07'), ('frillesås', '0:17:59'), (None, '0:18:04'), ('frillesås', '0:18:29'), ('sirius', '0:18:37'), (None, '0:19:18'), ('sirius', '0:19:27'), ('frillesås', '0:19:35'), ('sirius', '0:19:54'), (None, '0:20:18'), ('sirius', '0:20:49'), ('frillesås', '0:21:06'), ('sirius', '0:21:15'), ('frillesås', '0:21:43'), ('sirius', '0:21:55'), ('frillesås', '0:22:26'), ('sirius', '0:23:11'), ('frillesås', '0:23:56'), ('sirius', '0:24:21'), ('frillesås', '0:25:28'), (None, '0:25:54'), ('sirius', '0:26:25'), ('frillesås', '0:26:52'), ('sirius', '0:27:09'), ('frillesås', '0:27:23'), ('sirius', '0:27:42'), ('frillesås', '0:27:45'), (None, '0:28:04'), ('frillesås', '0:28:26'), ('sirius', '0:28:36'), ('frillesås', '0:28:41'), ('sirius', '0:29:10'), ('frillesås', '0:29:35'), ('sirius', '0:30:06'), (None, '0:30:55'), ('sirius', '0:31:19'), ('frillesås', '0:31:25'), (None, '0:31:51'), ('sirius', '0:32:40'), ('frillesås', '0:33:18'), ('sirius', '0:33:56'), ('frillesås', '0:34:08'), ('sirius', '0:34:14'), ('frillesås', '0:34:35'), ('sirius', '0:34:41'), (None, '0:36:16'), ('sirius', '0:36:23'), ('frillesås', '0:37:00'), ('sirius', '0:37:31'), (None, '0:37:52'), ('sirius', '0:38:18'), ('frillesås', '0:38:34'), ('sirius', '0:38:49'), ('frillesås', '0:39:01'), ('sirius', '0:39:09'), ('frillesås', '0:39:30'), ('sirius', '0:39:51'), ('frillesås', '0:39:59'), ('sirius', '0:40:05'), ('frillesås', '0:40:12'), ('sirius', '0:40:40'), ('frillesås', '0:40:46'), ('sirius', '0:40:57'), (None, '0:41:38'), ('sirius', '0:42:06'), ('frillesås', '0:42:19'), ('sirius', '0:43:24'), ('frillesås', '0:43:48'), (None, '0:44:22'), ('frillesås', '0:45:03'), (None, '0:45:10')]  
    #pl = [('sirius', '0:00:00'),('frillesås', '0:00:15'),('sirius', '0:00:20'),(None, '0:00:50'),('sirius', '0:01:00'),('frillesås', '0:01:01'),('sirius', '0:01:10'),('frillesås', '0:02:00'),('sirius', '0:03:00'),(None, '0:03:10'),('frillesås', '0:04:00'),('sirius', '0:06:00'), (None, '0:07:10')]
    tl = {team : [0 for i in range(gf.readable_to_sec(pl[-1][1])//60 + 1)] for team in teams}
    i = 0 
    min_length = 60
    disruption_length = 10
    while i < len(pl) - 1:
        current_team, current_time = pl[i]
        attack_time = 0 
        for j in range(i, len(pl)):
            following_team, following_time  = pl[j]
            # team has the ball
            if following_team == current_team:
                attack_time += gf.readable_to_sec(pl[j+1][1])-gf.readable_to_sec(following_time)
            # other team has the ball
            elif following_team == other[current_team]:
                # they have the ball long enough or get a break in play
                if gf.readable_to_sec(pl[j+1][1])-gf.readable_to_sec(following_time) > disruption_length or pl[j+1][0] == None:
                    break
            else:
                pass
        if attack_time >= min_length:
            tl[current_team][gf.readable_to_sec(current_time)//60] = attack_time
        i = j

    for t in tl:
        print(f'{t}:{tl[t]}')
        
    
    '''