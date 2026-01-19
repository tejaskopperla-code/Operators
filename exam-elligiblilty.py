medical_cause =input("enter Y or N:")

if medical_cause == 'Y':
    print("you are aloowed to write")
else:
 attendence =int(input("enter the attendence count :"))
 if attendence  >=75:
    print("allowed")
 else:
    print("you are not allowed")
 