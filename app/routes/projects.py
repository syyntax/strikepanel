from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.forms import ProjectForm
from app.models import Project

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

@projects_bp.route('/')
@login_required
def index():
    projects = Project.query.filter_by(user_id=current_user.id).all()
    return render_template('projects.html', projects=projects)

@projects_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data, description=form.description.data, service_type=form.service_type.data, user_id=current_user.id)
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('projects.index'))
    return render_template('create_project.html', form=form)
