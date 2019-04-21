from databattle import json



data = {'armies': [{'name': 'Ukraine',
                    'squads': [{'type': 'soldiers',
                                'units': [{'health': 100, 'recharge': 91}]
                                }
                               ]
                    },
                    {'name': 'Russia',
                     'squads': [{'type': 'soldiers',
                                 'units': [{'health':100, 'recharge': 105}]
                                 }
                                ]
                     }
                   ]
        }
                   

armyOne = {'name': 'Ukraine',
                    'squads': [{'type': 'soldiers',
                                'units': [{'health': 100, 'recharge': 91}]
                                }
                               ]
                    }
           


# класс обрабатывающий одну армию
class Army():
    def __init__(self, army):
        self.army = army
        print(army)
    def __repr__(self):
        info = self.army['name']  + ' -> ' + str(len(self.army['squads'])) + ' squads'
        return info



class Battle():
    def __init__(self, armies):
        # цикл ниже, разделяет все армии по
        # отдельным индексам в списке
        self.singlArmy = []
        self.armies = armies
        for x in self.armies['armies']:
            self.singlArmy.append(x)
        print(len(self.singlArmy))
    def __repr__(self):
        info = ''
        for x in self.singlArmy:
            info += x['name'] + '\n'
        return info.strip()
    def __len__(self):
        return len(self.singlArmy)
    def detail(self):
        info = [Army(x) for x in self.singlArmy]
        [print(x) for x in info]
    def start(self):
        pass
