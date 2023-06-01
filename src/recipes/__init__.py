# External Imports
from flask import Blueprint

# Blueprint Imports
recipes_bp = Blueprint(
    'recipes_bp',
    __name__,
    url_prefix='/recipes'
)

from . import views # noqa

__all__ = (
    "views",
)
