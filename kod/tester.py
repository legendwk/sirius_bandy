import time as t
import random as r 
import string
import matplotlib.pyplot as plt




l = [2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
labels = [str(i) for i in range(len(l))]

plt.bar(labels, l)
plt.ylabel('antal 40-spel')
plt.yticks([i for i in range(max(l) + 1)])
plt.xlabel('matchminut')
plt.title(f'Spridningen av de totalt {sum(l)} "40-spelen"')
plt.margins(x=0.02)

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
    '''