students_first_name = []
students_last_name = []
students_age = []
students_mark = []


while True:
    students_data= input("Enter student's data: ")
    if students_data=="":
        break
    
    students_data_list= students_data.split()

    students_first_name.append( students_data_list[0])
    students_last_name.append( students_data_list[1])
    if int(students_data_list[2]) >= 18 and int(students_data_list[2])<=30:
        students_age.append(int(students_data_list[2]))
    else:
        print("Error! Incorrect age!")
        
    
    if int(students_data_list[3])>=1 and int(students_data_list[3])<=10:
        students_mark.append(int(students_data_list[3]))
    else:
        print("Error! Incorrect mark!")
        



for i in range(len(students_first_name)):
    print(students_first_name[i], students_last_name[i], students_age[i], students_mark[i])
        
