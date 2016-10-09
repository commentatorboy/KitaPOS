import re
import unittest
from flask import url_for
from app import create_app, db
from app.models import User, Role

class OrderModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_order(self):
        orderItems = []
        productIds = [1,2,3,4,5]
        itemsSold =
        totalPrice = 0
        self.assertTrue(True)