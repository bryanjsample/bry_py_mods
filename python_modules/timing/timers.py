from time import time, sleep

def time_it(func):
    def timing(*args, **kwargs):
        start = time()
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
            end = time()
            duration = format_time(start, end)
            print(f'\n{func.__name__}() failed after {duration}.\n')
        else:
            end = time()
            duration = format_time(start, end)
            print(f'\n{func.__name__}() executed after {duration}.\n')
        
    def format_time(start, end):
        duration = end - start
        return expand_time(duration)

    def expand_time(duration, minutes = False, hours = False):
        if duration > 60:
            minutes = duration // 60
            seconds = round(duration % 60, ndigits=5)
            if minutes > 60:
                hours = minutes // 60
                minutes = minutes % 60
        else:
            seconds = duration
        duration_string = arrange_time_elements(seconds, int(minutes), int(hours))
        return duration_string

    def arrange_time_elements(seconds, minutes, hours):
        if hours and minutes:
            return f'{hours} hours, {minutes} minutes, and {seconds} seconds'
        elif minutes:
            return f'{minutes} minutes and {seconds} seconds'
        elif seconds <1:
            return f'{round(seconds * 1000, ndigits=5)} milliseconds'
        else:
            return f'{round(seconds, ndigits=5)} seconds'

    return timing

@time_it
def counter():
    for i in range(1000000):
        x = 1
        y = 2
        z = x + y


def main():
    counter()

if __name__ == "__main__":
    main()

