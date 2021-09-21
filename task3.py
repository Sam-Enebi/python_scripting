'''In the recucer function, the if loop checks if a number is even using
the modulus operator.The accept_input function uses try except and if loops
to ensure that the user input is an integer above zero'''


def reducer(number:int):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def main(number):
    number = reducer(number)
    print(number)
    if number != 1:
        main(number)

def accept_input():
    try:
        number = int(input("Enter an integer>> "))
        if number > 0:
            return number
        else:
            print("Number must be greater than 0")
            return accept_input()
    except ValueError:
        print("Input must be a number")
        return accept_input()


num = accept_input()
main(num)