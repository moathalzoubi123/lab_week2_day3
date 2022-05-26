import unittest 
# from src.drinks import Drinks 
from src.customer import Customer
from src.pub import Pub 

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("the prancing pony", 100, "burger")
        self.customer = Customer("andrew" , 400, 25, 0)
        

    def test_pub_has_name(self):  
        self.assertEqual("the prancing pony", self.pub.name)  

    def test_has_till(self):

        # exp value = 100 
        # actual v = ?? (self.pub.till)
        self.assertEqual(100, self.pub.till)  


    def test_increase_till(self):

        # 3 as as of testing 
        # 1 arrange 
        # 2 act 
        # 3 assert 
        self.pub.increase_till(50)
        self.assertEqual(150, self.pub.till)

    def test_customer_age__above_18(self):
        is_18 = self.pub.checking_age(self.customer.age)
        self.assertEqual(True, is_18 )

    def test_checking_drunkness(self):
        is_drunk = self.pub.checking_drunkness(self.customer.drunkness)
        self.assertEqual(False, is_drunk )

    
        
    # def test_customer_age__under_18(self):
    #     is_18 = self.pub.checking_age(self.customer.age)
    #     self.assertEqual(False, is_18 )

    
    def test_stock_total_value(self):
        self.pub.stock_total_value(self)
        self.assertEqual(180, self.pub.stock_total_value())
