from flask import request, jsonify
from config import app, db
from models import Task

@app.route("/tasks",methods=["GET","POST"])
def tasks():
    if request.method =='GET':
        tasks = Task.query.all()
        json_tasks = list(map(lambda x: x.to_json(),tasks))
        return jsonify({"tasks":json_tasks}),200
   
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

@app.route("/task/<int:id>",methods=["PUT","DELETE"])
def task(id):
    if request.method == 'PUT':
        task = Task.query.get(id)

        if not task:
            return jsonify({"message":"Tarea no encontrada"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()



    app.run(debug=True)
