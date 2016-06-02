import unittest
from flask import current_app
from app import app, create_app, db, Product, CustomerOrder
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
        product1 = Product(name=name, amount=amount, salesPrice=salesPrice, purchasedPrice=purchasedPrice)
        product2 = Product(name=name2, amount=amount2, salesPrice=salesPrice2, purchasedPrice=purchasedPrice2)
        #order1 = CustomerOrder(product_id=product1.id, timeBrought=datetime.now())
        #order2 = CustomerOrder(product_id=product2.id, timeBrought=datetime.now())
        products = [product1, product2]
        print(products)
        order3 = CustomerOrder(products=products, timeBrought=datetime.now())
        db.session.add(product1)
        db.session.add(product2)
        db.session.add(order3)
        allproducts = order3.products
