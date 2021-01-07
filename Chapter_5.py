#Author: Charles D. Maddux
#Date: 12/28/2020
#Description: Think Python Chapter 5 exercises

import time
import turtle

def exercise_1(current_time):
    """
    times the current time and converts to days, hours, minutes, seconds since the epoch
    """
    #declare variables
    unit_min = 60                       #[seconds/minute]
    unit_hour = 60                      #[minutes/hour]
    unit_day = 24                       #[hours/day]

    hours = unit_min * unit_hour        #[seconds/hour]
    days = hours * unit_day             #[seconds/day]

    current_days = int(current_time // days)
    current_day = current_time % days
    current_hours = int(current_day // hours)
    current_hour = current_day % hours
    current_minutes = int(current_hour // unit_min)
    current_seconds = round(current_hour % unit_min, 1)

    print(current_time, "seconds have passed since January 1, 1970 GMT")
    print("That equates to", current_days, "days,", current_hours, "hours,", current_minutes, "minutes, and ", current_seconds, "seconds.")

def check_fermat(num_a, num_b, num_c, num_n=2):
    """
    verifies Fermat's Theorem - "there are no positive integers (n > 2) such that a^n + b^n = c^n
    :param num_a: int
    :param num_b: int
    :param num_c: int
    :param num_n: int
    :return: 0
    """
    left_side = num_a**num_n + num_b**num_n
    right_side = num_c**num_n
    if left_side == right_side:
        print("Holy smokes!  Fermat was wrong!")
    else:
        print("No, that doesn't work.")
    return left_side == right_side

def exercise_2():
    """
    retrieves inputs for "check_fermat" function and prints results
    :return: 0
    """
    check_a = False
    check_b = False
    check_c = False
    check_n = False

    while check_a == False:
        num_a = int(input("Enter 1st positive integer:"))
        if num_a > 0:
            check_a = True
        else:
            print("Input MUST be an integer greater than zero.")
    while check_b == False:
        num_b = int(input("Enter 2nd positive integer:"))
        if num_b > 0:
            check_b = True
        else:
            print("Input MUST be an integer greater than zero.")
    while check_c == False:
        num_c = int(input("Enter 3rd positive integer:"))
        if num_c > 0:
            check_c = True
        else:
            print("Input MUST be an integer greater than zero.")
    while check_n == False:
        num_n = int(input("Enter Exponent (must be a positive integer greater than 2):"))
        if num_n > 2:
            check_n = True
        else:
            print("Input MUST be an integer greater than two.")
    verify = check_fermat(num_a, num_b, num_c, num_n)
    #print(verify)

def is_triangle(leg_a, leg_b, leg_c):
    """
    checks if 3 given sides can form a triangle
    :param leg_a: int
    :param leg_b: int
    :param leg_c: int
    :return: str
    """
    if leg_a > (leg_b + leg_c):
        return "No"
    elif leg_b > (leg_a + leg_c):
        return "No"
    elif leg_c > (leg_a + leg_b):
        return "No"
    else:
        return "Yes"

def exercise_3():
    """
    retrieves user input for triangle sides
    :return: 0
    """
    leg_1 = input("Enter the length of the first leg: ")
    leg_1 = int(leg_1)
    leg_2 = input("Enter the length of the second leg: ")
    leg_2 = int(leg_2)
    leg_3 = input("Enter the length of the third leg: ")
    leg_3 = int(leg_3)
    possible = is_triangle(leg_1, leg_2, leg_3)
    print(possible)

def recurse(n, s):
    """
    copy from text
    """
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)

def draw(pencil, length, num):
    """
    aefe
    """
    if num == 0:
        return
    angle = 50
    pencil.fd(length* num)
    pencil.lt(angle)
    draw(pencil, length, num - 1)
    pencil.rt(2* angle)
    draw(pencil, length, num - 1)
    pencil.lt(angle)
    pencil.bk(length* num)

def kock(pencil, length, a=1):
    """
    draws a Kock curve
    """
    angle = 60 * a
    pencil.fd(length)
    pencil.lt(angle)
    pencil.fd(length)
    pencil.rt(2*angle)
    pencil.fd(length)
    pencil.lt(angle)
    pencil.fd(length)
    pencil.lt(angle)

def snowflake(pencil, length, num, a=1):
    """
    adf
    """
    if num == 0:
        return
    for j in range(2):
        for i in range(3):
            kock(pencil, length, a)
        a = (-1)* a
    pencil.lt(60)
    snowflake(pencil, length, num - 1, a)

def main():
    current_time = round(time.time(), 1)
    exercise_1((current_time))
#    print("\n")
#    exercise_2()
#    print("\n")
#    exercise_3()
    recurse(5, 0)
    bobo = turtle.Turtle()
    snowflake(bobo, 10, 3)
    turtle.mainloop()


main()
