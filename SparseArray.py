import math
import os
import random
import re
import sys

class SparseArray:
    """
    For a given queries list, count the occurence of each element that appears in the strings list
    """
    
    def __init__(self, strings):
        self.strings = strings
    
    
    def matchingStrings(self, queries):
        result = []
        for item in queries:
            nb_item = 0
            for item_bis in self.strings:
                if item == item_bis:
                    nb_item += 1
            result.append(nb_item)
        return dict(zip(queries, result))