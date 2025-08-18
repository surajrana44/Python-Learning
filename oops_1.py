# oops 

''' 
oops - object
      1> data (attributes,properties)
      2> function(method/behaviour)
'''

# without oops example

warrior_name='thor'
warrior_health=100
warrior_attack=80

mage_name='wanda'
mage_health=80
mage_attack=100

def attack_warrior():
    print(f'warrior attack with full might',warrior_attack)

def attack_mage():
     print(f'mage attack with full might',mage_attack)

attack_warrior()
attack_mage()

# using oops 

class character:
     def __init__(self , name ,health,attack):
          self.name= name
          self.health= health
          self.attack= attack 

     def attack_enemy(self):
          print(f'{self.name} attack with power {self.attack}')

warrior=character('thor',100,80)
mage=character('mage',80,100)

warrior.attack_enemy()
mage.attack_enemy()


        

        