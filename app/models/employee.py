from .. import db


class Employee(db.Model):
    __tablename__ = 'Employees'
    employee_id = db.Column(db.Integer, primary_key=True, index=True)
    last_name = db.Column(db.String)
    first_name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))

    def __repr__(self):
        return '<Employee %r>' % self.employee_id


