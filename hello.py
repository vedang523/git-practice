def first_program():
    for i in range(0,11):
        print(i)

first_program()

def even_odd():
    num = int(input("Enter a Number: "))

    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd Number")

even_odd()