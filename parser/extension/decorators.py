import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        treatment_time = time.time() - start_time
        print(f'Время обработки: {treatment_time} секунд')
        return res

    return wrapped
