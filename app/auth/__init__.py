from flask import Blueprint

auth = Blueprint('auth', __name__)


from . import views
from app.models import User, Role
