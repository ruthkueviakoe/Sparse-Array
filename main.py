import math
import os
import random
import re
import sys

from SparseArray import *

query_res = SparseArray(os.environ['strings'].split(","))

print(query_res.matchingStrings((sys.argv[1].split(','))))
