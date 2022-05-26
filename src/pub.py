class Pub:
    def __init__(self, name, till, food):
        
        self.name = name 
        self.till = till 
        self.drinks = [{
            "name": "vodka", "price":5, "alchol_level":10, "stock":15}, {
            "name": "beer", "price":3, "alchol_level":5, "stock":11
        }, {"name": "cider", "price":8, "alchol_level":2, "stock":9}] 
        self.food = food    



    def increase_till(self, amount):
        self.till += amount 


    def checking_age(self, age):
        if age >= 18:
            return True 
        else:
            return False     
    

    def checking_drunkness(self, drunkness):
        if drunkness > 15:
            return True
        else:
            return False     

    
    def stock_total_value(self):
        stock_total_value = 0 
        for drink in self.drinks:
            drink["price"] * drink["stock"] += stock_total_value
