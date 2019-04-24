import pprint
import random
from databattle import data, json
pprint.pprint(data)




class Unit():
    def __init__(self, unit):
        self.health = unit['health']
        self.recharge = unit['recharge']
    def display(self):
        return self.health, self.recharge
    def __repr__(self):
        info = ('Soldier %d hp and %d recharge' % (self.health, self.recharge))
        return info


class Soldier():
    def __init__(self, sold):
        self.soldier = Unit(sold)
        self.experience = 0
        self.hitRating = self.hitR()
        self.damage = self.dmg()
        
    def hitR(self):
        hr = 0.5 * (1 + self.soldier.health/100) * random.randint(50 + self.experience, 100) / 100
        self.hitRating = hr
        return hr

    def dmg(self):
        dm = 0.05 + self.experience / 100
        self.damage = dm
        return dm
    def __repr__(self):
        return str(self.soldier)


class Vehicle():
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.operators = []
        for x in self.vehicle['operators']:
            sold = Soldier(x)
            self.operators.append(sold)
    def __repr__(self):
        return str(self.vehicle)
        
class Squad():
    def __init__(self, squad):
        self.squad = squad
        self.soldiers = []
        self.vehicles = []
        if self.squad['type'] == 'soldiers':
            print("Soldiers")
            for sol in self.squad['units']:
                soldr = Soldier(sol)
                self.soldiers.append(soldr)
        elif self.squad['type'] == 'vehicles':
            print('Vehicles')
            for veh in self.squad['units']:
                vehicle = Vehicle(veh)
                self.vehicles.append(vehicle)
        else:
            print('Not found')
    def __repr__(self):
        info = '\nVehicles - %d; Soldiers - %d' % (len(self.soldiers), len(self.vehicles))
        return info

# класс обрабатывающий одну армию
class Army():
    def __init__(self, army):
        self.army = army
        self.squads = []
    def __repr__(self):
        info = self.army['name']  + ' -> ' + str(len(self.army['squads'])) + ' squads'
        return info
    def __getitem__(self, key):
        return self.army[key]
    def generate(self):
        for squad in self.army['squads']:
            self.squads.append(Squad(squad))



class Countries():
    def __init__(self, armies):
        # цикл ниже, разделяет все армии по
        # отдельным индексам в списке
        self.army = []
        self.armies = armies
        for x in self.armies['armies']:
           
            self.army.append(Army(x))
        print(len(self.army))

    def __getitem__(self, key):
        return self.army[key]

    def __repr__(self):
        return str(self.army)


    

if __name__ == '__main__':
            
    cn = Countries(json)
    ven = {'type': 'vehicles',
                             'units': [{'health': 100,
                                        'operators': [{'health': 100,
                                                       'recharge': 47}],
                                        'recharge': 47},
                                       {'health': 100,
                                        'operators': [{'health': 100,
                                                       'recharge': 58}],
                                        'recharge': 58}]}
    print('*'*10)


    vn = Vehicle(ven['units'][0])
    squ = Squad(ven)
