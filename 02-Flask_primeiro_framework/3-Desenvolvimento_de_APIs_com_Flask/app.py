from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete - Criar, Ler, Atualizar e Deletar
# Tabela: Tarefa

tasks = []
task_id_control = 1 #precisamos criar essa varivel fora da rota para ter o valor salvo

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control  #precisa ser global para conseguir alterar o valor
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data["title"], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks] #cada task dentro da lista tasks, execute task.to_dict() e monte uma nova lista com os resultados
    # adicionar "to_dict()" faz com que sas tarefas já cheguem formatadas, função no arquivo task.py

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Não foi possível encrontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=["PUT"])
def update_taks(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)

    if task == None:
        return jsonify({"message": "Não foi possível encrontrar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "tarefa atualizada com sucesso"}) #nao precisamos colocar 200, pois já é o padrão

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        print(t.to_dict())
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)