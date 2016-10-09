from .. import db


class Product(db.Model):
    __tablename__ = 'products'
    product_code = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    # købspris
    suggested_unit_price = db.Column(db.Integer)
    # salgspris
    buy_unit_price = db.Column(db.Integer)
    units_in_stock = db.Column(db.Integer)
    units_on_order = db.Column(db.Integer)
    reorder_level = db.Column(db.Integer)
    supplier_id = db.Column(db.Integer)
    order_line = db.relationship('OrderLine', backref='product', uselist=False)
    invoice_line = db.Column(db.Integer, db.ForeignKey('invoice_lines.invoice_id'))
    product_details = db.relationship('ProductDetails', backref='product', uselist=False)

    def __repr__(self):
        return '<Product %r>' % self.product_code


class ProductDetails(db.Model):
    __tablename__ = 'product_details'
    product_code = db.Column(db.Integer, db.ForeignKey('products.product_code'), primary_key=True)
    more_description = db.Column(db.String)
    image = db.Column(db.Integer)
    comment = db.Column(db.String)
    html_description = db.Column(db.String)

    def __repr__(self):
        return '<ProductDetails %r>' % self.product_code


class ProductSupplier(db.Model):
    __tablename__ = 'product_suppliers'
    product_code = db.Column(db.Integer, db.ForeignKey('product_details.product_code'), primary_key=True)
    supplier_id = db.relationship('Supplier', backref='ProductSupplier', uselist=False)
    notes = db.Column(db.String)

    def __repr__(self):
        return '<ProductSupplier %r>' % self.product_code


class Supplier(db.Model):
    __tablename__ = 'suppliers'
    supplier_id = db.Column(db.Integer, db.ForeignKey('product_suppliers.product_code'), primary_key=True, index=True)
    company_name = db.Column(db.String)
    contact_name = db.Column(db.String)
    contact_job_title = db.Column(db.String)
    phone_office = db.Column(db.String)
    phone_mobile = db.Column(db.String)
    email = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    country = db.Column(db.String)
    postal_code = db.Column(db.String)
    home_page = db.Column(db.String)

    def __repr__(self):
        return '<Supplier %r>' % self.supplier_id

