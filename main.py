from fastapi import FastAPI

app = FastAPI()
students = {}
student_data = {
    "id":0,
    "Name":"",
    "Age":"",
    "Sex":"",
    "Height":0,
}
  
@app.get("/")
def home():
    return{"massage": "This ia a student record API"}

@app.get('/student')
def get_students():
    return {"massage": "succesful", "data": students}


@app.post('/students')
def Create_student(id: int, Name: str, Age: int, Sex: str, Height: float):
    new_student = student_data.copy()
    new_student['id']= id
    new_student['Name'] = Name
    new_student['Age'] = Age
    new_student['Sex'] = Sex
    new_student['Height'] = Height
    return{'message': 'Student profile sucessfully created', 'data': new_student}

@app.get('/single_student')
def Retrive_single_student(id):
    student = students(id)
    return{'message': "Student profile read successsfully", "data": student}

@app.put('/single_student')
def update_single_student(id):
    student = students(id)
    return{'message': "Student profile udated successsfully", "data": student}

@app.delete('/single_student')
def delete_single_student(id):
    student = students(id)
    return{'message': "Student successsfully deleted", "data": student}
