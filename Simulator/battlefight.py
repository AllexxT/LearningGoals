import time
import _thread
import threading
import random
import databattle
import battle


lock = threading.Lock()


player1 = {
    'health': 100,
    'recharge': 100,
    }

player2 = {
    'health': 100,
    'recharge': 100,
    }

class Unit():
    def __init__(self, player):
        self.experience = 0
        self.health = player['health']
        self.recharge = player['recharge']
        self.damage = self.dmg()
        self.hitRating = self.hitR()

    def hitR(self):
        hr = 0.5 * (1 + self.health/100) * random.randint(50 + self.experience, 100) / 100
        self.hitRating = hr
        return hr
    
    def dmg(self):
        dmg = 0.05 + self.experience / 100
        self.damage = dmg
        return dmg
    
    def __repr__(self):
        info = 'Health - %d\nRecharge - %d\nDamage - %d'
        values = (self.health, self.recharge, self.damage)
        return info % values
    def __sub__(self, other):
        if self.hitRating > other.hitR():
            self.health = self.health - other.damage
            if self.experience < 50:
                self.experience += 1
        else:
            print('Miss')
            

class Battle():
    def __init__(self, squad1, squad2):
        self.squad1 = squad1
        self.squad2 = squad2
        
    def hpbar(self, arg):
        return '[' + str((arg.health//5) * '*') + ']'
        
    # метод нанесения урона, выполняющийся асинхронно
    # для каждой из двух армий
    def dmgToEnemy(self, sq1, sq2, nameSq1, nameSq2):
        while sq1.health > 0 and sq2.health > 0:
            time.sleep(sq1.recharge / 1000)
            lock.acquire()
            if sq1.health > 0:
                sq2 - sq1
                print('Squad',nameSq1,'hit ->' ,nameSq2, sq2.health)
                if sq2.health <= 0:
                    print('Squad', nameSq1, 'is winner\n')
            lock.release()
                    
    def display(self):
        print('Squad 1 -> ' + str(self.squad1.health))
        print('Squad 2 -> ' + str(self.squad2.health))
        
    def fight(self):
        _thread.start_new_thread(self.dmgToEnemy, (self.squad1, self.squad2, 'Grihi', 'Arsena'))
        _thread.start_new_thread(self.dmgToEnemy, (self.squad2, self.squad1, 'Arsena', 'Grihi'))
    

playa1 = Unit(player1)
playa2 = Unit(player2)

battle = Battle(playa1, playa2)
#battle.fight()









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
