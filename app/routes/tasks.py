from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.forms import TaskForm
from app.models import Task, Project

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.route('/<int:project_id>')
@login_required
def index(project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first_or_404()
    tasks = Task.query.filter_by(project_id=project_id).all()
    return render_template('tasks.html', project=project, tasks=tasks)

@tasks_bp.route('/<int:project_id>/create', methods=['GET', 'POST'])
@login_required
def create(project_id):
    form = TaskForm()
    project = Project.query.get_or_404(project_id)
    if form.validate_on_submit():
        task = Task(name=form.name.data, phase=form.phase.data, project_id=project.id)
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('tasks.index', project_id=project.id))
    return render_template('create_task.html', form=form, project=project)
