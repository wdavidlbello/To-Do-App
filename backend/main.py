from flask import request, jsonify
from config import app, db
from models import Task

@app.route("/tasks",methods=["GET","POST"])
def tasks():
    if request.method =='GET':
        tasks = Task.query.all()
        json_tasks = list(map(lambda x: x.to_json(),tasks))
        return jsonify(json_tasks),200
   
    if request.method =='POST':
        name = request.json.get("name")
        done = request.json.get("done")

        if not name:
            return (jsonify({"message:" "Debe añadir una tarea"}),
            400,)
        new_task = Task(name= name,done= done)
        try: 
            db.session.add(new_task)
            db.session.commit()
        except Exception as e:
            return jsonify({"message":str(e)}),400
    
        return jsonify({"message":"Tarea creada"}),201

@app.route("/task/<int:id>",methods=["GET","PUT","DELETE"])
def task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"message":"Tarea no encontrada"}),404
    
    if request.method == 'GET':   
        json_task = task.to_json()
        return jsonify(json_task),200
    
    if request.method == 'PUT':
        data = request.json
        task.name = data.get("name",task.name)
        task.done = data.get("done",task.done)

        db.session.commit()

        return jsonify({"message":"Task updated"}),200
    
    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()

        return jsonify({"message":"Task deleted"}),200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()



    app.run(debug=True)
