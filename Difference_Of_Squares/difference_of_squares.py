def square_of_sum(number):
    aux = 0
    for i in range(number + 1):
        aux = aux + i
    return aux ** 2

def sum_of_squares(number):
    aux = 0
    for i in range(number + 1):
        aux = aux + i ** 2
    return aux 

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

