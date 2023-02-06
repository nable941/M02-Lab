'''
Nathan Able
M02_Lap_Case_Study.py

Program takes in students name and GPA and outputs Deans list/Honor role status
'''
#Set variables
dean = 3.5
honor = 3.25
quitter = "ZZZ"

#Set initial check variable
lname = input("Enter the students last name or " + quitter + " to quit: ")

#Validate condition to run the loop
while lname.upper() != quitter:
    fname = input("Enter students first name: ")
    gpa = float(input("Enter students GPA: "))
    #Validate the conditions for Dean's and Honor 
    if gpa >= dean:
        print(fname, lname, "has made it on the Dead's List.")
    elif gpa >= honor:
        print(fname, lname, "has made Honor Role.")
    else:
        print(fname, lname, "has not qualified for either Dean's List or Honor Role.")
    #Set check variable
    lname = input("Enter the students last name or 'ZZZ' to quit: ")    
