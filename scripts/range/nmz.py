import time

from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

PRAYER_LOC = [555, 110, 565, 120]
NINE_LOC = [58, 224, 62, 228]

GRASS_LOC = [100, 100, 350, 350]
GRASS_CLR = [42, 77, 10]

b = OSBrain()

def flick_prayer():
    b.per.moveToBox(PRAYER_LOC, 'fast')
    t.randomSleep(150, 50) 
    b.per.click('left')
    t.randomSleep(250, 25) 
    b.per.click('left')
    t.randomSleep(150, 50) 

def click_on_potion(pot_type=None):
    inv = b.detection.getInventoryStatus()
    # define locations
    overload_loc = range(7)
    absorb_loc = range(7, 27)
    # reference list we want to check against
    if pot_type=='overload':
        check_list = overload_loc
    elif pot_type=='absorb':
        check_list = absorb_loc
    else:
        print("TypeError: click_on_potion: {}".format(pot_type))
        quit()
    for i, item in enumerate(inv):
        if (i in check_list) and item:
            # drink potion
            loc = b.getInvLoc(i)
            b.per.moveToBox(loc, 'fast')
            t.randomSleep(150, 50)
            b.per.click('left')
            t.randomSleep(1200, 200)
            return

    print("WARNING: Could not find anymore potions!")
    if pot_type=='overload':
        quit()
    return

def time_elapsed(target_time, duration):
    time_elapsed = time.time()-target_time
    #print("Time Elapsed: {}".format(time_elapsed))
    if time_elapsed >= duration:
        return True
    return False

o_time = -np.inf
p_time = -np.inf
a_time = -np.inf
m_time = -np.inf
o_duration = 60*5 # 5 minutes
p_duration = 15 # 15 seconds
a_duration = 45
m_duration = 200

nine = np.load("data/nmz_nine.npy")

# while(True):
#     im = b.window.getImage(NINE_LOC)
#     im_arr = np.array(im)
#     plt.figure(1)
#     plt.imshow(nine)
#     plt.figure(2)
#     plt.imshow(im_arr)
#     plt.show()
#     if np.array_equal(nine, im_arr) is False:
#         print("Is not 9XX")
#         click_on_potion('absorb')
#     else:
#         print("All g")
#     t.randomSleep(3000, 200)
# quit()

while(True):
    grass_detected = b.detection.colorSearch(GRASS_LOC, GRASS_CLR)
    if grass_detected:
        print("Detected grass: Quitting")
        quit()
    if time_elapsed(o_time, o_duration):
        click_on_potion('overload')
        o_time = time.time()
    if time_elapsed(p_time, p_duration):
        flick_prayer()
        p_time = time.time()
    im = b.window.getImage(NINE_LOC)
    im_arr = np.array(im)
    if np.array_equal(nine, im_arr) is False and time_elapsed(a_time, a_duration):
        a_time = time.time()
        print("Is not 9XX")
        click_on_potion('absorb')
        t.randomSleep(2000, 150)
    else:
        if time_elapsed(m_time, m_duration):
            b.per.moveToBox([0,0,2000,2000], 'medium')
            m_time = time.time()
        continue


# while(True):

#     nine = np.load("data/nmz_nine.npy")
#     if np.array_equal(nine, im_arr) is False:
#         print("Is not 9XX")
#         click_on_potion('absorb')
#     else:
#         print("Absorption is OK.")
#     t.randomSleep(10000, 800)

# Every 15 seconds, flick the prayer.
# Every 5 minutes, drink an overload

