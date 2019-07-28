# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 06:47:02 2019

@author: Jamesrulz
"""

import territory as t
import csv
##with open('mapterritories.csv') as csvfile:
##    readCSV = csv.reader(csvfile, delimiter=',')
##    i = 0
##    for row in readCSV:
##        name, subtype, adjacent, owner, supplyCentre = row[0], row[1], row[2], row[3], row[4]
##        i += 1
##        if i == 3:
##            break



class notTerritoryException(Exception):
    pass

class Map:
    ''' has a name and a list of Territory classes '''
    name = None
    territories = []
    temp = None
    
    
    def __init__(self, name, filename):
        self.name = name

        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            next(readCSV)
            i = 0
            for row in readCSV:
                name, subtype, adjacent, owner = row[0], row[1], row[2], row[3]
                supplyCentre = True if row[4]=='y' else False
                self.territories.append(t.Territory(name, subtype, adjacent, owner, supplyCentre))
                i += 1
                if i == 3:
                    break

        for territory in self.territories:
            print(territory)
        # need the below to stop creation of the class if it doesn't complete
##        self.temp = True
##
##               
##        for obj in territories:
##            if isinstance(obj, territory.Territory):
##                pass
##            else:
##                self.temp = False
##                
##        if self.temp == True:
##            self.territories = []
##            self.territories.extend(territories)
##        else:
##            raise notTerritoryException("a map's territories must be of the class Territory")
            
newMap = Map('Europe', 'mapterritories.csv')
