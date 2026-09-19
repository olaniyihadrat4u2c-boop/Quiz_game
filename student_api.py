from flask import Flask, request, jsonify

app = Flask(__name__)

#student data
students_db = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john.doe@univ.edu", "gpa": 3.6},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "email": "jane.smith@univ.edu", "gpa": 3.9},
    {"id": 3, "first_name": "Alex", "last_name": "Jones", "email": "alex.jones@univ.edu", "gpa": 2.8}
]

#most basic route
@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "status": "success",
        "message": "Student Information System API Active",
        "version": "1.0.0"
    }), 200


#get route for all students
@app.route("/api/v1/students", methods=["GET"])
def get_all_students():
    return jsonify({
        "count": len(students_db),
        "students": students_db
    }), 200


#get a singile student id
@app.route("/api/v1/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students_db:
        if student["id"] == student_id:
            return jsonify({"status": "success", "data": student}), 200
            
    return jsonify({"error": "Student record not found", "id": student_id}), 404


#post create email
@app.route("/api/v1/students", methods=["POST"])
def create_student():
    data = request.json or {}
    
    # Required field validation
    required_fields = ["first_name", "last_name", "email", "gpa"]
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            "error": "Bad Request",
            "message": f"Missing required fields: {', '.join(missing_fields)}"
        }), 400
        
    #auto-generate incremental ID
    next_id = max([s["id"] for s in students_db], default=0) + 1
    
    new_student = {
        "id": next_id,
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "email": data["email"],
        "gpa": float(data["gpa"])
    }
    
    students_db.append(new_student)
    return jsonify({
        "status": "created",
        "message": "Student record successfully initialized",
        "data": new_student
    }), 201


#put overide student records
@app.route("/api/v1/students/<int:student_id>", methods=["PUT"])
def update_student_complete(student_id):
    data = request.json or {}
    
    #put idk whatelse
    required_fields = ["first_name", "last_name", "email", "gpa"]
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            "error": "Bad Request",
            "message": f"Complete replacement requires all fields. Missing: {', '.join(missing_fields)}"
        }), 400

    for student in students_db:
        if student["id"] == student_id:
            student["first_name"] = data["first_name"]
            student["last_name"] = data["last_name"]
            student["email"] = data["email"]
            student["gpa"] = float(data["gpa"])
            return jsonify({
                "status": "updated",
                "message": "Student record fully replaced",
                "data": student
            }), 200
            
    return jsonify({"error": "Target student record does not exist", "id": student_id}), 404


#pacth profile changing
@app.route("/api/v1/students/<int:student_id>", methods=["PATCH"])
def update_student_partial(student_id):
    data = request.json or {}
    
    for student in students_db:
        if student["id"] == student_id:
            #updates only the specific things below
            if "first_name" in data:
                student["first_name"] = data["first_name"]
            if "last_name" in data:
                student["last_name"] = data["last_name"]
            if "email" in data:
                student["email"] = data["email"]
            if "gpa" in data:
                student["gpa"] = float(data["gpa"])
                
            return jsonify({
                "status": "updated",
                "message": "Student records modified successfully",
                "data": student
            }), 200
            
    return jsonify({"error": "Target student record does not exist", "id": student_id}), 404


#delte records
@app.route("/api/v1/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    for student in students_db:
        if student["id"] == student_id:
            students_db.remove(student)
            return jsonify({
                "status": "success",
                "message": f"Student record with ID {student_id} permanently deleted"
            }), 200
            
    return jsonify({"error": "Target student record could not be found for deletion", "id": student_id}), 404


if __name__ == "__main__":
    # Runs the application locally on http://127.0.0.1:5000
    app.run(debug=True)
