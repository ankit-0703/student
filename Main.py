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
def Load_from_file():
    try:
        with open("student.txt","r")as f:
            for line in f:
                name,age,marks,passed =line.strip().split(",")
                students.append({
                    "name":name,
                    "age":int(age),
                    "marks":float(marks),
                    "passed":passed=="True"
                })
            print("Data loaded from student.txt \n")
    except FileNotFoundError:
        print("File not Found")
    except Exception as e:
        print(f"Error loading file: {e}")

def menu():
    while True:
        print("\n Student record Manager")
        print("1. Add Student")
        print("2. View all student")
        print("3. Search")
        print("4. Save to file")
        print("5. Load from file")
        print("6. EXIT")

        choice = input("--> Choose an Option: ")

        if choice == '1':
            add_student()
        
        elif choice == '2':
            view_student();

        elif choice == '3':
            search_student()

        elif choice == '4':
            saveINfile()
            
        elif choice == '5':
            Load_from_file()
            
        elif choice == '6':
            print("Exiting")
            break
        else:
            print("Choose the correct option")

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("Interrupted by user")