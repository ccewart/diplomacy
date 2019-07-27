# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 06:47:02 2019

@author: Jamesrulz
"""

import territory

class notTerritoryException(Exception):
    pass

class Map:
    ''' has a name and a list of Territory classes '''
    name = None
    mapTerritory = None
    temp = None
    
    def __init__(self, name, mapTerritory):
        self.name = name
        
        # need the below to stop creation of the class if it doesn't complete
        self.temp = True
        for obj in mapTerritory:
            if isinstance(obj, territory.Territory):
                pass
            else:
                self.temp = False
                
        if self.temp == True:
            self.mapTerritory = []
            self.mapTerritory.extend(mapTerritory)
        else:
            raise notTerritoryException("a map's territories must be of the class Territory")
            
                
        
### random test code        
#x = []
#for i in range(1, 10):
#    x.append(territory.Territory('name', ['lolzor'], 'land', True, 'Me'))