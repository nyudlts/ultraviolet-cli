from flask import Blueprint

blueprint = Blueprint(
    'ultraviolet_cli',
    __name__,
    static_folder='static',
)
