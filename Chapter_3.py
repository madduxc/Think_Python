#Author: Charles D. Maddux
#Date: 12/24/2020
#Description: exercises from chapter 3 of the book

def right_justify(text):
    """
    inserts enough leading spaces to put given text in col 70 and prints result
    :param text:
    :return: 0
    """
    len_text = len(text)
    space = 70 - len_text
    for i in range(space):
        text = " " + text
    print(text)

def print_text(text):
    """
    prints given text
    """
    print(text, end=" ")

def do_twice(f, txt):
    """
    calls a function twice
    """
    f(txt)
    f(txt)

def do_four(f, new_text):
    """
    calls a function four times
    """
    do_twice(f, new_text)
    do_twice(f, new_text)

def border_grid():
    """
    builds border grid
    """
    print_text("+")
    do_four(print_text, "-")
    print_text("+")
    do_four(print_text, "-")
    print_text("+")
    print("")

def middle_grid(txt):
    """
    builds middle of grid
    """
    print_text(txt)
    do_four(print_text, " ")
    print_text(txt)
    do_four(print_text, " ")
    print_text(txt)
    print("")

def draw_grid():
    """
    draws a  grid
    """
    border_grid()
    do_four(middle_grid, "|")
    border_grid()
    do_four(middle_grid, "|")
    border_grid()

def main():
    #  3.1: write a function that takes a string and prints the string with enough leading spaces
    #       that the last letter of the string is in col 70 of the display
    text_str = "Monty Python Psycho Killer."
    right_justify(text_str)
    text_str_2 = "I love my job!"
    right_justify(text_str_2)

    #  3.2:
    input_text = "Cessna 172"
    input_text_2 = "Beech Bonanza!"
    do_twice(print_text, input_text)
    print("")
    do_four(print_text, input_text_2)
    print("")

    #  3.3:
    draw_grid()


main()