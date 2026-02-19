Quick tool so that I can weight hireling options dependent on my campaign world and specific cities.

I'm using Old-School Essentials so stats are based on that, should be fine for most OSR games with minor updates. There are better generators out there, this is just what works for my game and flexibility.

To add a class:
1. Add it to raceclass.py
2. Override the attributes that differ from default there
3. Make sure to add it to at least one location so that there is a chance that it will come up
4. Add it to dictRetClass in generator.py

To add a location, add a new .csv file to the locations folder including classes and weights, and change loc_path in main.py to point to this instead.

Classes mostly come from Old-School Essentials Advanced.

Some generation steps (esp. equipment) from Carcass Crawler 2, tweaked because a couple torches is enough but you should always have a couple days food when adventuring.

If you are reading this, please buy the above to refer to in more detail.

I don't calculate AC because it is so frequently changed straight away that it doesn't seem worth it. Likewise, only one weapon because folks will equip hirelings quickly too so it feels more like a specialisation.

Haven't done anything with spells because effort for reward seems low for now; we house rule some stuff anyway, you can roll on relevant table if you want something completely random, and manually picking to build a coherent flavour for a character can be more fun.