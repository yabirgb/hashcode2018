population = 50
generations = 50
mutate_vertical_percent = 0.2
mutate_random_percent = 0.2
parent_percent = 0.25

import sys
from photo import Photo
from evolution import Evolution
from individual import Individual

def get_info(filename):

    with open(filename) as f:
        #get the first line of the input
        n = int(f.readline()[:-1])
        
        photos = []
        verticals = 0
        
        for line in f:
            line=line[:-1].split(' ')
            
            if line[0] == 'V':
                verticals+=1
            
            photos.append(Photo(len(photos)), line[0], line[1], set(line[2:]))
        return n, photos, verticals
    
if __name__ == "__main__":
    """
    uso:

    python3 main.py nombre-entrada
    """
    filename = sys.argv[1]

    n, photos, verticals = get_info('input/{}.txt'.format(filename))

    e = evolution.Evolution(population, photos)
    if verticals <=1:
        vertical_mutation = 0
    else:
        vertical_mutation = mutate_vertical_percent

    e.init_params(vertical_mutation, mutate_random_percent, parent_percent)

    for _ in range(generations):
        e.run_generation()

    best = e.best_ever()
    
    with open("output/{}.out".format(filename), "w") as f:

        f.writeline(len(best.slides))
        for s in best.slides:
            f.writeline(' '.join(list(map(str,best.photos))))
