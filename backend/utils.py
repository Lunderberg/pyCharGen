#!/usr/bin/env python

import re
import os.path
import sys

def multiple_replace(changes,text):
    regex = re.compile("|".join(re.escape(key) for key in changes))
    try:
        return regex.sub(lambda res:changes[res.group(0)],text)
    except Exception as e:
        print e,changes,text
        raise e

def resource(*args):
    paths = []
    paths.append(os.getcwd())
    paths.append(os.path.dirname(sys.argv[0]))
    if hasattr(sys,'_MEIPASS'):
        paths.append(sys._MEIPASS)
    for path in paths:
        possible = os.path.join(path,*args)
        if os.path.exists(possible):
            return possible
    return None

def listReplace(inputList, a, b, onlyOne = True):
    """
    From a list <inputList>,
      replace a single instance of <a> with <b>.
    Raises a ValueError if <a> is not found, or is found multiple times.
    """
    index = None
    for i,item in enumerate(inputList):
        if index is None and item==a:
            index = i
            if onlyOne:
                break
        elif index is not None and item==a:
            raise ValueError("Multiple copies of {0} were found".format(str(a)))
    if index is None:
        raise ValueError("{0} was not found".format(str(a)))
    inputList[index] = b

