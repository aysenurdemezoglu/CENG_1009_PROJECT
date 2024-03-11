# 1
def list_all_courses():
    allCourse = open("course.txt", "r", encoding="utf-8")
    x = allCourse.read()
    return x


#2
def at_least_one_student_register():
    with open("course.txt", "r", encoding="utf-8") as f:
        mylist = []
        for line in f:
            line = line.rstrip("\n")
            values = line.split(";")
            mylist.append(values)
        for i in mylist:
            if int(i[3]) > 0:
                print(i[1])


# 3
def add_new_course():
    print("What is your class code?")
    input1 = input().upper()
    print("What is your course name?")
    input2 = input().capitalize()
    print("What is your teacher name?")
    input3 = input().capitalize()
    print("How many student are registered?")
    input4 = input()
    file1 = open('course.txt', 'a')
    file1.write(input1)
    file1.write(";")
    file1.write(input2)
    file1.write(";")
    file1.write(input3)
    file1.write(";")
    file1.write(input4)
    file1.write("\n")


# 4
def search_course_by_course_code():
    f = open("course.txt", "r", encoding="utf-8")
    lines = f.readlines()
    name = input("Please write course code: ").upper()

    for line in lines:
        values = line.split(";")
        if values[0] == name:
            print("The course is available.")
            return
    else:
        print("The course you are looking for is not available")


# 5
def search_a_course_by_name():
    f = open("course.txt", "r", encoding="utf-8")
    lines = f.readlines()
    course = input("Please write the course that you are searching: ").lower()

    for line in lines:
        values = line.split(";")
        if course in values[1].lower():
            print(values[1])
        else:
            continue


#6
def register_a_student_to_a_course():
    while True:
        student_id = input("Enter student ID:")
        code = input("Enter the course code you want to register:")
        with open("student.txt", "r+") as file6:
            lines = file6.readlines()
            found = False
            for i, line in enumerate(lines):
                line = line.strip()
                parts = line.split(";")
                if student_id == parts[0]:
                    parts.append(code)
                    lines[i] = ",".join(parts) + "\n"
                    file6.seek(0)
                    file6.writelines(lines)
                    found = True
                    break
            if not found:
                student_name = input("Enter student name and surname:")
                new_student = f"{student_id};{student_name};{code}\n"
                file6.write(new_student)
                break
        break


# 7
def list_all_the_student_their_registered_courses():
    f = open("student.txt", "r", encoding="utf-8")
    for line in f:
        values = line.split(";")
        name = values[1]
        taken_courses = []
        courses = values[2]
        taken_courses.append(courses)
        print(name, "=", taken_courses)


# 8
def list_top_three_courses():
    f = open("course.txt", "r", encoding="utf-8")
    list_of_courses = f.readlines()
    my_dict = {}
    for i in range(len(list_of_courses)):
        if list_of_courses[i].split(";")[1] not in my_dict:
            my_dict[list_of_courses[i].split(";")[1]] = int(list_of_courses[i].split(";")[3])
        else:
            pass
    print("Top 3 most crowded courses:")

    sorted_my_dict = sorted(my_dict.items(), key=lambda x: x[1])
    for i in range(3):
        a = str(sorted_my_dict[-(i + 1)]).strip("(").strip(")").split(
            "'")
        print(a[1])


#9
def list_top_three_students():
    with open("student.txt", "r", encoding="utf-8") as f:
        list_of_students = f.readlines()
        my_dict = {}
        for line in list_of_students:
            parts = line.strip().split(";")
            student_name = parts[1]
            courses = parts[2].split(",")
            my_dict[student_name] = len(courses)

        print("Top 3 students with the most course registrations:")
        sorted_my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        for i in range(min(3, len(sorted_my_dict))):
            print(sorted_my_dict[i][0])




while True:

    process = input("1 = List all courses\n"
                    "2 = List all the course that have at least one student registered\n"
                    "3 = Add a new course\n"
                    "4 = Search a course by course code\n"
                    "5 = Search a course by name\n"
                    "6 = Register a student to a course\n"
                    "7 = List all the students their registered courses.\n"
                    "8 = List top 3 most crowded courses\n"
                    "9 = List top 3 students with the most course registrations\n"
                    "10 = exit\n"
                    "Please select number ")
    if process == "1":
        print(list_all_courses())

    elif process == "2":
        print(at_least_one_student_register())

    elif process == "3":
        print(add_new_course())

    elif process == "4":
        print(search_course_by_course_code())

    elif process == "5":
        print(search_a_course_by_name())

    elif process == "6":
        print(register_a_student_to_a_course())

    elif process == "7":
        print(list_all_the_student_their_registered_courses())

    elif process == "8":
        print(list_top_three_courses())

    elif process == "9":
        print(list_top_three_students())

    elif process == "10":
        break