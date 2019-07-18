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
    '''defines a territory superclass'''
    ''' a territory is just the unit of earth. It knows nothing about its adjacent territories and only has name.'''
    name = None
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    
    def no_duplicate_territories(self, other):
        try:
            assert self.name != other
        except AssertionError:
            print("This territory already exists on the map")
        

class LandTerritory(Territory):
    '''specific features of a territory that is landlocked'''
    coasts = []
    
    def __init(self, name, coastal_territories):
        super().__init__(name)
        self.coastal_territories = coastal_territories
        self.coasts.append(coastal_territories)
        
    
    
#    def check_coasts()
    
    
class CoastTerritory(Territory):
    '''specific features of a land territory that is on the coast'''
    #TODO
    
class SeaTerritory(Territory):
    '''features of a seabased territory'''
    #TODO