# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 06:47:02 2019

@author: Jamesrulz
"""

class subtypeException(Exception):
    pass

class supplyCentreException(Exception):
    pass

class Territory:
    ''' defines a territory which is the unit that the map consists of '''
    ''' a territory has a name, a set of adjacent territories, a subtype and a flag for supply centre '''
    name = None # name of the territory
    adjacent = None # name of territories adjacent
    subtype = None # land, coast or sea
    supplyCentre = None # boolean flag indicating whether territory is a supply centre or not
    owner = None # the name of the player who owns the territory
    
    def __init__(self, name, subtype, adjacent, owner, supplyCentre):
        self.name = name
        
        self.adjacent = [] # need to enforce that these are only from the list of given territories
        for territories in adjacent:
            self.adjacent.append(territories)
        
        if subtype not in ['Land', 'Sea', 'Coast']: # this doesn't handle if someone inputs multiple or duplicate subtypes
            raise subtypeException('a territory must be of the type land, sea or coast')
        else:
            self.subtype = subtype
            
        if not isinstance(supplyCentre, bool):
            raise supplyCentreException('a territory can only be a supply centre or not be a supply centre')
        else:
            self.supplyCentre = supplyCentre
            
        self.owner = owner # not certain whether this should be owner or whether a territory contains a unit, or both?
    
    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name

    
    def get_adjacent(self):
        return self.adjacent
    
    def get_subtype(self):
        return self.subtype
    
    def get_supplyCentre(self):
        return self.supplyCentre
    
    def get_owner(self):
        return self.owner
