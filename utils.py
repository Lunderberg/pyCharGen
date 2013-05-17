#!/usr/bin/env python

import re
import os.path
import sys

def multiple_replace(changes,text):
    regex = re.compile("|".join(re.escape(key) for key in changes))
    return regex.sub(lambda res:changes[res.group(0)],text)

def resource(*args):
    paths = []
    paths.append('.')
    paths.append(os.path.dirname(sys.argv[0]))
    if hasattr(sys,'_MEIPASS'):
        paths.append(sys._MEIPASS)
    for path in paths:
        possible = os.path.join(path,*args)
        if os.path.exists(possible):
            return possible
    return None
