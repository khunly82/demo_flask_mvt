from flask import redirect, render_template, url_for, request
from app import app
from app.models.db.db_model import Task
from app.models.forms.task_form import Task_form
from app.tools.session_scope import session_scope


# Lister toutes les tâches
@app.route('/tasks', methods=['GET'])
def get_tasks():
    with session_scope() as session:
        tasks = session.query(Task).all()
    return render_template('task/tasks.html', tasks=tasks)


# Créer une nouvelle tâche
@app.route('/task/create', methods=['GET', 'POST'])
def create_Task():
    form = Task_form()
    if form.validate_on_submit():
        nouvelle_tache = Task(description=form.description.data)
        with session_scope() as session:
            session.add(nouvelle_tache)
        return redirect(url_for('get_tasks'))
    return render_template('task/create_task.html', form=form)


# Mettre à jour une tâche existante
@app.route('/task/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    form = Task_form()
    with session_scope() as session:
        task = session.query(Task).get(id)
        if not task:
            return redirect(url_for('get_tasks'))

        if request.method == 'POST' and form.validate_on_submit():
            task.description = form.description.data
            session.add(task)
            return redirect(url_for('get_tasks'))

        form.description.data = task.description

    return render_template('task/update_task.html', form=form, task_id=id)


# Supprimer une tâche
@app.route('/task/delete/<int:id>', methods=['POST'])
def delete_task(id):
    with session_scope() as session:
        task = session.query(Task).get(id)
        if task:
            session.delete(task)
    return redirect(url_for('get_tasks'))
