import random

class Pilot:
    def __init__(self, name, determination, grit, intuition, kills):
        self.name = name
        self.determination = determination
        self.grit = grit
        self.intuition = intuition
        self.kills = kills

class Robot:

    def __init__(self, unit, starting_health, atk, armor, evasion, weapons, pilot=Pilot("", 0, 0, 0, 0)):
        self.unit = unit
        self.pilot = pilot
        self.starting_health = starting_health
        self.current_health = starting_health
        self.atk = atk
        self.armor = armor
        self.evasion = evasion
        self.weapons = weapons

    def pilot_adjust(self):
        print(f'{self.unit} is a Robot piloted by {self.pilot.name}.')
        self.atk = self.atk + (self.pilot.determination * 10)
        self.armor = self.armor + (self.pilot.grit * 10)
        self.evasion = self.evasion + (self.pilot.intuition * 10)

    def fight(self, opponent):
        # Robot A Fights Robot B 
        
        ''' 
        Fail Safe: If neither unit has attacks (ie dummy units), print "Draw"
        Otherwise, else, both sides will fight until someone has won.
        After each fight, neither, one, or both will take damage.
        Then, the program checks if either self or opponent is alive.
        If one is dead, the winner is announced.
        '''

        if not self.weapons or not opponent.weapons:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                if opponent.evasion_check() == False:
                    opponent.take_damage(self.attack(opponent))
                    if opponent.is_alive() == False:
                        print(self.pilot.name + " has won!")
                        self.add_kill(1)
                if self.evasion_check() == False:
                    self.take_damage(opponent.attack(self))
                    if self.is_alive() == False:
                        print(opponent.pilot.name + " has won!")
                        opponent.add_kill(1)


    def attack(self, opponent):
        # Starts total damage at 0.
        total_damage = 0
        total_damage = (self.atk - opponent.armor)
        if total_damage < 0:
            total_damage = 0
        # Returns the total damage.
        return total_damage

    def evasion_check(self):
        checker = random.randint(1, 100)
        if self.evasion > checker:
            return True
        else:
            return False
        
             
    def take_damage(self, damage):
        # Updates self.current_health to reflect damage dealt.

        self.current_health -= damage

    def is_alive(self):
        '''
        Returns True or False depending on whether the unit is destroyed or not.
        i.e, is its current health above 0 or not?
        ''' 
        if self.current_health <= 0:
            return False
        else:
            return True
            
    def add_kill(self, num_kills):
        # Update self.kills by num_kills amount
        self.pilot.kills += num_kills


class superRobot(Robot):

    def __init__(self, unit, starting_health, atk, armor, evasion, weapons, pilot=Pilot("", 0, 0, 0, 0)):
        super().__init__(unit, starting_health, atk, armor, evasion, weapons, pilot)
        self.type = "Super"
        self.size = "Large"

    def announce_type(self):
        print(f'{self.unit} is a {self.type} Robot piloted by {self.pilot.name}.')
        self.atk = self.atk + (self.pilot.determination * 8)
        self.armor = self.armor + (self.pilot.grit * 10)
        self.evasion = self.evasion + (self.pilot.intuition * 7)

class realRobot(Robot):

    def __init__(self, unit, starting_health, atk, armor, evasion, weapons, pilot=Pilot("", 0, 0, 0, 0)):
        super().__init__(unit, starting_health, atk, armor, evasion, weapons, pilot)
        self.type = "Real"
        self.size = "Small"
        
    def announce_type(self):
        print(f'{self.unit} is a {self.type} Robot piloted by {self.pilot.name}.')
        self.atk = self.atk + (self.pilot.determination * 8)
        self.armor = self.armor + (self.pilot.grit * 8)
        self.evasion = self.evasion + (self.pilot.intuition * 10)

if __name__ == "__main__":
    Koji = Pilot("Koji", 4, 4, 3, 0)

    Mazinger_Z = superRobot("Mazinger Z", 280, 150, 110, 40, "Rocket Punch", Koji)

    Amuro = Pilot("Amuro", 4, 3, 5, 0)
    Nu_Gundam = realRobot("Nu Gundam", 130, 140, 40, 60, "Fin Funnels", Amuro)

    Mazinger_Z.pilot_adjust()
    Nu_Gundam.pilot_adjust()

    Mazinger_Z.fight(Nu_Gundam)