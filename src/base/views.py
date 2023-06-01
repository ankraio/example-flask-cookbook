# External Imports
from flask import (
    render_template,
)

# Local Imports
from base import base_bp


@base_bp.route('/', methods=['GET'])
def home() -> str:
    """
    Returns a list of recipes.
    """
    return render_template(
        'base/home/home.html'
    )
