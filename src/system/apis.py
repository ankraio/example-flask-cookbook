# External Imports
from flask import jsonify

# Local Imports
from system import system_bp


@system_bp.route('/health', methods=['GET'])
def get_health() -> str:
    """
    Returns a list of recipes.
    """
    return jsonify(
        {
            'status': 'healthy'
        }
    )
