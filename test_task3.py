"""
Testing file for Question 3 of Interview Prac 2

__author__ = "Maria Garcia de la Banda"
__edited__ = "Ben Di Stefano"
__edited__ = "Saksham Nagpal"
__last_modified__ = "29.08.2021"
"""

import unittest
from pokemon import Charmander, Bulbasaur, Squirtle
from poke_team import PokeTeam

class TestTask3(unittest.TestCase):
    SINGLE = False

    def setUp(self):
        self.verificationErrors = []
        self.MaxDiff = None

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = "+str(len(self.verificationErrors)))

    def test__correct_team_given(self):
        t1 = PokeTeam()

        # Test if a (low) valid combination of Pokemon values is accepted
        try:
            self.assertTrue(t1._PokeTeam__correct_team_given(1,1,1), msg = "Stack test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        #Test 1: input == 0
        t1 = PokeTeam()

        # Test if a (low) valid combination of Pokemon values is accepted
        try:
            self.assertTrue(t1._PokeTeam__correct_team_given(2,1,0), msg = "Stack test 2,1,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        #Test2: input more than limit;return False
        t1 = PokeTeam()
        try:
            self.assertFalse(t1._PokeTeam__correct_team_given(2,11,1), msg = "Stack test 2,11,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test3: if input is less than 0; return False
        t1 = PokeTeam()
        try:
            self.assertFalse(t1._PokeTeam__correct_team_given(-1,1,1), msg = "Stack test -1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test__str__(self):
        charmander = "Charmander's health = 7 and level = 1"
        bulbasaur = "Bulbasaur's health = 9 and level = 1"
        squirtle = "Squirtle's health = 8 and level = 1"
        t1 = PokeTeam()
        t1.battle_mode = 0

        # Test if the string representation of the team matches expected output for low unit values
        t1._PokeTeam__assign_team("Ash",1,1,1)
        try:
            self.assertEqual(str(t1),charmander+","+bulbasaur+","+squirtle, msg = "String test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        #Test case 1: 2 Charmander
        charmander = "Charmander's health = 7 and level = 1"
        bulbasaur = "Bulbasaur's health = 9 and level = 1"
        squirtle = "Squirtle's health = 8 and level = 1"
        t1 = PokeTeam()
        t1.battle_mode = 0

        # Test if the string representation of the team matches expected output for low unit values
        t1._PokeTeam__assign_team("Ash",2,1,1)
        try:
            self.assertEqual(str(t1),charmander+","+charmander+","+bulbasaur+","+squirtle, msg = "String test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            
        #Test case 2: no Squirtle
        charmander = "Charmander's health = 7 and level = 1"
        bulbasaur = "Bulbasaur's health = 9 and level = 1"
        squirtle = "Squirtle's health = 8 and level = 1"
        t1 = PokeTeam()
        t1.battle_mode = 0

        # Test if the string representation of the team matches expected output for low unit values
        t1._PokeTeam__assign_team("Ash",1,1,0)
        try:
            self.assertEqual(str(t1),charmander+","+bulbasaur, msg = "String test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask3)
    unittest.TextTestRunner(verbosity=0).run(suite)

