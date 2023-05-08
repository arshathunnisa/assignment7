#list=[jhj -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def credit_card_offer(salary,credit_card_limit):
    if salary<10000:
        credit_limit=salary*.10
    elif salary>=10000 and salary<=30000:
        credit_limit=salary*.30
        return credit_limit
    credit_card_offer(35000,2)
    
    def dmart_discount_offer(purchase_amount,discount):
        if purchase_amount<20000:
            discount=0.2
        elif purchase_amount>=20000 and purchase_amount<=40000:
            discount=0.3
        elif purchase_amount>50000:
            discount=0.4
            return discount
        
        def amazon_offer(product_type,discount):
            if product_type=="electronic":
                discount=0.2
            elif product_type=="cloth":
                discount=0.3
            elif product_type=="footware":
                discount=0.4
                return discount
amazon_offer("footware",1)
        
    
