from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Task
from app.utils.token_required import token_required

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/', methods=['POST'])
@token_required
def create_task(user_id):
    data = request.get_json()
    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        done=data.get('done', False)
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created'}), 201

@task_bp.route('/', methods=['GET'])
@token_required
def get_tasks(user_id):
    tasks = Task.query.all()
    result = []
    for task in tasks:
        result.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done
        })
    return jsonify(result)

@task_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_task(user_id, id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.done = data.get('done', task.done)
    db.session.commit()
    return jsonify({'message': 'Task updated'})


@task_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_task(user_id, id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})
