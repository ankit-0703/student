students=[]
def add_student():
    try:
        name=input("Enter the Name")
        age=int(input("Enter the age"))
        marks=float(input("Enter the marks"))
        passed=marks>=40
        student={
            "name":name,
            "age":age,
            "marks":marks,
            "passed":passed
        }
        students.append(student)
        print("Student added successfully")
    except:
        print("Please enter the values coorectly, make sure age must be an integer, marks must be a float")

def view_student():
    if not students:
        print("No student record found")
        return
    for i, s in enumerate(students,1):
        print(f"{i}.{s['name']},Age: {s['age']},Marks:{s['marks']},Passed:{s['passed']}")
    
def search_student():
    name=input("[SEARCH] \n Enter teh name to search")
    for s in students:
        if s["name"].lower()==name.lower():
            print(f"[FOUND] Found:{s} \n")
            return
    print("[EROOR] Student not found")

def saveINfile():
    try:
        with open("student.txt","w") as f:
            for s in students:
                f.write(f"{s['name']},{s['age']},{s['marks']},{s['passed']} \n")
        print(f"File saved successfully")
    except Exception as e:
        print(f"[ERROR] Error while saving the file:{e} \n")
