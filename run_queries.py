
from app import app, db
from app.models import Student, Course, Teacher

with app.app_context():
    # Query all students
    students = Student.query.all()
    for student in students:
        print(f"Student ID: {student.id}, Student Name: {student.name}")

    # Query all courses taught by a teacher with a specific ID
    teacher_id = 1
    courses_taught = Course.query.filter_by(teacher_id=teacher_id).all()
    for course in courses_taught:
        print(f"Course ID: {course.id}, Course Title: {course.title}")

    # Query all teachers of a student with a specific ID
    student_id = 1
    student = Student.query.get(student_id)
    for teacher in student.teachers:
        print(f"Teacher ID: {teacher.id}, Teacher Name: {teacher.name}")
