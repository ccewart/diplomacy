class Player:
    ''' defines a player '''
    Factions = {
        0 : 'England',
        1 : 'France',
        2 : 'Germany',
        3 : 'Italy',
        4 : 'Austria',
        5 : 'Russia',
        6 : 'Turkey'
        }
    units = []
    
    class Unit:
        def __init__(self, owner, territory, fleet=False):
            self.owner = owner  # player object
            self.fleet = fleet
            self.territory = territory
    
    def __init__(self, name, faction):
        self.name = name
        if faction not in range(0,7):
            raise ValueError('faction value must be between 0 and 6')
        else:
            self.faction = self.Factions[faction]

        # to do error sheet

    def create_unit(self, territory, fleet=False):
        new_unit = self.Unit(self.name, territory, fleet)
        self.units.append(new_unit)

   
    
        
      
        
     
Jim = Player('jimbo', 6)

print(Jim.name)
print(Jim.faction)

print(Jim.units)
Jim.create_unit('Edinburgh')
print(Jim.units)
for army in Jim.units:
    print(army.owner)
    print(army.territory)


