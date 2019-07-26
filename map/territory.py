# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 06:47:02 2019

@author: Jamesrulz
"""

''' territories should map out the relationships between the three types in a hierchical fashion '''
'''
 This can be implemented through the following rule set adjacencies: list of tuples of names representing adjacent territories. Must be legal:
        * Sea adjacent only to Sea or Coast
        * Coast adjacent only to Sea or Coast
        * Land adjacent only to Land
        * All names must be provided in territory_descriptors
        * No duplicate adjacencies!
'''

class Territory:
    ''' defines a territory which is the unit that the map consists of '''
    ''' a territory has a name and a set of adjacent territories '''
    name = None
    adjacencies = None
    
    def __init__(self, name, adjacencies): # name and adjacency restrictions implemented in map.py
        self.name = name # should probably enforce name restrictions (i.e. only ww1 territory names)
        self.adjacencies = []
        for i in adjacencies:
            self.adjacencies.append(i) # same point as above but for adjacency
        
    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    
    def get_adjacencies(self):
        return self.adjacencies
    
    def no_duplicate_territories(self, other):
        try:
            assert self.name != other
        except AssertionError:
            print("This territory already exists on the map")

territoryList = ['Austria-Hungary', 'England', 'France', 'Germany', 'Italy', 'Russia', 'Turkey']

worldMap = list()

for i in range(len(territoryList)):
    worldMap.append(Territory(territoryList[i], ['none']))
    
    
        
# TODO
# want to implement these when unit types are defined. They should be enforcing movement of certain unit types only

#class LandTerritory(Territory):
#    '''specific features of a territory that is landlocked'''
#        
#class CoastTerritory(Territory):
#    '''specific features of a land territory that is on the coast'''
#    
#class SeaTerritory(Territory):
#    '''features of a seabased territory'''
