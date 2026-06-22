from flask import Blueprint

auth_bp = Blueprint(
    'auth', 
    _name_, 
    template_folder='../../templates/auth'
    )
from . import routes