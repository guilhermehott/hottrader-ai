# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 05:20:49 2019

@author: Guilherme Hott
"""

# -*- coding: utf-8 -*-

with open('C:\\trading_data\\{}\\{}.hcc'.format('USIM5','2019'), "rb") as f:
    byte = f.read(1)
    count = 0
    while byte:
        # Do stuff with byte.
        byte = f.read(1)
        if byte != b'\x00':
            print(byte)
        count += 1
        if count == 50:
            break