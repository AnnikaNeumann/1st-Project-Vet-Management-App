import unittest
from modules.animal import Animal
from modules.owner import Owner

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal_1= Animal("Elliot", "11092011", "Cat", "Flea treatment")
        self.animal_2=Animal("Gimley", "12121998", "Sheep", "Hip Physio", 38)

    # # def test_animal_has_name(self):
    #     self.assertEqual("Elliot", self.animal_1)

    




# Demonstrate testing in your program. Include in your screenshot(s):
# *Example of a test and the code it is testing
# *The test running but failing to pass (i.e. not a syntax or execution error 
# that prevents the test from being run, but an incorrect test case or logic error that results in the test being marked as failed)
# *Example of the test and the code it is testing, with errors corrected

# *The test running and passing

 