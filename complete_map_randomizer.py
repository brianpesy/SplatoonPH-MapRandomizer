from random import shuffle
from random import randint
import time

# time.sleep(30)

modes = ["Splat Zones","Tower Control","Rainmaker","Clam Blitz"]
maps = ["Arowana Mall", "Blackbelly Skatepark", "Camp Triggerfish", "Goby Arena", "Humpback Pump Track", "Inkblot Art Academy", "Kelp Dome", "MakoMart", "Manta Maria", "Moray Towers", "Musselforge Fitness", "Piranha Pit", "Port Mackerel", "Shellendorf Institute", "Snapper Canal", "Starfish Mainstage", "Sturgeon Shipyard", "The Reef", "Wahoo World", "Walleye Warehouse"]

ctr = 1
i = 0
doneFlag = False

while ctr < 7:
    i = 0
    j = 0
    while j < 5:
        shuffle(modes)
        shuffle(maps)
        j = j + 1
    print("\n\nBracket ", ctr, " maps are...\n\n")
    print("\n\nProcessing...\n\n")
    time.sleep(10)
    print(".\n")
    time.sleep(10)
    print("..\n")
    time.sleep(10)
    print("...\n\n")
    time.sleep(5)
    if ctr <= 5:
        while i < 3:
            print(modes[i], ", ", maps[i])
            i = i + 1
    if ctr >= 6:
        while i < 5:
            if i == 4:
                oldI = i
                i = randint(0,2)
                print(modes[i], ", ", maps[oldI])
                break
            print(modes[i], ", ", maps[i])
            i = i + 1
    ctr = ctr + 1
