# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:27:32 2019

@author: Jamesrulz
"""

import Unit

class Player:
    ''' a player that is able to give commands '''
    
    units = []
        
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def createUnit(self, territory):
        self.units.append(Unit.Army(territory))
        
    def listUnits(self):
        return self.units
        