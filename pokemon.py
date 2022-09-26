"""
#This class holds the base of the characters in pokemon and their unique attributes
#
__name__Neevashinie
"""
from pokemon_base import PokemonBase

"""
Function: This class hold the Charmanders actual hp, speed, attack and defence and also implements method that changes compared to the ones in the parent class
"""
class Charmander(PokemonBase):
    CLASS_EFFECTIVENESS={"Water":0.5,"Grass":2,"Fire":1}
    def __init__(self):
        super().__init__(7, "Fire")
        self.speed= 8
        self.defence= 4
        self.attack= 6
        self.poke_name="Charmander"

    
    """
    Function: returns attack damage
    Input: none
    Output: parent get_attack_damage
    Complexity: O(1) , only has mathematical calculation
    """    
    def get_attack_damage(self):
        self.attack = self.attack+self.level
        return super().get_attack_damage()
    
    """
    Function: returns defence
    Input:
    Output: parent get_defence
    Complexity: O(1)
    """
    def get_defence(self):
        return super().get_defence()
    
    """
    Function: returns speed after level up
    Input: 
    Output:parent get_speed
    Complexity: O(1)
    """
    def get_speed(self):
        self.speed= self.speed+self.level
        return super().get_speed()
    
    """
    Function: returns defend calculation
    Input: damage, int
    Output: parent defend
    Complexity: O(1)
    """
    def defend(self,damage):
        if damage>self.defence:
            self.hp = self.hp -damage
        else:
            self.hp=self.hp-damage//2
        return super().defend(damage)

    def __str__(self):
        return super().__str__()

    """
    Function: This class hold the Bulbasaur actual hp, speed, attack and defence and also implements method that changes compared to the ones in the parent class
    """
class Bulbasaur(PokemonBase):
    CLASS_EFFECTIVENESS={"Water":2,"Grass":1,"Fire":0.5}
    def __init__(self):
        super().__init__(9, "Grass")
        self.speed= 7
        self.defence=5
        self.attack=5
        self.poke_name="Bulbasaur"
    """
    Function: returns attack damage
    Input: none
    Output: parent get_attack_damage
    Complexity: O(1) , only has mathematical calculation
    """
    def get_attack_damage(self):
        return super().get_attack_damage()
    """
    Function: returns defence
    Input:
    Output: parent get_defence
    Complexity: O(1)
    """
    def get_defence(self):
        return super().get_defence()
    """
    Function: returns speed after level up
    Input: 
    Output:parent get_speed
    Complexity: O(1)
    """
    def get_speed(self):
        self.speed= self.speed+self.level//2
        return super().get_speed()
    """
    Function: returns defend calculation
    Input: damage, int
    Output: parent defend
    Complexity: O(1)
    """
    def defend(self,damage):
        if damage>self.defence+5:
            self.hp = self.hp -damage
        else:
            self.hp=self.hp-damage//2
        return super().defend(damage)
    
    def __str__(self):
        return super().__str__()


    """
    Function: This class hold the Squirtle actual hp, speed, attack and defence and also implements method that changes compared to the ones in the parent class
    """
class Squirtle(PokemonBase):
    CLASS_EFFECTIVENESS={"Water":1,"Grass":0.5,"Fire":2}
    def __init__(self):
        super().__init__(8, "Water")
        self.speed= 7
        self.defence=6
        self.attack=4
        self.poke_name="Squirtle"
    """
    Function: calculate attack damage
    Input: none
    Output: parent get_attack_damage
    Complexity: O(1) , only has mathematical calculation
    """
    def get_attack_damage(self):
        self.attack = self.attack+self.level//2
        return super().get_attack_damage()
    """
    Function: calulate self.defence
    Input:
    Output: parent get_defence
    Complexity: O(1)
    """
    def get_defence(self):
        self.defence=self.defence+self.level
        return super().get_defence()
    """
    Function: returns speed 
    Input: 
    Output:parent get_speed
    Complexity: O(1)
    """
    def get_speed(self):
        return super().get_speed()
    """
    Function: returns defend calculation
    Input: damage, int
    Output: parent defend
    Complexity: O(1)
    """
    def defend(self,damage):
        if damage>self.defence*2:
            self.hp = self.hp -damage
        else:
            self.hp=self.hp-damage//2
        return super().defend(damage)

    def __str__(self):
        return super().__str__()
