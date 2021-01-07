# Author: Charles D. Maddux
# Date: 12/18/2020
# Description: practice by doing exercises in the book

def main():
    #Q1: what is the volume of a sphere?
    rad = 3 #float(input("Enter Radius in inches: "))
    vol_sphere = round(4/3 * 3.14159 * rad**3, 3)
    print("The volume of the sphere is", str(vol_sphere), "cubic inches.")

    #Q2: suppose the retail price of a book is $24.95, but the bookstore gets a 40% discount.
    #   Shipping cost is $3.00 for the first copy and $0.75 for each additional copy.
    #   What is the total wholesale cost for 60 copies?
    discount = 0.40
    unit_cost = 24.95
    wholesale_cost = (1 - discount) * unit_cost
    num_books = 60  #int(input("Enter the number of books ordered: "))
    book_cost = num_books * wholesale_cost
    shipping_cost = 3.00            #cost of shipping the first book
    if num_books > 1:
        shipping_cost = shipping_cost + 0.75 * (num_books - 1)
    total_cost = round(book_cost + shipping_cost, 2)
    print("The wholesale cost of {0} books is ${1}" . format(num_books, total_cost))

main()
