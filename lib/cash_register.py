#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount=discount
        self.total=0
        self.items=[]
        self.last_transaction=0
    def add_item(self, title, price, quantity=1):
        self.total+=quantity*price
        self.last_transaction=quantity*price
        i=0
        for i in range(quantity):
            self.items.append(title)

    def apply_discount(self):
       
        if self.discount==0:
            print('There is no discount to apply.')
        else:
            self.total=int((1-(self.discount/100))*self.total)
            print(f"After the discount, the total comes to ${self.total}.")
        
    
    def void_last_transaction(self):
        self.total-=self.last_transaction

        
        