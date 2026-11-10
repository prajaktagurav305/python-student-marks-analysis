def filefun(filename):      
    with open(filename,"r") as file:
        count = 0
        total =0
        highest = -1
        lowest = float("inf")
        highest_m = " "
        lowest_m = " "
        
        lines = file.readlines()
    
        for line in lines:
            name , mark = line.strip().split(",")    
            print("Name :",name)
            print("marks.:",mark)
            marks = int(mark)
            count +=1
            total +=marks
            if(marks > 25):
                print("name",name)
            if(marks > highest):
                highest = marks
                highest_m = name
            if(marks < lowest):
                lowest = marks
                lowest_m = name
    return{"average":total/count,"number of count":count,"total":total,"highest marks":highest_m,"lowest marks":lowest_m}

file =open("student.txt","w")
file.write("Raj,25\n")
file.write("Sham,23\n")
file.write("Prajakta,07\n")
filefun("student.txt") 
 
    