VERBOSE = 1
SILENT = 0
MODERATE = 1
DEBUG = 2

INV_LOC = (556, 233, 736, 492)

def debugPrint(string, thresh):
  if (thresh <= VERBOSE):
    print(string)