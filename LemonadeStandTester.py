# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 09-22-2022
# Description: Unit testing for LemonadeStand.py

import unittest
from LemonadeStand import MenuItem
from LemonadeStand import SalesForDay
from LemonadeStand import LemonadeStand

class TestMenuItem(unittest.TestCase):
    """Unit test for the MenuItem class within LemonadeStand.py"""

    def test_1(self):
        """Testing get_name()"""
        test_1 = MenuItem("Lemonade", 0.15, 1.00)
        self.assertEqual(item_1.get_name(), "Lemonade")

    def test_2(self):
        """Testing get_wholesale_cost"""
        item_1 = MenuItem("Lemonade", 0.15, 1.00)
        self.assertAlmostEqual(item_1.get_wholesale_cost(), 0.15)

    def test_3(self):
        """Testing get_selling_price in MenuItem class"""
        item_1 = MenuItem("Lemonade", 0.15, 1.00)
        self.assertAlmostEqual(item_1.get_selling_price(), 1.00)

    def test_4(self):
        """Testing in SalesForDay class"""
    def test_5(self):
        """Testing get_name() in LemonadeStand Class"""
        stand = LemonadeStand("Da' Last Stand")
        self.assertEqual(stand.get_name(), "Da' Last Stand")

    def test_6(self):
        """Testing to verify if InvalidSalesItem is raised"""
        with self.assertRaises(InvalidSalesItem):
            item_1.enter_sales_for_today()

    def lemonade_test_7(self):
        """Testing total_profit_for_stand() in LemonadeStand class"""


if __name__ == '__main__':
    unittest.main()