from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db, bcrypt
from app.forms import UpdateProfileForm, ChangePasswordForm
from app.models import User

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')

@profile_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = UpdateProfileForm(obj=current_user)

    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile.index'))

    return render_template('profile.html', form=form)

@profile_bp.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()

    if form.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password_hash, form.old_password.data):
            new_password_hash = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
            current_user.password_hash = new_password_hash
            db.session.commit()
            flash('Password updated successfully!', 'success')
            return redirect(url_for('profile.index'))
        else:
            flash('Old password is incorrect.', 'danger')

    return render_template('change_password.html', form=form)
