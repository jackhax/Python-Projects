# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:02:29 2020
@author: Adnan Jakati
"""

from time import time

def performance(fn):
    def wrapper(*args,**kwargs):
        t1 = round(time() * 1000)
        result = fn(*args,**kwargs)
        t2 = round(time() * 1000)
        print(f'took {t2-t1} ms')
        return result
    return wrapper