# External Imports
from flask import Blueprint

# Blueprint Imports
system_bp = Blueprint(
    'system_bp',
    __name__,
    url_prefix='/system'
)

from . import apis # noqa

__all__ = (
    "apis",
)