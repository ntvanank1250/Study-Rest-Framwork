from students import *

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({'Students': Student.get_all_students()})

@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    return_value = Student.get_student(id)
    return jsonify(return_value)

@app.route('/students', methods=['POST'])
def add_student():
    request_data = request.get_json()
    Student.add_student(request_data["name"], request_data["age"], request_data["sex"])
    response = Response("Student added", 201, mimetype='application/json')
    return response


@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    request_data = request.get_json()
    Student.update_student(id, request_data['name'], request_data['age'],request_data['sex'])
    response = Response("Student Updated", status=200, mimetype='application/json')
    return response

@app.route('/students/<int:id>', methods=['DELETE'])
def remove_student(id):
    Student.delete_student(id)
    response = Response("Student Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)