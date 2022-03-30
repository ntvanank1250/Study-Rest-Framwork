from setting import *
import json

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name,
                'age': self.age, 'sex': self.sex}

    def add_student(_name, _age, _sex):
        new_student = Student(name=_name, age=_age, sex=_sex)
        db.session.add(new_student)
        db.session.commit()

    def get_all_students():
        return [Student.json(student) for student in Student.query.all()]

    def get_student(_id):
        return [Student.json(Student.query.filter_by(id=_id).first())]

    def update_student(_id, _name, _age, _sex):
        student_to_update = Student.query.filter_by(id=_id).first()
        student_to_update.name = _name
        student_to_update.age = _age
        student_to_update.sex = _sex
        db.session.commit()

    def delete_student(_id):
        Student.query.filter_by(id=_id).delete()
        db.session.commit()