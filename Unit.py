# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:25:30 2019

@author: Jamesrulz
"""

import Map

class Army:
    ''' the standard unit for the game Diplomacy '''    
    
    def __init__(self, position):
        if position in Map.Map.validTerritories():
            self.position = position
        else:
            return "not a valid territory"
        
    def __str__(self):
        return self.position