{% extends "base.html" %}

{% block title %}Profile{% endblock %}

{% block content %}
<div class="container">
    <div class="card">
        <h2 class="roboto-bold">Update Profile</h2>
        <form method="POST" action="{{ url_for('profile.index') }}">
            {{ form.hidden_tag() }}

            <div class="form-group">
                {{ form.first_name.label(class="roboto-medium") }}
                {{ form.first_name(class="form-control") }}
            </div>

            <div class="form-group">
                {{ form.last_name.label(class="roboto-medium") }}
                {{ form.last_name(class="form-control") }}
            </div>

            <div class="form-group">
                {{ form.submit(class="primary-btn") }}
            </div>
        </form>
    </div>
</div>
{% endblock %}
