# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 09-22-2022
# Description: Code that contains three classes of menu items, daily sales, and a lemonade stand.

class MenuItem:
    """
    Represents the items that are being sold at the lemonade stand.
    """
    def __init__(self, name, wholesale_cost, selling_price):
        """Initializes menu item names, wholesale cost, and selling price at the lemonade stand."""
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """Get method for name of menu items."""
        return self._name

    def get_wholesale_cost(self):
        """Get method for menu items' wholesale cost"""
        return self._wholesale_cost

    def get_selling_price(self):
        """Get method for menu items' selling price."""
        return self._selling_price

class SalesForDay:
    """
    Represents the sales generated at the lemonade stand for a day.
    """
    def __init__(self, day, sales_dict):
        """Initializes the day and sales dictionary."""
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """Get method for displaying the number of days the lemonade stand has been open"""
        return self._day

    def get_sales_dict(self):
        """Get method that shows the items being sold and their values."""
        return self._sales_dict

class LemonadeStand:
    """
    Represents a lemond stand displaying the store title, the current day, menu items for sale for the day alongside
    their sales.
    """
    def __init__(self, name):
        """Initializes lemonade stand name."""
        self._name = name
        self._current_day = 0
        self._menu_items = {}
        self._sales_for_day = []

    def get_name(self):
        """Get method for lemonade stand name."""
        return self._name

    def add_menu_item(self, item_on_menu):
        """Function that adds menu items to the lemonade stand."""
        item_key = item_on_menu.get_name()
        self._menu_items[item_key] = item_on_menu

    def enter_sales_for_today(self, sales_dict):
        """
        Uses dictionary where keys are the menu items being sold and the values are the number of those items sold at
        the lemonade stand for the day.
        """
        sales_for_today = SalesForDay(self._current_day, sales_dict)
        self._sales_for_day.append(sales_for_today)
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, item_name):
        """Returns the quantity of an item sold at the lemonade stand on a particular day."""
        items_sold_on_day = self._sales_for_day[day]
        sales_dict = items_sold_on_day.get_sales_dict()
        return sales_dict[item_name]

    def total_sales_for_menu_item(self, day, item_name):
        """
        Returns the total number of times an item has been sold for the entirity of however long the lemonade stand has
        been open.
        """
        total_number_of_item_sold = 0
        for days in range(self._current_day):
            total_number_of_item_sold += self.sales_of_menu_item_for_day(day, item_name)
        return total_number_of_item_sold

    def total_profit_for_menu_item(self, item_name):
        """
        Returns the total profit of menu item sold for the entirity of however long the lemonade stand has been open.
        """
        total_item_sale = self.total_sales_for_menu_item(day, item_name)
        menu_item = self._menu_items[item_name]
        total_item_profit =
        return total_item_profit

    def total_profit_for_stand(self):
        """
        Returns the total profit on all items sold over the entirity of however long the lemonade stand has been open.
        """
        pass

def main():
    stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand callled 'Lemons R Us'
    item1 = MenuItem('lemonade', 0.5,
                     1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
    stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
    item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
    stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
    item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
    stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'

    #print(stand._menu_items)

    # This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori was sold
    day_0_sales = {
        'lemonade' : 5,
        'cookie'   : 2
    }

    stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
    print(stand.total_profit_for_menu_item("lemonade"))
if __name__ == "__main__":
    main()