from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.forms import ProjectForm
from app.models import Project

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

@projects_bp.route('/', methods=['GET'])
@login_required
def index():
    projects = Project.query.filter_by(user_id=current_user.id).all()
    return render_template('projects.html', projects=projects)

@projects_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ProjectForm()

    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            description=form.description.data,
            service_type=form.service_type.data,
            user_id=current_user.id
        )
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('projects.index'))

    return render_template('create_project.html', form=form)

@projects_bp.route('/edit/<int:project_id>', methods=['GET', 'POST'])
@login_required
def edit(project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first_or_404()
    form = ProjectForm(obj=project)

    if form.validate_on_submit():
        project.name = form.name.data
        project.description = form.description.data
        project.service_type = form.service_type.data
        db.session.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('projects.index'))

    return render_template('edit_project.html', form=form, project=project)

@projects_bp.route('/delete/<int:project_id>', methods=['POST'])
@login_required
def delete(project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first_or_404()
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('projects.index'))
