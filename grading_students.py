# HackerLand University has the following grading policy:

# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round 
# each student's grade according to these rules:

# If the difference between the grade and the next multiple 
# of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs 
# as the result will still be a failing grade.

# Given the initial value of grade for each of Sam's n students, 
# write code to automate the rounding process.

import os

def grading_students(grades):
    output = []
    for grade in grades:
        if (grade < 38):
            output.append(grade)
        else:
            if (grade % 5 == 4):
                output.append(grade + 1)
            elif (grade % 5 == 3):
                output.append(grade + 2)
            else:
                output.append(grade)
    return output

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = grading_students(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()