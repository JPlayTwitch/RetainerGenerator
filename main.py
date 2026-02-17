import random
random.seed()
import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import math


import generator

window = tk.Tk()

# 1. Max retainers

def MaxRetainers():
    maxRetainersCalc = intSettlementSize.get()
    if boolTownCrier:
        maxRetainersCalc = maxRetainersCalc * 1.5
    if boolBadRep:
        maxRetainersCalc = maxRetainersCalc * 0.5
    return math.ceil(maxRetainersCalc)

frameOptions = tk.Frame(window)

frameRetainerCount = tk.Frame(frameOptions, bd=2, relief=tk.GROOVE)
frameSettlementSize = tk.Frame(frameRetainerCount)
frameSettlementMod = tk.Frame(frameRetainerCount)

# Settlement size frame
intSettlementSize = tk.IntVar(window,4)
dictSettlementValues = {"City (6)" : 6,
                        "Large Town (4)" : 4,
                        "Small Town (3)" : 3,
                        "Village (1)" : 1}
temp = 1
for (text,value) in dictSettlementValues.items():
    tk.Radiobutton(frameSettlementSize,
                   text = text,
                   variable = intSettlementSize,
                   value = value).grid(row=temp,column=0)
    temp += 1

# Additional modifiers to settlement size
boolTownCrier = tk.BooleanVar()
chkTownCrier = tk.Checkbutton(frameSettlementMod,
                              text = "Town Crier",
                              variable = boolTownCrier)
chkTownCrier.grid(column=0,row=0)

boolBadRep = tk.BooleanVar()
chkBadRep = tk.Checkbutton(frameSettlementMod,
                              text = "Bad Reputation",
                              variable = boolBadRep)
chkBadRep.grid(column=0,row=1)

# layout Max Retainers
lblMaxRecruits = tk.Label(frameRetainerCount,text="Max Recruits:")
lblMaxRecruits.grid(row=0,column=0,pady=10, columnspan=2)
frameSettlementSize.grid(row=1,column=0,padx=1)
frameSettlementMod.grid(row=1,column=1,padx=1)

# 2. Max Level
frameMaxLevel = tk.Frame(frameOptions, bd=2, relief=tk.GROOVE)

#Chance
lblLevelChance = tk.Label(frameMaxLevel,text="Higher level chance:")
varLevelChance = tk.StringVar()
dictLevelChance = {"Always" : 1,
                   "1-in-2" : 2,
                   "1-in-3" : 3,
                   "1-in-4" : 4,
                   "1-in-6" : 6,
                   "1-in-10" : 10,
                   "1-in-12" : 12,
                   "1-in-20" : 20,
                   "Impossible" : 0}

comboLevelChance = ttk.Combobox(frameMaxLevel,textvariable=varLevelChance, values=list(dictLevelChance.keys()), state="readonly")
comboLevelChance.current(4)
lblLevelChance.grid(column=0,row=0)
comboLevelChance.grid(column=0,row=1)


# Max level
# Carcass Crawler #2 suggests one-in-six chance for level 1d3+1 character.
# That's too high for my party atm so tunable max
max_level = 2

loc_path = r'locations\silverkeep.csv'
# Override for location specific weighting


# 3. Import retainer class probability
df = pd.read_csv(loc_path)
rc_avail = [str(v) for v in df.rc.values]
rc_prob = [float(v) for v in df.prob.values]


# 4. Generate retainer list

def RetList():

    num_retainers_max = MaxRetainers()
    num_retainers = random.randint(1, num_retainers_max)

    level_chance = dictLevelChance[comboLevelChance.get()]

    print(level_chance)

    stat_block = ""
    for _ in range(num_retainers):

        # pick a class
        ret_class=random.choices(rc_avail,weights=rc_prob,k=1)[0]

        stat_block += generator.RetGen(ret_class, max_level, level_chance) + "\n\n"

    txtStatBlock.delete("1.0",tk.END)
    txtStatBlock.insert(tk.INSERT,stat_block)

butGenerate = tk.Button(window,text="Recruit",command=RetList)

txtStatBlock = scrolledtext.ScrolledText(window,height=15,width=80)


# Final Layout

frameRetainerCount.grid(row=1,column=0)
frameMaxLevel.grid(row=1,column=1)
frameOptions.grid(row=1,column=0)
butGenerate.grid (row=5, column=0)
txtStatBlock.grid (row=6, column=0)


window.mainloop()