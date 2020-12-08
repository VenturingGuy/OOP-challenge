import random

class Pilot:
    def __init__(self, name, determination, grit, intuition, kills, newtype_status):
        self._name = name
        self._determination = determination
        self._grit = grit
        self._intuition = intuition
        self._kills = kills
        self._newtype_status = newtype_status

    def ace_bonus(self):
        if self._kills > 50:
            self._determination += 2
        
    def newtype_checker(self):
        if self._newtype_status == True:
            self._intuition += 1

class Robot:

    def __init__(self, unit, starting_health, atk, armor, evasion, weapons, pilot=Pilot("", 0, 0, 0, 0, False)):
        self._unit = unit
        self._pilot = pilot
        self.__starting_health = starting_health
        self.__current_health = starting_health
        self._atk = atk
        self._armor = armor
        self._evasion = evasion
        self._weapons = weapons

    def pilot_adjust(self):
        print(f'{self._unit} is a Robot piloted by {self._pilot._name}.')
        self._pilot.ace_bonus()
        self._pilot.newtype_checker()
        self._atk = self._atk + (self._pilot.determination * 10)
        self._armor = self._armor + (self._pilot.grit * 10)
        self._evasion = self._evasion + (self._pilot.intuition * 10)

    def fight(self, opponent):
        # Robot A Fights Robot B 
        
        ''' 
        Fail Safe: If neither unit has attacks (ie dummy units), print "Draw"
        Otherwise, else, both sides will fight until someone has won.
        After each fight, neither, one, or both will take damage.
        Then, the program checks if either self or opponent is alive.
        If one is dead, the winner is announced.
        '''

        if not self._weapons or not opponent._weapons:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                if opponent.evasion_check() == False:
                    opponent.take_damage(self.attack(opponent))
                    if opponent.is_alive() == False:
                        print(self._pilot._name + " has won!")
                        self.add_kill(1)
                if self.evasion_check() == False:
                    self.take_damage(opponent.attack(self))
                    if self.is_alive() == False:
                        print(opponent._pilot._name + " has won!")
                        opponent.add_kill(1)


    def attack(self, opponent):
        # Starts total damage at 0.
        total_damage = 0
        total_damage = (self._atk - opponent._armor)
        if total_damage < 0:
            total_damage = 0
        # Returns the total damage.
        return total_damage

    def evasion_check(self):
        checker = random.randint(1, 100)
        if self._evasion > checker:
            return True
        else:
            return False
        
             
    def take_damage(self, damage):
        # Updates self.current_health to reflect damage dealt.

        self.__current_health -= damage

    def is_alive(self):
        '''
        Returns True or False depending on whether the unit is destroyed or not.
        i.e, is its current health above 0 or not?
        ''' 
        if self.__current_health <= 0:
            return False
        else:
            return True
            
    def add_kill(self, num_kills):
        # Update self.kills by num_kills amount
        self._pilot._kills += num_kills


class superRobot(Robot):

    def __init__(self, unit, starting_health, atk, armor, evasion, weapons, pilot=Pilot("", 0, 0, 0, 0, False)):
        super().__init__(unit, starting_health, atk, armor, evasion, weapons, pilot)
        self.type = "Super"
        self.size = "Large"

    def pilot_adjust(self):
        print(f'{self._unit} is a {self.type} Robot piloted by {self._pilot._name}.')
        self._atk = self._atk + (self._pilot._determination * 8)
        self._armor = self._armor + (self._pilot._grit * 10)
        self._evasion = self._evasion + (self._pilot._intuition * 8)

    def size_adjust(self):
        if self.size == "Large":
            self._armor += 3
            self._evasion -= 2

class realRobot(Robot):

    def __init__(self, unit, starting_health, atk, armor, evasion, weapons, pilot=Pilot("", 0, 0, 0, 0, False)):
        super().__init__(unit, starting_health, atk, armor, evasion, weapons, pilot)
        self.type = "Real"
        self.size = "Small"
        
    def pilot_adjust(self):
        print(f'{self._unit} is a {self.type} Robot piloted by {self._pilot._name}.')
        self._atk = self._atk + (self._pilot._determination * 10)
        self._armor = self._armor + (self._pilot._grit * 10)
        self._evasion = self._evasion + (self._pilot._intuition * 5)

    def size_adjust(self):
        if self.size == "Small":
            self._armor -= 1
            self._evasion += 2

if __name__ == "__main__":
    Koji = Pilot("Koji", 4, 4, 3, 0, False)

    Mazinger_Z = superRobot("Mazinger Z", 280, 150, 90, 40, "Rocket Punch", Koji)

    Amuro = Pilot("Amuro", 4, 3, 5, 0, True)
    Nu_Gundam = realRobot("Nu Gundam", 130, 140, 40, 60, "Fin Funnels", Amuro)

    Mazinger_Z.pilot_adjust()
    Nu_Gundam.pilot_adjust()

    Mazinger_Z.fight(Nu_Gundam)