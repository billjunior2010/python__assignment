Class_data = [
    [True, 34, 5, 'School'],
    [8, 23, 20, 11, 37, 55, 17, 5],
    ['book', 'mosh', 'arc', 'photo'],
    [-1, 'Mani']
]
# print (students)


def is_prime(n):  # function to define prime numbers
    for i in range(2, int(n/2)):
        if (n % i) == 0:
            return False
    return True


def Reverse(lst):  # function used to reverse the list
    new_lst = lst[::-1]
    return new_lst


# firstly break up the matrix into lists
for students in Class_data:
    # print(students)
   # check if there are lists containing only strings
    if all([isinstance(student, str) for student in students]) == True:
        # loop from the last element to the first in reverse and print them
        for value in range(len(students)):

            # convert lowercase to uppercase
            student_upper = students[value].upper()
            print(student_upper)
        # check if there are lists with all elements only intergers
    elif all([isinstance(student, int) for student in students]) == True:
        # print("intergers")
        # reversed list  is stored in the variable and used to produce a list of prime numbers
        students_reverse = Reverse(students)
        for student in students_reverse:
            # checking if each element is a prime number.
            if is_prime(student) == True:
                print("{} is a prime number".format(student))
            # else:
            #     print("{} is not a prime number".format(student))
                # could remove this block of code if i wanted only the list of prime numbers printed to the console.
    # else:
    #     print("This list contains mixed data types")

print()


# students_name=students[2]
# print(students_name)
# for individual in students_name:
#     individual=individual.upper()

#     print(individual)
