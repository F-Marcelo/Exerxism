def steps(number):
    i = 0
    if number > 0:
        while number != 1:
            if number % 2 == 0:
                number = number / 2
                i += 1 
            elif number % 2 == 1:
                number = number * 3 + 1
                i += 1
    
        return i
    raise ValueError("Only positive integers are allowed")     

print(steps(1000000))

