from databattle import json, showJson
import time
import _thread
import threading


lock = threading.Lock()


player1 = {
    'health': 100,
    'recharge': 800,
    'damage': 9
    }

player2 = {
    'health': 100,
    'recharge': 400,
    'damage': 9
    }

class Unit():
    def __init__(self, player):
        self.health = player['health']
        self.recharge = player['recharge']
        self.damage = player['damage']
    def __repr__(self):
        info = 'Health - %d\nRecharge - %d\nDamage - %d'
        values = (self.health, self.recharge, self.damage)
        return info % values
    def __sub__(self, other):
        self.health = self.health - other.damage

class Battle():
    def __init__(self, squad1, squad2):
        self.squad1 = squad1
        self.squad2 = squad2
        
    def hpbar(self, arg):
        return '[' + str((arg.health//5) * '*') + ']'
        
    # метод нанесения урона, выполняющийся асинхронно
    # для каждой из двух армий
    def dmgToEnemy(self, arg1, arg2, arg3, arg4):
        while arg1.health > 0 and arg2.health > 0:
            time.sleep(arg1.recharge / 1000)
            lock.acquire()
            if arg1.health > 0:
                arg2 - arg1
                print('Squad',arg3,'hit ->' ,arg4, arg2.health, end=' ')
                print(self.hpbar(arg2))
                if arg2.health <= 0:
                    print('Squad', arg3, 'is winner\n')
            lock.release()
                    
    def display(self):
        print('Squad 1 -> ' + str(self.squad1.health))
        print('Squad 2 -> ' + str(self.squad2.health))
        
    def fight(self):
        _thread.start_new_thread(self.dmgToEnemy, (self.squad1, self.squad2, 'one', 'Second'))
        _thread.start_new_thread(self.dmgToEnemy, (self.squad2, self.squad1, 'Second', 'one'))
    

playa1 = Unit(player1)
playa2 = Unit(player2)

battle = Battle(playa1, playa2)
battle.fight()









'''
while True:
    time.sleep(1)
    p - n
    n - p
    print('Player1 \n', p.health)
    print()
    print('Player2 \n', n.health)
    if p.health <= 0:
        print('Player2 - Winner')
        break
    elif n.health <= 0:
        print('Player1 - Winner')
        break
    print('='*15)
'''
