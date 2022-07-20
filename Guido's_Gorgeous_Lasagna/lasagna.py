EXPECTED_BAKE_TIME = 40
'''
Define o tempo máximo de preparo de uma lasanha
'''
PREPARATION_TIME = 2
'''
Define o tempo para preparo de cada camada da lasanha
'''


def bake_time_remaining(baking_time):
    '''
    Calcula o tempo faltando para assar a lasanha
    '''
    return EXPECTED_BAKE_TIME - baking_time

def preparation_time_in_minutes(numb_of_layer):
    '''
    Retorna o tempo de preparo para uma quantidade de camadas de uma lasanha
    '''
    return numb_of_layer * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''
    Retorna o decorrido do preparo de uma lasanha com determinada quantidade de camadas
    '''
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
