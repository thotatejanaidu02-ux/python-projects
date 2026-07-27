max_marks = int(input("Enter maximum marks: "))
pass_percentage = int(input("Enter pass percentage: "))

while True:
    student_name = input("Enter student name (or 'quit' to exit): ")
    
    if student_name.lower() == 'quit':
        break
    
    marks = int(input(f"Enter marks for {student_name}: "))
    
    percentage = (marks / max_marks) * 100
    
    if percentage >= pass_percentage:
        print(f"✓ {student_name} PASSED ({percentage:.2f}%)\n")
    else:
        print(f"✗ {student_name} FAILED ({percentage:.2f}%)\n")
