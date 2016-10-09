from .. import db


class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True, index=True)
    time_brought = db.Column(db.DateTime())
    total_price = db.Column(db.Integer)
    # the user in this case is the gopher
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    order_status = db.Column(db.String)
    shipper_id = db.relationship('Shipping', backref='Order', uselist=False)

    # the one that sells the order for the person (The cashier)

    def __repr__(self):
        return '<Order %r>' % self.order_id


class OrderLine(db.Model):
    __tablename__ = 'order_lines'
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True, nullable=False)
    unit_price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    product_code = db.Column(db.Integer, db.ForeignKey('products.product_code'))
    line_number = db.Column(db.Integer)

    def __repr__(self):
        return '<OrderLine %r>' % self.order_id


class Shipping(db.Model):
    __tablename__ = 'shippers'
    shipper_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), primary_key=True)
    company_name = db.Column(db.String)
    contact_name = db.Column(db.String)
    contact_phone = db.Column(db.String)

    def __repr__(self):
        return '<Shipping %r>' % self.shipper_id


class Payment(db.Model):
    __tablename__ = 'payments'
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False,
                         primary_key=True)
    timeBrought = db.Column(db.DateTime())
    totalPrice = db.Column(db.Integer)

    def __repr__(self):
        return '<Payment %r>' % self.order_id


class Invoice(db.Model):
    __tablename__ = 'invoices'
    id = db.Column(db.Integer, primary_key=True, index=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False,
                         primary_key=True)
    invoice_date = db.Column(db.DateTime())
    invoice_status = db.Column(db.Integer)
    invoice_line_id = db.relationship('InvoiceLine', backref='Invoice', uselist=False)

    def __repr__(self):
        return '<Invoice %r>' % self.id


class InvoiceLine(db.Model):
    __tablename__ = 'invoice_lines'
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id', onupdate='CASCADE', ondelete='CASCADE'),
                           primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    product_code = db.relationship('Product', backref='InvoiceLine')
    unit_price = db.Column(db.Integer)
    units_shipped = db.Column(db.Integer)
    line_number = db.Column(db.Integer)

    def __repr__(self):
        return '<InvoiceLine %r>' % self.invoice_id
