from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.forms import TaskForm
from app.models import Task, Project

# Define the blueprint
tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.route('/<int:project_id>', methods=['GET'])
@login_required
def index(project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first_or_404()
    tasks = Task.query.filter_by(project_id=project_id).all()
    return render_template('tasks.html', project=project, tasks=tasks)

@tasks_bp.route('/<int:project_id>/create', methods=['GET', 'POST'])
@login_required
def create(project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first_or_404()
    form = TaskForm()

    if form.validate_on_submit():
        task = Task(
            name=form.name.data,
            phase=form.phase.data,
            status='pending',
            project_id=project_id
        )
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('tasks.index', project_id=project_id))

    return render_template('create_task.html', form=form, project=project)

@tasks_bp.route('/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(task_id):
    task = Task.query.filter_by(id=task_id).first_or_404()
    project = Project.query.filter_by(id=task.project_id, user_id=current_user.id).first_or_404()
    form = TaskForm(obj=task)

    if form.validate_on_submit():
        task.name = form.name.data
        task.phase = form.phase.data
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('tasks.index', project_id=task.project_id))

    return render_template('edit_task.html', form=form, task=task, project=project)

@tasks_bp.route('/<int:task_id>/delete', methods=['POST'])
@login_required
def delete(task_id):
    task = Task.query.filter_by(id=task_id).first_or_404()
    project = Project.query.filter_by(id=task.project_id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('tasks.index', project_id=task.project_id))
