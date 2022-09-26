"""
This code functions to create and assign team into stack and create and choose the team for battle_mode
__name__Neevashinie
"""
from pokemon import Charmander, Bulbasaur, Squirtle
from stack_adt import ArrayStack

class PokeTeam(Charmander, Bulbasaur, Squirtle):
    LIMIT = 6
    def __init__(self):
        self.name = None
        self.team = None
        self.battle_mode = None
    """
    Function: Ensure the number of pokemon in a team does not exceed
    Input: number of charmanders,bulbasaurs,squirtles
    Output: None
    Complexity: O(1), only uses if statement and some mathematical calculation
    """
    def __correct_team_given(self, charmanders: int, bulbasaurs: int, squirtles: int) -> bool:
        # returns true if the total num of pokemon is equal to or less thn limit,else negative
        total_pokemon = charmanders + bulbasaurs + squirtles
        if int(total_pokemon) <= self.LIMIT:
            if charmanders <= -1 or bulbasaurs <= -1 or squirtles <= -1:
                return False
            else:
                return True
        else:
            return False
    """
    Function: Assign team in either a stack or queue based on battle mode
    Input: name and number of charmanders,bulbasaurs,squirtles
    Output: None
    Complexity: O(n) has a few for loop that used to store the characters
    """
    def __assign_team(self, name: str, charmanders: int, bulbasaurs: int, squirtles: int) -> None:
        if self.battle_mode == 0:
            length=charmanders+bulbasaurs+squirtles
            stack_array = ArrayStack(length)
            self.name = name
            for i in range(0, charmanders):
                p1 = Charmander()
                stack_array.push(p1)
            for i in range(0, bulbasaurs):
                p2 = Bulbasaur()
                stack_array.push(p2)
            for i in range(0, squirtles):
                p3 = Squirtle()
                stack_array.push(p3)
            self.team = stack_array
        # print("here", self.team.peek())
    """
    Function: The main choose team function which calles the correct team and assign team 
    Input: name and battle_mode
    Output:None
    Complexity: O(n) mainly due to assign team complexity
    """
    def choose_team(self, name: str, battle_mode: int) -> None:
        self.name = name
        if battle_mode not in [0, 1]:
            raise ValueError("Battle mode can either be 0 or 1 only")
        self.battle_mode = battle_mode
        print("Trainer " + self.name + "!" + " Choose your team as C B S")
        print("where C is the number of Charmanders \n B is the number of Bulbasaurs \n S is the number of Squirtles")
        c, b, s = input().split(" ")
        C= int(c)
        B= int(b)
        S= int(s)
        correct_team = self.__correct_team_given(C,B,S)
        if correct_team == True:
            self.__assign_team(name,C, B, S)
        else:
            print("Try again!!")
            self.choose_team(name,battle_mode)

    """
    Function: Prints str on pokemon's stat in a team
    Output: self.team
    Complexity: O(1)
    """
    def __str__(self):
        return str(self.team)


if __name__ == '__main__':
    p1 = PokeTeam()
    p1.choose_team("Ash", 0)


    
