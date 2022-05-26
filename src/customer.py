class Customer:
    def __init__(self, customer_name, customer_wallet, age, drunkness):
        self.name = customer_name
        self.wallet = customer_wallet 
        self.age = age
        self.drunkness = drunkness

    def reduce_money(self, amount):
        self.wallet -= amount   

    def drunkness_incrase(self, alchol_level):
        self.drunkness += alchol_level  


    def decrease_drunkness(self, rej):
        return self.drunkness - rej 