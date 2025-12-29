# class defaults

class RaceClass:
    def __init__(self, hd=6, min_str=0, min_int=0, min_wis=0, min_dex=0, min_con=0, min_cha=0, alignments = None,armour=None, weapons=None, specitem=""):
        # mutable array defaults
        if armour is None:
            armour = ["Leather Armour",
                      "Leather Armour, Shield",
                      "Chainmail",
                      "Chainmail, Shield",
                      "Plate Mail",
                      "Plate Mail, Shield"]
        if weapons is None:
            weapons = ["Battle Axe", "Crossbow + 20 Bolts", "Hand Axe", "Mace",
                       "Pole Arm", "Shortbow + 20 Arrows", "Short Sword", "Silver Dagger",
                       "Sling + 20 Stones", "Spear", "Sword", "War Hammer"]
        if alignments is None:
            alignments = ["Lawful", "Neutral", "Chaotic"]

        # attributes
        self.hd = hd
        self.min_str = min_str
        self.min_int = min_int
        self.min_wis = min_wis
        self.min_dex = min_dex
        self.min_con = min_con
        self.min_cha = min_cha
        self.alignments = alignments
        self.armour = armour
        self.weapons = weapons
        self.specitem = specitem

# Individual classes

acrobat = RaceClass(
    hd=4,
    armour = ["Leather Armour"],
    weapons = ["Pole Arm", "Shortbow + 20 Arrows", "Spear", "Staff"]
)

assassin = RaceClass(
    hd=4,
    armour = ["Leather Armour"],
    alignments = ["Neutral", "Chaotic"]
)

barbarian = RaceClass(
    hd=8,
    min_dex=9,
    armour = ["Leather Armour",
              "Leather Armour, Shield",
              "Chainmail",
              "Chainmail, Shield"]
)

bard = RaceClass(
    min_dex=9,
    min_int=9,
    armour = ["Leather Armour", "Chainmail"],
    weapons = ["Crossbow + 20 Bolts", "Sling + 20 Stones",
               "Short Sword", "Sword"]
)

cleric = RaceClass(
    weapons = ["Mace", "Sling + 20 Stones", "Staff", "War Hammer"],
    specitem = ", Holy Symbol\nSpells: Cleric Spell List"
)

druid = RaceClass(
    armour = ["Leather Armour"],
    weapons = ["Club", "Dagger", "Sling + 20 Stones", "Staff"],
    alignments = ["Neutral"],
    specitem = ", Sprig of Mistletoe\nSpells: Druid Spell List"
)

dwarf = RaceClass(
    hd=8,
    min_con=9
)

elf = RaceClass(
    min_int=9,
    specitem="\nSpells: [Roll on Magic-User table]"
)

fighter = RaceClass(
    hd= 8
)

gnome = RaceClass(
    hd=4,
    min_con=9,
    armour = ["Leather Armour"],
    specitem="\nSpells: [Roll on Illusionist table]"
)

half_elf = RaceClass(
    min_cha=9,
    min_con=9
)

halfling = RaceClass(
    min_con=9
)

illusionist = RaceClass(
    hd=4,
    armour = ["No Armour"],
    weapons = ["Dagger"],
    specitem="\nSpells: [Roll on Illusionist table]"
)

knight = RaceClass(
    hd=8,
    min_con=9,
    min_dex=9,
    weapons = ["Lance", "Short Sword", "Sword", "War Hammer"]
)

magic_user = RaceClass(
    hd=4,
    armour = ["No Armour"],
    weapons = ["Dagger"],
    specitem = "\nSpells: [Roll on Arcane Magic table]"
)

paladin = RaceClass(
    hd= 8,
    min_cha = 9,
    alignments = ["Lawful"],
    specitem = ", Holy Symbol\nSpells: Cleric Spell List"
)

ranger = RaceClass(
    hd=8,
    min_con=9,
    min_wis=9,
    alignments = ["Lawful", "Neutral"],
    specitem = "\nSpells: Druid Spell List"
)

thief = RaceClass(
    hd=4,
    specitem = ", Thieves' Tools"
)