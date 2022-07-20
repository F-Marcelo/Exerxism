from datetime import timedelta


def add(moment):
    delta = timedelta(seconds = 1000000000)
    data2 = moment + delta
    return data2
