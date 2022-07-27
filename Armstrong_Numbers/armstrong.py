def is_armstrong_number(number):
    armstrong = 0
    i = 0
    digits = len(str(number))
    for i in range(digits):
        aux = number // (10 ** i) % 10
        armstrong = armstrong + aux ** digits
    if number == armstrong:
        return True 
    return False 
