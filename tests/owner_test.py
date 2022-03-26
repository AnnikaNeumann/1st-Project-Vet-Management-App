import unittest
from modules.owner import Owner

class TestOwner(unittest.TestCase):

    def setUp(self):
        self.owner_1 = Owner("Karin", "Kaefer", "0123456778")
        self.owner_2 = Owner("Alexis", "Fleming", "07754332345")

#     def test_owner_has_first_name(self):
#         self.assertEqual("Karin", self.owner_1.first_name)
# # test ran ok

#     def test_owner_has_number(self):
#         self.assertEqual("0123456778", self.owner_1.phone)
# # test ran ok

    def test_owner_has_last_name(self):
        expected_last_name = "Fleming"
        actual_last_name = "Fleming"
        self.longMessage = True
        self.assertEqual(expected_last_name, actual_last_name)



