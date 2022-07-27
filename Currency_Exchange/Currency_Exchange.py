def exchange_money(budget, exchange_rate):
    return budget/exchange_rate 

def get_change(budget, exchanging_value):
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    return int(denomination * number_of_bills)

def get_number_of_bills(budget, denomination):
    return int(budget/denomination)
    
def exchangeable_value(budget, exchange_rate, spread, denomination):
    number_of_bills = budget / (exchange_rate * (1 + spread / 100)) / denomination
    return int(number_of_bills) * denomination

def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    full_value = budget / (exchange_rate * (1 + spread / 100))
    return int(full_value - exchangeable_value(budget, exchange_rate, spread, denomination))
