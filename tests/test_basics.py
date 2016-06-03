import unittest
from flask import current_app
from app import app, create_app, db, Product, CustomerOrder, OrderItem
from datetime import datetime
class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    def test_app_exists(self):
        self.assertFalse(current_app is None)
    def test_insert(self):
        name = "pay"
        amount = 111
        salesPrice = 41
        purchasedPrice = 13
        product = Product(name=name, amount=amount, salesPrice=salesPrice, purchasedPrice=purchasedPrice)
        db.session.add(product)
        print(product.amount)
        assert name == product.name
    def test_buy(self):
        #test if the buy button saves the order in database
        #conditions: save all products, and the time.
        name = "pay"
        amount = 111
        salesPrice = 41
        purchasedPrice = 13

        name2 = "pay2"
        amount2 = 1112
        salesPrice2 = 412
        purchasedPrice2 = 132

        #save products
        product1 = Product(name=name, amount=amount, salesPrice=salesPrice, purchasedPrice=purchasedPrice)
        product2 = Product(name=name2, amount=amount2, salesPrice=salesPrice2, purchasedPrice=purchasedPrice2)


        buyAmount = 5
        #save order items
        orderItem1 = OrderItem(product=product1, amount= buyAmount)
        orderItem2 = OrderItem(product=product2, amount= buyAmount)

        orderItems = [orderItem1, orderItem2]

        totalPrice = purchasedPrice+purchasedPrice2

        order3 = CustomerOrder(order_items=orderItems, timeBrought=datetime.now() , totalPrice=totalPrice)
        db.session.add(product1)
        db.session.add(product2)
        db.session.add(orderItem1)
        db.session.add(orderItem2)
        db.session.add(order3)
        allItems = order3.order_items
        print(allItems[0].product.purchasedPrice)
        print(order3.timeBrought)

        #update product.amount for each product in order
        for item in allItems:
            item.product.amount -= buyAmount
        db.session.commit()

