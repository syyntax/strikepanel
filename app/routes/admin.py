from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def index():
    # Placeholder for admin dashboard view
    return render_template('admin.html')
