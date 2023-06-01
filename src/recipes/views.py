# External Imports
from flask import (
    render_template,
)

# Local Imports
from recipes import recipes_bp


@recipes_bp.route('/', methods=['GET'])
def get_recipes() -> str:
    """
    Returns a list of recipes.
    """
    return render_template(
        'recipes/catalog/catalog.html'
    )
