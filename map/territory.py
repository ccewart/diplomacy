# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 06:47:02 2019

@author: Jamesrulz
"""

class Territory:
    '''defines a territory superclass'''
    ''' a territory is just the unit of earth. It knows nothing about its adjacent territories and only has name.'''
    name = None
    
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class LandTerritory(Territory):
    '''specific features of a territory that is landlocked'''
    #TODO pydip uses __eq__ and __ne__ for instance checking that one territory type isn't another. Look into these
    
class CoastTerritory(Territory):
    '''specific features of a land territory that is on the coast'''
    #TODO
    
class SeaTerritory(Territory):
    '''features of a seabased territory'''
    #TODO