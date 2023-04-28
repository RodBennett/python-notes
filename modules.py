# MODULES
# @syntax for imports

# if imported file is in another directory, example lib, you need to create an __init__.py file in that directory and then impot using lib.fileName

# can import whole files and select function w dot notation:
import lib.functions as functions
functions.hello("Rod")

# import specific functions from file via directory
from lib.functions import hi
hi()

# import via directory (lib)
from lib import functions
functions.hi()



