from home.models import Student

def student_names():
    student = Student.objects.all()
    names = []
    for my_name in student:
        names.append(my_name.name)

    return names
