# BSIS 2AB : ACTIVITY 2

"""
Members:

Fulminar, Aladiah Mehriel P.
Pesongco, Daniel Y.

"""

import random


def add(x, y):
    return x + y


def subtrct(x, y):
    return x - y


def multiply(x, y):
    return x * y


def dividiby(x, y):
    return x / y


while True:

    choice = input("Enter your choice: ")

    if choice in ('1', '2', '3', '4'):

        terminate = 1
        correct = 0

        no_of_problem = int(input("How many problems?: "))

        while terminate <= no_of_problem:

            if choice == '1':
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = add(num1, num2)
                print("What is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    correct += 1
                else:
                    print("Wrong! the correct answer is", num3)

            elif choice == '2':
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = subtrct(num1, num2)
                print("What is the difference of " +
                      str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    correct += 1
                else:
                    print("Wrong! the correct answer is", num3)

            elif choice == '3':
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = multiply(num1, num2)
                print("What is the product of " +
                      str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    correct += 1
                else:
                    print("Wrong! the correct answer is", num3)

            elif choice == '4':
                num1 = round(float(random.randint(0, 9)), 2)
                num2 = round(float(random.randrange(2, 10, 2)), 2)
                num3 = dividiby(num1, num2)
                print("What is the division of " +
                      str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    correct += 1
                else:
                    print("Wrong! the correct answer is", num3)

            terminate += 1

            if no_of_problem < terminate:
                print("Your score is " + str(correct) + "/" + str(no_of_problem))

    try_again = input("Want to try again? (yes/no): ")
    if try_again == "no":
        break

else:
    print("Invalid input")
