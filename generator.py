import raceclass
import random
random.seed()

import ret_archetype

def RetGen (ret_class,max_level,level_chance):
    # define retainer object
    ret = ret_archetype.RetArchetype(raceclass.fighter,1,0,0,0,0,0,0,0, "Neutral", "")

    # parse classes
    # this is hideous, fix it
    if ret_class == "Acrobat":
        ret.rc = raceclass.acrobat
    elif ret_class == "Assassin":
        ret.rc = raceclass.assassin
    elif ret_class == "Barbarian":
        ret.rc = raceclass.barbarian
    elif ret_class == "Bard":
        ret.rc = raceclass.bard
    elif ret_class == "Cleric":
        ret.rc = raceclass.cleric
    elif ret_class == "Druid":
        ret.rc = raceclass.druid
    elif ret_class == "Dwarf":
        ret.rc = raceclass.dwarf
    elif ret_class == "Elf":
        ret.rc = raceclass.elf
    elif ret_class == "Fighter":
        ret.rc = raceclass.fighter #not strictly necessary but
    elif ret_class == "Gnome":
        ret.rc = raceclass.gnome
    elif ret_class == "Half-Elf":
        ret.rc = raceclass.half_elf
    elif ret_class == "Halfling":
        ret.rc = raceclass.halfling
    elif ret_class == "Illusionist":
        ret.rc = raceclass.illusionist
    elif ret_class == "Knight":
        ret.rc = raceclass.knight
    elif ret_class == "Magic-User":
        ret.rc = raceclass.magic_user
    elif ret_class == "Paladin":
        ret.rc = raceclass.paladin
    elif ret_class == "Ranger":
        ret.rc = raceclass.ranger
    elif ret_class == "Thief":
        ret.rc = raceclass.thief

    # Chance of higher level than L1
    if level_chance > 0:
        if random.randint(1,level_chance) == 1:
            ret.level = random.randint(1, max_level-1)+1

    # stats
    ret.att_str = max(
        random.randint(1, 6)
        + random.randint(1, 6)
        + random.randint(1, 6),
        ret.rc.min_str)

    ret.att_int = max(
        random.randint(1, 6)
        + random.randint(1, 6)
        + random.randint(1, 6),
        ret.rc.min_int)

    ret.att_wis = max(
        random.randint(1, 6)
        + random.randint(1, 6)
        + random.randint(1, 6),
        ret.rc.min_wis)

    ret.att_dex = max(
        random.randint(1, 6)
        + random.randint(1, 6)
        + random.randint(1, 6),
        ret.rc.min_dex)

    ret.att_con = max(
        random.randint(1, 6)
        + random.randint(1, 6)
        + random.randint(1, 6),
        ret.rc.min_con)

    ret.att_cha = max(
        random.randint(1, 6)
        + random.randint(1, 6)
        + random.randint(1, 6),
        ret.rc.min_cha)

    # get hp modifier from con
    # to do
    con_mod = 0
    if ret.att_cha <= 3:
        con_mod = -3
    elif ret.att_cha <= 5:
        con_mod = -2
    elif ret.att_cha <= 8:
        con_mod = -1
    elif ret.att_cha >= 18:
        con_mod = 3
    elif ret.att_cha >= 16:
        con_mod = 2
    elif ret.att_cha >= 13:
        con_mod = 1

    # calculate hp
    for _ in range(ret.level):
        ret.hp += max(random.randint(1, ret.rc.hd) + con_mod, 1)

    # get weapons, armour, and items
    ret.equipment = "Equip: "
    ret.equipment += random.choice(ret.rc.armour) + ", "
    ret.equipment += random.choice(ret.rc.weapons)
    ret.equipment += ", Backpack, Tinderbox, Waterskin, "
    ret.equipment += str(random.randint(1,3)) + " Torches, "
    ret.equipment += str(random.randint(2, 6)) + " Iron Rations"
    ret.equipment += ret.rc.specitem


    #output

    stat_block = "Level " + str(ret.level) + " " + ret_class + "\n"
    stat_block += "AC [TBD], HP:"
    stat_block += str(ret.hp)
    stat_block += ", THAC0 [As Class], MV [TBD], SV [As Class], "
    stat_block += "AL " + random.choice(ret.rc.alignments)
    stat_block += ", STR " + str(ret.att_str)
    stat_block += ", INT " + str(ret.att_int)
    stat_block += ", WIS " + str(ret.att_wis)
    stat_block += ", DEX " + str(ret.att_dex)
    stat_block += ", CON " + str(ret.att_con)
    stat_block += ", CHA " + str(ret.att_cha)
    stat_block += ", ML [TBD] \n"
    stat_block += ret.equipment

    return stat_block