# External Imports
from flask import Blueprint

# Blueprint Imports
base_bp = Blueprint(
    'base_bp',
    __name__,
    url_prefix='/'
)

from . import views # noqa

__all__ = (
    "views",
)
