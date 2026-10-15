# todo_api.py
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
todos = [
    {"id": 1, "task": "Learn Flask", "done": False},
    {"id": 2, "task": "Build an API", "done": False},
]
next_id = 3


def find_todo(todo_id):
    return next((t for t in todos if t["id"] == todo_id), None)


def read_fields(*, require_task=False):
    data = request.get_json()  # malformed JSON: 400; non-JSON content type: 415
    if not isinstance(data, dict):
        abort(400, description="Send a JSON object.")
    if require_task or "task" in data:
        task = data.get("task")
        if not isinstance(task, str) or not task.strip():
            abort(400, description="task must be a non-empty string.")
    if "done" in data and not isinstance(data["done"], bool):
        abort(400, description="done must be true or false.")
    return data


@app.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(todos)


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = find_todo(todo_id)
    if todo is None:
        abort(404)
    return jsonify(todo)


@app.route("/todos", methods=["POST"])
def create_todo():
    global next_id
    data = read_fields(require_task=True)
    todo = {"id": next_id, "task": data["task"], "done": data.get("done", False)}
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201


@app.route("/todos/<int:todo_id>", methods=["PATCH"])
def update_todo(todo_id):
    todo = find_todo(todo_id)
    if todo is None:
        abort(404)
    data = read_fields()
    todo["task"] = data.get("task", todo["task"])
    todo["done"] = data.get("done", todo["done"])
    return jsonify(todo)


@app.route("/todos/<int:todo_id>", methods=["PUT"])
def replace_todo(todo_id):
    todo = find_todo(todo_id)
    if todo is None:
        abort(404)
    data = read_fields(require_task=True)
    if set(data) != {"task", "done"}:
        abort(400, description="PUT requires exactly task and done.")
    todo.update(task=data["task"], done=data["done"])
    return jsonify(todo)


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todo = find_todo(todo_id)
    if todo is None:
        abort(404)
    todos = [t for t in todos if t["id"] != todo_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
