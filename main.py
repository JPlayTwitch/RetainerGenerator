import random
random.seed()
import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import math


import generator
import raceclass

window = tk.Tk()

############################
##### 1. Max retainers #####
############################

def max_retainers():
    max_retainers_calc = intSettlementSize.get()
    if boolTownCrier:
        max_retainers_calc = max_retainers_calc * 1.5
    if boolBadRep:
        max_retainers_calc = max_retainers_calc * 0.5
    return math.ceil(max_retainers_calc)

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

########################
##### 2. Max Level #####
########################

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

# Max level
# Carcass Crawler #2 suggests one-in-six chance for level 1d3+1 character.
# That's too high for my party atm so tunable max
lblMaxLevel = tk.Label(frameMaxLevel,text="Max level:")

spinMaxLevel = tk.Spinbox(frameMaxLevel,from_=2,to=6, state="readonly")


# layout frameMaxLevel
lblLevelChance.grid(column=0,row=0, pady=5)
comboLevelChance.grid(column=0,row=1, pady=5)
lblMaxLevel.grid(column=0,row=2, pady=5)
spinMaxLevel.grid(column=0,row=3, pady=5)

#############################
##### 3. Location/Class #####
#############################

frameLocation = tk.Frame(frameOptions, bd=2, relief=tk.GROOVE)

# pick if using Location csv or class-specific generation
intLocClass = tk.IntVar(window,1)
radioLocClass1 = tk.Radiobutton(frameLocation, text = "Location:", variable = intLocClass, value=1)
radioLocClass2 = tk.Radiobutton(frameLocation, text = "Class:", variable = intLocClass, value=2)

# If location csv
loc_path = r'locations\silverkeep.csv'

# If class-specific
varSpecClass = tk.StringVar()
comboSpecClass = ttk.Combobox(frameLocation,textvariable=varSpecClass, values=list(generator.dictRetClass.keys()), state="readonly")
comboSpecClass.current(4)

# layout
lblLocClass = tk.Label(frameLocation,text="OR")
radioLocClass1.grid(column=0,row=0, pady=5)
lblLocClass.grid(column=0,row=2,pady=5)
radioLocClass2.grid(column=0,row=3,pady=5)
comboSpecClass.grid(column=0,row=4,pady=5)




########################
##### Do the thing #####
########################

def ret_list():

    if intLocClass.get() == 1: # If class randomised based on location file
        # Import retainer class probability
        df = pd.read_csv(loc_path)
        rc_avail = [str(v) for v in df.rc.values]
        rc_prob = [float(v) for v in df.prob.values]
    else: # If class preselected
        ret_class = comboSpecClass.get()
        print("Class")

    # Choose number of retainers
    num_retainers_max = max_retainers()
    num_retainers = random.randint(1, num_retainers_max)

    level_chance = dictLevelChance[comboLevelChance.get()]
    max_level = int(spinMaxLevel.get())

    stat_block = ""
    for _ in range(num_retainers):

        # select ret_class if based on location csv
        if intLocClass.get() == 1:
            ret_class=random.choices(rc_avail,weights=rc_prob,k=1)[0]

        stat_block += generator.RetGen(ret_class, max_level, level_chance) + "\n\n"

    txtStatBlock.delete("1.0",tk.END)
    txtStatBlock.insert(tk.INSERT,stat_block)

###########################
##### Button & Output #####
###########################
butGenerate = tk.Button(window, text="Recruit", command=ret_list)
txtStatBlock = scrolledtext.ScrolledText(window,height=15,width=80)

##################
##### Layout #####
##################

# Within frameOptions
frameRetainerCount.grid(row=1,column=0)
frameMaxLevel.grid(row=1,column=1)
frameLocation.grid(row=1,column=2)

# Final
frameOptions.grid(row=1,column=0)
butGenerate.grid (row=2, column=0)
txtStatBlock.grid (row=3, column=0)


window.mainloop()