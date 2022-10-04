# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 09-22-2022
# Description: Unit testing for LemonadeStand.py from different methods that derive from the program's classes.

import unittest
from LemonadeStand import MenuItem
from LemonadeStand import SalesForDay
from LemonadeStand import LemonadeStand

class TestMenuItem(unittest.TestCase):
    """Unit test for the MenuItem class within LemonadeStand.py"""
    def test_1(self):
        """Testing for the get_name() method in MenuItem class."""
        item_1 = MenuItem("Lemonade", 0.15, 1.00)
        self.assertEqual(item_1.get_name(), "Lemonade")

    def test_2(self):
        """Testing for the get_wholesale_cost() method in MenuItem class."""
        item_1 = MenuItem("Lemonade", 0.15, 1.00)
        self.assertAlmostEqual(item_1.get_wholesale_cost(), 0.15)

    def test_3(self):
        """Testing for the get_selling_price() method in MenuItem class."""
        item_1 = MenuItem("Lemonade", 0.15, 1.00)
        self.assertAlmostEqual(item_1.get_selling_price(), 1.00)

    def test_4(self):
        """Testing for the get_name() method in LemonadeStand class."""
        stand = LemonadeStand("Da' Last Stand")
        self.assertEqual(stand.get_name(), "Da' Last Stand")

    def test_5(self):
        """Testing for the total_profit_for_menu_item() method in LemonadeStand class."""
        stand = LemonadeStand("Da' Last Stand")
        item_1 = MenuItem("Orangeade", 0.25, 1.25)
        dict_of_sales_day_0 = {"Lemonade": 49, "Limeade": 24, "Orageade": 0}
        stand.enter_sales_for_today(dict_of_sales_day_0)
        self.assertEqual(stand.total_profit_for_stand(), 0)


if __name__ == '__main__':
    unittest.main()