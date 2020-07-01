VERBOSITY = 1
SILENT = 0
MODERATE = 1
DEBUG = 2

# All locations are defined in the format x1, y1, x2, y2
# where x1, y1, correpsond to the top left corner and
# x2, y2 correspond to the bottom right corner of the box.
INV_LOC = (562, 240, 730, 492) # Location of inventory in RuneLite client
CLK_BOX = (10, 10, 25, 25) # Interactable square within each inventory grid

def debugPrint(string, thresh):
  if (thresh <= VERBOSITY):
    print(string)