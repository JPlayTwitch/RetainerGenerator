import random
random.seed()
import pandas as pd
import tkinter as tk


import raceclass
import ret_archetype
import generator

window = tk.Tk()

# 1. Variables

# max retainers
# village = 1, small town = 3, large town = 4, city = 6
# +50% if town crier, -50% if bad local reputation
num_retainers_max = 6

# Max level
# Carcass Crawler #2 suggests one-in-six chance for level 1d3+1 character.
# That's too high for my party atm so tunable max
max_level = 2

loc_path = r'locations\silverkeep.csv'
# Override for location specific weighting

# 2. Number of retainers
num_retainers = random.randint(1, num_retainers_max)

# print(num_retainers)


# 3. Import retainer class probability
df = pd.read_csv(loc_path)
rc_avail = [str(v) for v in df.rc.values]
rc_prob = [float(v) for v in df.prob.values]

# print(rc_avail)
# print(rc_prob)

#4. Generate individual retainers

for _ in range(num_retainers):

    # pick a class
    ret_class=random.choices(rc_avail,weights=rc_prob,k=1)[0]

    stat_block = generator.RetGen(ret_class, max_level)
    print(stat_block)
    print()

window.mainloop()