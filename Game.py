# sup fam

# testing out my git

# another sneaky testarino


# a user can have zero or more armies. How we do we go about doing this?
class Player:
    player_armies = [] # can we store the armies of a player with a dictionary of locations and a 1 or 0 indicating if they have an army there or not?    
    
    def __init__(self, name = None):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_name(self, playername):
        self.name = playername
        return ("Player name is now %s" % self.name)
    
    def add_army(self):
        self.player_armies.append(Army())
    
class Army:
    def __init__(self):
        self.name = 'Army'
        
class Map:
    
    
    

