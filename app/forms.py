from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.'),
            Length(max=120)
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, message='Password must be at least 8 characters long.')
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.'),
            Length(max=120)
        ]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class UpdateProfileForm(FlaskForm):
    first_name = StringField(
        'First Name',
        validators=[Length(max=50)]
    )
    last_name = StringField(
        'Last Name',
        validators=[Length(max=50)]
    )
    submit = SubmitField('Update Profile')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(
        'Old Password',
        validators=[DataRequired()]
    )
    new_password = PasswordField(
        'New Password',
        validators=[DataRequired(), Length(min=8)]
    )
    confirm_password = PasswordField(
        'Confirm New Password',
        validators=[
            DataRequired(),
            EqualTo('new_password', message='Passwords must match.')
        ]
    )
    submit = SubmitField('Change Password')

class ProjectForm(FlaskForm):
    name = StringField(
        'Project Name',
        validators=[DataRequired(), Length(max=100)]
    )
    description = TextAreaField(
        'Description',
        validators=[Length(max=500)]
    )
    service_type = SelectField(
        'Service Type',
        choices=[
            ('cloud', 'Cloud Penetration Testing'),
            ('iot', 'IoT Penetration Testing'),
            ('api', 'API Penetration Testing'),
            ('physical', 'Physical Penetration Testing'),
            ('red_team', 'Red Team Assessment')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Save Project')
