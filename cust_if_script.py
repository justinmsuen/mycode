#!/usr/bin/env python3

def main():


    grade = input("Enter your numeric grade(type exit to stop): ")
    if(grade.lower() == "exit"):
        print("Exiting script")
        exit()

    grade = int(grade)
    print("You entered:", grade)

    if (grade >= 90 and grade <= 100):
        print("You got an A")
    elif (grade >= 80 and grade < 90):
        print("You got a B")
    elif(grade >= 70 and grade < 80):
        print("You got a C")
    elif(grade >= 60 and grade < 70):
        print("You got a D")
    elif(grade > 100):
        print("Not possible, nice try")
    elif(grade < 60):
        print("You Failed")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
