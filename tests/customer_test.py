import unittest 
# from src.drinks import Drinks 
from src.pub import Pub 
from src.customer import Customer
from src.drinks import Drinks
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer= Customer("Tim", 50, 25, 8)
        self.pub = Pub("the prancing pony", 0, "burger")
        self.drinks = Drinks(self.pub.drinks[0]["name"], self.pub.drinks[0]["price"], self.pub.drinks[0]["alchol_level"]) 
        self.food = Food("burger", 18, 5)
   
    def test_customer_has_name(self):
        self.assertEqual("Tim", self.customer.name)  

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet) 


    @unittest.skip("siglirgeirgeriog")
    def test_buy_a_drink(self):
        self.customer.reduce_money(10)
        self.pub.increase_till(10) 

        self.customer.drunkness_incrase(self.drinks.alchol_level)
        self.assertEqual(40, self.customer.wallet)
        self.assertEqual(10, self.pub.till)
        self.assertEqual(10, self.customer.drunkness)

    def test_buy_a_food(self):
        new_drunkness_level = self.customer.decrease_drunkness(self.food.rejuvenation_level)
        self.assertEqual(3 , new_drunkness_level)


   


        