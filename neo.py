import time
import os
import random


def matrix():
    message = ('Wake up, Neo...',
               'The Matrix has you...',
               'Follow the white rabbit.',
               'Knock, knock, Neo.')
    slow_string = ''
    os.system('cls')
    for i in message[random.randint(0, len(message))]:
        slow_string += i
        print('\n' + slow_string)
        time.sleep(random.uniform(0.05, 0.2))
        os.system('cls')
    c = 7  # number of space blinks
    while c > 0:
        print('\n' + slow_string + "█")
        time.sleep(0.3)
        os.system('cls')
        print('\n' + slow_string)
        time.sleep(0.1)
        os.system('cls')
        c -= 1


# matrix()
