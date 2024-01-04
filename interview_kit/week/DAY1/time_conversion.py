#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s):
    t = int(s.split(":")[0])
    if s.endswith('AM'):
        if s.startswith('12'):
            print(s.replace('12','00').removesuffix('AM'))
        else:
            print(s.removesuffix('AM'))
    else:
        if s.startswith('12'):
            print(s.removesuffix('PM'))
        else:
            print(s.replace(s.split(":")[0], str(t+12)).removesuffix('PM'))


s = input()

timeConversion(s)

