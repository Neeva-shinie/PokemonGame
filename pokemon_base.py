"""
This class is created to initialise all the variable so that when an error occurs it can 
raise an Exception
__name__ Neevashinie
"""
class PokemonBase:
    # An example of a base value for a stat
    BASE_LEVEL = 1 #Constant variable 
    #Initialise all the attribute
    def __init__(self, hp: int, poke_class: str):
        self.hp = hp
        self.level = 1
        self.poke_class = poke_class 
        self.speed = 0
        self.attack= 0
        self.defence= 0
        self.poke_name=""
        self.lose_hp= 0

        #Raises error when invalid input is provided
        if hp < 0:
            raise ValueError("Pika pika!! : Invalid hp")
        if poke_class != "Fire" and poke_class != "Grass" and poke_class != "Water":
            raise TypeError("Pika pika!! : Invalid Poke class")
    """
    Function: Returns pokemon's hp
    Input: no input
    Output: self.hp
    Complexity: O(1) because it only returns the hp of a pokemon
    """
    # returns hp
    # complexity: O(1)    
    def get_hp(self):
        return self.hp
    """
    Function: Returns pokemon's level and raises error if invalid input
    Input: no input
    Output: self.level
    Complexity: O(1) because it only returns the level of a pokemon
    """
    # returns level
    # complexity: O(1)  
    def get_level(self):
        if self.level <= 0:
            raise ValueError("Pika pika!! : Invalid level")
        return self.level

    """
    Function: Returns pokemon's class
    Input: no input
    Output: self.poke_class
    Complexity: O(1) because it only returns the class of a pokemon
    """
    # return poke_class
    # complexity: O(1) 
    def get_poke_class(self):
        return self.poke_class

    """
    Function: Returns true if the pokemon's hp <= 0
    Input: no input
    Output: boolean true or false
    Complexity: O(1) because it only returns a boolean
    """
    #returns true is fainted
    def is_fainted(self):
        faint=False
        if self.hp <= 0:
            faint=True
        return faint

    """
    Function: Level up a pokemon 
    Input: no input
    Output: self.level
    Complexity: O(1) because it only returns the level and has only an arithmatic calculation 
    """
    #return new level    
    def level_up(self):
        self.level = self.BASE_LEVEL + self.level
        return self.level
    """
    Function: Returns pokemon's speed and raises error if invalid input
    Input: no input
    Output: self.speed
    Complexity: O(1) because it only returns the speed of a pokemon
    """
    #returns speed
    def get_speed(self):
        if self.speed <=0:
            raise ValueError("Pika pika!! : Invalid speed")
        return self.speed
    """
    Function: Returns pokemon's attack stat and raises error
    Input: no input
    Output: self.attack
    Complexity: O(1) because it only returns the attack stat of a pokemon
    """
    #returns attack stat
    def get_attack_damage(self):
        if self.attack <=0:
            raise ValueError("Pika pika!! : Invalid attack")
        return self.attack
    """
    Function: Returns pokemon's defence stat and raise error if invalid input
    Input: no input
    Output: self.hp
    Complexity: O(1) because it only returns the defense stat of a pokemon
    """
    #returns defence stat
    def get_defence(self):
        if self.defence <= 0:
            raise ValueError("Pika pika!! : Invalid defence")
        return self.defence

    """
    Function: Returns pokemon's hp after subtracting
    Input: lost_hp,int
    Output: none
    Complexity: O(1) because it only  has arithmatic calculation
    """
    #returns hp after subtracting with lost_hp
    def lose_hp(self,lost_hp:int):
        if lost_hp < 0:
            raise ValueError("Pika pika!! : Invalid value")
        else:
            self.hp=self.hp - lost_hp
    """
    Function: Returns pokemon's defend based on damage
    Input: damage,int
    Output: none
    Complexity: O(1) 
    """
    #returns hp after defending
    def defend(self, damage: int):
        if damage <= 0:
            raise ValueError("Pika pika!!: Invalid damage")
        
    """
    Function: Returns pokemon's hp
    Input: no input
    Output: none
    Complexity: O(1) 
    """
    #returns poke name
    def get_poke_name(self):
        list_of_poke_name =["Charmander","Bulbasaur", "Squirtle"]
        for i in range(0,len(list_of_poke_name)):
            if list_of_poke_name[i]== self.poke_name:
                return self.poke_name
            else: 
                raise TypeError("Pika pika!! : Invalid Poke name")
    """
    Function: returns string with pokemon's hp and level
    Input: no input
    Output: self.hp
    Complexity: O(1) because it a series of if statement
    """
    #Complexity: O(1)
    def __str__(self):
        if self.poke_name == "Charmander": #O(1) boolean 
            return "Charmander's health = " + str(self.hp)+ " and level = " + str(self.level)
        elif self.poke_name == "Bulbasaur":
            return "Bulbasaur's health = "+str(self.hp) +" and level = " +str(self.level)
        else:
            return "Squirtle's health = "+str(self.hp) +" and level = " +str(self.level)
