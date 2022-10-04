# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 09-22-2022
# Description: Unit testing for LemonadeStand.py

import unittest
from LemonadeStand import MenuItem
from LemonadeStand import SalesForDay
from LemonadeStand import LemonadeStand
from LemonadeStand import InvalidSalesItemError
class TestMenuItem(unittest.TestCase):
    """Unit test for the MenuItem class within LemonadeStand.py"""

    def test_1(self):
        """Testing get_name() method"""
        test_1 = MenuItem("Lemonade", 0.15, 1.00)
        self.assertEqual(item_1.get_name(), "Lemonade")

    def test_2(self):
        """Testing get_wholesale_cost() method"""
        item_1 = MenuItem("Lemonade", 0.15, 1.00)
        self.assertAlmostEqual(item_1.get_wholesale_cost(), 0.15)

    def test_3(self):
        """Testing get_selling_price() method in MenuItem class"""
        item_1 = MenuItem("Lemonade", 0.15, 1.00)
        self.assertAlmostEqual(item_1.get_selling_price(), 1.00)

    def test_4(self):
        """Testing the get_sales_dict() method in SalesForDay class"""
        sales_dict = SalesForDay(sales_dict)
        self._assertEqual(sales_dict.get_sales_dict(), {})
    def test_5(self):
        """Testing get_name() in LemonadeStand class"""
        stand = LemonadeStand("Da' Last Stand")
        self.assertEqual(stand.get_name(), "Da' Last Stand")

    def test_6(self):
        """Testing to check if the InvalidSalesItemError exception is raised"""
        with self.assertRaises(InvalidSalesItemError):
            item_1.enter_sales_for_today()

    def test_7(self):
        """Testing total_profit_for_stand() in LemonadeStand class"""


if __name__ == '__main__':
    unittest.main()