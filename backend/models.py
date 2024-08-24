from config import db  

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),unique=False, nullable=False)
    done = db.Column(db.Boolean, default=False,nullable=False)

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "done":self.done,
        }