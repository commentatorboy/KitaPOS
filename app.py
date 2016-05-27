import os
from flask import Flask, render_template, session, redirect, url_for, request
from flask.ext.script import Manager, Shell
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask.ext.uploads import UploadSet, IMAGES

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
images = UploadSet('images', IMAGES)
app.debug=True

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64), unique=True)
    salesPrice = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    purchasedPrice = db.Column(db.Integer)
    #supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    #desc = db.Column(db.String(64))
    #the path for the image?
    #image = db.Column(db.String(64))
    #brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))

    def __repr__(self):
        return '<Product %r>' % self.name

def tmpl_show_menu():
    return render_template('base.html')

#insert form
class InsertForm(Form):
    name = StringField('Name of the product', validators=[Required()])
    salesPrice = IntegerField('What is the sales price?', validators=[Required()])
    amount = IntegerField('How many did you brought?', validators=[Required()])
    purchasedPrice = IntegerField('What is the purchased price?', validators=[Required()])
    #supplier = StringField('Name of the supplier', validators=[Required()])
    #desc = StringField('The description of the product')
    #image = FileField('image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    #brand = StringField('Name of the brand', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return tmpl_show_menu()

@app.route('/Insert', methods=['GET', 'POST'])
def insert():
    form = InsertForm()
    if form.validate_on_submit():
        # check for the different classes, to insert into database
        # name,price, amount supplier,desc,image,brand,submit
        product = Product.query.filter_by(name=form.name.data).first()

        if product is None:
            print(form.name)
            product = Product(name=form.name.data, amount=form.amount.data, salesPrice=form.salesPrice.data, purchasedPrice=form.purchasedPrice.data)
            db.session.add(product)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('insert'))
    return render_template('insert.html', form=form, name=session.get('name'),
                           known=session.get('known', False))

@app.route('/Products')
def show():
    products = Product.query.order_by(Product.name).all()
    return render_template('products.html', products=products)

#credits to http://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
@app.route('/formbuy', methods=['POST'])
def buy():
    print("I got it!")
    print(request.form['projectFilepath'])
    return redirect(url_for('index'))

def make_shell_context():
    return dict(app=app, db=db, Product=Product)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()