# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:11:32 2019

@author: Jamesrulz
"""

class Map:
    ''' class for implementing a simple game map '''
    
    territories = ['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE']
    
    def __init__(self):
        self.map_name = 'The New World'
    
    def __str__(self):
        return self.map_name
    
    def validTerritories(self):
        return self.territories
    